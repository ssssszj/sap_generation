from __future__ import annotations

from sapgen.benchmark import DEFAULT_RUBRICS, BenchmarkEvaluator
from sapgen.modules import (
    AnalysisDesignModule,
    ComplexDataModule,
    MultiplicityModule,
    SafetyAnalysisModule,
    TFLGenerationModule,
)


def test_benchmark_scores_all_seven_rubrics(demo_ir) -> None:
    ir = demo_ir.model_copy(deep=True)
    for module in (
        AnalysisDesignModule(),
        ComplexDataModule(),
        MultiplicityModule(),
        SafetyAnalysisModule(),
        TFLGenerationModule(),
    ):
        module.enrich(ir)
    result = BenchmarkEvaluator().evaluate(ir)
    assert len(result.criteria) == len(DEFAULT_RUBRICS) == 7
    assert result.max_score == 14
    assert result.total_score == result.max_score
    assert result.critical_error_count == 0
