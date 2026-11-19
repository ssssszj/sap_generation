from __future__ import annotations

import hashlib
import re
from typing import Any

from pydantic import Field, ValidationError

from sapgen.domain.models import (
    SAPIR,
    AnalysisConventions,
    AnalysisMethodSpec,
    AnalysisPopulation,
    CenterHandlingPlan,
    ClarificationItem,
    DerivationRule,
    Endpoint,
    EndpointType,
    Estimand,
    EvidenceRef,
    EvidenceStatus,
    IntercurrentEventPlan,
    InterimAnalysisPlan,
    MissingDataPlan,
    MultiplicityPlan,
    Provenance,
    RandomizationPlan,
    SafetyAnalysisPlan,
    SampleSizePlan,
    StrictModel,
    StudyDesign,
    SuccessCriteria,
    VisitSchedule,
)
from sapgen.harness.base import (
    HarnessAdapter,
    HarnessResponseError,
    HarnessUnavailableError,
)
from sapgen.ingest.documents import EvidenceChunk, EvidenceCorpus

SYSTEM_PROMPT = """You are the exhaustive evidence-extraction stage of a clinical-trial SAP
system. Extract only study facts and decisions supported by the supplied materials. Every
confirmed record must include a short verbatim quote and its exact source locator.

Inventory every named endpoint, outcome instrument, authored outcome item, safety endpoint, and
qualitative outcome together with every stated assessment timepoint. Do not omit secondary or
exploratory outcomes merely because the protocol does not declare a formal primary endpoint.
Preserve an explicit primary/secondary/exploratory hierarchy when supported; otherwise use the
least-promotional defensible hierarchy and add a blocking clarification instead of labelling every
endpoint primary. Create an estimand record linked to each extracted endpoint, but do not invent
analysis decisions.

Describe whether the study is single-arm, multi-arm, randomized, controlled, and longitudinal
only from supported evidence, and explicitly retain evidence that no comparator or randomization
is described. Keep estimands, intercurrent events, missing data, safety rules, and analysis methods
separate. When a statistical choice is absent or ambiguous, leave the relevant field explicitly
missing and add a blocking clarification. Do not convert common practice into a protocol decision;
deterministic downstream modules will create visibly labelled proposals."""


class DesignExtraction(StrictModel):
    study: StudyDesign
    sample_size: SampleSizePlan | None = None
    randomization_plan: RandomizationPlan | None = None
    visit_schedule: VisitSchedule | None = None
    analysis_conventions: AnalysisConventions | None = None
    center_handling: CenterHandlingPlan | None = None
    success_criteria: SuccessCriteria | None = None
    interim_analysis: InterimAnalysisPlan | None = None
    clarifications: list[ClarificationItem] = Field(default_factory=list)


class OutcomeExtraction(StrictModel):
    endpoints: list[Endpoint] = Field(default_factory=list)
    derivation_rules: list[DerivationRule] = Field(default_factory=list)
    clarifications: list[ClarificationItem] = Field(default_factory=list)


class EstimandExtraction(StrictModel):
    estimands: list[Estimand] = Field(default_factory=list)
    clarifications: list[ClarificationItem] = Field(default_factory=list)


class PopulationSafetyExtraction(StrictModel):
    analysis_populations: list[AnalysisPopulation] = Field(default_factory=list)
    safety: SafetyAnalysisPlan | None = None
    clarifications: list[ClarificationItem] = Field(default_factory=list)


class AnalysisExtraction(StrictModel):
    analysis_methods: list[AnalysisMethodSpec] = Field(default_factory=list)
    intercurrent_events: list[IntercurrentEventPlan] = Field(default_factory=list)
    missing_data: list[MissingDataPlan] = Field(default_factory=list)
    multiplicity: MultiplicityPlan | None = None
    clarifications: list[ClarificationItem] = Field(default_factory=list)


