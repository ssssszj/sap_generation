from __future__ import annotations

from dataclasses import dataclass

from sapgen.domain.models import (
    SAPIR,
    AnalysisMethodSpec,
    AnalysisPopulation,
    AnalysisRole,
    Endpoint,
    EndpointType,
    Estimand,
    EvidenceStatus,
    Provenance,
)
from sapgen.modules.common import add_clarification


@dataclass(frozen=True, slots=True)
class MethodCandidate:
    model: str
    effect_measure: str
    test_method: str
    assumptions: tuple[str, ...]


MULTI_ARM_CANDIDATES: dict[EndpointType, MethodCandidate] = {
    EndpointType.CONTINUOUS: MethodCandidate(
        model="ANCOVA with treatment as a fixed effect and baseline value as a covariate",
        effect_measure="adjusted mean difference with two-sided 95% confidence interval",
        test_method="two-sided Wald test at alpha 0.05",
        assumptions=("linearity", "approximately normal residuals", "homogeneous variance"),
    ),
    EndpointType.BINARY: MethodCandidate(
        model="logistic regression with treatment as a fixed effect",
        effect_measure="odds ratio with two-sided 95% confidence interval",
        test_method="two-sided Wald test at alpha 0.05",
        assumptions=("independent observations", "correct link function"),
    ),
    EndpointType.TIME_TO_EVENT: MethodCandidate(
        model="Cox proportional hazards regression with treatment as a covariate",
        effect_measure="hazard ratio with two-sided 95% confidence interval",
        test_method="stratified log-rank test at two-sided alpha 0.05",
        assumptions=("proportional hazards", "non-informative censoring"),
    ),
    EndpointType.COUNT: MethodCandidate(
        model="negative binomial regression with log exposure as an offset",
        effect_measure="rate ratio with two-sided 95% confidence interval",
        test_method="two-sided Wald test at alpha 0.05",
        assumptions=("conditional mean-variance relationship",),
    ),
    EndpointType.ORDINAL: MethodCandidate(
        model="proportional odds logistic regression",
        effect_measure="common odds ratio with two-sided 95% confidence interval",
        test_method="two-sided Wald test at alpha 0.05",
        assumptions=("proportional odds",),
    ),
    EndpointType.OTHER: MethodCandidate(
        model="descriptive analysis appropriate to the endpoint definition",
        effect_measure="endpoint-specific descriptive summary",
        test_method="no formal hypothesis test unless prespecified after review",
        assumptions=(),
    ),
}


SINGLE_ARM_REPEATED_CANDIDATES: dict[EndpointType, MethodCandidate] = {
    EndpointType.CONTINUOUS: MethodCandidate(
        model=(
            "linear mixed-effects model with categorical time as a fixed effect and a "
            "participant-specific random intercept"
        ),
        effect_measure=(
            "estimated mean change from baseline at each post-baseline timepoint with "
            "two-sided 95% confidence intervals"
        ),
        test_method=(
            "two-sided Wald tests of prespecified baseline-to-follow-up contrasts at alpha 0.05"
        ),
        assumptions=(
            "approximately normal conditional residuals",
            "correct within-participant covariance structure",
            "missing at random conditional on observed data",
        ),
    ),
    EndpointType.BINARY: MethodCandidate(
        model=(
            "logistic generalized linear mixed model with categorical time as a fixed effect "
            "and a participant-specific random intercept"
        ),
        effect_measure="odds ratio at each follow-up versus baseline with 95% confidence interval",
        test_method="two-sided Wald tests of time contrasts at alpha 0.05",
        assumptions=("correct logit link", "adequate within-participant correlation model"),
    ),
    EndpointType.COUNT: MethodCandidate(
        model=(
            "negative binomial generalized linear mixed model with categorical time as a fixed "
            "effect and a participant-specific random intercept"
        ),
        effect_measure="rate ratio at each follow-up versus baseline with 95% confidence interval",
        test_method="two-sided Wald tests of time contrasts at alpha 0.05",
        assumptions=("negative-binomial mean-variance relationship", "correct exposure offset"),
    ),
    EndpointType.ORDINAL: MethodCandidate(
        model=(
            "cumulative-logit mixed model with categorical time as a fixed effect and a "
            "participant-specific random intercept"
        ),
        effect_measure="common odds ratio at each follow-up versus baseline with 95% CI",
        test_method="two-sided Wald tests of time contrasts at alpha 0.05",
        assumptions=("proportional odds", "adequate within-participant correlation model"),
    ),
    EndpointType.TIME_TO_EVENT: MethodCandidate(
        model="Kaplan-Meier analysis for the single study cohort",
        effect_measure=(
            "median time-to-event and event-free probability with 95% confidence intervals"
        ),
        test_method="descriptive inference; no between-group test for a single cohort",
        assumptions=("non-informative censoring",),
    ),
    EndpointType.OTHER: MethodCandidate(
        model="descriptive or qualitative thematic analysis appropriate to the endpoint",
        effect_measure="theme frequencies and structured descriptive summaries",
        test_method="no formal hypothesis test",
        assumptions=("prespecified coding framework",),
    ),
}


