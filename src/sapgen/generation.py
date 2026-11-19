from __future__ import annotations

import json
import warnings

from pydantic import Field, ValidationError

from sapgen.chapter_guidance import chapter_guidance
from sapgen.domain.models import SAPIR, SAPSection, StrictModel
from sapgen.harness.base import HarnessAdapter, HarnessResponseError

CHAPTER_BODY_MAX_CHARS = 12_000
REVIEW_RETRY_TARGET_CHARS = 9_000
REVIEW_BODY_ABSOLUTE_MAX_CHARS = 18_000
REVIEW_BODY_GROWTH_ALLOWANCE_CHARS = 2_000


def build_study_contract(ir: SAPIR) -> str:
    """Create a compact, single-source-of-truth view used by every chapter."""

    primary_endpoints = [
        {
            "id": endpoint.id,
            "name": endpoint.name,
            "timepoint": endpoint.timepoint,
            "derivation": endpoint.derivation,
        }
        for endpoint in ir.endpoints
        if endpoint.priority == "primary"
    ]
    safety_population = next(
        (
            population.id
            for population in ir.analysis_populations
            if "safety" in f"{population.id} {population.name}".lower()
        ),
        None,
    )
    contract = {
        "study_id": ir.study.study_id,
        "design": ir.study.design,
        "treatment_arms": ir.study.treatment_arms,
        "randomization": ir.study.randomization,
        "planned_sample_size": ir.sample_size.planned_total if ir.sample_size else None,
        "primary_endpoints": primary_endpoints,
        "analysis_populations": [
            {"id": item.id, "name": item.name, "definition": item.definition}
            for item in ir.analysis_populations
        ],
        "safety_population_id": safety_population,
        "alpha": ir.analysis_conventions.alpha if ir.analysis_conventions else None,
        "sidedness": ir.analysis_conventions.sidedness if ir.analysis_conventions else None,
        "success_rule": ir.success_criteria.rule if ir.success_criteria else None,
    }
    return json.dumps(contract, ensure_ascii=False, indent=2)


CHAPTER_PLAN: tuple[tuple[str, str, str, list[str]], ...] = (
    (
        "section-overview",
        "Study Synopsis and Design",
        "State the study purpose, design, arms, masking, control, duration, and study-specific context.",
        ["study"],
    ),
    (
        "section-randomization-sample",
        "Randomization and Sample Size",
        "State allocation and concealment rules plus planned total/per-group sample size, statistical basis, dropout assumptions, and operational constraints.",
        ["randomization_plan", "sample_size"],
    ),
    (
        "section-endpoints-estimands",
        "Objectives Endpoints and Estimands",
        "Cover every supported endpoint at its correct hierarchy and timepoint; state estimand attributes without silently filling missing decisions.",
        ["endpoints", "estimands", "success_criteria", "decision_support"],
    ),
    (
        "section-populations",
        "Analysis Populations",
        "Give operational membership, exclusion, treatment-attribution, denominator, and analysis binding rules for every population.",
        ["analysis_populations"],
    ),
    (
        "section-conventions",
        "General Statistical Conventions",
        "State descriptive summaries, alpha and sidedness only when supported, confidence intervals, baseline conventions, software, and center handling.",
        ["analysis_conventions", "center_handling", "visit_schedule"],
    ),
    (
        "section-methods",
        "Statistical Analysis Methods",
        "For each supported analysis state outcome, population, contrast, model or descriptive method, covariates/strata, estimate, uncertainty, and decision rule. Preserve descriptive and qualitative intent.",
        ["analysis_methods", "endpoints", "analysis_populations"],
    ),
    (
        "section-complex-data",
        "Intercurrent Events Missing Data and Sensitivity Analyses",
        "State supported strategies and operational rules. If absent, identify the exact decision requiring confirmation; do not insert generic MAR/MNAR machinery.",
        ["intercurrent_events", "missing_data", "estimands", "decision_support"],
    ),
    (
        "section-multiplicity-interim",
        "Multiplicity and Interim Analyses",
        "State supported testing families, success logic, alpha control, interim timing, decision rules, and information flow, or clearly mark them unresolved.",
        ["multiplicity", "success_criteria", "interim_analysis"],
    ),
    (
        "section-safety",
        "Safety Analyses",
        "Define safety population and treatment attribution, TEAE window, MedDRA levels, participant/event counting, severity, seriousness, relatedness, discontinuations, deaths, laboratories, and vital signs only as supported.",
        ["safety", "analysis_populations", "decision_support"],
    ),
    (
        "section-derivations",
        "Data Handling Derivations and Visit Windows",
        "Make baseline, change, scoring, units, direction of benefit, analysis visits, windows, and time anchors executable where supported.",
        ["derivation_rules", "visit_schedule", "endpoints", "decision_support"],
    ),
    (
        "section-tfl",
        "Tables Figures and Listings",
        "Specify concise executable shells with population, rows, columns, statistics, units, denominator, and essential footnotes; do not repeat entire methods.",
        ["tfl_specs", "decision_support"],
    ),
    (
        "section-clarifications",
        "Items Requiring Confirmation",
        "Consolidate unresolved decisions into specific non-duplicative questions grouped by domain.",
        ["clarifications"],
    ),
    (
        "section-traceability",
        "Traceability Appendix",
        "Map material study facts and decisions to source locators or label them explicitly as unresolved/proposed.",
        ["study", "endpoints", "analysis_methods", "safety", "tfl_specs"],
    ),
)


