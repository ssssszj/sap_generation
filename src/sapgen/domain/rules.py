from __future__ import annotations

from collections.abc import Iterable

from sapgen.domain.models import (
    SAPIR,
    EvidenceStatus,
    IntercurrentEventStrategy,
    MissingnessMechanism,
    Severity,
    ValidationIssue,
    ValidationReport,
)


def issue(
    code: str,
    severity: Severity,
    module: str,
    message: str,
    path: str,
    suggested_fix: str | None = None,
    related_ids: Iterable[str] = (),
) -> ValidationIssue:
    return ValidationIssue(
        code=code,
        severity=severity,
        module=module,
        message=message,
        path=path,
        suggested_fix=suggested_fix,
        related_ids=list(related_ids),
    )


class RuleEngine:
    """Deterministic checks for the high-risk SAP decisions in the proposal."""

    def validate(self, ir: SAPIR) -> ValidationReport:
        issues: list[ValidationIssue] = []
        issues.extend(self._validate_references(ir))
        issues.extend(self._validate_estimands(ir))
        issues.extend(self._validate_analysis_methods(ir))
        issues.extend(self._validate_complex_data(ir))
        issues.extend(self._validate_multiplicity(ir))
        issues.extend(self._validate_safety(ir))
        issues.extend(self._validate_tfl(ir))
        issues.extend(self._validate_provenance(ir))
        return ValidationReport(issues=issues)

    def _validate_references(self, ir: SAPIR) -> list[ValidationIssue]:
        issues: list[ValidationIssue] = []
        population_ids = {item.id for item in ir.analysis_populations}
        endpoint_ids = {item.id for item in ir.endpoints}
        estimand_ids = {item.id for item in ir.estimands}
        method_ids = {item.id for item in ir.analysis_methods}

        for index, estimand in enumerate(ir.estimands):
            if estimand.endpoint_id not in endpoint_ids:
                issues.append(
                    issue(
                        "REF-EST-ENDPOINT",
                        Severity.ERROR,
                        "analysis_design",
                        "估计目标引用了不存在的终点。",
                        f"estimands.{index}.endpoint_id",
                        "选择已定义终点或先补充终点定义。",
                        [estimand.id, estimand.endpoint_id],
                    )
                )
        for index, method in enumerate(ir.analysis_methods):
            if method.estimand_id not in estimand_ids:
                issues.append(
                    issue(
                        "REF-METHOD-ESTIMAND",
                        Severity.ERROR,
                        "analysis_design",
                        "分析方法引用了不存在的估计目标。",
                        f"analysis_methods.{index}.estimand_id",
                        related_ids=[method.id, method.estimand_id],
                    )
                )
            if method.analysis_population_id not in population_ids:
                issues.append(
                    issue(
                        "REF-METHOD-POP",
                        Severity.ERROR,
                        "analysis_design",
                        "分析方法引用了不存在的分析人群。",
                        f"analysis_methods.{index}.analysis_population_id",
                        related_ids=[method.id, method.analysis_population_id],
                    )
                )
        for index, spec in enumerate(ir.tfl_specs):
            unknown = set(spec.source_analysis_ids) - method_ids
            if unknown:
                issues.append(
                    issue(
                        "REF-TFL-METHOD",
                        Severity.ERROR,
                        "tfl",
                        f"TFL 引用了不存在的分析方法：{', '.join(sorted(unknown))}。",
                        f"tfl_specs.{index}.source_analysis_ids",
                        related_ids=[spec.id, *sorted(unknown)],
                    )
                )
            if spec.population_id not in population_ids:
                issues.append(
                    issue(
                        "REF-TFL-POP",
                        Severity.ERROR,
                        "tfl",
                        "TFL 引用了不存在的分析人群。",
                        f"tfl_specs.{index}.population_id",
                        related_ids=[spec.id, spec.population_id],
                    )
                )
        return issues

    @staticmethod
    def _validate_multiplicity(ir: SAPIR) -> list[ValidationIssue]:
        if ir.multiplicity is None:
            return [
                issue(
                    "MULTIPLICITY-MISSING",
                    Severity.WARNING,
                    "multiplicity",
                    "缺少多重性范围及处理状态。",
                    "multiplicity",
                    "方案未规定时应明确标记为待确认，不得默认调整或不调整。",
                )
            ]
        if "unresolved" not in ir.multiplicity.strategy.lower():
            return [
                issue(
                    "MULTIPLICITY-DECISION",
                    Severity.INFO,
                    "multiplicity",
                    "多重性策略已给出；请确认其具有方案或统计审阅依据。",
                    "multiplicity.strategy",
                    related_ids=[ir.multiplicity.id],
                )
            ]
        return []

    def _validate_estimands(self, ir: SAPIR) -> list[ValidationIssue]:
        issues: list[ValidationIssue] = []
        required = (
            "population",
            "variable",
            "treatment_condition",
            "population_summary",
        )
        for index, estimand in enumerate(ir.estimands):
            for field_name in required:
                value = getattr(estimand, field_name)
                if not value or value.strip() in {"待确认", "TBD"}:
                    issues.append(
                        issue(
                            f"EST-{field_name.upper()}",
                            Severity.ERROR,
                            "analysis_design",
                            f"估计目标缺少五属性中的 {field_name}。",
                            f"estimands.{index}.{field_name}",
                            "依据方案证据填写；方案未规定时创建待确认项。",
                            [estimand.id],
                        )
                    )
            if not estimand.intercurrent_event_strategies:
                issues.append(
                    issue(
                        "EST-ICE",
                        Severity.WARNING,
                        "complex_data",
                        "估计目标未记录伴发事件及处理策略。",
                        f"estimands.{index}.intercurrent_event_strategies",
                        "至少确认停药、换药、救援治疗和死亡是否适用。",
                        [estimand.id],
                    )
                )
        return issues

    def _validate_analysis_methods(self, ir: SAPIR) -> list[ValidationIssue]:
        issues: list[ValidationIssue] = []
        primary_by_estimand: dict[str, int] = {}
        supportive_by_estimand: dict[str, int] = {}
        for index, method in enumerate(ir.analysis_methods):
            if method.role.value == "primary":
                primary_by_estimand[method.estimand_id] = (
                    primary_by_estimand.get(method.estimand_id, 0) + 1
                )
            elif method.role.value == "supportive":
                supportive_by_estimand[method.estimand_id] = (
                    supportive_by_estimand.get(method.estimand_id, 0) + 1
                )
            for field_name, label in (
                ("model", "模型"),
                ("effect_measure", "效应量"),
                ("test_method", "检验方法"),
            ):
                value = getattr(method, field_name)
                if not value or value.strip() in {"待确认", "TBD"}:
                    issues.append(
                        issue(
                            f"METHOD-{field_name.upper()}",
                            Severity.ERROR,
                            "analysis_design",
                            f"分析方法缺少可执行的{label}。",
                            f"analysis_methods.{index}.{field_name}",
                            related_ids=[method.id],
                        )
                    )
        endpoint_by_id = {endpoint.id: endpoint for endpoint in ir.endpoints}
        for estimand in ir.estimands:
            endpoint = endpoint_by_id.get(estimand.endpoint_id)
            count = primary_by_estimand.get(estimand.id, 0)
            if endpoint is not None and endpoint.priority == "primary" and count != 1:
                issues.append(
                    issue(
                        "METHOD-PRIMARY-COUNT",
                        Severity.WARNING,
                        "analysis_design",
                        f"估计目标 {estimand.id} 应恰好对应一个主分析，当前为 {count} 个。",
                        "analysis_methods",
                        "保留一个已确认的主分析，其余标为敏感性或支持性分析。",
                        [estimand.id],
                    )
                )
            if endpoint is not None and endpoint.priority != "primary" and count:
                issues.append(
                    issue(
                        "METHOD-HIERARCHY",
                        Severity.ERROR,
                        "analysis_design",
                        f"非主要终点 {endpoint.id} 不应自动标记为主分析。",
                        "analysis_methods",
                        "将其标记为支持性分析，除非方案明确提升为主要终点。",
                        [estimand.id, endpoint.id],
                    )
                )
            if (
                endpoint is not None
                and endpoint.priority != "primary"
                and supportive_by_estimand.get(estimand.id, 0) == 0
            ):
                issues.append(
                    issue(
                        "METHOD-SUPPORTIVE-MISSING",
                        Severity.WARNING,
                        "analysis_design",
                        f"终点 {endpoint.id} 尚无支持性分析方法。",
                        "analysis_methods",
                        related_ids=[estimand.id, endpoint.id],
                    )
                )
        return issues

    def _validate_complex_data(self, ir: SAPIR) -> list[ValidationIssue]:
        issues: list[ValidationIssue] = []
        estimand_ids = {item.id for item in ir.estimands}
        ice_estimands: set[str] = set()
        for index, plan in enumerate(ir.intercurrent_events):
            ice_estimands.add(plan.estimand_id)
            if plan.estimand_id not in estimand_ids:
                issues.append(
                    issue(
                        "ICE-ESTIMAND-REF",
                        Severity.ERROR,
                        "complex_data",
                        "伴发事件计划未关联有效估计目标。",
                        f"intercurrent_events.{index}.estimand_id",
                        related_ids=[plan.id, plan.estimand_id],
                    )
                )
            if plan.strategy == IntercurrentEventStrategy.UNRESOLVED:
                issues.append(
                    issue(
                        "ICE-STRATEGY-UNRESOLVED",
                        Severity.WARNING,
                        "complex_data",
                        f"伴发事件“{plan.event}”的处理策略尚未确定。",
                        f"intercurrent_events.{index}.strategy",
                        "由统计专家结合治疗效果问题确认策略。",
                        [plan.id, plan.estimand_id],
                    )
                )
            if not plan.operational_rule.strip():
                issues.append(
                    issue(
                        "ICE-OPERATIONAL-RULE",
                        (
                            Severity.WARNING
                            if plan.strategy == IntercurrentEventStrategy.UNRESOLVED
                            else Severity.ERROR
                        ),
                        "complex_data",
                        "伴发事件策略缺少可实施的数据处理规则。",
                        f"intercurrent_events.{index}.operational_rule",
                        related_ids=[plan.id],
                    )
                )
        for estimand in ir.estimands:
            if estimand.id not in ice_estimands:
                issues.append(
                    issue(
                        "ICE-PLAN-MISSING",
                        Severity.WARNING,
                        "complex_data",
                        f"估计目标 {estimand.id} 没有独立的伴发事件计划。",
                        "intercurrent_events",
                        related_ids=[estimand.id],
                    )
                )

        missing_estimands: set[str] = set()
        for index, plan in enumerate(ir.missing_data):
            missing_estimands.add(plan.estimand_id)
            if plan.mechanism == MissingnessMechanism.UNRESOLVED:
                issues.append(
                    issue(
                        "MISS-MECHANISM",
                        Severity.WARNING,
                        "complex_data",
                        f"缺失原因“{plan.reason}”尚未给出机制假设。",
                        f"missing_data.{index}.mechanism",
                        related_ids=[plan.id, plan.estimand_id],
                    )
                )
            if not plan.primary_method.strip():
                issues.append(
                    issue(
                        "MISS-PRIMARY-METHOD",
                        (
                            Severity.WARNING
                            if plan.mechanism == MissingnessMechanism.UNRESOLVED
                            else Severity.ERROR
                        ),
                        "complex_data",
                        "缺失数据计划缺少主分析处理方法。",
                        f"missing_data.{index}.primary_method",
                        related_ids=[plan.id],
                    )
                )
            if plan.mechanism == MissingnessMechanism.MNAR and not plan.sensitivity_method:
                issues.append(
                    issue(
                        "MISS-MNAR-SENSITIVITY",
                        Severity.WARNING,
                        "complex_data",
                        "MNAR 假设下未给出敏感性分析方法。",
                        f"missing_data.{index}.sensitivity_method",
                        "考虑参考值插补、delta 调整或临界点分析，并由专家确认。",
                        [plan.id],
                    )
                )
        for estimand in ir.estimands:
            if estimand.id not in missing_estimands:
                issues.append(
                    issue(
                        "MISS-PLAN-MISSING",
                        Severity.WARNING,
                        "complex_data",
                        f"估计目标 {estimand.id} 尚无缺失数据计划。",
                        "missing_data",
                        related_ids=[estimand.id],
                    )
                )
        return issues

    def _validate_safety(self, ir: SAPIR) -> list[ValidationIssue]:
        if ir.safety is None:
            return [
                issue(
                    "SAFETY-MISSING",
                    Severity.WARNING,
                    "safety",
                    "缺少安全性分析规格。",
                    "safety",
                    "补充 TEAE 时间窗、MedDRA 版本、SOC/PT 汇总和分母。",
                )
            ]
        issues: list[ValidationIssue] = []
        population_ids = {item.id for item in ir.analysis_populations}
        checks = (
            ("teae_window_start", "TEAE 起点"),
            ("teae_window_end", "TEAE 终点"),
            ("meddra_version", "MedDRA 版本"),
            ("subject_denominator", "受试者分母"),
        )
        for field_name, label in checks:
            value = getattr(ir.safety, field_name)
            if not value or value.strip() in {"待确认", "TBD"}:
                issues.append(
                    issue(
                        f"SAFETY-{field_name.upper()}",
                        Severity.WARNING,
                        "safety",
                        f"安全性分析缺少明确的{label}。",
                        f"safety.{field_name}",
                        related_ids=[ir.safety.id],
                    )
                )
        if not {"SOC", "PT"}.issubset(set(ir.safety.coding_levels)):
            issues.append(
                issue(
                    "SAFETY-CODING-LEVELS",
                    Severity.WARNING,
                    "safety",
                    "不良事件汇总至少应明确 SOC 和 PT 层级。",
                    "safety.coding_levels",
                    related_ids=[ir.safety.id],
                )
            )
        if ir.safety.analysis_population_id not in population_ids:
            issues.append(
                issue(
                    "SAFETY-POPULATION",
                    Severity.ERROR,
                    "safety",
                    "安全性分析分母未关联有效分析人群。",
                    "safety.analysis_population_id",
                    related_ids=[ir.safety.id, ir.safety.analysis_population_id],
                )
            )
        return issues

    def _validate_tfl(self, ir: SAPIR) -> list[ValidationIssue]:
        issues: list[ValidationIssue] = []
        if not ir.tfl_specs:
            issues.append(
                issue(
                    "TFL-MISSING",
                    Severity.WARNING,
                    "tfl",
                    "尚未生成 TFL 规格。",
                    "tfl_specs",
                )
            )
            return issues
        for index, spec in enumerate(ir.tfl_specs):
            required = (
                ("number", "表号"),
                ("title", "标题"),
                ("denominator", "分母"),
            )
            for field_name, label in required:
                if not getattr(spec, field_name).strip():
                    issues.append(
                        issue(
                            f"TFL-{field_name.upper()}",
                            Severity.ERROR,
                            "tfl",
                            f"TFL 缺少{label}。",
                            f"tfl_specs.{index}.{field_name}",
                            related_ids=[spec.id],
                        )
                    )
            if spec.kind == "table" and (not spec.rows or not spec.columns):
                issues.append(
                    issue(
                        "TFL-DIMENSIONS",
                        Severity.ERROR,
                        "tfl",
                        "表格规格必须同时定义行和列。",
                        f"tfl_specs.{index}",
                        related_ids=[spec.id],
                    )
                )
            if not spec.statistics and spec.kind != "listing":
                issues.append(
                    issue(
                        "TFL-STATISTICS",
                        Severity.ERROR,
                        "tfl",
                        "表图规格缺少统计量。",
                        f"tfl_specs.{index}.statistics",
                        related_ids=[spec.id],
                    )
                )
        return issues

    def _validate_provenance(self, ir: SAPIR) -> list[ValidationIssue]:
        issues: list[ValidationIssue] = []
        groups = (
            ("endpoints", ir.endpoints),
            ("estimands", ir.estimands),
            ("analysis_methods", ir.analysis_methods),
            ("intercurrent_events", ir.intercurrent_events),
            ("missing_data", ir.missing_data),
            ("tfl_specs", ir.tfl_specs),
            ("decision_support", ir.decision_support),
        )
        for group_name, records in groups:
            for index, record in enumerate(records):
                provenance = record.provenance
                if provenance.status in {EvidenceStatus.CONFIRMED, EvidenceStatus.USER_CONFIRMED}:
                    if provenance.status == EvidenceStatus.CONFIRMED and not provenance.evidence:
                        issues.append(
                            issue(
                                "TRACE-EVIDENCE-MISSING",
                                Severity.WARNING,
                                "evidence",
                                "记录标记为来源确认，但没有证据定位。",
                                f"{group_name}.{index}.provenance.evidence",
                                related_ids=[record.id],
                            )
                        )
                elif provenance.status == EvidenceStatus.INFERRED:
                    issues.append(
                        issue(
                            "TRACE-INFERRED",
                            Severity.INFO,
                            "evidence",
                            "该记录属于系统推断，导出前应由统计人员确认。",
                            f"{group_name}.{index}.provenance.status",
                            related_ids=[record.id],
                        )
                    )
        return issues