def is_single_arm(ir: SAPIR) -> bool:
    """Return true only when extraction supports a within-cohort interpretation."""

    if len(ir.study.treatment_arms) > 1:
        return False
    randomization = (ir.study.randomization or "").strip().lower()
    no_randomization_terms = (
        "none",
        "not specified",
        "not described",
        "no randomization",
        "no randomisation",
        "non-randomized",
        "non-randomised",
        "n/a",
    )
    if randomization and not any(term in randomization for term in no_randomization_terms):
        return False
    design_text = " ".join(
        [
            ir.study.design or "",
            ir.study.provenance.note or "",
            *(item.treatment_condition for item in ir.estimands),
        ]
    ).lower()
    signals = (
        "single-arm",
        "single arm",
        "single-group",
        "single group",
        "no comparator",
        "within-participant",
        "within participant",
        "pre-post",
        "pre post",
    )
    return len(ir.study.treatment_arms) == 1 or any(signal in design_text for signal in signals)


def has_repeated_measurements(ir: SAPIR, endpoint: Endpoint) -> bool:
    text = " ".join(
        [
            ir.study.design or "",
            endpoint.timepoint or "",
            endpoint.definition,
            endpoint.derivation or "",
        ]
    ).lower()
    has_baseline = "baseline" in text or "基线" in text
    followup_terms = ("follow-up", "follow up", "post-baseline", "week", "month", "随访")
    multiple_time_terms = (" and ", ",", "multiple", "repeated", "2 weeks", "3 months")
    return (
        has_baseline
        and any(term in text for term in followup_terms)
        and any(term in text for term in multiple_time_terms)
    )