class HarnessChapterGenerator:
    """Generate the SAP sequentially, carrying the full prior draft into every chapter."""

    def __init__(self, harness: HarnessAdapter) -> None:
        self.harness = harness

    def generate(self, ir: SAPIR, *, session_id: str) -> list[SAPSection]:
        ir_json = ir.model_dump_json(indent=2, exclude={"generated_sections"})
        contract = build_study_contract(ir)
        sections: list[SAPSection] = []
        for index, (chapter_id, title, instruction, source_paths) in enumerate(
            CHAPTER_PLAN, start=1
        ):
            prior = self._render_prior(sections)
            payload = self.harness.complete_json(
                system_prompt=(
                    "You are a senior clinical-trial statistician drafting one chapter of a "
                    "protocol-only Statistical Analysis Plan. Use only the supplied evidence-backed "
                    "SAP-IR and the complete prior draft. Keep terminology and locked facts consistent "
                    "with all prior chapters. Do not invent protocol decisions. When information is "
                    "absent, state the precise unresolved decision or conditional proposal. Items in "
                    "decision_support and records with inferred provenance are advisory and must remain "
                    "visibly labelled 'Proposed for confirmation', never protocol facts. Do not omit "
                    "these proposals: state the selected proposal operationally so the draft remains "
                    "programmable while awaiting confirmation. When two or more reasonable candidates "
                    "are available, select exactly one "
                    "and use it consistently; never write 'A or B', a menu of alternatives, or an "
                    "unresolved choice between available candidates. Only state unresolved when no "
                    "candidate exists. Write "
                    "professional, concise, implementation-ready Markdown."
                ),
                user_prompt=(
                    f"CHAPTER {index}: {title}\n\n"
                    f"CHAPTER PURPOSE\n{instruction}\n\n"
                    f"GENERAL CHAPTER GUIDANCE\n{chapter_guidance(chapter_id)}\n\n"
                    "Return this chapter only. Do not repeat earlier chapters and do not add a "
                    "document-level title. Aim for the shortest text that is complete and executable.\n\n"
                    f"STUDY-WIDE CONSISTENCY CONTRACT\n{contract}\n\n"
                    f"EVIDENCE-BACKED SAP-IR\n{ir_json}\n\n"
                    f"ALL PREVIOUS CHAPTERS\n{prior}"
                ),
                schema={
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["body_markdown"],
                    "properties": {
                        "body_markdown": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": CHAPTER_BODY_MAX_CHARS,
                        }
                    },
                },
                session_id=f"{session_id}-{index:02d}",
            )
            body = str(payload.get("body_markdown") or "").strip()
            if not body:
                raise ValueError(f"Harness returned an empty chapter: {title}")
            sections.append(
                SAPSection(
                    id=chapter_id,
                    title=title,
                    body_markdown=body,
                    source_paths=source_paths,
                )
            )
        ir.generated_sections = sections
        ir.touch()
        return sections

    @staticmethod
    def _render_prior(sections: list[SAPSection]) -> str:
        if not sections:
            return "No previous chapter; this is the first chapter."
        return "\n\n".join(
            f"# {index}. {section.title}\n\n{section.body_markdown}"
            for index, section in enumerate(sections, start=1)
        )


