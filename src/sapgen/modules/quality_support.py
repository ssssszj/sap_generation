from __future__ import annotations

from sapgen.domain.models import (
    SAPIR,
    AnalysisPopulation,
    DecisionSupportItem,
    Endpoint,
    EndpointType,
    EvidenceStatus,
    Provenance,
    TFLSpec,
)


def _add_support(ir: SAPIR, item: DecisionSupportItem) -> None:
    if not any(existing.id == item.id for existing in ir.decision_support):
        ir.decision_support.append(item)


def _proposal_provenance(note: str) -> Provenance:
    return Provenance(status=EvidenceStatus.INFERRED, note=note)


def _primary_population(ir: SAPIR) -> AnalysisPopulation | None:
    preferred = ("full analysis", "intent-to-treat", "itt", "fas", "eligible")
    for population in ir.analysis_populations:
        value = f"{population.id} {population.name}".lower()
        if any(term in value for term in preferred):
            return population
    return next(
        (
            population
            for population in ir.analysis_populations
            if "safety" not in f"{population.id} {population.name}".lower()
        ),
        None,
    )


class EstimandDecisionModule:
    """Create complete, conditional estimand and ICE decision frames for primary questions."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        population = _primary_population(ir)
        estimand_by_endpoint = {item.endpoint_id: item for item in ir.estimands}
        arms = " versus ".join(ir.study.treatment_arms) if ir.study.treatment_arms else None
        for endpoint in (item for item in ir.endpoints if item.priority == "primary"):
            estimand = estimand_by_endpoint.get(endpoint.id)
            if estimand is None:
                recommendation = (
                    f"Define one integrated estimand for {endpoint.name}: population="
                    f"{population.name if population else '[confirm target population]'}; "
                    f"treatment condition={arms or '[confirm treatment condition/comparator]'}; "
                    f"variable={endpoint.definition}; intercurrent-event strategies=[confirm per "
                    "event]; population summary=[select the measure matching the clinical question "
                    "and analysis method]."
                )
                conditions = [
                    "Confirm the target analysis population.",
                    "Confirm which post-randomization events are relevant.",
                    "Confirm the population-level summary before finalization.",
                ]
                related = [endpoint.id]
            else:
                recommendation = (
                    f"Keep the five estimand attributes jointly visible for {endpoint.name}: "
                    f"population={estimand.population}; treatment condition="
                    f"{estimand.treatment_condition}; variable={estimand.variable}; "
                    f"intercurrent-event strategy={'; '.join(estimand.intercurrent_event_strategies) or '[confirm per event]'}; "
                    f"population summary={estimand.population_summary}."
                )
                conditions = ["Reconcile every attribute with the primary analysis and TFL."]
                related = [endpoint.id, estimand.id]
            _add_support(
                ir,
                DecisionSupportItem(
                    id=f"support-estimand-{endpoint.id}",
                    domain="estimand",
                    status="conditional_proposal",
                    recommendation=recommendation,
                    conditions=conditions,
                    related_ids=related,
                    rationale=(
                        "A primary clinical question should be expressed as one coherent estimand; "
                        "unconfirmed attributes remain conditional rather than protocol facts."
                    ),
                    provenance=_proposal_provenance(
                        "System decision frame derived from extracted primary-endpoint facts."
                    ),
                ),
            )
            _add_support(
                ir,
                DecisionSupportItem(
                    id=f"support-ice-{endpoint.id}",
                    domain="intercurrent_event",
                    status="unresolved",
                    recommendation=(
                        "For treatment discontinuation/non-completion, treatment switching or "
                        "alternative therapy, rescue treatment, and death before assessment: first "
                        "determine applicability, then select treatment-policy, hypothetical, "
                        "composite, while-on-treatment, or principal-stratum handling according to "
                        "the treatment effect being estimated; state the operational data rule for "
                        "each applicable event. Explicitly state when an event is not applicable."
                    ),
                    conditions=[
                        "Do not apply the same strategy automatically to every event.",
                        "Do not treat an intercurrent event as ordinary missingness without justification.",
                    ],
                    related_ids=[endpoint.id],
                    rationale="Makes post-randomization event handling explicit without choosing it blindly.",
                    provenance=_proposal_provenance(
                        "Applicability and strategy require protocol and clinical confirmation."
                    ),
                ),
            )
        ir.touch()
        return ir


class SamplePopulationSpecificationModule:
    """Make sample-size distinctions and population membership operationally visible."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        sample = ir.sample_size
        if sample is None:
            recommendation = (
                "Confirm the prospective total and per-group sample size, statistical calculation "
                "inputs, dropout allowance, and any larger operational target; do not substitute "
                "actual enrollment for the prospective target."
            )
            status = "unresolved"
        else:
            per_group = (
                ", ".join(f"{name}={value}" for name, value in sample.planned_per_group.items())
                or "[confirm per-group allocation]"
            )
            recommendation = (
                f"Report planned total={sample.planned_total or '[confirm]'} and {per_group}; "
                f"statistical basis={sample.statistical_basis or '[confirm power/precision inputs]'}; "
                f"dropout assumption={sample.dropout_assumption or '[confirm]'}; operational "
                f"constraints={sample.operational_constraints or '[confirm whether distinct from the statistical minimum]'}."
            )
            status = "conditional_proposal"
        _add_support(
            ir,
            DecisionSupportItem(
                id="support-sample-size-contract",
                domain="sample_size",
                status=status,
                recommendation=recommendation,
                conditions=[
                    "Keep the statistical minimum distinct from the final operational target.",
                    "State when the study is descriptive, feasibility-focused, or not formally powered.",
                ],
                rationale="Prevents omission or conflation of prospective sample-size quantities.",
                provenance=_proposal_provenance(
                    "Assembled from the extracted sample-size record; missing values remain open."
                ),
            ),
        )

        if not ir.analysis_populations:
            _add_support(
                ir,
                DecisionSupportItem(
                    id="support-analysis-populations",
                    domain="population",
                    status="unresolved",
                    recommendation=(
                        "Define each efficacy, per-protocol, and safety population with operational "
                        "membership, exclusion, treatment-attribution, and denominator rules; bind "
                        "every analysis and TFL to exactly one appropriate population."
                    ),
                    provenance=_proposal_provenance(
                        "No operational analysis population was extracted."
                    ),
                ),
            )
        for population in ir.analysis_populations:
            value = f"{population.id} {population.name}".lower()
            additions = []
            if "per-protocol" in value or "per protocol" in value or "pps" in value:
                additions.append(
                    "state actionable major-deviation exclusions and its relationship to FAS/ITT"
                )
            if "safety" in value:
                additions.append("state exposure eligibility and actual-treatment attribution")
            recommendation = (
                f"Population {population.name}: membership={population.definition}; denominator="
                f"{population.denominator_rule or '[confirm]'}"
            )
            if additions:
                recommendation += "; additionally " + "; ".join(additions)
            _add_support(
                ir,
                DecisionSupportItem(
                    id=f"support-population-{population.id}",
                    domain="population",
                    status="conditional_proposal",
                    recommendation=recommendation,
                    conditions=[
                        "Use the same membership and denominator rule in methods, safety, and TFLs."
                    ],
                    related_ids=[population.id],
                    rationale="Makes analysis-population definitions executable and consistently bound.",
                    provenance=_proposal_provenance(
                        "Derived from the extracted population definition without changing membership."
                    ),
                ),
            )
        ir.touch()
        return ir


