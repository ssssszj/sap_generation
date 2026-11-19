from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


def utc_now() -> datetime:
    return datetime.now(UTC)


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_assignment=True)


class EvidenceStatus(StrEnum):
    CONFIRMED = "confirmed"
    USER_CONFIRMED = "user_confirmed"
    INFERRED = "inferred"
    MISSING = "missing"


class ReviewStatus(StrEnum):
    OPEN = "open"
    ANSWERED = "answered"
    ACCEPTED = "accepted"
    REJECTED = "rejected"


class EndpointType(StrEnum):
    CONTINUOUS = "continuous"
    BINARY = "binary"
    TIME_TO_EVENT = "time_to_event"
    COUNT = "count"
    ORDINAL = "ordinal"
    OTHER = "other"


class AnalysisRole(StrEnum):
    PRIMARY = "primary"
    SENSITIVITY = "sensitivity"
    SUPPORTIVE = "supportive"


class IntercurrentEventStrategy(StrEnum):
    TREATMENT_POLICY = "treatment_policy"
    HYPOTHETICAL = "hypothetical"
    COMPOSITE = "composite"
    WHILE_ON_TREATMENT = "while_on_treatment"
    PRINCIPAL_STRATUM = "principal_stratum"
    UNRESOLVED = "unresolved"


class MissingnessMechanism(StrEnum):
    MCAR = "MCAR"
    MAR = "MAR"
    MNAR = "MNAR"
    UNRESOLVED = "unresolved"