class ChapterReview(StrictModel):
    issues: list[str] = Field(default_factory=list, max_length=6)
    body_markdown: str = ""


class HarnessDraftReviewer:
    """Review one chapter per call so a full-draft rewrite cannot exhaust output tokens."""

    def __init__(self, harness: HarnessAdapter) -> None:
        self.harness = harness

    def review(self, ir: SAPIR, *, session_id: str) -> list[SAPSection]:
        contract = build_study_contract(ir)
        ir_json = ir.model_dump_json(indent=2, exclude={"generated_sections"})
        for index, section in enumerate(ir.generated_sections, start=1):
            review = self._review_chapter(
                ir_json=ir_json,
                contract=contract,
                sections=ir.generated_sections,
                current=section,
                index=index,
                session_id=session_id,
            )
            if review is not None and review.body_markdown.strip():
                section.body_markdown = review.body_markdown.strip()
        ir.touch()
        return ir.generated_sections

    def _review_chapter(
        self,
        *,
        ir_json: str,
        contract: str,
        sections: list[SAPSection],
        current: SAPSection,
        index: int,
        session_id: str,
    ) -> ChapterReview | None:
        cross_chapter_context = self._render_cross_chapter_context(sections, current.id)
        review_body_limit = min(
            REVIEW_BODY_ABSOLUTE_MAX_CHARS,
            max(
                CHAPTER_BODY_MAX_CHARS,
                len(current.body_markdown) + REVIEW_BODY_GROWTH_ALLOWANCE_CHARS,
            ),
        )
        for attempt in range(2):
            retry_instruction = (
                " This is a retry after an overlong or invalid response. Return at most three short "
                f"issues and keep the revised chapter under {REVIEW_RETRY_TARGET_CHARS} characters."
                if attempt
                else ""
            )
            try:
                review_schema = ChapterReview.model_json_schema()
                review_schema["properties"]["body_markdown"]["maxLength"] = review_body_limit
                payload = self.harness.complete_json(
                    system_prompt=(
                        "You are the final statistical and editorial reviewer of one chapter of a "
                        "protocol-only SAP. Check omissions, internal contradictions, endpoint hierarchy, "
                        "analysis-population binding, study-design compatibility, sample size, "
                        "randomization, visit timing, derivations, safety counting, and unsupported "
                        "decisions. When multiple reasonable candidates exist, keep exactly one selected "
                        "option and remove A-or-B language or menus. Use the other-chapter excerpts only "
                        "for consistency checks. Review and, if needed, rewrite only the current chapter. "
                        "Never return another chapter. If no change is needed, return an empty "
                        "body_markdown. List no more than six concise issues. Do not introduce facts absent "
                        "from the SAP-IR. Retain executable inferred proposals, clearly labelled as proposed "
                        f"rather than protocol-specified.{retry_instruction}"
                    ),
                    user_prompt=(
                        f"CURRENT CHAPTER {index}: {current.title} [{current.id}]\n"
                        f"{current.body_markdown}\n\n"
                        f"GENERAL CHAPTER GUIDANCE\n{chapter_guidance(current.id)}\n\n"
                        f"STUDY-WIDE CONSISTENCY CONTRACT\n{contract}\n\n"
                        f"OTHER-CHAPTER COMPACT CONTEXT\n{cross_chapter_context}\n\n"
                        f"EVIDENCE-BACKED SAP-IR\n{ir_json}"
                    ),
                    schema=review_schema,
                    session_id=(
                        f"{session_id}-{index:02d}"
                        if attempt == 0
                        else f"{session_id}-{index:02d}-retry"
                    ),
                )
                review = ChapterReview.model_validate(payload)
                if len(review.body_markdown) > review_body_limit:
                    raise ValueError(
                        "review body exceeds the chapter-specific limit "
                        f"({len(review.body_markdown)} > {review_body_limit})"
                    )
                return review
            except (HarnessResponseError, ValidationError, ValueError) as exc:
                if attempt == 1:
                    warnings.warn(
                        f"Final review failed twice for {current.id}; keeping the generated chapter: {exc}",
                        stacklevel=2,
                    )
        return None

    @staticmethod
    def _render_cross_chapter_context(
        sections: list[SAPSection], current_id: str, *, per_chapter_limit: int = 900
    ) -> str:
        excerpts: list[str] = []
        for section in sections:
            if section.id == current_id:
                continue
            compact = " ".join(section.body_markdown.split())
            if len(compact) > per_chapter_limit:
                head = per_chapter_limit * 2 // 3
                tail = per_chapter_limit - head
                compact = f"{compact[:head]} ... {compact[-tail:]}"
            excerpts.append(f"[{section.id}] {section.title}: {compact}")
        return "\n".join(excerpts) or "No other chapters are available."


