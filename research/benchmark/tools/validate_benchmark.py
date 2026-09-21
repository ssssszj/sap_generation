#!/usr/bin/env python3
"""Validate benchmark JSON/JSONL structure, references, hashes, and split policy."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
BENCHMARK = ROOT / "research" / "benchmark"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path):
    records = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
    return records


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_keys(record, keys, label, errors):
    missing = [key for key in keys if key not in record]
    if missing:
        errors.append(f"{label}: missing keys {missing}")


def main() -> int:
    errors = []
    warnings = []

    config = load_json(BENCHMARK / "configs" / "benchmark_v0.1.json")
    studies = load_jsonl(BENCHMARK / "manifests" / "studies.jsonl")
    documents = load_jsonl(BENCHMARK / "manifests" / "documents.jsonl")
    legacy_runs = load_jsonl(BENCHMARK / "manifests" / "legacy_runs.jsonl")
    rubric_paths = [BENCHMARK / item for item in config["rubrics"]]
    rubrics = [item for path in rubric_paths for item in load_jsonl(path)]

    for index, study in enumerate(studies, start=1):
        require_keys(
            study,
            ["study_id", "study_family_id", "title", "document_ids", "split", "status"],
            f"study[{index}]",
            errors,
        )
    for index, document in enumerate(documents, start=1):
        require_keys(
            document,
            ["document_id", "study_id", "role", "format", "path", "sha256"],
            f"document[{index}]",
            errors,
        )
    for index, rubric in enumerate(rubrics, start=1):
        require_keys(
            rubric,
            ["rubric_id", "category", "requirement", "severity", "weight", "applies_if", "evaluator"],
            f"rubric[{index}]",
            errors,
        )

    study_ids = [record.get("study_id") for record in studies]
    document_ids = [record.get("document_id") for record in documents]
    rubric_ids = [record.get("rubric_id") for record in rubrics]
    for name, values in [("study_id", study_ids), ("document_id", document_ids), ("rubric_id", rubric_ids)]:
        duplicates = sorted({value for value in values if value and values.count(value) > 1})
        if duplicates:
            errors.append(f"duplicate {name}: {duplicates}")

    study_id_set = set(study_ids)
    document_id_set = set(document_ids)
    rubric_id_set = set(rubric_ids)
    for document in documents:
        if document["study_id"] not in study_id_set:
            errors.append(f"document {document['document_id']} references unknown study {document['study_id']}")
        source_path = ROOT / document["path"]
        if not source_path.is_file():
            errors.append(f"document {document['document_id']} missing at {source_path}")
        else:
            actual_hash = file_sha256(source_path)
            if actual_hash != document["sha256"]:
                errors.append(
                    f"document {document['document_id']} hash mismatch: manifest={document['sha256']} actual={actual_hash}"
                )

    run_ids = [record.get("run_id") for record in legacy_runs]
    duplicate_runs = sorted({value for value in run_ids if value and run_ids.count(value) > 1})
    if duplicate_runs:
        errors.append(f"duplicate run_id: {duplicate_runs}")
    for index, run in enumerate(legacy_runs, start=1):
        require_keys(
            run,
            ["run_id", "study_id", "track", "method", "model", "input_document_ids", "status"],
            f"legacy_run[{index}]",
            errors,
        )
        if run.get("study_id") not in study_id_set:
            errors.append(f"legacy run {run.get('run_id')} references unknown study {run.get('study_id')}")
        unknown_inputs = sorted(set(run.get("input_document_ids", [])) - document_id_set)
        if unknown_inputs:
            errors.append(f"legacy run {run.get('run_id')} references unknown inputs {unknown_inputs}")
        output_path = run.get("output_path")
        if output_path:
            resolved = ROOT / output_path
            if not resolved.is_file():
                errors.append(f"legacy run {run.get('run_id')} output missing at {resolved}")
            elif run.get("output_sha256") and file_sha256(resolved) != run["output_sha256"]:
                errors.append(f"legacy run {run.get('run_id')} output hash mismatch")

    family_splits = {}
    for study in studies:
        family_splits.setdefault(study["study_family_id"], set()).add(study["split"])
        unknown_docs = sorted(set(study["document_ids"]) - document_id_set)
        if unknown_docs:
            errors.append(f"study {study['study_id']} references unknown documents {unknown_docs}")
    for family_id, splits in family_splits.items():
        if len(splits) > 1:
            errors.append(f"study family {family_id} appears in multiple splits: {sorted(splits)}")

    requirements = []
    for requirement_file in sorted((BENCHMARK / "gold").glob("*/requirements.jsonl")):
        file_records = load_jsonl(requirement_file)
        requirements.extend(file_records)
        annotation_status_path = requirement_file.parent / "annotation_status.json"
        if annotation_status_path.is_file():
            declared = load_json(annotation_status_path).get("requirement_count")
            if declared != len(file_records):
                errors.append(
                    f"{annotation_status_path}: requirement_count={declared}, actual={len(file_records)}"
                )
        for line_number, requirement in enumerate(file_records, start=1):
            label = f"{requirement_file}:{line_number}"
            require_keys(
                requirement,
                [
                    "requirement_id",
                    "study_id",
                    "rubric_id",
                    "tracks",
                    "applies",
                    "status",
                    "severity",
                    "requirement",
                    "acceptable_values",
                    "evidence",
                ],
                label,
                errors,
            )
            if requirement.get("study_id") not in study_id_set:
                errors.append(f"{label}: unknown study_id {requirement.get('study_id')}")
            if requirement.get("rubric_id") not in rubric_id_set:
                errors.append(f"{label}: unknown rubric_id {requirement.get('rubric_id')}")
            for evidence in requirement.get("evidence", []):
                if evidence.get("document_id") not in document_id_set:
                    errors.append(f"{label}: unknown evidence document {evidence.get('document_id')}")
                if not evidence.get("locator") or not evidence.get("text"):
                    errors.append(f"{label}: evidence must include non-empty locator and text")
            if requirement.get("status") == "needs_confirmation" and "deterministic" in requirement:
                warnings.append(
                    f"{label}: needs_confirmation item has deterministic hints; semantic review remains mandatory"
                )

    requirement_ids = [record.get("requirement_id") for record in requirements]
    duplicates = sorted({value for value in requirement_ids if value and requirement_ids.count(value) > 1})
    if duplicates:
        errors.append(f"duplicate requirement_id: {duplicates}")

    pilot_split = load_json(BENCHMARK / "splits" / "pilot.json")
    for study_id in pilot_split["study_ids"]:
        match = next((study for study in studies if study["study_id"] == study_id), None)
        if not match:
            errors.append(f"pilot split references unknown study {study_id}")
        elif match["split"] != "pilot" or match["status"] != "pilot_only":
            errors.append(f"pilot study {study_id} is not marked pilot/pilot_only")

    print(
        json.dumps(
            {
                "benchmark_version": config["version"],
                "studies": len(studies),
                "documents": len(documents),
                "legacy_runs": len(legacy_runs),
                "rubric_items": len(rubrics),
                "requirements": len(requirements),
                "warnings": warnings,
                "errors": errors,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
