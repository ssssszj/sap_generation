from __future__ import annotations

import pytest

from sapgen.domain.models import SAPSection
from sapgen.generation import (
    CHAPTER_BODY_MAX_CHARS,
    CHAPTER_PLAN,
    HarnessChapterGenerator,
    HarnessDraftReviewer,
)
from sapgen.harness.base import HarnessResponseError
from sapgen.harness.fake import FakeHarnessAdapter
from sapgen.ingest.documents import EvidenceChunk, EvidenceCorpus
from sapgen.ingest.extractor import SAPIRExtractor


def _provenance() -> dict:
    return {"status": "missing", "evidence": [], "note": None}


def test_staged_extraction_merges_four_domain_responses() -> None:
    responses = [
        {
            "study": {
                "study_id": "S-1",
                "title": "Test study",
                "phase": None,
                "design": "Randomized parallel-group study",
                "treatment_arms": ["A", "B"],
                "randomization": "1:1",
                "blinding": None,
                "provenance": _provenance(),
            },
            "sample_size": {
                "planned_total": "100",
                "planned_per_group": {"A": "50", "B": "50"},
                "statistical_basis": "Protocol calculation",
                "dropout_assumption": None,
                "operational_constraints": None,
                "provenance": _provenance(),
            },
            "clarifications": [],
        },
        {
            "endpoints": [
                {
                    "id": "EP-1",
                    "name": "Outcome",
                    "endpoint_type": "continuous",
                    "definition": "Outcome at Week 4",
                    "timepoint": "Week 4",
                    "derivation": None,
                    "priority": "primary",
                    "provenance": _provenance(),
                }
            ],
            "derivation_rules": [],
            "clarifications": [],
        },
        {
            "estimands": [
                {
                    "id": "EST-1",
                    "objective": "Estimate change",
                    "population": "FAS",
                    "variable": "Outcome at Week 4",
                    "treatment_condition": "Treatment",
                    "intercurrent_event_strategies": [],
                    "population_summary": "Mean change",
                    "endpoint_id": "EP-1",
                    "provenance": _provenance(),
                }
            ],
            "clarifications": [],
        },
        {
            "analysis_populations": [
                {
                    "id": "FAS",
                    "name": "Full Analysis Set",
                    "definition": "All enrolled participants",
                    "denominator_rule": "Number in FAS",
                    "provenance": _provenance(),
                }
            ],
            "safety": None,
            "clarifications": [],
        },
        {
            "analysis_methods": [
                {
                    "id": "AN-1",
                    "role": "secondary",
                    "endpoint_type": "continuous",
                    "model": "Repeated-measures model",
                    "effect_measure": "Mean change",
                    "test_method": "Model-based contrast",
                    "provenance": _provenance(),
                }
            ],
            "intercurrent_events": [],
            "missing_data": {
                "-001": [
                    {
                        "id": "MD-1",
                        "estimand_id": "EST-1",
                        "reason": "Missing follow-up measurement",
                        "mechanism": "unresolved",
                        "primary_method": "Not specified",
                        "provenance": _provenance(),
                    }
                ]
            },
            "multiplicity": None,
            "clarifications": [],
        },
    ]
    harness = FakeHarnessAdapter(responses)
    corpus = EvidenceCorpus(
        chunks=[
            EvidenceChunk(source_id="x", document_name="p.txt", locator="block 1", text="Protocol")
        ]
    )

    ir, used_harness = SAPIRExtractor(harness).extract(
        corpus, session_id="staged", allow_fallback=False
    )

    assert used_harness is True
    assert ir.study.study_id == "S-1"
    assert ir.sample_size is not None
    assert ir.sample_size.planned_total == "100"
    assert ir.analysis_methods[0].estimand_id == "EST-1"
    assert ir.analysis_methods[0].analysis_population_id == "FAS"
    assert ir.analysis_methods[0].role.value == "supportive"
    assert ir.analysis_methods[0].provenance.status.value == "inferred"
    assert ir.missing_data[0].id == "MD-1"
    assert len(harness.calls) == 5
    assert [call["session_id"] for call in harness.calls] == [
        "staged-design",
        "staged-endpoints",
        "staged-estimands",
        "staged-populations-safety",
        "staged-analysis",
    ]