class AnalysisDesignModule:
    """Preserve supported decisions and add explicitly labelled executable fallbacks."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        self._ensure_endpoint_hierarchy(ir)
        self._ensure_analysis_population(ir)
        self._ensure_primary_estimands(ir)
        endpoints = {endpoint.id: endpoint for endpoint in ir.endpoints}
        estimands = {estimand.id: estimand for estimand in ir.estimands}
        self._repair_inferred_roles(ir, estimands, endpoints)
        population_id = self._default_population(ir)
        for estimand in ir.estimands:
            endpoint = endpoints.get(estimand.endpoint_id)
            if endpoint is None:
                continue
            expected_role = (
                AnalysisRole.PRIMARY if endpoint.priority == "primary" else AnalysisRole.SUPPORTIVE
            )
            existing = next(
                (
                    method
                    for method in ir.analysis_methods
                    if method.estimand_id == estimand.id and method.role == expected_role
                ),
                None,
            )
            if existing is not None:
                self._complete_placeholder_method(existing, self._candidate(ir, endpoint), endpoint)
                continue
            if population_id is not None:
                candidate = self._candidate(ir, endpoint)
                method = AnalysisMethodSpec(
                    id=f"analysis-proposed-{estimand.id}",
                    estimand_id=estimand.id,
                    role=expected_role,
                    endpoint_type=endpoint.endpoint_type,
                    analysis_population_id=population_id,
                    model=candidate.model,
                    effect_measure=candidate.effect_measure,
                    test_method=candidate.test_method,
                    covariates=self._candidate_covariates(candidate, endpoint),
                    assumptions=list(candidate.assumptions),
                    rationale=(
                        "Executable design-aware fallback selected from arm structure, endpoint "
                        "scale and visit schedule. It is a proposed SAP decision requiring review, "
                        "not a claim about the protocol."
                    ),
                    provenance=Provenance(
                        status=EvidenceStatus.INFERRED,
                        note="System-proposed executable analysis; confirm before SAP finalization.",
                    ),
                )
                ir.analysis_methods.append(method)
            add_clarification(
                ir,
                item_id=f"confirm-analysis-{estimand.id}",
                module="analysis_design",
                question=(
                    f"请确认估计目标 {estimand.id} 的系统建议分析，包括人群、模型、效应量、"
                    "协变量/分层因素、不确定性区间和判定规则。"
                ),
                paths=["analysis_methods"],
            )
        ir.touch()
        return ir

    @staticmethod
    def _ensure_analysis_population(ir: SAPIR) -> None:
        if ir.analysis_populations or not ir.endpoints:
            return
        randomization = (ir.study.randomization or "").lower()
        randomized = any(
            term in randomization for term in ("randomized", "randomised", "randomly")
        ) and not any(
            term in randomization
            for term in ("not randomized", "not randomised", "non-random", "no random")
        )
        definition = (
            "All randomized participants, analyzed according to randomized treatment assignment, "
            "regardless of adherence or treatment discontinuation."
            if randomized or len(ir.study.treatment_arms) > 1
            else (
                "All enrolled eligible participants, retained in the analysis regardless of "
                "intervention completion."
            )
        )
        ir.analysis_populations.append(
            AnalysisPopulation(
                id="FAS-PROPOSED",
                name="Proposed Full Analysis Set",
                definition=definition,
                denominator_rule="All participants meeting the proposed membership rule.",
                provenance=Provenance(
                    status=EvidenceStatus.INFERRED,
                    note="System-proposed analysis population; confirmation required.",
                ),
            )
        )

    @classmethod
    def _ensure_primary_estimands(cls, ir: SAPIR) -> None:
        existing = {item.endpoint_id for item in ir.estimands}
        population = cls._default_population(ir)
        population_name = next(
            (item.name for item in ir.analysis_populations if item.id == population),
            "Proposed target population",
        )
        treatment = (
            " versus ".join(ir.study.treatment_arms)
            if len(ir.study.treatment_arms) > 1
            else (ir.study.treatment_arms[0] if ir.study.treatment_arms else "Study intervention")
        )
        for endpoint in ir.endpoints:
            if endpoint.priority != "primary" or endpoint.id in existing:
                continue
            ir.estimands.append(
                Estimand(
                    id=f"estimand-proposed-{endpoint.id}",
                    objective=f"Estimate the treatment effect for {endpoint.name}",
                    population=population_name,
                    variable=endpoint.definition,
                    treatment_condition=treatment,
                    population_summary=cls._population_summary(endpoint.endpoint_type),
                    endpoint_id=endpoint.id,
                    provenance=Provenance(
                        status=EvidenceStatus.INFERRED,
                        note="System-proposed estimand frame; confirmation required.",
                    ),
                )
            )

    @staticmethod
    def _population_summary(endpoint_type: EndpointType) -> str:
        return {
            EndpointType.CONTINUOUS: "adjusted mean difference or mean change, with 95% CI",
            EndpointType.BINARY: "odds ratio and response proportions, with 95% CIs",
            EndpointType.TIME_TO_EVENT: "hazard ratio and event-free probabilities, with 95% CIs",
            EndpointType.COUNT: "rate ratio with 95% CI",
            EndpointType.ORDINAL: "common odds ratio with 95% CI",
            EndpointType.OTHER: "structured descriptive summary",
        }[endpoint_type]

    @staticmethod
    def _ensure_endpoint_hierarchy(ir: SAPIR) -> None:
        if not ir.endpoints or any(endpoint.priority == "primary" for endpoint in ir.endpoints):
            return
        title_tokens = {
            token for token in ir.study.title.lower().replace("-", " ").split() if len(token) >= 4
        }

        def relevance(endpoint: Endpoint) -> tuple[int, int]:
            value = f"{endpoint.name} {endpoint.definition}".lower()
            overlap = sum(token in value for token in title_tokens)
            quantitative = int(endpoint.endpoint_type != EndpointType.OTHER)
            return overlap, quantitative

        proposed_primary = max(ir.endpoints, key=relevance)
        proposed_primary.priority = "primary"
        proposed_primary.provenance = Provenance(
            status=EvidenceStatus.INFERRED,
            evidence=list(proposed_primary.provenance.evidence),
            note=(
                "The protocol did not declare a formal endpoint hierarchy. This endpoint is a "
                "proposed primary because it most directly matches the study title/objective; "
                "confirmation is required."
            ),
        )
        for endpoint in ir.endpoints:
            if endpoint.id == proposed_primary.id or endpoint.priority != "exploratory":
                continue
            if endpoint.endpoint_type != EndpointType.OTHER:
                endpoint.priority = "secondary"
                endpoint.provenance = Provenance(
                    status=EvidenceStatus.INFERRED,
                    evidence=list(endpoint.provenance.evidence),
                    note=(
                        "The protocol did not declare a formal hierarchy; this quantitative "
                        "outcome is proposed as secondary and requires confirmation."
                    ),
                )
        add_clarification(
            ir,
            item_id="confirm-endpoint-hierarchy-proposal",
            module="analysis_design",
            question=(
                f"方案未声明正式终点层级。请确认将 {proposed_primary.name} 作为 proposed "
                "primary、其他定量结局作为 secondary、定性结局作为 exploratory。"
            ),
            paths=["endpoints"],
        )

    @classmethod
    def _complete_placeholder_method(
        cls,
        method: AnalysisMethodSpec,
        candidate: MethodCandidate,
        endpoint: Endpoint,
    ) -> bool:
        changed = False
        if cls._is_missing(method.model):
            method.model = candidate.model
            changed = True
        if cls._is_missing(method.effect_measure):
            method.effect_measure = candidate.effect_measure
            changed = True
        if cls._is_missing(method.test_method):
            method.test_method = candidate.test_method
            changed = True
        if not method.assumptions or all(cls._is_missing(item) for item in method.assumptions):
            method.assumptions = list(candidate.assumptions)
            changed = True
        if not method.covariates or all(cls._is_missing(item) for item in method.covariates):
            method.covariates = cls._candidate_covariates(candidate, endpoint)
        if changed:
            method.rationale = (
                "The protocol did not specify an analysis. This design-aware proposal uses the "
                "extracted arm structure, schedule, endpoint type, and hierarchy and requires "
                "statistical confirmation."
            )
            method.provenance = Provenance(
                status=EvidenceStatus.INFERRED,
                note="Placeholder completed by design-aware deterministic rules.",
            )
        return changed

    @staticmethod
    def _repair_inferred_roles(
        ir: SAPIR,
        estimands: dict[str, object],
        endpoints: dict[str, Endpoint],
    ) -> None:
        for method in ir.analysis_methods:
            estimand = estimands.get(method.estimand_id)
            endpoint = endpoints.get(getattr(estimand, "endpoint_id", ""))
            if (
                endpoint is not None
                and endpoint.priority != "primary"
                and method.role == AnalysisRole.PRIMARY
                and method.provenance.status in {EvidenceStatus.INFERRED, EvidenceStatus.MISSING}
            ):
                method.role = AnalysisRole.SUPPORTIVE

    @staticmethod
    def _candidate(ir: SAPIR, endpoint: Endpoint) -> MethodCandidate:
        if is_single_arm(ir) and has_repeated_measurements(ir, endpoint):
            return SINGLE_ARM_REPEATED_CANDIDATES[endpoint.endpoint_type]
        return MULTI_ARM_CANDIDATES[endpoint.endpoint_type]

    @staticmethod
    def _default_population(ir: SAPIR) -> str | None:
        preferred = ("full analysis", "intent-to-treat", "itt", "fas", "eligible")
        for population in ir.analysis_populations:
            value = f"{population.id} {population.name}".lower()
            if any(term in value for term in preferred):
                return population.id
        return ir.analysis_populations[0].id if ir.analysis_populations else None

    @staticmethod
    def _candidate_covariates(candidate: MethodCandidate, endpoint: Endpoint) -> list[str]:
        if endpoint.endpoint_type == EndpointType.CONTINUOUS and "ANCOVA" in candidate.model:
            return ["baseline value of the endpoint"]
        return []

    @staticmethod
    def _is_missing(value: str | None) -> bool:
        if not value:
            return True
        normalized = value.strip().lower().rstrip(".;:")
        return normalized in {
            "待确认",
            "tbd",
            "not specified",
            "not specified in the protocol",
            "unresolved",
        }
