from __future__ import annotations

from sapgen.domain.models import (
    SAPIR,
    AnalysisMethodSpec,
    AnalysisRole,
    Endpoint,
    EndpointType,
    EvidenceStatus,
    IntercurrentEventPlan,
    IntercurrentEventStrategy,
    MissingDataPlan,
    MissingnessMechanism,
    Provenance,
)
from sapgen.modules.common import add_clarification

DEFAULT_EVENTS = (
    "study intervention discontinuation or non-completion",
    "treatment switching or initiation of an alternative therapy",
    "rescue treatment",
    "death before endpoint assessment",
)


class ComplexDataModule:
    """Preserve supported decisions and complete explicitly labelled robustness proposals."""

    def enrich(self, ir: SAPIR) -> SAPIR:
        primary_endpoints = {
            endpoint.id: endpoint for endpoint in ir.endpoints if endpoint.priority == "primary"
        }
        for estimand in ir.estimands:
            endpoint = primary_endpoints.get(estimand.endpoint_id)
            if endpoint is None:
                self._sync_estimand_strategies(ir, estimand.id)
                continue
            events = DEFAULT_EVENTS
            endpoint_text = f"{endpoint.name} {endpoint.definition}".lower()
            if endpoint.endpoint_type == EndpointType.TIME_TO_EVENT or any(
                term in endpoint_text for term in ("death", "mortality", "survival")
            ):
                events = tuple(event for event in DEFAULT_EVENTS if "death" not in event)
            self._enrich_events(ir, estimand.id, events)
            missing_plan = self._enrich_missing_data(ir, estimand.id, endpoint)
            self._bind_missing_strategy(ir, estimand.id, missing_plan)
            self._add_sensitivity_method(ir, estimand.id, missing_plan)
            self._sync_estimand_strategies(ir, estimand.id)
        ir.touch()
        return ir

    def _enrich_events(
        self,
        ir: SAPIR,
        estimand_id: str,
        proposed_events: tuple[str, ...],
    ) -> None:
        plans = [item for item in ir.intercurrent_events if item.estimand_id == estimand_id]
        existing_kinds = {self._event_kind(item.event) for item in plans}
        for plan in plans:
            if plan.strategy == IntercurrentEventStrategy.UNRESOLVED:
                self._apply_event_proposal(plan)
                self._add_event_clarification(ir, plan)

        for event_index, event in enumerate(proposed_events, start=1):
            kind = self._event_kind(event)
            if kind in existing_kinds:
                continue
            plan = IntercurrentEventPlan(
                id=f"ice-{estimand_id}-{event_index}",
                estimand_id=estimand_id,
                event=event,
                strategy=IntercurrentEventStrategy.UNRESOLVED,
                operational_rule="",
                provenance=Provenance(status=EvidenceStatus.MISSING),
            )
            self._apply_event_proposal(plan)
            ir.intercurrent_events.append(plan)
            self._add_event_clarification(ir, plan)
            existing_kinds.add(kind)

    @staticmethod
    def _apply_event_proposal(plan: IntercurrentEventPlan) -> None:
        kind = ComplexDataModule._event_kind(plan.event)
        if kind == "death":
            plan.strategy = IntercurrentEventStrategy.HYPOTHETICAL
            plan.operational_rule = (
                "Post-death endpoint values are not imputed in the primary analysis. Estimate "
                "the outcome under the hypothetical condition that the participant remained "
                "alive through assessment, and assess departures with a prespecified "
                "worst-plausible delta sensitivity analysis."
            )
            plan.rationale = (
                "Death makes the patient-reported endpoint undefined; a hypothetical strategy "
                "keeps that assumption explicit and testable."
            )
        elif kind in {"switch", "rescue"}:
            plan.strategy = IntercurrentEventStrategy.TREATMENT_POLICY
            plan.operational_rule = (
                "Retain all outcome observations collected after the event in the primary "
                "analysis, record timing and reason, and repeat the analysis censoring at the "
                "event as a supportive analysis."
            )
            plan.rationale = (
                "The primary effect concerns outcomes after offering the study intervention, "
                "regardless of additional care; censoring is reserved for a supportive analysis."
            )
        else:
            plan.strategy = IntercurrentEventStrategy.TREATMENT_POLICY
            plan.operational_rule = (
                "Keep the participant in the assigned analysis population and use all available "
                "post-event outcome assessments regardless of intervention completion. Summarize "
                "attendance, exposure, timing, and reason separately."
            )
            plan.rationale = (
                "A treatment-policy strategy avoids conditioning the primary result on "
                "post-baseline intervention completion."
            )
        plan.provenance = Provenance(
            status=EvidenceStatus.INFERRED,
            note=(
                "Operational proposal generated because the protocol did not specify an ICE "
                "strategy; statistical and clinical confirmation is required."
            ),
        )

    @staticmethod
    def _add_event_clarification(ir: SAPIR, plan: IntercurrentEventPlan) -> None:
        add_clarification(
            ir,
            item_id=f"confirm-{plan.id}",
            module="complex_data",
            question=(
                f"请确认估计目标 {plan.estimand_id} 对伴发事件“{plan.event}”采用 "
                f"{plan.strategy.value} 策略及以下操作规则：{plan.operational_rule}"
            ),
            paths=[f"intercurrent_events.{len(ir.intercurrent_events) - 1}"],
        )

    def _enrich_missing_data(
        self,
        ir: SAPIR,
        estimand_id: str,
        endpoint: Endpoint,
    ) -> MissingDataPlan:
        plans = [item for item in ir.missing_data if item.estimand_id == estimand_id]
        if plans:
            plan = plans[0]
        else:
            plan = MissingDataPlan(
                id=f"missing-{estimand_id}-general",
                estimand_id=estimand_id,
                reason=(
                    "loss to follow-up, withdrawal, or an unavailable scheduled endpoint assessment"
                ),
                mechanism=MissingnessMechanism.UNRESOLVED,
                primary_method="",
                provenance=Provenance(status=EvidenceStatus.MISSING),
            )
            ir.missing_data.append(plan)

        if plan.mechanism == MissingnessMechanism.UNRESOLVED:
            plan.mechanism = MissingnessMechanism.MAR
        if self._is_missing(plan.primary_method):
            plan.primary_method = self._primary_missing_method(endpoint.endpoint_type)
        if self._is_missing(plan.sensitivity_method):
            plan.sensitivity_method = self._sensitivity_missing_method(endpoint.endpoint_type)
        if self._is_missing(plan.tipping_point_rule):
            plan.tipping_point_rule = self._tipping_point_rule(endpoint.endpoint_type)
        plan.provenance = Provenance(
            status=EvidenceStatus.INFERRED,
            note=(
                "MAR primary handling and MNAR delta sensitivity are explicit proposals because "
                "the protocol did not specify a missing-data strategy."
            ),
        )
        add_clarification(
            ir,
            item_id=f"confirm-{plan.id}",
            module="complex_data",
            question=(
                f"请确认估计目标 {estimand_id} 的 MAR 主假设、似然法主处理、"
                "与终点类型匹配的 MNAR/信息性缺失敏感性分析及临界点规则。"
            ),
            paths=[f"missing_data.{ir.missing_data.index(plan)}"],
        )
        return plan

    @staticmethod
    def _bind_missing_strategy(
        ir: SAPIR,
        estimand_id: str,
        plan: MissingDataPlan,
    ) -> None:
        for method in ir.analysis_methods:
            if method.estimand_id == estimand_id and method.role != AnalysisRole.SENSITIVITY:
                method.missing_data_strategy = plan.primary_method

    @staticmethod
    def _add_sensitivity_method(
        ir: SAPIR,
        estimand_id: str,
        plan: MissingDataPlan,
    ) -> None:
        primary = next(
            (
                method
                for method in ir.analysis_methods
                if method.estimand_id == estimand_id and method.role == AnalysisRole.PRIMARY
            ),
            None,
        )
        if primary is None or any(
            method.estimand_id == estimand_id and method.role == AnalysisRole.SENSITIVITY
            for method in ir.analysis_methods
        ):
            return
        ir.analysis_methods.append(
            AnalysisMethodSpec(
                id=f"analysis-{estimand_id}-sensitivity-mnar",
                estimand_id=estimand_id,
                role=AnalysisRole.SENSITIVITY,
                endpoint_type=primary.endpoint_type,
                analysis_population_id=primary.analysis_population_id,
                model=plan.sensitivity_method or "delta-adjusted pattern-mixture model",
                effect_measure=primary.effect_measure,
                test_method=(
                    "Repeat the primary contrast across the prespecified departure grid and "
                    "identify where its direction, confidence interval, or conclusion changes."
                ),
                covariates=list(primary.covariates),
                missing_data_strategy=plan.sensitivity_method,
                assumptions=[
                    "missing not at random",
                    "the departure grid spans clinically plausible departures from the primary assumption",
                ],
                rationale=(
                    "This sensitivity analysis changes the MAR assumption in the primary analysis "
                    "to explicit MNAR departures and measures robustness by a tipping point."
                ),
                provenance=Provenance(
                    status=EvidenceStatus.INFERRED,
                    note="System-proposed sensitivity analysis; confirmation required.",
                ),
            )
        )

    @staticmethod
    def _sync_estimand_strategies(ir: SAPIR, estimand_id: str) -> None:
        estimand = next(item for item in ir.estimands if item.id == estimand_id)
        supported = [
            f"{plan.event}: {plan.strategy.value}; {plan.operational_rule}"
            for plan in ir.intercurrent_events
            if plan.estimand_id == estimand_id
        ]
        if supported:
            estimand.intercurrent_event_strategies = supported

    @staticmethod
    def _event_kind(event: str) -> str:
        value = event.lower()
        if "death" in value or "死亡" in value:
            return "death"
        if "rescue" in value or "救援" in value:
            return "rescue"
        if any(term in value for term in ("switch", "alternative", "concomitant", "换药")):
            return "switch"
        return "discontinuation"

    @staticmethod
    def _primary_missing_method(endpoint_type: EndpointType) -> str:
        if endpoint_type == EndpointType.TIME_TO_EVENT:
            return (
                "Use all observed event and censoring times; censor event-free participants at "
                "their last confirmed event-free assessment under the primary non-informative "
                "censoring assumption, with active follow-up status summarized by treatment."
            )
        if endpoint_type == EndpointType.BINARY:
            return (
                "Use model-compatible multiple imputation under MAR, conditioning on treatment, "
                "baseline outcome/risk factors and observed follow-up; fit the primary binary "
                "model in each imputed data set and combine estimates using Rubin's rules."
            )
        if endpoint_type in {EndpointType.CONTINUOUS, EndpointType.ORDINAL}:
            return (
                "Use the likelihood-based longitudinal primary model with every observed baseline "
                "and post-baseline value and no single imputation, under MAR conditional on "
                "observed outcomes and prespecified baseline predictors."
            )
        if endpoint_type == EndpointType.COUNT:
            return (
                "Fit the primary count model using observed follow-up and the prespecified exposure "
                "offset; impute missing covariates under MAR and summarize follow-up exposure and "
                "reasons for incomplete observation by treatment."
            )
        return (
            "Analyze all observed endpoint data and describe the amount, timing and reasons for "
            "missingness; use model-compatible multiple imputation under MAR when the endpoint "
            "supports a formal contrast."
        )

    @staticmethod
    def _sensitivity_missing_method(endpoint_type: EndpointType) -> str:
        if endpoint_type == EndpointType.TIME_TO_EVENT:
            return (
                "Assess informative censoring with a prespecified tipping-point analysis that "
                "multiplies the post-censoring event hazard over a clinically plausible grid; "
                "refit the primary time-to-event model at each multiplier."
            )
        return (
            "Use an MNAR pattern-mixture sensitivity analysis, shifting imputed missing outcomes "
            "over the standardized departure grid 0, ±0.25, ±0.50, ±0.75 and ±1.00 residual SD "
            "or the endpoint-scale equivalent; refit the primary model at each value."
        )

    @staticmethod
    def _tipping_point_rule(endpoint_type: EndpointType) -> str:
        parameter = "post-censoring hazard multiplier" if endpoint_type == EndpointType.TIME_TO_EVENT else "adverse departure"
        return (
            f"Increase the {parameter} until the primary conclusion changes; report the smallest "
            "tipping-point value and compare it with clinically plausible departures."
        )

    @staticmethod
    def _is_missing(value: str | None) -> bool:
        if not value:
            return True
        normalized = value.strip().lower()
        return normalized.startswith("not specified") or normalized in {
            "待确认",
            "tbd",
            "unresolved",
        }