def test_staged_extraction_recovers_with_compact_source_after_harness_failure() -> None:
    class RecoveringHarness(FakeHarnessAdapter):
        def __init__(self) -> None:
            super().__init__(
                [
                    {
                        "study": {
                            "study_id": "S-1",
                            "title": "Recovery study",
                            "phase": None,
                            "design": "Single-arm study",
                            "treatment_arms": ["A"],
                            "randomization": None,
                            "blinding": None,
                            "provenance": _provenance(),
                        },
                        "clarifications": [],
                    },
                    {"endpoints": [], "derivation_rules": [], "clarifications": []},
                    {"estimands": [], "clarifications": []},
                    {"analysis_populations": [], "safety": None, "clarifications": []},
                    {
                        "analysis_methods": [],
                        "intercurrent_events": [],
                        "missing_data": [],
                        "multiplicity": None,
                        "clarifications": [],
                    },
                ]
            )
            self.failed = False

        def complete_json(self, **kwargs) -> dict:
            if not self.failed:
                self.failed = True
                self.calls.append(kwargs)
                raise HarnessResponseError("ended with max-tokens")
            return super().complete_json(**kwargs)

    corpus = EvidenceCorpus(
        chunks=[
            EvidenceChunk(
                source_id="x",
                document_name="p.txt",
                locator=f"block {index}",
                text=("Study design and endpoint analysis. " * 80),
            )
            for index in range(30)
        ]
    )
    harness = RecoveringHarness()

    ir, used_harness = SAPIRExtractor(harness).extract(
        corpus, session_id="recovery", allow_fallback=False
    )

    assert used_harness is True
    assert ir.study.study_id == "S-1"
    assert [call["session_id"] for call in harness.calls[:2]] == [
        "recovery-design",
        "recovery-design-compact-retry",
    ]
    assert "RECOVERY MODE" in harness.calls[1]["user_prompt"]
    assert len(harness.calls[1]["user_prompt"]) < len(harness.calls[0]["user_prompt"])


def test_chapter_generation_carries_every_previous_chapter(demo_ir) -> None:
    responses = [
        {"body_markdown": f"Unique body for chapter {index}"}
        for index in range(1, len(CHAPTER_PLAN) + 1)
    ]
    harness = FakeHarnessAdapter(responses)

    sections = HarnessChapterGenerator(harness).generate(demo_ir, session_id="draft")

    assert len(sections) == len(CHAPTER_PLAN)
    assert len(harness.calls) == len(CHAPTER_PLAN)
    for index, call in enumerate(harness.calls, start=1):
        for previous in range(1, index):
            assert f"Unique body for chapter {previous}" in call["user_prompt"]
        assert f"Unique body for chapter {index}" not in call["user_prompt"]


def test_final_review_applies_only_named_chapter_revisions(demo_ir) -> None:
    demo_ir.generated_sections = [
        SAPSection(id="one", title="One", body_markdown="Original one"),
        SAPSection(id="two", title="Two", body_markdown="Original two"),
    ]
    harness = FakeHarnessAdapter(
        [
            {"issues": [], "body_markdown": ""},
            {
                "issues": ["Population binding was inconsistent."],
                "body_markdown": "Revised two",
            },
        ]
    )

    HarnessDraftReviewer(harness).review(demo_ir, session_id="review")

    assert demo_ir.generated_sections[0].body_markdown == "Original one"
    assert demo_ir.generated_sections[1].body_markdown == "Revised two"
    assert len(harness.calls) == 2
    assert [call["session_id"] for call in harness.calls] == ["review-01", "review-02"]
    assert "CURRENT CHAPTER 1: One [one]\nOriginal one" in harness.calls[0]["user_prompt"]
    assert "[two] Two: Original two" in harness.calls[0]["user_prompt"]
    assert "CURRENT CHAPTER 2: Two [two]\nOriginal two" in harness.calls[1]["user_prompt"]
    assert "[one] One: Original one" in harness.calls[1]["user_prompt"]


def test_final_review_keeps_chapter_after_two_harness_failures(demo_ir) -> None:
    class FailingHarness:
        def __init__(self) -> None:
            self.calls: list[str] = []

        def complete_json(self, **kwargs) -> dict:
            self.calls.append(kwargs["session_id"])
            raise HarnessResponseError("ended with max-tokens")

    demo_ir.generated_sections = [SAPSection(id="one", title="One", body_markdown="Original one")]
    harness = FailingHarness()

    with pytest.warns(UserWarning, match="keeping the generated chapter"):
        HarnessDraftReviewer(harness).review(demo_ir, session_id="review")

    assert demo_ir.generated_sections[0].body_markdown == "Original one"
    assert harness.calls == ["review-01", "review-01-retry"]


def test_final_review_retries_an_overlong_chapter(demo_ir) -> None:
    demo_ir.generated_sections = [SAPSection(id="one", title="One", body_markdown="Original one")]
    harness = FakeHarnessAdapter(
        [
            {
                "issues": ["Too verbose."],
                "body_markdown": "x" * (CHAPTER_BODY_MAX_CHARS + 1),
            },
            {"issues": ["Condensed."], "body_markdown": "Revised one"},
        ]
    )

    HarnessDraftReviewer(harness).review(demo_ir, session_id="review")

    assert demo_ir.generated_sections[0].body_markdown == "Revised one"
    assert [call["session_id"] for call in harness.calls] == [
        "review-01",
        "review-01-retry",
    ]


def test_final_review_allows_bounded_growth_for_an_already_long_chapter(demo_ir) -> None:
    original = "x" * 12_500
    revised = "y" * 13_000
    demo_ir.generated_sections = [SAPSection(id="one", title="One", body_markdown=original)]
    harness = FakeHarnessAdapter(
        [{"issues": ["A concise correction was applied."], "body_markdown": revised}]
    )

    HarnessDraftReviewer(harness).review(demo_ir, session_id="review")

    assert demo_ir.generated_sections[0].body_markdown == revised
    assert len(harness.calls) == 1
    assert harness.calls[0]["schema"]["properties"]["body_markdown"]["maxLength"] == 14_500