class MethodSpecificationModule:
    """Audit the complete primary-analysis contract without selecting a model."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        estimand_by_endpoint = {item.endpoint_id: item for item in ir.estimands}
        for endpoint in (item for item in ir.endpoints if item.priority == "primary"):
            estimand = estimand_by_endpoint.get(endpoint.id)
            methods = (
                [item for item in ir.analysis_methods if item.estimand_id == estimand.id]
                if estimand
                else []
            )
            method = next((item for item in methods if item.role.value == "primary"), None)
            if method is None:
                recommendation = (
                    f"Freeze the primary analysis for {endpoint.name}: analysis population, treatment "
                    "contrast, model/test or descriptive method, covariates and stratification, effect "
                    "estimate, uncertainty interval, alpha/sidedness when inferential, missing-data "
                    "handling, and decision rule. Preserve protocol-specified qualitative or "
                    "descriptive intent."
                )
                status = "unresolved"
                related = [endpoint.id, *([estimand.id] if estimand else [])]
            else:
                recommendation = (
                    f"Primary analysis for {endpoint.name}: population={method.analysis_population_id}; "
                    f"model/method={method.model}; effect measure={method.effect_measure}; test/decision="
                    f"{method.test_method}; covariates/strata={', '.join(method.covariates) or '[none stated]'}; "
                    f"missing handling={method.missing_data_strategy or '[confirm]'}."
                )
                status = "conditional_proposal"
                related = (
                    [endpoint.id, estimand.id, method.id] if estimand else [endpoint.id, method.id]
                )
            _add_support(
                ir,
                DecisionSupportItem(
                    id=f"support-method-contract-{endpoint.id}",
                    domain="method",
                    status=status,
                    recommendation=recommendation,
                    conditions=[
                        "Use center and randomization strata exactly as supported by the source.",
                        "Do not add formal inference to a descriptive or feasibility objective.",
                        "Keep the effect estimate, interval and decision rule aligned with the estimand.",
                    ],
                    related_ids=related,
                    rationale="Prevents a named test from standing in for an incomplete executable analysis contract.",
                    provenance=_proposal_provenance(
                        "Method completeness audit; unsupported choices remain unresolved."
                    ),
                ),
            )
        ir.touch()
        return ir


class RobustnessDecisionModule:
    """Tie missing-data and sensitivity proposals to the primary method's actual assumptions."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        estimands = {item.id: item for item in ir.estimands}
        methods_by_endpoint: dict[str, list] = {}
        for method in ir.analysis_methods:
            estimand = estimands.get(method.estimand_id)
            if estimand is not None:
                methods_by_endpoint.setdefault(estimand.endpoint_id, []).append(method)
        for endpoint in (item for item in ir.endpoints if item.priority == "primary"):
            methods = methods_by_endpoint.get(endpoint.id, [])
            method = next((item for item in methods if item.role.value == "primary"), None)
            _add_support(
                ir,
                DecisionSupportItem(
                    id=f"support-missing-{endpoint.id}",
                    domain="missing_data",
                    status="conditional_proposal" if method else "unresolved",
                    recommendation=self._missing_recommendation(endpoint, method),
                    conditions=[
                        "Tabulate missingness and reasons by treatment group and scheduled timepoint.",
                        "Keep the primary handling consistent in the method, missing-data, and TFL chapters.",
                    ],
                    related_ids=[endpoint.id, *([method.id] if method else [])],
                    rationale="Missing-data handling must follow the endpoint and primary analysis.",
                    provenance=_proposal_provenance(
                        "Conditional statistical support; protocol-specified handling takes precedence."
                    ),
                ),
            )
            _add_support(
                ir,
                DecisionSupportItem(
                    id=f"support-sensitivity-{endpoint.id}",
                    domain="sensitivity",
                    status="conditional_proposal" if method else "unresolved",
                    recommendation=self._sensitivity_recommendation(endpoint, method),
                    conditions=[
                        "Name the primary assumption being changed.",
                        "Preserve the primary estimand unless the sensitivity analysis intentionally changes it.",
                        "Define how robustness will be judged from estimates, intervals, and conclusion stability.",
                    ],
                    related_ids=[endpoint.id, *([method.id] if method else [])],
                    rationale="A sensitivity analysis must change a material assumption, not merely repeat the primary model.",
                    provenance=_proposal_provenance(
                        "Endpoint-type guidance gated by the presence of a primary method."
                    ),
                ),
            )
        ir.touch()
        return ir

    @staticmethod
    def _missing_recommendation(endpoint: Endpoint, method: object | None) -> str:
        if method is None:
            return (
                f"For {endpoint.name}, confirm the missingness assumptions and an operational "
                "primary handling method after the primary analysis model is frozen; do not choose "
                "MAR, imputation, LOCF, nonresponder imputation, or complete case by default."
            )
        stated = getattr(method, "missing_data_strategy", None)
        if stated:
            return f"Use the extracted primary handling for {endpoint.name}: {stated}"
        return (
            f"The primary method for {endpoint.name} is {getattr(method, 'model', 'defined')}. "
            "Confirm the compatible likelihood, imputation, censoring, or observed-data rule and "
            "the covariates/history included in the missingness assumption."
        )

    @staticmethod
    def _sensitivity_recommendation(endpoint: Endpoint, method: object | None) -> str:
        if method is None:
            return (
                f"Freeze the primary method for {endpoint.name} before selecting a sensitivity "
                "analysis; then change its key missingness, distributional, censoring, covariance, "
                "or population assumption in an executable alternative."
            )
        model = str(getattr(method, "model", "")).lower()
        if "descriptive" in model or "qualitative" in model:
            return (
                "No inferential sensitivity model should be added automatically. Confirm whether "
                "robustness is needed for coding, denominator, visit-window, or descriptive-summary rules."
            )
        if endpoint.endpoint_type == EndpointType.CONTINUOUS:
            return (
                "If the primary analysis relies on MAR or repeated-measures assumptions, use a "
                "prespecified MNAR pattern-mixture/reference-based or delta-adjusted analysis and, "
                "where material, an alternative covariance/distribution specification."
            )
        if endpoint.endpoint_type == EndpointType.BINARY:
            return (
                "Vary the handling of missing binary responses using clinically ordered response "
                "scenarios or a prespecified imputation model; assess exact/model-based inference "
                "only when small-cell behavior is a primary-method assumption."
            )
        if endpoint.endpoint_type == EndpointType.TIME_TO_EVENT:
            return (
                "Vary informative-censoring and competing-risk assumptions using a prespecified "
                "alternative that preserves the clinical event definition and time origin."
            )
        if endpoint.endpoint_type == EndpointType.COUNT:
            return (
                "Assess the count distribution, overdispersion, zero inflation, and exposure-offset "
                "assumptions with a prespecified alternative model."
            )
        return "Change the primary model's material assumption in a prespecified executable alternative."


