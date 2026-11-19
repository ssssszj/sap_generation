from __future__ import annotations

import re

from sapgen.domain.models import (
    SAPIR,
    AnalysisRole,
    Endpoint,
    EndpointType,
    EvidenceStatus,
    Provenance,
    TFLSpec,
)
from sapgen.modules.analysis_design import is_single_arm


class TFLGenerationModule:
    """Translate every primary/supportive analysis contract into a concrete shell."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        table_number = 1
        endpoint_by_id = {item.id: item for item in ir.endpoints}
        estimand_by_id = {item.id: item for item in ir.estimands}
        population_by_id = {item.id: item for item in ir.analysis_populations}
        linked_methods = {
            method_id for spec in ir.tfl_specs for method_id in spec.source_analysis_ids
        }

        for method in ir.analysis_methods:
            if (
                method.role == AnalysisRole.SENSITIVITY
                or method.id in linked_methods
            ):
                continue
            estimand = estimand_by_id.get(method.estimand_id)
            endpoint = endpoint_by_id.get(estimand.endpoint_id) if estimand else None
            population = population_by_id.get(method.analysis_population_id)
            if estimand is None or endpoint is None or population is None:
                continue
            rows, statistics = self._layout(endpoint.endpoint_type)
            role_label = "Primary" if method.role == AnalysisRole.PRIMARY else "Supportive"
            ir.tfl_specs.append(
                TFLSpec(
                    id=f"tfl-{method.role.value}-{method.id}",
                    number=f"Table 14.2.{table_number}",
                    kind="table",
                    title=f"{role_label} analysis of {endpoint.name}",
                    population_id=population.id,
                    source_analysis_ids=[method.id],
                    rows=rows,
                    columns=self._columns(ir, endpoint),
                    statistics=statistics,
                    unit=self._unit(endpoint),
                    denominator=population.denominator_rule or population.definition,
                    footnotes=[
                        f"Endpoint timing: {endpoint.timepoint or 'confirm scheduled assessment'}.",
                        f"Model: {method.model}.",
                        f"Effect measure: {method.effect_measure}.",
                        f"Test: {method.test_method}.",
                        (
                            "Missing data: "
                            f"{method.missing_data_strategy or 'refer to the estimand-specific plan'}."
                        ),
                        (
                            "Percentages use the displayed analysis-population column denominator; "
                            "observed-data n is shown for every assessment."
                        ),
                    ],
                    provenance=Provenance(
                        status=(
                            EvidenceStatus.CONFIRMED
                            if method.provenance.status
                            in {EvidenceStatus.CONFIRMED, EvidenceStatus.USER_CONFIRMED}
                            else EvidenceStatus.INFERRED
                        ),
                        note=(
                            "Programming shell derived from the linked analysis method, endpoint, "
                            "schedule, and population; inferred source methods remain proposed and "
                            "must be confirmed before production programming."
                        ),
                    ),
                )
            )
            table_number += 1

        if ir.safety is not None and not any(
            spec.id == "tfl-safety-overview" for spec in ir.tfl_specs
        ):
            safety_population = population_by_id.get(ir.safety.analysis_population_id)
            if safety_population is not None:
                ir.tfl_specs.append(
                    TFLSpec(
                        id="tfl-safety-overview",
                        number="Table 14.3.1",
                        kind="table",
                        title="Overview of treatment-emergent adverse events",
                        population_id=safety_population.id,
                        rows=list(ir.safety.summaries),
                        columns=(
                            ["SOC", "PT", "Subjects n (%)", "Events n"]
                            if is_single_arm(ir)
                            else ["SOC", "PT", "Treatment groups", "Total"]
                        ),
                        statistics=["subjects with event n (%)", "number of events"],
                        unit="subjects and events",
                        denominator=ir.safety.subject_denominator,
                        footnotes=[
                            (
                                "TEAE window: "
                                f"{ir.safety.teae_window_start} to {ir.safety.teae_window_end}."
                            ),
                            (
                                f"Adverse events coded using MedDRA {ir.safety.meddra_version} "
                                "and summarized by SOC and PT."
                            ),
                            (
                                "Subject percentages use the safety-population denominator; event "
                                "counts use the number of TEAEs and are not percentages."
                            ),
                        ],
                        provenance=Provenance(
                            status=EvidenceStatus.INFERRED,
                            note="Derived from the proposed safety analysis specification.",
                        ),
                    )
                )
        ir.touch()
        return ir

    @staticmethod
    def _columns(ir: SAPIR, endpoint: Endpoint) -> list[str]:
        if not is_single_arm(ir):
            return ["Treatment groups", "Treatment comparison"]
        visits = [
            visit
            for visit in TFLGenerationModule._visits(endpoint.timepoint)
            if "baseline" not in visit.lower() and "基线" not in visit
        ]
        if not visits:
            visits = ["Post-baseline assessment (confirm timing)"]
        columns = ["Baseline"] if endpoint.endpoint_type != EndpointType.OTHER else []
        columns.extend(visits)
        if endpoint.endpoint_type != EndpointType.OTHER:
            columns.extend(f"Change from baseline at {visit}" for visit in visits)
        return columns or ["Assessment", "Result"]

    @staticmethod
    def _visits(timepoint: str | None) -> list[str]:
        if not timepoint:
            return ["Post-baseline assessment (confirm timing)"]
        lowered = timepoint.lower()
        if any(term in lowered for term in ("not specified", "not stated", "whether")):
            return ["Post-baseline assessment (confirm timing)"]
        cleaned = re.sub(r"\s+post-intervention\s*$", "", timepoint, flags=re.IGNORECASE)
        parts = [
            item.strip(" ,;")
            for item in re.split(r"\s+(?:and|&)\s+|[,;]", cleaned)
            if item.strip(" ,;")
        ]
        return parts or [timepoint]

    @staticmethod
    def _unit(endpoint: Endpoint) -> str:
        if endpoint.endpoint_type == EndpointType.CONTINUOUS:
            return "endpoint score units"
        if endpoint.endpoint_type == EndpointType.BINARY:
            return "subjects and percent"
        if endpoint.endpoint_type == EndpointType.COUNT:
            return "events per protocol-defined assessment period"
        if endpoint.endpoint_type == EndpointType.ORDINAL:
            return "ordered response category"
        if endpoint.endpoint_type == EndpointType.TIME_TO_EVENT:
            return "protocol-defined time unit"
        return "not applicable; qualitative/descriptive output"

    @staticmethod
    def _layout(endpoint_type: EndpointType) -> tuple[list[str], list[str]]:
        if endpoint_type == EndpointType.CONTINUOUS:
            return (
                [
                    "Number in analysis population",
                    "Number with observed data",
                    "Observed endpoint summary",
                    "Model-based change from baseline",
                ],
                ["N", "n", "mean", "SD", "estimate", "SE", "95% CI", "p-value"],
            )
        if endpoint_type == EndpointType.BINARY:
            return (
                ["Number in population", "Number observed", "Number with response", "Time effect"],
                ["N", "n", "%", "odds ratio", "95% CI", "p-value"],
            )
        if endpoint_type == EndpointType.TIME_TO_EVENT:
            return (
                ["Number of subjects", "Number of events", "Time-to-event summary"],
                ["N", "events", "median", "95% CI", "event-free probability"],
            )
        if endpoint_type == EndpointType.COUNT:
            return (
                ["Number in population", "Number observed", "Total exposure", "Event rate"],
                ["N", "n", "exposure", "rate", "rate ratio", "95% CI", "p-value"],
            )
        if endpoint_type == EndpointType.ORDINAL:
            return (
                ["Number observed", "Response category", "Time effect"],
                ["n", "%", "common odds ratio", "95% CI", "p-value"],
            )
        return (
            ["Number assessed", "Theme or endpoint category", "Structured summary"],
            ["n", "% where meaningful", "descriptive summary"],
        )
