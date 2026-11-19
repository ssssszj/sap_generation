from __future__ import annotations

from sapgen.domain.models import (
    SAPIR,
    AnalysisPopulation,
    EvidenceStatus,
    Provenance,
    SafetyAnalysisPlan,
)
from sapgen.modules.analysis_design import is_single_arm
from sapgen.modules.common import add_clarification


class SafetyAnalysisModule:
    """Preserve a supported safety contract or add a labelled executable proposal."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        if ir.safety is not None:
            return ir
        population_id, dedicated_safety_population = self._safety_population(ir)
        if population_id is None and ir.study.treatment_arms:
            population = AnalysisPopulation(
                id="SAFETY-PROPOSED",
                name="Proposed Safety Population",
                definition=(
                    "All participants who receive any amount of study intervention, analyzed "
                    "according to treatment actually received."
                ),
                denominator_rule="All exposed participants in the actual-treatment group.",
                provenance=Provenance(
                    status=EvidenceStatus.INFERRED,
                    note="System-proposed safety population; confirmation required.",
                ),
            )
            ir.analysis_populations.append(population)
            population_id = population.id
            dedicated_safety_population = True
        if population_id is not None:
            ir.safety = SafetyAnalysisPlan(
                id="safety-proposed",
                analysis_population_id=population_id,
                teae_window_start="First administration of study intervention (confirm)",
                teae_window_end="Protocol-defined post-treatment safety cutoff (confirm)",
                meddra_version="Version current at database lock; record exact version before finalization",
                coding_levels=["SOC", "PT"],
                subject_denominator=(
                    "All exposed participants"
                    if is_single_arm(ir)
                    else "All exposed participants in each actual-treatment group"
                ),
                event_denominator="Number of treatment-emergent adverse events",
                summaries=[
                    "Any TEAE",
                    "Serious TEAEs",
                    "Severe TEAEs",
                    "Treatment-related TEAEs",
                    "TEAEs leading to interruption or discontinuation",
                    "Deaths",
                    "TEAEs by SOC and PT",
                    "Laboratory values and clinically significant abnormalities",
                    "Vital signs and change from baseline",
                ],
                provenance=Provenance(
                    status=EvidenceStatus.INFERRED,
                    note="System-proposed safety reporting contract; confirmation required.",
                ),
            )
        add_clarification(
            ir,
            item_id="confirm-safety-contract",
            module="safety",
            question=(
                "请确认安全性分析集、实际治疗归属、TEAE起止窗口、MedDRA版本、SOC/PT层级、"
                "受试者与事件计数规则，以及严重性、相关性、SAE、停药和死亡汇总。"
                + (
                    f" 已识别候选安全性人群 {population_id}。"
                    if dedicated_safety_population
                    else ""
                )
            ),
            paths=["analysis_populations", "safety"],
        )
        ir.touch()
        return ir

    @staticmethod
    def _safety_population(ir: SAPIR) -> tuple[str | None, bool]:
        for population in ir.analysis_populations:
            value = f"{population.id} {population.name}".lower()
            if "safety" in value or "安全" in value:
                return population.id, True
        return None, False