class SafetySpecificationModule:
    """Build a complete conditional safety contract without inventing a denominator or window."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        text = " ".join(
            [
                ir.study.title,
                ir.study.design or "",
                *ir.study.treatment_arms,
                *(endpoint.name for endpoint in ir.endpoints),
            ]
        ).lower()
        applicable = bool(ir.study.treatment_arms) or any(
            term in text for term in ("safety", "drug", "treatment", "intervention", "adverse")
        )
        if not applicable:
            return ir
        safety_population = next(
            (
                item
                for item in ir.analysis_populations
                if "safety" in f"{item.id} {item.name}".lower()
            ),
            None,
        )
        recommendation = (
            "Define the safety population using an operational exposure/treatment rule and actual-"
            "treatment attribution; define the TEAE start/end window; identify the coding dictionary "
            "and version; summarize participant incidence and event counts by SOC and PT, severity, "
            "seriousness, relationship, action taken, discontinuation, and death; use the safety-"
            "population denominator consistently; separately summarize laboratories, vital signs, "
            "ECG or other protocol-specified safety domains."
        )
        conditions = [
            f"Safety population candidate: {safety_population.id}."
            if safety_population
            else "A dedicated safety population and denominator must be confirmed.",
            "The TEAE window and MedDRA version must come from the protocol, data standard, or confirmation.",
            "Do not add inferential treatment tests unless explicitly planned.",
        ]
        _add_support(
            ir,
            DecisionSupportItem(
                id="support-safety-contract",
                domain="safety",
                status="conditional_proposal" if safety_population else "unresolved",
                recommendation=recommendation,
                conditions=conditions,
                related_ids=[safety_population.id] if safety_population else [],
                rationale="Creates an executable safety reporting contract while leaving unsupported decisions open.",
                provenance=_proposal_provenance(
                    "Standard safety completeness frame; study-specific values require evidence."
                ),
            ),
        )
        ir.touch()
        return ir


class DerivationSupportModule:
    """Promote supported endpoint derivations and expose missing scoring decisions."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        existing = {item.variable.lower() for item in ir.derivation_rules}
        for endpoint in ir.endpoints:
            if endpoint.derivation and endpoint.name.lower() not in existing:
                from sapgen.domain.models import DerivationRule

                ir.derivation_rules.append(
                    DerivationRule(
                        id=f"derivation-{endpoint.id}",
                        variable=endpoint.name,
                        rule=endpoint.derivation,
                        provenance=endpoint.provenance.model_copy(deep=True),
                    )
                )
                continue
            if endpoint.derivation:
                continue
            _add_support(
                ir,
                DecisionSupportItem(
                    id=f"support-derivation-{endpoint.id}",
                    domain="derivation",
                    status="unresolved",
                    recommendation=(
                        f"For {endpoint.name}, confirm the analysis unit, source items, scoring or "
                        "aggregation algorithm, baseline rule, change formula, unit, direction of "
                        "benefit, partial-item handling, visit window, and missing-component rule."
                    ),
                    related_ids=[endpoint.id],
                    rationale="Names the executable derivation elements rather than using a generic TBD.",
                    provenance=_proposal_provenance(
                        "Derivation completeness checklist; no calculation is inferred."
                    ),
                ),
            )
        ir.touch()
        return ir


