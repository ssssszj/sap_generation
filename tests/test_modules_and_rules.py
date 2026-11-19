from __future__ import annotations

from sapgen.domain.models import Endpoint, EndpointType, Estimand
from sapgen.domain.rules import RuleEngine
from sapgen.modules import (
    AnalysisDesignModule,
    ComplexDataModule,
    DerivationSupportModule,
    EstimandDecisionModule,
    MethodSpecificationModule,
    MultiplicityModule,
    RobustnessDecisionModule,
    SafetyAnalysisModule,
    SafetySpecificationModule,
    SamplePopulationSpecificationModule,
    TFLGenerationModule,
    TFLSpecificationModule,
)


def test_specialized_modules_enrich_shared_ir(demo_ir) -> None:
    ir = demo_ir.model_copy(deep=True)
    for module in (
        AnalysisDesignModule(),
        ComplexDataModule(),
        MultiplicityModule(),
        SafetyAnalysisModule(),
        TFLGenerationModule(),
    ):
        module.enrich(ir)

    assert any(item.role.value == "primary" for item in ir.analysis_methods)
    assert ir.intercurrent_events
    assert ir.missing_data
    assert ir.safety is not None
    assert ir.tfl_specs
    clarification_ids = {item.id for item in ir.clarifications}
    assert "confirm-analysis-EST-PRIMARY" in clarification_ids
    assert any(item.startswith("confirm-ice-EST-PRIMARY-") for item in clarification_ids)
    assert "confirm-missing-EST-PRIMARY-general" in clarification_ids
    assert "confirm-safety-contract" in clarification_ids
    assert "confirm-multiplicity-policy" in clarification_ids


def test_rules_detect_unresolved_high_risk_fields(demo_ir) -> None:
    ir = demo_ir.model_copy(deep=True)
    AnalysisDesignModule().enrich(ir)
    ComplexDataModule().enrich(ir)
    MultiplicityModule().enrich(ir)
    SafetyAnalysisModule().enrich(ir)
    TFLGenerationModule().enrich(ir)
    report = RuleEngine().validate(ir)
    codes = {item.code for item in report.issues}

    assert "ICE-PLAN-MISSING" not in codes
    assert "MISS-PLAN-MISSING" not in codes
    assert "SAFETY-MISSING" not in codes
    assert "MULTIPLICITY-MISSING" not in codes
    assert "TFL-MISSING" not in codes
    assert not report.has_errors


def test_single_arm_repeated_design_adds_labelled_executable_proposal(demo_ir) -> None:
    ir = demo_ir.model_copy(deep=True)
    ir.study.design = "Single-arm pre-post study with baseline, Week 2, and Month 3 assessments"
    ir.study.treatment_arms = []
    ir.study.randomization = "Not described - the protocol contains no randomization statement"
    ir.endpoints[0].timepoint = "Baseline, Week 2 and Month 3"
    ir.endpoints[0].priority = "exploratory"
    ir.estimands[0].treatment_condition = "One workshop; no comparator arm"
    ir.endpoints.append(
        Endpoint(
            id="EP-SECONDARY",
            name="Secondary score",
            endpoint_type=EndpointType.CONTINUOUS,
            definition="Secondary score at baseline, Week 2 and Month 3",
            timepoint="Baseline, Week 2 and Month 3",
            priority="secondary",
        )
    )
    ir.estimands.append(
        Estimand(
            id="EST-SECONDARY",
            objective="Describe secondary score change",
            population="Full Analysis Set",
            variable="Secondary score",
            treatment_condition="One workshop; no comparator arm",
            population_summary="Mean change from baseline",
            endpoint_id="EP-SECONDARY",
        )
    )

    AnalysisDesignModule().enrich(ir)

    assert ir.analysis_methods
    assert ir.endpoints[0].priority == "primary"
    assert ir.endpoints[1].priority == "secondary"
    assert any(item.id == "confirm-endpoint-hierarchy-proposal" for item in ir.clarifications)
    assert ir.analysis_methods[0].provenance.status.value == "inferred"
    assert "mixed-effects" in ir.analysis_methods[0].model


def test_quality_support_targets_native_gaps_without_inventing_decisions(demo_ir) -> None:
    ir = demo_ir.model_copy(deep=True)
    for module in (
        EstimandDecisionModule(),
        SamplePopulationSpecificationModule(),
        MethodSpecificationModule(),
        RobustnessDecisionModule(),
        SafetySpecificationModule(),
        DerivationSupportModule(),
        TFLSpecificationModule(),
    ):
        module.enrich(ir)

    domains = {item.domain for item in ir.decision_support}
    assert {
        "estimand",
        "sample_size",
        "population",
        "method",
        "intercurrent_event",
        "missing_data",
        "sensitivity",
        "safety",
    }.issubset(domains)
    assert ir.analysis_methods == []
    assert ir.safety is None
    assert len(ir.derivation_rules) == 1
    assert len(ir.tfl_specs) == 1
    shell = ir.tfl_specs[0]
    assert shell.population_id == "FAS"
    assert "p-value" not in shell.statistics
    assert shell.provenance.status.value == "inferred"