STAGES: tuple[tuple[str, type[StrictModel], str], ...] = (
    (
        "design",
        DesignExtraction,
        (
            "Extract study design, arms, masking, randomization, planned sample size and its basis, "
            "visit schedule, global statistical conventions, center handling, success criteria, and "
            "interim-analysis rules. Distinguish a statistical calculation from an operational target."
        ),
    ),
    (
        "endpoints",
        OutcomeExtraction,
        (
            "Inventory every primary, secondary, exploratory, safety, qualitative, and feasibility "
            "outcome with analysis unit, exact timepoint, derivation, unit, direction of benefit, and "
            "supported hierarchy. Be concise: one endpoint record per distinct analyzed variable, "
            "one short evidence quote per record, and no narrative outside the JSON."
        ),
    ),
    (
        "estimands",
        EstimandExtraction,
        (
            "Create estimands only for primary clinical questions whose attributes are supported. "
            "Link them to endpoint IDs visible in the source, keep every field concise, and record a "
            "precise clarification instead of guessing any missing attribute."
        ),
    ),
    (
        "populations-safety",
        PopulationSafetyExtraction,
        (
            "Extract operational FAS/ITT, per-protocol, and safety-population membership and "
            "denominator rules. Extract safety windows, coding, counting units, and summaries only "
            "when supported. Never use an efficacy population as a provisional safety population."
        ),
    ),
    (
        "analysis",
        AnalysisExtraction,
        (
            "Extract protocol-specified statistical methods, treatment contrasts, covariates, alpha, "
            "multiplicity, missing-data handling, and intercurrent-event decisions. Preserve "
            "descriptive or qualitative intent; do not introduce inferential models not stated in "
            "the source."
        ),
    ),
)

STAGE_RECOVERY_TERMS: dict[str, tuple[str, ...]] = {
    "design": (
        "design",
        "random",
        "blind",
        "mask",
        "sample size",
        "visit",
        "interim",
        "alpha",
    ),
    "endpoints": (
        "endpoint",
        "outcome",
        "objective",
        "measure",
        "assessment",
        "primary",
        "secondary",
        "exploratory",
    ),
    "estimands": (
        "estimand",
        "objective",
        "endpoint",
        "population",
        "treatment",
        "intercurrent",
    ),
    "populations-safety": (
        "population",
        "intention-to-treat",
        "per-protocol",
        "safety",
        "adverse",
        "laboratory",
        "vital",
    ),
    "analysis": (
        "analysis",
        "statistical",
        "model",
        "missing",
        "multiplicity",
        "covariate",
        "sensitivity",
        "intercurrent",
    ),
}
STAGE_RECOVERY_MAX_CHARS = 20_000