class Severity(StrEnum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class EvidenceRef(StrictModel):
    source_id: str
    document_name: str
    locator: str = Field(description="Section, page, table, or chunk locator")
    quote: str = Field(min_length=1, max_length=2000)


class Provenance(StrictModel):
    status: EvidenceStatus = EvidenceStatus.MISSING
    evidence: list[EvidenceRef] = Field(default_factory=list)
    note: str | None = None


class StudyDesign(StrictModel):
    study_id: str = "study-001"
    title: str = "待确认"
    phase: str | None = None
    design: str | None = None
    treatment_arms: list[str] = Field(default_factory=list)
    randomization: str | None = None
    blinding: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class SampleSizePlan(StrictModel):
    planned_total: str | None = None
    planned_per_group: dict[str, str] = Field(default_factory=dict)
    statistical_basis: str | None = None
    dropout_assumption: str | None = None
    operational_constraints: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class RandomizationPlan(StrictModel):
    allocation_ratio: str | None = None
    sequence_generation: str | None = None
    stratification_factors: list[str] = Field(default_factory=list)
    concealment: str | None = None
    implementation: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class VisitSchedule(StrictModel):
    time_anchor: str | None = None
    visits: list[str] = Field(default_factory=list)
    visit_windows: list[str] = Field(default_factory=list)
    provenance: Provenance = Field(default_factory=Provenance)


class AnalysisConventions(StrictModel):
    alpha: str | None = None
    sidedness: str | None = None
    confidence_level: str | None = None
    descriptive_statistics: str | None = None
    baseline_definition: str | None = None
    software: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class DerivationRule(StrictModel):
    id: str
    variable: str
    rule: str
    unit: str | None = None
    direction_of_benefit: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class CenterHandlingPlan(StrictModel):
    strategy: str
    interaction_assessment: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class SuccessCriteria(StrictModel):
    rule: str
    linked_endpoint_ids: list[str] = Field(default_factory=list)
    provenance: Provenance = Field(default_factory=Provenance)


class InterimAnalysisPlan(StrictModel):
    planned: bool | None = None
    timing: str | None = None
    decision_rules: str | None = None
    information_flow: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class AnalysisPopulation(StrictModel):
    id: str
    name: str
    definition: str
    denominator_rule: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class Endpoint(StrictModel):
    id: str
    name: str
    endpoint_type: EndpointType
    definition: str
    timepoint: str | None = None
    derivation: str | None = None
    priority: Literal["primary", "secondary", "exploratory", "safety"]
    provenance: Provenance = Field(default_factory=Provenance)


class Estimand(StrictModel):
    id: str
    objective: str
    population: str
    variable: str
    treatment_condition: str
    intercurrent_event_strategies: list[str] = Field(default_factory=list)
    population_summary: str
    endpoint_id: str
    provenance: Provenance = Field(default_factory=Provenance)


class AnalysisMethodSpec(StrictModel):
    id: str
    estimand_id: str
    role: AnalysisRole
    endpoint_type: EndpointType
    analysis_population_id: str
    model: str
    effect_measure: str
    test_method: str
    covariates: list[str] = Field(default_factory=list)
    missing_data_strategy: str | None = None
    assumptions: list[str] = Field(default_factory=list)
    rationale: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class IntercurrentEventPlan(StrictModel):
    id: str
    estimand_id: str
    event: str
    strategy: IntercurrentEventStrategy
    operational_rule: str
    rationale: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class MissingDataPlan(StrictModel):
    id: str
    estimand_id: str
    reason: str
    mechanism: MissingnessMechanism
    primary_method: str
    sensitivity_method: str | None = None
    tipping_point_rule: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class MultiplicityPlan(StrictModel):
    id: str = "multiplicity-001"
    outcome_family: str
    timepoint_family: str
    strategy: str
    inferential_thresholds: str
    provenance: Provenance = Field(default_factory=Provenance)


class SafetyAnalysisPlan(StrictModel):
    id: str = "safety-001"
    analysis_population_id: str
    teae_window_start: str
    teae_window_end: str
    meddra_version: str
    coding_levels: list[Literal["SOC", "HLGT", "HLT", "PT", "LLT"]] = Field(
        default_factory=lambda: ["SOC", "PT"]
    )
    subject_denominator: str
    event_denominator: str | None = None
    summaries: list[str] = Field(default_factory=list)
    provenance: Provenance = Field(default_factory=Provenance)


class TFLSpec(StrictModel):
    id: str
    number: str
    kind: Literal["table", "figure", "listing"]
    title: str
    population_id: str
    source_analysis_ids: list[str] = Field(default_factory=list)
    rows: list[str] = Field(default_factory=list)
    columns: list[str] = Field(default_factory=list)
    statistics: list[str] = Field(default_factory=list)
    unit: str | None = None
    denominator: str
    footnotes: list[str] = Field(default_factory=list)
    provenance: Provenance = Field(default_factory=Provenance)


class ClarificationItem(StrictModel):
    id: str
    module: str
    question: str
    blocking: bool = True
    related_paths: list[str] = Field(default_factory=list)
    status: ReviewStatus = ReviewStatus.OPEN
    answer: str | None = None


class DecisionSupportItem(StrictModel):
    id: str
    domain: Literal[
        "estimand",
        "sample_size",
        "population",
        "intercurrent_event",
        "missing_data",
        "sensitivity",
        "safety",
        "tfl",
        "derivation",
        "method",
    ]
    status: Literal["conditional_proposal", "unresolved"]
    recommendation: str
    conditions: list[str] = Field(default_factory=list)
    related_ids: list[str] = Field(default_factory=list)
    rationale: str | None = None
    provenance: Provenance = Field(default_factory=Provenance)


class SAPSection(StrictModel):
    id: str
    title: str
    body_markdown: str
    source_paths: list[str] = Field(default_factory=list)


class SAPIR(StrictModel):
    schema_version: str = "1.0"
    study: StudyDesign = Field(default_factory=StudyDesign)
    sample_size: SampleSizePlan | None = None
    randomization_plan: RandomizationPlan | None = None
    visit_schedule: VisitSchedule | None = None
    analysis_conventions: AnalysisConventions | None = None
    center_handling: CenterHandlingPlan | None = None
    success_criteria: SuccessCriteria | None = None
    interim_analysis: InterimAnalysisPlan | None = None
    analysis_populations: list[AnalysisPopulation] = Field(default_factory=list)
    endpoints: list[Endpoint] = Field(default_factory=list)
    derivation_rules: list[DerivationRule] = Field(default_factory=list)
    estimands: list[Estimand] = Field(default_factory=list)
    analysis_methods: list[AnalysisMethodSpec] = Field(default_factory=list)
    intercurrent_events: list[IntercurrentEventPlan] = Field(default_factory=list)
    missing_data: list[MissingDataPlan] = Field(default_factory=list)
    multiplicity: MultiplicityPlan | None = None
    safety: SafetyAnalysisPlan | None = None
    tfl_specs: list[TFLSpec] = Field(default_factory=list)
    decision_support: list[DecisionSupportItem] = Field(default_factory=list)
    clarifications: list[ClarificationItem] = Field(default_factory=list)
    generated_sections: list[SAPSection] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    @model_validator(mode="after")
    def unique_ids(self) -> SAPIR:
        groups = [
            self.analysis_populations,
            self.endpoints,
            self.derivation_rules,
            self.estimands,
            self.analysis_methods,
            self.intercurrent_events,
            self.missing_data,
            self.tfl_specs,
            self.decision_support,
            self.clarifications,
            self.generated_sections,
        ]
        for group in groups:
            ids = [item.id for item in group]
            if len(ids) != len(set(ids)):
                raise ValueError(f"duplicate ids detected: {ids}")
        return self

    def touch(self) -> None:
        self.updated_at = utc_now()


class ValidationIssue(StrictModel):
    code: str
    severity: Severity
    module: str
    message: str
    path: str
    suggested_fix: str | None = None
    related_ids: list[str] = Field(default_factory=list)
    evidence: list[EvidenceRef] = Field(default_factory=list)


class ValidationReport(StrictModel):
    issues: list[ValidationIssue] = Field(default_factory=list)

    @property
    def has_errors(self) -> bool:
        return any(issue.severity == Severity.ERROR for issue in self.issues)

    def counts(self) -> dict[str, int]:
        result = {severity.value: 0 for severity in Severity}
        for issue in self.issues:
            result[issue.severity.value] += 1
        return result


class PipelineResult(StrictModel):
    project_id: str
    run_id: str
    ir_path: str
    draft_markdown_path: str
    docx_path: str
    tfl_docx_path: str
    validation_path: str
    report: ValidationReport
    harness_session_id: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