def _bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- Not specified"


class SectionGenerator:
    """Render reviewable prose from shared SAP-IR; never invent new decisions."""

    def generate(self, ir: SAPIR) -> list[SAPSection]:
        sections = [
            self._overview(ir),
            self._randomization_sample(ir),
            self._populations(ir),
            self._endpoints_estimands(ir),
            self._conventions(ir),
            self._methods(ir),
            self._multiplicity(ir),
            self._complex_data(ir),
            self._safety(ir),
            self._derivations(ir),
            self._tfl(ir),
            self._clarifications(ir),
            self._traceability(ir),
        ]
        ir.generated_sections = sections
        ir.touch()
        return sections

    def render_document(self, ir: SAPIR) -> str:
        if not ir.generated_sections:
            self.generate(ir)
        lines = [f"# Statistical Analysis Plan\n\n## {ir.study.title}\n"]
        for section in ir.generated_sections:
            lines.extend([f"# {section.title}", section.body_markdown, ""])
        return "\n\n".join(lines).strip() + "\n"

    @staticmethod
    def _overview(ir: SAPIR) -> SAPSection:
        study = ir.study
        body = (
            f"Study identifier: {study.study_id}\n\n"
            f"Study title: {study.title}\n\n"
            f"Phase: {study.phase or 'Not specified'}\n\n"
            f"Design: {study.design or 'Not specified'}\n\n"
            f"Treatment arms:\n{_bullets(study.treatment_arms)}\n\n"
            f"Randomization: {study.randomization or 'Not specified'}\n\n"
            f"Blinding: {study.blinding or 'Not specified'}"
        )
        return SAPSection(id="section-overview", title="Study Overview", body_markdown=body)

    @staticmethod
    def _randomization_sample(ir: SAPIR) -> SAPSection:
        randomization = ir.randomization_plan
        sample = ir.sample_size
        body = (
            "## Randomization\n\n"
            f"Allocation ratio: {randomization.allocation_ratio if randomization else 'Not specified; confirmation required'}\n\n"
            f"Sequence generation: {randomization.sequence_generation if randomization else 'Not specified; confirmation required'}\n\n"
            "Stratification factors:\n"
            f"{_bullets(randomization.stratification_factors if randomization else [])}\n\n"
            f"Allocation concealment: {randomization.concealment if randomization else 'Not specified; confirmation required'}\n\n"
            "## Sample size\n\n"
            f"Planned total: {sample.planned_total if sample else 'Not specified; confirmation required'}\n\n"
            "Planned per group:\n"
            f"{_bullets([f'{key}: {value}' for key, value in sample.planned_per_group.items()] if sample else [])}\n\n"
            f"Statistical basis: {sample.statistical_basis if sample else 'Not specified; confirmation required'}\n\n"
            f"Dropout assumption: {sample.dropout_assumption if sample else 'Not specified; confirmation required'}\n\n"
            f"Operational constraints: {sample.operational_constraints if sample else 'Not specified; confirmation required'}"
        )
        return SAPSection(
            id="section-randomization-sample",
            title="Randomization and Sample Size",
            body_markdown=body,
            source_paths=["randomization_plan", "sample_size"],
        )

    @staticmethod
    def _populations(ir: SAPIR) -> SAPSection:
        blocks = []
        for population in ir.analysis_populations:
            blocks.append(
                f"## {population.name} ({population.id})\n\n"
                f"{population.definition}\n\n"
                f"Denominator: {population.denominator_rule or 'Not specified'}"
            )
        return SAPSection(
            id="section-populations",
            title="Analysis Populations",
            body_markdown="\n\n".join(blocks) or "No analysis population has been defined.",
            source_paths=["analysis_populations"],
        )

    @staticmethod
    def _endpoints_estimands(ir: SAPIR) -> SAPSection:
        endpoint_by_id = {item.id: item for item in ir.endpoints}
        blocks = []
        for estimand in ir.estimands:
            endpoint = endpoint_by_id.get(estimand.endpoint_id)
            blocks.append(
                f"## {estimand.objective} ({estimand.id})\n\n"
                f"Endpoint: {endpoint.name if endpoint else estimand.endpoint_id}\n\n"
                f"Endpoint hierarchy: {endpoint.priority if endpoint else 'Not specified'}\n\n"
                f"Population: {estimand.population}\n\n"
                f"Variable: {estimand.variable}\n\n"
                f"Treatment condition: {estimand.treatment_condition}\n\n"
                "Intercurrent event strategies:\n"
                f"{_bullets(estimand.intercurrent_event_strategies)}\n\n"
                f"Population-level summary: {estimand.population_summary}"
            )
        if not blocks:
            endpoint_lines = [
                f"- {endpoint.priority}: {endpoint.name} ({endpoint.endpoint_type})"
                for endpoint in ir.endpoints
            ]
            body = "No complete estimand has been confirmed. Identified endpoints:\n" + (
                "\n".join(endpoint_lines) if endpoint_lines else "- None"
            )
        else:
            body = "\n\n".join(blocks)
        return SAPSection(
            id="section-estimands",
            title="Objectives Endpoints and Estimands",
            body_markdown=body,
            source_paths=["endpoints", "estimands"],
        )

    @staticmethod
    def _methods(ir: SAPIR) -> SAPSection:
        blocks = []
        for method in ir.analysis_methods:
            blocks.append(
                f"## {method.role.value.title()} analysis ({method.id})\n\n"
                f"Estimand: {method.estimand_id}\n\n"
                f"Analysis population: {method.analysis_population_id}\n\n"
                f"Model: {method.model}\n\n"
                f"Effect measure: {method.effect_measure}\n\n"
                f"Test: {method.test_method}\n\n"
                f"Covariates:\n{_bullets(method.covariates)}\n\n"
                f"Missing data strategy: {method.missing_data_strategy or 'See the missing-data plan'}\n\n"
                f"Assumptions:\n{_bullets(method.assumptions)}\n\n"
                f"Rationale and status: {method.rationale or 'Not specified'}"
            )
        return SAPSection(
            id="section-methods",
            title="Statistical Analysis Methods",
            body_markdown="\n\n".join(blocks) or "No analysis method has been confirmed.",
            source_paths=["analysis_methods"],
        )

    @staticmethod
    def _conventions(ir: SAPIR) -> SAPSection:
        conventions = ir.analysis_conventions
        visits = ir.visit_schedule
        center = ir.center_handling
        body = (
            f"Alpha: {conventions.alpha if conventions else 'Not specified; confirmation required'}\n\n"
            f"Sidedness: {conventions.sidedness if conventions else 'Not specified; confirmation required'}\n\n"
            f"Confidence level: {conventions.confidence_level if conventions else 'Not specified; confirmation required'}\n\n"
            f"Descriptive summaries: {conventions.descriptive_statistics if conventions else 'Not specified; confirmation required'}\n\n"
            f"Baseline definition: {conventions.baseline_definition if conventions else 'Not specified; confirmation required'}\n\n"
            f"Software: {conventions.software if conventions else 'Not specified; confirmation required'}\n\n"
            f"Visit time anchor: {visits.time_anchor if visits else 'Not specified; confirmation required'}\n\n"
            f"Center handling: {center.strategy if center else 'Not specified; confirmation required'}"
        )
        return SAPSection(
            id="section-conventions",
            title="General Statistical Conventions",
            body_markdown=body,
            source_paths=["analysis_conventions", "visit_schedule", "center_handling"],
        )

    @staticmethod
    def _complex_data(ir: SAPIR) -> SAPSection:
        event_blocks = [
            (
                f"- {plan.event}: {plan.strategy.value}; operational rule: "
                f"{plan.operational_rule}; rationale: {plan.rationale or 'Not specified'} "
                f"(estimand {plan.estimand_id})"
            )
            for plan in ir.intercurrent_events
        ]
        missing_blocks = [
            (
                f"- {plan.reason}: assumption {plan.mechanism.value}; primary method: "
                f"{plan.primary_method}; sensitivity method: "
                f"{plan.sensitivity_method or 'Not specified'}; tipping-point rule: "
                f"{plan.tipping_point_rule or 'Not specified'} (estimand {plan.estimand_id})"
            )
            for plan in ir.missing_data
        ]
        body = (
            "## Intercurrent events\n\n"
            + ("\n".join(event_blocks) if event_blocks else "No plan defined.")
            + "\n\n## Missing data\n\n"
            + ("\n".join(missing_blocks) if missing_blocks else "No plan defined.")
        )
        return SAPSection(
            id="section-complex-data",
            title="Intercurrent Events and Missing Data",
            body_markdown=body,
            source_paths=["intercurrent_events", "missing_data"],
        )

    @staticmethod
    def _multiplicity(ir: SAPIR) -> SAPSection:
        if ir.multiplicity is None:
            body = "No multiplicity contract has been defined; confirmation is required."
        else:
            plan = ir.multiplicity
            body = (
                f"Outcome family: {plan.outcome_family}\n\n"
                f"Timepoint/contrast family: {plan.timepoint_family}\n\n"
                f"Multiplicity strategy: {plan.strategy}\n\n"
                f"Inferential thresholds: {plan.inferential_thresholds}\n\n"
                f"Protocol status: {plan.provenance.note or plan.provenance.status.value}"
            )
        return SAPSection(
            id="section-multiplicity",
            title="Multiplicity and Inferential Error Control",
            body_markdown=body,
            source_paths=["multiplicity"],
        )

    @staticmethod
    def _safety(ir: SAPIR) -> SAPSection:
        if ir.safety is None:
            body = "No safety analysis specification has been defined."
        else:
            safety = ir.safety
            body = (
                f"Analysis population: {safety.analysis_population_id}\n\n"
                f"TEAE window: {safety.teae_window_start} to {safety.teae_window_end}\n\n"
                f"Dictionary: MedDRA {safety.meddra_version}\n\n"
                f"Coding levels: {', '.join(safety.coding_levels)}\n\n"
                f"Subject denominator: {safety.subject_denominator}\n\n"
                f"Event denominator: {safety.event_denominator or 'Not applicable'}\n\n"
                f"Planned summaries:\n{_bullets(safety.summaries)}\n\n"
                f"Protocol status: {safety.provenance.note or safety.provenance.status.value}"
            )
        return SAPSection(
            id="section-safety",
            title="Safety Analysis",
            body_markdown=body,
            source_paths=["safety"],
        )

    @staticmethod
    def _derivations(ir: SAPIR) -> SAPSection:
        derivations = [
            (
                f"- {item.variable}: {item.rule}; unit: {item.unit or 'not specified'}; "
                f"direction of benefit: {item.direction_of_benefit or 'not specified'}"
            )
            for item in ir.derivation_rules
        ]
        schedule = ir.visit_schedule
        body = (
            "## Derivations\n\n"
            + (
                "\n".join(derivations)
                if derivations
                else "No supported derivation rule was extracted."
            )
            + "\n\n## Visit schedule and windows\n\nVisits:\n"
            + _bullets(schedule.visits if schedule else [])
            + "\n\nVisit windows:\n"
            + _bullets(schedule.visit_windows if schedule else [])
        )
        return SAPSection(
            id="section-derivations",
            title="Data Handling Derivations and Visit Windows",
            body_markdown=body,
            source_paths=["derivation_rules", "visit_schedule"],
        )

    @staticmethod
    def _tfl(ir: SAPIR) -> SAPSection:
        blocks = []
        for spec in ir.tfl_specs:
            blocks.append(
                f"## {spec.number} {spec.title}\n\n"
                f"Population: {spec.population_id}\n\n"
                f"Rows:\n{_bullets(spec.rows)}\n\n"
                f"Columns:\n{_bullets(spec.columns)}\n\n"
                f"Statistics:\n{_bullets(spec.statistics)}\n\n"
                f"Unit: {spec.unit or 'Not specified'}\n\n"
                f"Denominator: {spec.denominator}\n\n"
                f"Footnotes:\n{_bullets(spec.footnotes)}"
            )
        return SAPSection(
            id="section-tfl",
            title="Tables Figures and Listings",
            body_markdown="\n\n".join(blocks) or "No TFL specification has been generated.",
            source_paths=["tfl_specs"],
        )

    @staticmethod
    def _clarifications(ir: SAPIR) -> SAPSection:
        open_items = [item for item in ir.clarifications if item.status.value == "open"]
        questions = "\n".join(
            f"- [{item.id}] {item.question} (blocking: {'yes' if item.blocking else 'no'})"
            for item in open_items
        )
        proposals = "\n".join(
            f"- [{item.id}; {item.status}] {item.recommendation}" for item in ir.decision_support
        )
        body = (
            "## Confirmation questions\n\n"
            + (questions or "No open item remains.")
            + "\n\n## Conditional decision support\n\n"
            + (proposals or "No conditional proposal was generated.")
        )
        return SAPSection(
            id="section-clarifications",
            title="Items Requiring Confirmation",
            body_markdown=body or "No open item remains.",
            source_paths=["clarifications"],
        )

    @staticmethod
    def _traceability(ir: SAPIR) -> SAPSection:
        lines = []
        for group_name, records in (
            ("Endpoint", ir.endpoints),
            ("Estimand", ir.estimands),
            ("Analysis", ir.analysis_methods),
            ("Intercurrent event", ir.intercurrent_events),
            ("Missing data", ir.missing_data),
            ("TFL", ir.tfl_specs),
            ("Decision support", ir.decision_support),
        ):
            for record in records:
                evidence = record.provenance.evidence
                if evidence:
                    refs = "; ".join(f"{item.document_name}, {item.locator}" for item in evidence)
                else:
                    refs = record.provenance.status.value
                lines.append(f"- {group_name} {record.id}: {refs}")
        return SAPSection(
            id="section-traceability",
            title="Traceability Appendix",
            body_markdown="\n".join(lines) or "No traceable record is available.",
        )