class SAPIRExtractor:
    def __init__(self, harness: HarnessAdapter | None = None) -> None:
        self.harness = harness

    def extract(
        self,
        corpus: EvidenceCorpus,
        *,
        session_id: str,
        allow_fallback: bool = True,
    ) -> tuple[SAPIR, bool]:
        if self.harness is not None:
            try:
                return self._extract_staged(corpus, session_id=session_id), True
            except (HarnessUnavailableError, HarnessResponseError, ValidationError):
                if not allow_fallback:
                    raise
        return self._heuristic_seed(corpus), False

    def _extract_staged(self, corpus: EvidenceCorpus, *, session_id: str) -> SAPIR:
        if self.harness is None:
            raise HarnessUnavailableError("No harness is configured.")
        source = corpus.to_prompt()
        results: dict[str, StrictModel] = {}
        for stage_name, stage_model, instruction in STAGES:
            prior = "\n\n".join(
                f"[{name}]\n{value.model_dump_json(indent=2)}" for name, value in results.items()
            )
            try:
                results[stage_name] = self._extract_stage(
                    stage_name=stage_name,
                    stage_model=stage_model,
                    instruction=instruction,
                    prior=prior,
                    source_text=source,
                    session_id=session_id,
                    results=results,
                )
            except (HarnessResponseError, ValidationError):
                results[stage_name] = self._extract_stage(
                    stage_name=stage_name,
                    stage_model=stage_model,
                    instruction=instruction,
                    prior=prior,
                    source_text=self._compact_stage_source(corpus, stage_name),
                    session_id=session_id,
                    results=results,
                    recovery=True,
                )

        design = results["design"]
        outcomes = results["endpoints"]
        estimands = results["estimands"]
        populations = results["populations-safety"]
        analysis = results["analysis"]
        clarifications: list[ClarificationItem] = []
        seen: set[str] = set()
        for stage in results.values():
            for item in getattr(stage, "clarifications", []):
                if item.id not in seen:
                    clarifications.append(item)
                    seen.add(item.id)
        return SAPIR(
            study=design.study,
            sample_size=design.sample_size,
            randomization_plan=design.randomization_plan,
            visit_schedule=design.visit_schedule,
            analysis_conventions=design.analysis_conventions,
            center_handling=design.center_handling,
            success_criteria=design.success_criteria,
            interim_analysis=design.interim_analysis,
            analysis_populations=populations.analysis_populations,
            endpoints=outcomes.endpoints,
            derivation_rules=outcomes.derivation_rules,
            estimands=estimands.estimands,
            analysis_methods=analysis.analysis_methods,
            intercurrent_events=analysis.intercurrent_events,
            missing_data=analysis.missing_data,
            multiplicity=analysis.multiplicity,
            safety=populations.safety,
            clarifications=clarifications,
        )

    def _extract_stage(
        self,
        *,
        stage_name: str,
        stage_model: type[StrictModel],
        instruction: str,
        prior: str,
        source_text: str,
        session_id: str,
        results: dict[str, StrictModel],
        recovery: bool = False,
    ) -> StrictModel:
        assert self.harness is not None
        payload = self.harness.complete_json(
            system_prompt=(
                f"{SYSTEM_PROMPT}\n\nYou are now working only on the {stage_name} domain. "
                "Do not duplicate records outside this domain."
            ),
            user_prompt=(
                f"{instruction}\n\n"
                + (
                    "RECOVERY MODE\nThe source below is a relevance-selected excerpt after "
                    "the full-source structured call failed. Extract only supported facts "
                    "visible in this excerpt and keep records concise.\n\n"
                    if recovery
                    else ""
                )
                + f"PRIOR EXTRACTED DOMAINS\n{prior or 'None; this is the first stage.'}\n\n"
                + f"SOURCE MATERIALS\n{source_text}"
            ),
            schema=stage_model.model_json_schema(),
            session_id=(
                f"{session_id}-{stage_name}-compact-retry"
                if recovery
                else f"{session_id}-{stage_name}"
            ),
        )
        payload = self._normalize_stage_payload(stage_name, payload, results)
        return stage_model.model_validate(payload)

    @staticmethod
    def _compact_stage_source(corpus: EvidenceCorpus, stage_name: str) -> str:
        """Select a bounded, source-ordered excerpt for one failed extraction domain."""

        selected = set(corpus.chunks[:4])
        selected.update(corpus.chunks[-2:])
        selected.update(corpus.search(list(STAGE_RECOVERY_TERMS[stage_name]), limit=18))
        ordered = [chunk for chunk in corpus.chunks if chunk in selected]
        return EvidenceCorpus(chunks=ordered).to_prompt(max_chars=STAGE_RECOVERY_MAX_CHARS)

    @staticmethod
    def _normalize_stage_payload(
        stage_name: str,
        payload: dict[str, Any],
        prior_results: dict[str, StrictModel],
    ) -> dict[str, Any]:
        """Repair cross-record bindings, then discard only irreparable method records."""

        if stage_name != "analysis":
            return payload
        normalized = dict(payload)
        for field_name in (
            "analysis_methods",
            "intercurrent_events",
            "missing_data",
            "clarifications",
        ):
            normalized[field_name] = SAPIRExtractor._coerce_record_list(normalized.get(field_name))
        valid_estimands = {
            item.id for item in getattr(prior_results.get("estimands"), "estimands", [])
        }
        valid_populations = {
            item.id
            for item in getattr(prior_results.get("populations-safety"), "analysis_populations", [])
        }
        methods: list[dict[str, Any]] = []
        dropped = 0
        study_id = getattr(getattr(prior_results.get("design"), "study", None), "study_id", "study")
        for raw in normalized["analysis_methods"]:
            candidate = dict(raw)
            if candidate.get("role") == "secondary":
                candidate["role"] = "supportive"
            selected_binding = False
            if candidate.get("estimand_id") not in valid_estimands and valid_estimands:
                candidate["estimand_id"] = SAPIRExtractor._choose_candidate(
                    valid_estimands,
                    f"{study_id}:{candidate.get('id', 'method')}:estimand",
                )
                selected_binding = True
            if (
                candidate.get("analysis_population_id") not in valid_populations
                and valid_populations
            ):
                candidate["analysis_population_id"] = SAPIRExtractor._choose_candidate(
                    valid_populations,
                    f"{study_id}:{candidate.get('id', 'method')}:population",
                )
                selected_binding = True
            if selected_binding:
                provenance = dict(candidate.get("provenance") or {})
                previous_note = str(provenance.get("note") or "").strip()
                selection_note = (
                    "Cross-record binding was selected reproducibly from the available extracted "
                    "candidates; the final SAP must use this single binding consistently."
                )
                provenance["status"] = "inferred"
                provenance.setdefault("evidence", [])
                provenance["note"] = (
                    f"{previous_note} {selection_note}".strip() if previous_note else selection_note
                )
                candidate["provenance"] = provenance
            try:
                method = AnalysisMethodSpec.model_validate(candidate)
            except ValidationError:
                dropped += 1
                continue
            if method.estimand_id not in valid_estimands:
                dropped += 1
                continue
            if method.analysis_population_id not in valid_populations:
                dropped += 1
                continue
            methods.append(method.model_dump(mode="json"))
        normalized["analysis_methods"] = methods
        if dropped:
            clarifications = list(normalized["clarifications"])
            clarifications.append(
                {
                    "id": "confirm-incomplete-analysis-methods",
                    "module": "evidence",
                    "question": (
                        f"The extraction returned {dropped} incomplete or unbound analysis method "
                        "record(s). Confirm the estimand, analysis population, model or descriptive "
                        "method, effect measure, and decision rule before finalization."
                    ),
                    "related_paths": ["analysis_methods"],
                }
            )
            normalized["clarifications"] = clarifications
        return normalized

    @staticmethod
    def _coerce_record_list(value: Any) -> list[dict[str, Any]]:
        """Flatten provider-created record groupings into the schema's list shape."""

        if value is None:
            return []
        if isinstance(value, list):
            records: list[dict[str, Any]] = []
            for item in value:
                records.extend(SAPIRExtractor._coerce_record_list(item))
            return records
        if not isinstance(value, dict):
            return []
        if "id" in value:
            return [dict(value)]
        records = []
        for nested in value.values():
            records.extend(SAPIRExtractor._coerce_record_list(nested))
        return records

    @staticmethod
    def _choose_candidate(values: set[str], key: str) -> str:
        ordered = sorted(values)
        digest = hashlib.sha256(key.encode("utf-8")).digest()
        return ordered[int.from_bytes(digest[:8], "big") % len(ordered)]

    def _heuristic_seed(self, corpus: EvidenceCorpus) -> SAPIR:
        title_chunk = self._find_title(corpus.chunks)
        title = title_chunk.text[:300] if title_chunk else "待确认"
        study_provenance = self._provenance(title_chunk)

        populations: list[AnalysisPopulation] = []
        joined = "\n".join(chunk.text for chunk in corpus.chunks).lower()
        if any(term in joined for term in ("full analysis set", "intent-to-treat", "itt", "fas")):
            populations.append(
                AnalysisPopulation(
                    id="FAS",
                    name="Full Analysis Set",
                    definition="Protocol-defined full analysis set; exact inclusion rules require confirmation.",
                    denominator_rule="Number of subjects in the Full Analysis Set",
                    provenance=Provenance(status=EvidenceStatus.INFERRED),
                )
            )
        if any(term in joined for term in ("safety set", "safety population", "安全性分析集")):
            populations.append(
                AnalysisPopulation(
                    id="SAF",
                    name="Safety Analysis Set",
                    definition=(
                        "Subjects who received at least one dose; verify against the protocol."
                    ),
                    denominator_rule="Number of subjects in the Safety Analysis Set",
                    provenance=Provenance(status=EvidenceStatus.INFERRED),
                )
            )
        if not populations:
            populations = [
                AnalysisPopulation(
                    id="FAS",
                    name="Full Analysis Set",
                    definition="待确认",
                    denominator_rule="待确认",
                    provenance=Provenance(status=EvidenceStatus.MISSING),
                ),
                AnalysisPopulation(
                    id="SAF",
                    name="Safety Analysis Set",
                    definition="待确认",
                    denominator_rule="待确认",
                    provenance=Provenance(status=EvidenceStatus.MISSING),
                ),
            ]

        endpoints = self._find_endpoints(corpus.chunks)
        clarifications = [
            ClarificationItem(
                id="confirm-populations",
                module="evidence",
                question="请依据方案确认 FAS 和安全性分析集的纳入规则与分母。",
                related_paths=["analysis_populations"],
            )
        ]
        if not endpoints:
            clarifications.append(
                ClarificationItem(
                    id="confirm-primary-endpoint",
                    module="evidence",
                    question="未可靠识别主要终点，请确认终点定义、时间点、推导规则和类型。",
                    related_paths=["endpoints"],
                )
            )
        return SAPIR(
            study=StudyDesign(title=title, provenance=study_provenance),
            analysis_populations=populations,
            endpoints=endpoints,
            clarifications=clarifications,
        )

    @staticmethod
    def _find_title(chunks: list[EvidenceChunk]) -> EvidenceChunk | None:
        title_pattern = re.compile(
            r"^(study\s+title|protocol\s+title|研究题目|试验名称)\s*[:：]", re.IGNORECASE
        )
        for chunk in chunks:
            if title_pattern.search(chunk.text):
                return chunk
        return chunks[0] if chunks else None

    def _find_endpoints(self, chunks: list[EvidenceChunk]) -> list[Endpoint]:
        endpoints: list[Endpoint] = []
        patterns = (
            (re.compile(r"primary\s+endpoint", re.IGNORECASE), "primary"),
            (re.compile(r"主要终点"), "primary"),
            (re.compile(r"secondary\s+endpoint", re.IGNORECASE), "secondary"),
            (re.compile(r"次要终点"), "secondary"),
        )
        for chunk in chunks:
            for pattern, priority in patterns:
                if not pattern.search(chunk.text):
                    continue
                endpoint_id = f"endpoint-{len(endpoints) + 1:03d}"
                endpoints.append(
                    Endpoint(
                        id=endpoint_id,
                        name=self._endpoint_name(chunk.text),
                        endpoint_type=self._endpoint_type(chunk.text),
                        definition=chunk.text[:1000],
                        priority=priority,
                        provenance=self._provenance(chunk),
                    )
                )
                break
            if len(endpoints) >= 12:
                break
        return endpoints

    @staticmethod
    def _endpoint_name(text: str) -> str:
        cleaned = re.sub(
            r"^(primary|secondary)\s+endpoint\s*[:：-]?\s*|^(主要|次要)终点\s*[:：-]?\s*",
            "",
            text.strip(),
            flags=re.IGNORECASE,
        )
        return cleaned[:180] or "待确认"

    @staticmethod
    def _endpoint_type(text: str) -> EndpointType:
        value = text.lower()
        if any(term in value for term in ("time to", "survival", "hazard", "生存", "至事件时间")):
            return EndpointType.TIME_TO_EVENT
        if any(
            term in value for term in ("response rate", "proportion", "responder", "率", "比例")
        ):
            return EndpointType.BINARY
        if any(term in value for term in ("count", "number of episodes", "次数", "计数")):
            return EndpointType.COUNT
        if any(term in value for term in ("score category", "ordinal", "等级", "分级")):
            return EndpointType.ORDINAL
        if any(
            term in value
            for term in ("change from baseline", "mean", "score", "较基线变化", "均值")
        ):
            return EndpointType.CONTINUOUS
        return EndpointType.OTHER

    @staticmethod
    def _provenance(chunk: EvidenceChunk | None) -> Provenance:
        if chunk is None:
            return Provenance(status=EvidenceStatus.MISSING)
        return Provenance(
            status=EvidenceStatus.CONFIRMED,
            evidence=[
                EvidenceRef(
                    source_id=chunk.source_id,
                    document_name=chunk.document_name,
                    locator=chunk.locator,
                    quote=chunk.text[:2000],
                )
            ],
        )
