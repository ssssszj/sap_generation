from __future__ import annotations

from sapgen.domain.models import (
    SAPIR,
    AnalysisConventions,
    EvidenceStatus,
    MultiplicityPlan,
    Provenance,
)
from sapgen.modules.common import add_clarification


class MultiplicityModule:
    """Preserve protocol rules or add a bounded, clearly labelled fallback."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        if ir.multiplicity is None:
            primary = [item for item in ir.endpoints if item.priority == "primary"]
            if primary:
                endpoint_ids = ", ".join(item.id for item in primary)
                if len(primary) == 1:
                    strategy = (
                        "No multiplicity adjustment for the single primary endpoint. Secondary "
                        "and exploratory analyses are supportive and do not recycle primary alpha."
                    )
                else:
                    strategy = (
                        "Proposed Holm step-down control across the co-primary endpoint family; "
                        "replace with any protocol-specified gatekeeping or graphical procedure."
                    )
                ir.multiplicity = MultiplicityPlan(
                    id="multiplicity-proposed",
                    outcome_family=f"Primary endpoint family: {endpoint_ids}",
                    timepoint_family=(
                        "One prespecified primary timepoint per primary endpoint; confirm where absent."
                    ),
                    strategy=strategy,
                    inferential_thresholds="Proposed two-sided family-wise alpha 0.05.",
                    provenance=Provenance(
                        status=EvidenceStatus.INFERRED,
                        note="System-proposed multiplicity fallback; confirmation required.",
                    ),
                )
                if ir.analysis_conventions is None:
                    ir.analysis_conventions = AnalysisConventions(
                        alpha="Proposed two-sided 0.05",
                        sidedness="two-sided",
                        confidence_level="95%",
                        descriptive_statistics=(
                            "Continuous: n, mean, SD, median, quartiles, minimum and maximum; "
                            "categorical: n and percent."
                        ),
                        provenance=Provenance(
                            status=EvidenceStatus.INFERRED,
                            note="System-proposed conventions; protocol-specific rules take precedence.",
                        ),
                    )
            add_clarification(
                ir,
                item_id="confirm-multiplicity-policy",
                module="multiplicity",
                question=(
                    "请确认适用的检验族、检验层级、单双侧、总体alpha、置信区间水平和"
                    "多重性策略；若研究仅为描述性分析，请明确无正式多重性控制的理由。"
                ),
                paths=["multiplicity", "analysis_conventions"],
            )
        ir.touch()
        return ir
