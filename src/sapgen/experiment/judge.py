from __future__ import annotations

import json
from collections import defaultdict
from json import JSONDecodeError
from pathlib import Path
from typing import Any

from sapgen.experiment.dataset import load_jsonl
from sapgen.experiment.llm import OpenAIChatClient, parse_json_object
from sapgen.experiment.rubrics import SAP7_RUBRICS


def _bounded_candidate(text: str, maximum: int = 180_000) -> str:
    if len(text) <= maximum:
        return text
    head = maximum - 45_000
    return text[:head] + "\n\n[...middle omitted for judge context limit...]\n\n" + text[-45_000:]


class SemanticJudge:
    def __init__(
        self,
        *,
        benchmark_root: Path,
        client: OpenAIChatClient,
    ) -> None:
        self.benchmark_root = benchmark_root.resolve()
        self.source_root = self.benchmark_root / "source"
        self.experiment_root = self.benchmark_root / "experiment"
        self.client = client
        self.document_roles = {
            item["document_id"]: item["role"]
            for item in load_jsonl(self.source_root / "manifests" / "documents.jsonl")
        }
        self.rubric_metadata = self._load_rubric_metadata()

    def _load_rubric_metadata(self) -> dict[str, dict[str, Any]]:
        records: dict[str, dict[str, Any]] = {}
        for path in (self.source_root / "rubrics").glob("*.jsonl"):
            for item in load_jsonl(path):
                records[item["rubric_id"]] = item
        for item in SAP7_RUBRICS:
            records[item["rubric_id"]] = item
        return records

    def requirements_for(self, question: dict[str, Any]) -> list[dict[str, Any]]:
        original = load_jsonl(self.source_root / question["requirements_path"])
        supplements = load_jsonl(self.benchmark_root / question["supplemental_requirements_path"])
        combined = []
        for requirement in [*original, *supplements]:
            item = dict(requirement)
            item["evidence"] = [
                evidence
                for evidence in requirement.get("evidence", [])
                if self.document_roles.get(evidence.get("document_id"))
                in {"protocol", "crf", "annotated_crf"}
            ]
            combined.append(item)
        return combined

    def evaluate(
        self,
        *,
        question: dict[str, Any],
        protocol_text: str,
        candidate_text: str,
    ) -> dict[str, Any]:
        requirements = self.requirements_for(question)
        compact_requirements = [
            {
                "requirement_id": item["requirement_id"],
                "rubric_id": item["rubric_id"],
                "severity": item["severity"],
                "status": item["status"],
                "requirement": item["requirement"],
                "acceptable_values": item.get("acceptable_values", []),
                "allowed_evidence": item.get("evidence", []),
                "notes": item.get("notes", ""),
            }
            for item in requirements
        ]
        prompt = (
            "Evaluate the candidate SAP against every requirement below. The candidate method is "
            "blinded. Use only the protocol, candidate SAP, and requirement record. Do not use or "
            "reconstruct a reference SAP. For proposed or needs_confirmation decisions, do not "
            "penalize a statistically defensible alternative or an explicit confirmation request "
            "when the protocol is silent; do penalize invented decisions presented as protocol facts.\n\n"
            "Return exactly one JSON object with key evaluations. evaluations must contain exactly "
            "one object per requirement, in the supplied order, with fields: requirement_id, "
            "result (pass|fail|na|uncertain), score (integer 0..4), reason, candidate_evidence "
            "(array of short verbatim candidate excerpts), confidence (0..1). Score 4 means fully "
            "satisfied and executable; 3 mostly satisfied; 2 partial; 1 superficial; 0 absent, "
            "contradictory, inappropriate, or invented. Use uncertain only when the supplied material "
            "cannot support a reliable judgment.\n\n"
            f"STUDY_ID\n{question['study_id']}\n\n"
            f"PROTOCOL\n{protocol_text}\n\n"
            f"REQUIREMENTS\n{json.dumps(compact_requirements, ensure_ascii=False)}\n\n"
            f"CANDIDATE_SAP\n{_bounded_candidate(candidate_text)}"
        )
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a conservative independent clinical-trial SAP judge. Apply the "
                    "rubric consistently and return auditable structured judgments."
                ),
            },
            {"role": "user", "content": prompt},
        ]
        parse_error: Exception | None = None
        for structured_attempt in range(2):
            attempt_messages = list(messages)
            if structured_attempt:
                attempt_messages.append(
                    {
                        "role": "user",
                        "content": (
                            "The previous response was not a complete valid JSON object. Re-evaluate "
                            "from the supplied material and return compact JSON only. Use short reasons "
                            "and at most two short candidate-evidence excerpts per requirement."
                        ),
                    }
                )
            result = self.client.complete(attempt_messages)
            try:
                parsed = parse_json_object(result.text)
                break
            except (JSONDecodeError, TypeError, ValueError) as exc:
                parse_error = exc
        else:
            raise RuntimeError(f"Judge returned invalid JSON twice: {parse_error}")
        raw_evaluations = parsed.get("evaluations")
        if not isinstance(raw_evaluations, list):
            raise TypeError("Judge response has no evaluations array")
        by_id = {
            item.get("requirement_id"): item
            for item in raw_evaluations
            if isinstance(item, dict) and item.get("requirement_id")
        }
        evaluations = []
        for requirement in requirements:
            requirement_id = requirement["requirement_id"]
            item = by_id.get(requirement_id)
            if item is None:
                item = {
                    "requirement_id": requirement_id,
                    "result": "uncertain",
                    "score": 0,
                    "reason": "Judge omitted this requirement.",
                    "candidate_evidence": [],
                    "confidence": 0.0,
                }
            item = self._normalize_evaluation(item, requirement)
            evaluations.append(item)
        summary = self._summarize(evaluations)
        return {
            "study_id": question["study_id"],
            "judge": {
                "model": result.model,
                "elapsed_ms": result.elapsed_ms,
                "usage": result.usage,
                "finish_reason": result.finish_reason,
            },
            "summary": summary,
            "evaluations": evaluations,
        }

    def _normalize_evaluation(
        self, item: dict[str, Any], requirement: dict[str, Any]
    ) -> dict[str, Any]:
        result = item.get("result")
        if result not in {"pass", "fail", "na", "uncertain"}:
            result = "uncertain"
        try:
            score = int(item.get("score", 0))
        except (TypeError, ValueError):
            score = 0
        score = max(0, min(4, score))
        if result == "na":
            score = 0
        rubric = self.rubric_metadata.get(requirement["rubric_id"], {})
        return {
            "requirement_id": requirement["requirement_id"],
            "rubric_id": requirement["rubric_id"],
            "category": rubric.get("category", requirement["rubric_id"]),
            "severity": requirement["severity"],
            "status": requirement["status"],
            "result": result,
            "score": score,
            "max_score": 4,
            "weight": float(rubric.get("weight", 1.0)),
            "reason": str(item.get("reason") or "No rationale returned."),
            "candidate_evidence": [
                str(value)[:500] for value in item.get("candidate_evidence", [])
            ],
            "confidence": max(0.0, min(1.0, float(item.get("confidence") or 0.0))),
        }

    @staticmethod
    def _summarize(evaluations: list[dict[str, Any]]) -> dict[str, Any]:
        applicable = [item for item in evaluations if item["result"] != "na"]
        weight_total = sum(item["weight"] for item in applicable)
        weighted_points = sum(item["weight"] * item["score"] / 4 for item in applicable)
        category_rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for item in applicable:
            if item["rubric_id"].startswith("SAP7-"):
                category_rows[item["category"]].append(item)
        category_scores = {
            category: round(100 * sum(row["score"] for row in rows) / (4 * len(rows)), 2)
            for category, rows in category_rows.items()
        }
        critical = [item for item in applicable if item["severity"] == "critical"]
        return {
            "weighted_score": round(100 * weighted_points / weight_total, 2)
            if weight_total
            else None,
            "critical_pass": bool(critical)
            and all(item["result"] == "pass" and item["score"] >= 3 for item in critical),
            "counts": {
                name: sum(item["result"] == name for item in evaluations)
                for name in ("pass", "fail", "na", "uncertain")
            },
            "sap7_category_scores": category_scores,
        }
