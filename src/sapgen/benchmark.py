from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from sapgen.domain.models import SAPIR, ValidationIssue
from sapgen.domain.rules import RuleEngine
from sapgen.harness.base import HarnessAdapter


class BenchmarkModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class RubricCriterion(BenchmarkModel):
    id: str
    category: str
    description: str
    max_score: int = 2
    critical: bool = False


class CriterionResult(BenchmarkModel):
    rubric_id: str
    score: float
    max_score: float
    rationale: str
    issue_codes: list[str] = Field(default_factory=list)


class BenchmarkResult(BenchmarkModel):
    criteria: list[CriterionResult]
    total_score: float
    max_score: float
    critical_error_count: int
    judge: str
    metadata: dict[str, Any] = Field(default_factory=dict)


DEFAULT_RUBRICS = [
    RubricCriterion(
        id="estimand",
        category="估计目标",
        description="五属性完整，且与终点和分析一致。",
        critical=True,
    ),
    RubricCriterion(
        id="primary_method",
        category="主分析方法",
        description="模型、效应量和检验方法明确且可执行。",
        critical=True,
    ),
    RubricCriterion(
        id="sensitivity",
        category="敏感性分析",
        description="围绕主分析关键假设提供替代设定。",
    ),
    RubricCriterion(
        id="intercurrent_event",
        category="伴发事件",
        description="识别事件并将策略关联到估计目标。",
        critical=True,
    ),
    RubricCriterion(
        id="missing_data",
        category="失访与缺失",
        description="区分原因、机制假设和具体处理方法。",
        critical=True,
    ),
    RubricCriterion(
        id="safety",
        category="安全性分析",
        description="明确 TEAE 时间窗、MedDRA、SOC/PT 和分母。",
        critical=True,
    ),
    RubricCriterion(
        id="tfl",
        category="TFL 表壳",
        description="表号、行列、统计量、分母和脚注落实正文规则。",
    ),
]


ISSUE_PREFIXES = {
    "estimand": ("EST-", "REF-EST-"),
    "primary_method": ("METHOD-", "REF-METHOD-"),
    "sensitivity": ("MISS-MNAR-SENSITIVITY",),
    "intercurrent_event": ("ICE-",),
    "missing_data": ("MISS-",),
    "safety": ("SAFETY-",),
    "tfl": ("TFL-", "REF-TFL-"),
}


class BenchmarkEvaluator:
    def __init__(self, harness: HarnessAdapter | None = None) -> None:
        self.harness = harness

    def evaluate(
        self,
        ir: SAPIR,
        rubrics: list[RubricCriterion] | None = None,
        *,
        session_id: str = "sapgen-benchmark",
        use_llm_judge: bool = False,
    ) -> BenchmarkResult:
        criteria = rubrics or DEFAULT_RUBRICS
        if use_llm_judge and self.harness is not None:
            payload = self.harness.complete_json(
                system_prompt=(
                    "You are a conservative clinical-trial SAP evaluator. Score each rubric only "
                    "from the supplied SAP-IR. Missing or unresolved decisions cannot receive full "
                    "credit. Return evidence paths, not new statistical recommendations."
                ),
                user_prompt=(
                    f"Rubrics:\n{[item.model_dump() for item in criteria]}\n\n"
                    f"SAP-IR:\n{ir.model_dump_json()}"
                ),
                schema=BenchmarkResult.model_json_schema(),
                session_id=session_id,
            )
            return BenchmarkResult.model_validate(payload)
        return self._deterministic(ir, criteria)

    @staticmethod
    def _deterministic(ir: SAPIR, rubrics: list[RubricCriterion]) -> BenchmarkResult:
        report = RuleEngine().validate(ir)
        results = []
        critical_error_count = 0
        for rubric in rubrics:
            prefixes = ISSUE_PREFIXES.get(rubric.id, ())
            relevant = [
                item
                for item in report.issues
                if any(item.code.startswith(prefix) for prefix in prefixes)
            ]
            errors = [item for item in relevant if item.severity.value == "error"]
            warnings = [item for item in relevant if item.severity.value == "warning"]
            if errors:
                score = 0.0
            elif warnings:
                score = rubric.max_score / 2
            else:
                score = float(rubric.max_score)
            if rubric.critical:
                critical_error_count += len(errors)
            results.append(
                CriterionResult(
                    rubric_id=rubric.id,
                    score=score,
                    max_score=rubric.max_score,
                    rationale=BenchmarkEvaluator._rationale(relevant),
                    issue_codes=[item.code for item in relevant],
                )
            )
        return BenchmarkResult(
            criteria=results,
            total_score=sum(item.score for item in results),
            max_score=sum(item.max_score for item in results),
            critical_error_count=critical_error_count,
            judge="deterministic-rules",
            metadata={"validation_issue_count": len(report.issues)},
        )

    @staticmethod
    def _rationale(issues: list[ValidationIssue]) -> str:
        if not issues:
            return "No rule violation was detected for this rubric."
        return " ".join(f"[{item.code}] {item.message}" for item in issues[:4])
