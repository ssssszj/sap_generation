#!/usr/bin/env python3
"""Run the deterministic subset of evidence-backed SAP requirements."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "").lower()
    translations = {
        "～": "~",
        "—": "-",
        "–": "-",
        "−": "-",
        "＜": "<",
        "＞": ">",
        "≤": "<=",
        "≥": ">=",
        "△": "delta",
        "Δ": "delta",
        "δ": "delta",
        "μ": "mu",
    }
    for source, target in translations.items():
        text = text.replace(source, target)
    return re.sub(r"\s+", "", text)


def snippet(text: str, needle: str, width: int = 90) -> str | None:
    normalized_text = normalize(text)
    normalized_needle = normalize(needle)
    position = normalized_text.find(normalized_needle)
    if position < 0:
        return None
    # Position is in normalized text, so return a general informative snippet from
    # the first original line containing the unnormalized or compact term.
    for line in text.splitlines():
        if normalized_needle in normalize(line):
            line = line.strip()
            return line[:width] + ("..." if len(line) > width else "")
    return needle


def evaluate(requirement, candidate_text: str, track: str):
    base = {
        "study_id": requirement["study_id"],
        "requirement_id": requirement["requirement_id"],
        "rubric_id": requirement["rubric_id"],
        "track": track,
        "severity": requirement["severity"],
        "evaluator": "rule",
        "gold_evidence": [item["text"] for item in requirement.get("evidence", [])],
    }
    if track not in requirement["tracks"] or not requirement["applies"]:
        return {
            **base,
            "result": "na",
            "reason": "Requirement is not applicable to this track.",
            "candidate_evidence": [],
            "confidence": 1.0,
        }

    check = requirement.get("deterministic")
    if not check:
        return {
            **base,
            "result": "uncertain",
            "reason": "No deterministic matcher is defined; semantic or human review is required.",
            "candidate_evidence": [],
            "confidence": None,
        }

    normalized_candidate = normalize(candidate_text)
    missing = []
    forbidden_hits = []
    evidence = []

    for term in check.get("all_of", []):
        if normalize(term) not in normalized_candidate:
            missing.append(f"required term: {term}")
        else:
            hit = snippet(candidate_text, term)
            if hit:
                evidence.append(hit)

    for alternatives in check.get("any_of", []):
        matched = next((term for term in alternatives if normalize(term) in normalized_candidate), None)
        if not matched:
            missing.append("one of: " + " | ".join(alternatives))
        else:
            hit = snippet(candidate_text, matched)
            if hit:
                evidence.append(hit)

    for pattern in check.get("regex_all", []):
        if not re.search(pattern, candidate_text, flags=re.IGNORECASE | re.MULTILINE):
            missing.append(f"regex: {pattern}")

    for term in check.get("forbidden", []):
        if normalize(term) in normalized_candidate:
            forbidden_hits.append(term)

    if missing or forbidden_hits:
        reason_parts = []
        if missing:
            reason_parts.append("Missing " + "; ".join(missing))
        if forbidden_hits:
            reason_parts.append("Forbidden terms found: " + ", ".join(forbidden_hits))
        return {
            **base,
            "result": "fail",
            "reason": ". ".join(reason_parts),
            "candidate_evidence": sorted(set(evidence)),
            "confidence": 1.0,
        }

    if requirement["status"] in {"proposed", "needs_confirmation"}:
        return {
            **base,
            "result": "uncertain",
            "reason": "Deterministic surface conditions were found, but the item requires semantic review of proposal/confirmation framing.",
            "candidate_evidence": sorted(set(evidence)),
            "confidence": None,
        }

    return {
        **base,
        "result": "pass",
        "reason": "All deterministic conditions were found.",
        "candidate_evidence": sorted(set(evidence)),
        "confidence": 1.0,
    }


def build_summary(results):
    applicable = [item for item in results if item["result"] != "na"]
    counts = {status: sum(item["result"] == status for item in results) for status in ["pass", "fail", "na", "uncertain"]}
    critical = [item for item in applicable if item["severity"] == "critical"]
    if any(item["result"] == "fail" for item in critical):
        study_pass = False
    elif any(item["result"] == "uncertain" for item in critical):
        study_pass = None
    else:
        study_pass = bool(critical)
    decided = [item for item in applicable if item["result"] in {"pass", "fail"}]
    return {
        "counts": counts,
        "deterministic_pass_rate": (
            sum(item["result"] == "pass" for item in decided) / len(decided) if decided else None
        ),
        "study_level_critical_pass": study_pass,
        "note": "Null study_level_critical_pass means at least one critical item still requires semantic or human adjudication.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--requirements", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument(
        "--candidate-label",
        help="Stable source label recorded in the result instead of a temporary extracted-text path.",
    )
    parser.add_argument(
        "--track",
        choices=["protocol_only", "protocol_crf", "confirmed_decisions"],
        required=True,
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    requirements = load_jsonl(args.requirements)
    candidate_text = args.candidate.read_text(encoding="utf-8")
    results = [evaluate(requirement, candidate_text, args.track) for requirement in requirements]
    payload = {
        "track": args.track,
        "candidate": args.candidate_label or str(args.candidate),
        "summary": build_summary(results),
        "results": results,
    }
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
