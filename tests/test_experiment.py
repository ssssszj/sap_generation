from __future__ import annotations

import json
from pathlib import Path

from sapgen.experiment.adapters import DirectLLMNativeAdapter
from sapgen.experiment.judge import SemanticJudge
from sapgen.experiment.llm import LLMCallResult, OpenAIChatClient
from sapgen.experiment.rubrics import SAP7_RUBRICS
from sapgen.experiment.runner import _protocol_excerpt, _repair_fragmented_words
from sapgen.ingest.documents import EvidenceChunk, EvidenceCorpus

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT_ROOT = PROJECT_ROOT / "benchmark" / "experiment"


class CapturingClient:
    def __init__(self) -> None:
        self.messages: list[dict[str, str]] = []

    def complete(self, messages: list[dict[str, str]]) -> LLMCallResult:
        self.messages = messages
        return LLMCallResult(
            text="SAP",
            model="test-model",
            elapsed_ms=1,
            finish_reason="stop",
        )


class FlakyStructuredClient:
    def __init__(self) -> None:
        self.calls = 0

    def complete(self, _messages: list[dict[str, str]]) -> LLMCallResult:
        self.calls += 1
        return LLMCallResult(
            text="{" if self.calls == 1 else '{"evaluations": []}',
            model="test-model",
            elapsed_ms=1,
            finish_reason="stop",
        )


def test_sample_has_twenty_unique_studies_and_three_named_methods() -> None:
    sample = json.loads((EXPERIMENT_ROOT / "sample.json").read_text(encoding="utf-8"))
    study_ids = [item["study_id"] for item in sample["questions"]]
    assert len(study_ids) == len(set(study_ids)) == 20
    assert sample["methods"] == ["direct_llm_native", "sap_ver1", "dsh_sap"]
    assert sample["generation_config"]["temperature_policy"] == "provider_default_omitted"


def test_every_sampled_study_has_all_seven_supplemental_rubrics() -> None:
    sample = json.loads((EXPERIMENT_ROOT / "sample.json").read_text(encoding="utf-8"))
    expected = {item["rubric_id"] for item in SAP7_RUBRICS}
    for question in sample["questions"]:
        path = PROJECT_ROOT / "benchmark" / question["supplemental_requirements_path"]
        records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        assert {item["rubric_id"] for item in records} == expected
        assert len(records) == 7


def test_common_llm_endpoint_and_weighted_summary() -> None:
    client = OpenAIChatClient(
        api_key="not-used",
        model="model",
        base_url="https://example.test",
        max_tokens=100,
    )
    assert client.endpoint == "https://example.test/v1/chat/completions"
    summary = SemanticJudge._summarize(
        [
            {
                "result": "pass",
                "score": 4,
                "weight": 2.0,
                "severity": "critical",
                "rubric_id": "SAP7-ESTIMAND-001",
                "category": "确定估计目标",
            },
            {
                "result": "fail",
                "score": 0,
                "weight": 1.0,
                "severity": "major",
                "rubric_id": "CORE-METHOD-001",
                "category": "method",
            },
        ]
    )
    assert summary["weighted_score"] == 66.67
    assert summary["critical_pass"] is True
    assert summary["sap7_category_scores"]["确定估计目标"] == 100.0


def test_native_direct_prompt_does_not_leak_rubric_categories(tmp_path: Path) -> None:
    client = CapturingClient()
    DirectLLMNativeAdapter(client).generate("protocol body", tmp_path / "p.txt", tmp_path / "c.txt")
    prompt = "\n".join(message["content"] for message in client.messages).lower()
    forbidden = (
        "estimand",
        "sensitivity analysis",
        "intercurrent event",
        "missing-data mechanism",
        "meddra",
        "soc/pt",
        "denominator",
        "tfl",
    )
    assert all(term not in prompt for term in forbidden)


def test_protocol_excerpt_selects_late_statistical_sections() -> None:
    corpus = EvidenceCorpus(
        chunks=[
            EvidenceChunk("x", "p.pdf", "page 1", "Study title and randomized design."),
            *[
                EvidenceChunk("x", "p.pdf", f"page {index}", "Administrative material. " * 80)
                for index in range(2, 20)
            ],
            EvidenceChunk(
                "x",
                "p.pdf",
                "page 20",
                "Statistical analysis: primary endpoint, analysis population, sample size, "
                "missing data, multiplicity, confidence interval and sensitivity analysis.",
            ),
        ]
    )

    excerpt, metadata = _protocol_excerpt(corpus, 2_000)

    assert "Study title" in excerpt
    assert "Statistical analysis" in excerpt
    assert metadata["chunks_selected"] < metadata["chunks_available"]


def test_fragmented_pdf_words_are_repaired() -> None:
    assert _repair_fragmented_words("S t a t i s t i c a l analysis") == "Statistical analysis"


def test_judge_retries_invalid_structured_output() -> None:
    client = FlakyStructuredClient()
    judge = SemanticJudge(benchmark_root=PROJECT_ROOT / "benchmark", client=client)
    sample = json.loads((EXPERIMENT_ROOT / "sample.json").read_text(encoding="utf-8"))

    result = judge.evaluate(
        question=sample["questions"][0],
        protocol_text="Protocol text",
        candidate_text="Candidate SAP",
    )

    assert client.calls == 2
    assert result["evaluations"]