class TFLSpecificationModule:
    """Create concise descriptive shells even when inferential decisions remain unresolved."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        population = _primary_population(ir)
        endpoints = [item for item in ir.endpoints if item.priority == "primary"]
        endpoints.extend(item for item in ir.endpoints if item.priority == "secondary")
        endpoints = endpoints[:6]
        if population is None:
            _add_support(
                ir,
                DecisionSupportItem(
                    id="support-tfl-population",
                    domain="tfl",
                    status="unresolved",
                    recommendation=(
                        "Define the analysis population and denominator before freezing endpoint TFLs; "
                        "each shell must state rows, columns, statistics, units, denominator, and footnotes."
                    ),
                    provenance=_proposal_provenance(
                        "A concrete shell cannot be bound without an analysis population."
                    ),
                ),
            )
            return ir
        existing_ids = {item.id for item in ir.tfl_specs}
        table_number = len(ir.tfl_specs) + 1
        for endpoint in endpoints:
            spec_id = f"tfl-descriptive-{endpoint.id}"
            if spec_id in existing_ids or any(
                endpoint.name.lower() in item.title.lower() for item in ir.tfl_specs
            ):
                continue
            rows, statistics, unit = self._layout(endpoint.endpoint_type)
            columns = [*ir.study.treatment_arms] or ["Overall"]
            if endpoint.timepoint:
                columns.append(f"Assessment: {endpoint.timepoint}")
            ir.tfl_specs.append(
                TFLSpec(
                    id=spec_id,
                    number=f"Table 14.2.{table_number}",
                    kind="table",
                    title=f"Descriptive summary of {endpoint.name}",
                    population_id=population.id,
                    rows=rows,
                    columns=columns,
                    statistics=statistics,
                    unit=unit,
                    denominator=population.denominator_rule or population.definition,
                    footnotes=[
                        f"Endpoint timing: {endpoint.timepoint or 'requires confirmation'}.",
                        "This descriptive shell does not imply a confirmatory test.",
                        "Add model-based estimates, intervals and p-values only after the analysis method is frozen.",
                    ],
                    provenance=_proposal_provenance(
                        "Descriptive programming shell derived from the endpoint and population only."
                    ),
                )
            )
            table_number += 1
        ir.touch()
        return ir

    @staticmethod
    def _layout(endpoint_type: EndpointType) -> tuple[list[str], list[str], str]:
        if endpoint_type == EndpointType.CONTINUOUS:
            return (
                ["Number in population", "Number observed", "Endpoint summary"],
                ["N", "n", "mean", "SD", "median", "minimum", "maximum"],
                "endpoint units; confirm",
            )
        if endpoint_type == EndpointType.BINARY:
            return (
                ["Number in population", "Number observed", "Number with response"],
                ["N", "n", "%", "confidence interval for response proportion; level to confirm"],
                "subjects and percent",
            )
        if endpoint_type == EndpointType.TIME_TO_EVENT:
            return (
                ["Number in population", "Number of events", "Time-to-event summary"],
                ["N", "events", "censored", "median", "confidence interval; level to confirm"],
                "protocol-defined time unit",
            )
        if endpoint_type == EndpointType.COUNT:
            return (
                ["Number in population", "Number observed", "Exposure", "Observed events"],
                ["N", "n", "total exposure", "event count", "crude rate"],
                "events per protocol-defined exposure unit",
            )
        if endpoint_type == EndpointType.ORDINAL:
            return (
                ["Number observed", "Ordered response category"],
                ["n", "%"],
                "ordered response category",
            )
        return (
            ["Number assessed", "Theme or endpoint category", "Structured result"],
            ["n", "% where meaningful", "descriptive summary"],
            "not applicable or confirm",
        )
