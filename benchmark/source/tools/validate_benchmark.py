#!/usr/bin/env python3
"""Validate benchmark JSON/JSONL structure, references, hashes, and split policy."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
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

    config = load_json(BENCHMARK / "configs" / "benchmark_v0.3.json")
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

    # A study family can acquire a different descriptive suffix while still
    # referring to the same registered trial.  Treat the NCT identifier as the
    # canonical public-study family key so suffix drift cannot put two
    # questions from one trial into the benchmark.
    studies_by_nct = {}
    for study in studies:
        match = re.search(r"NCT\d{8}", study.get("study_family_id", ""))
        if match:
            studies_by_nct.setdefault(match.group(0), []).append(study.get("study_id"))
    duplicate_nct_families = {
        nct: study_ids
        for nct, study_ids in studies_by_nct.items()
        if len(study_ids) > 1
    }
    if duplicate_nct_families:
        errors.append(f"duplicate NCT study families: {duplicate_nct_families}")

    study_id_set = set(study_ids)
    document_id_set = set(document_ids)
    rubric_id_set = set(rubric_ids)
    document_by_id = {record["document_id"]: record for record in documents}
    for document in documents:
        if document["study_id"] not in study_id_set:
            errors.append(f"document {document['document_id']} references unknown study {document['study_id']}")
        if document.get("availability") == "public":
            normalized_path = document["path"].replace("\\", "/")
            if document.get("role") == "reference_sap" and "/reference/" not in normalized_path:
                errors.append(
                    f"public reference SAP {document['document_id']} is not isolated under a reference directory"
                )
            if document.get("role") in {"protocol", "crf", "annotated_crf"} and "/input/" not in normalized_path:
                errors.append(
                    f"public model-visible document {document['document_id']} is not isolated under an input directory"
                )
        source_path = ROOT / document["path"]
        if not source_path.is_file():
            if document.get("availability") == "public" and document.get("source_url"):
                warnings.append(
                    f"document {document['document_id']} is public remote-only; "
                    f"fetch and verify SHA-256 before generation"
                )
            else:
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
            evidence_roles = {
                document_by_id[item["document_id"]]["role"]
                for item in requirement.get("evidence", [])
                if item.get("document_id") in document_by_id
            }
            if (
                requirement.get("status") == "explicit"
                and "protocol_only" in requirement.get("tracks", [])
                and evidence_roles
                and evidence_roles <= {"reference_sap"}
            ):
                errors.append(
                    f"{label}: explicit reference-only decision cannot be required on protocol_only"
                )
            if requirement.get("status") == "needs_confirmation" and "deterministic" in requirement:
                warnings.append(
                    f"{label}: needs_confirmation item has deterministic hints; semantic review remains mandatory"
                )

    requirement_ids = [record.get("requirement_id") for record in requirements]
    duplicates = sorted({value for value in requirement_ids if value and requirement_ids.count(value) > 1})
    if duplicates:
        errors.append(f"duplicate requirement_id: {duplicates}")

    final_audit_path = BENCHMARK / "final_audit" / "questions.jsonl"
    question_set_path = BENCHMARK / "final_audit" / "initial_draft_question_set.json"
    if final_audit_path.is_file() or question_set_path.is_file():
        if not final_audit_path.is_file() or not question_set_path.is_file():
            errors.append("final audit and initial draft question set must be present together")
        else:
            audit_rows = load_jsonl(final_audit_path)
            question_set = load_json(question_set_path)
            public_study_ids = {item["study_id"] for item in studies if item.get("status") != "pilot_only"}
            audit_ids = [item.get("study_id") for item in audit_rows]
            if len(audit_ids) != len(set(audit_ids)):
                errors.append("final audit contains duplicate study_id values")
            if set(audit_ids) != public_study_ids:
                errors.append("final audit study IDs do not exactly cover the registered public studies")
            allowed_dispositions = {
                "keep_draft",
                "hold_version_or_provenance",
                "exclude_post_primary_or_execution_informed",
            }
            unknown_dispositions = sorted(
                {item.get("disposition") for item in audit_rows} - allowed_dispositions
            )
            if unknown_dispositions:
                errors.append(f"final audit contains unknown dispositions: {unknown_dispositions}")
            selected_ids = question_set.get("study_ids", [])
            keep_ids = [item["study_id"] for item in audit_rows if item.get("disposition") == "keep_draft"]
            if selected_ids != keep_ids:
                errors.append("initial draft question set does not exactly match final-audit keep_draft rows")
            if question_set.get("question_count") != len(selected_ids):
                errors.append("initial draft question_count does not match study_ids length")
            questions = question_set.get("questions", [])
            if [item.get("study_id") for item in questions] != selected_ids:
                errors.append("initial draft question records do not exactly match study_ids")
            reference_ids = {item.get("reference_sap_document_id") for item in audit_rows}
            for question in questions:
                if set(question.get("input_document_ids", [])) & reference_ids:
                    errors.append(f"question {question.get('study_id')} exposes a reference SAP as input")
            for item in audit_rows:
                if item.get("annotation_status") != "draft_needs_expert_review":
                    errors.append(f"final audit {item.get('study_id')}: annotation is not draft_needs_expert_review")
                if item.get("requirement_count") != len(
                    [requirement for requirement in requirements if requirement.get("study_id") == item.get("study_id")]
                ):
                    errors.append(f"final audit {item.get('study_id')}: stale requirement_count")

    configured_question_count = config.get("scale_target", {}).get("initial_draft_questions")
    if configured_question_count is not None and question_set_path.is_file():
        actual_question_count = load_json(question_set_path).get("question_count")
        if actual_question_count != configured_question_count:
            errors.append(
                f"initial draft question count {actual_question_count} does not match configured {configured_question_count}"
            )

    configured_catalog = config.get("candidate_catalog")
    candidate_catalog_path = BENCHMARK / configured_catalog if configured_catalog else None
    candidate_count = 0
    if candidate_catalog_path and candidate_catalog_path.is_file():
        candidates = load_jsonl(candidate_catalog_path)
        candidate_catalog_records = len(candidates)
        acquisition_closed = config.get("scale_target", {}).get("collection_stopped_by_user", False)
        candidate_count = 0 if acquisition_closed else candidate_catalog_records
        candidate_ids = []
        for index, candidate in enumerate(candidates, start=1):
            require_keys(
                candidate,
                [
                    "candidate_id",
                    "title",
                    "source",
                    "domain",
                    "study_type",
                    "intervention_type",
                    "design_tags",
                    "endpoint_types",
                    "protocol_url",
                    "sap_url",
                    "status",
                    "priority",
                    "reason",
                    "blockers",
                    "screening_level",
                ],
                f"candidate[{index}]",
                errors,
            )
            candidate_ids.append(candidate.get("candidate_id"))
            if not re.fullmatch(r"NCT\d{8}", candidate.get("candidate_id", "")):
                errors.append(f"candidate[{index}]: candidate_id must be an NCT identifier")
            if candidate.get("protocol_url") == candidate.get("sap_url"):
                errors.append(f"candidate[{index}]: protocol_url and sap_url must be separate files")
            if "Prot_SAP" in candidate.get("protocol_url", "") or "Prot_SAP" in candidate.get("sap_url", ""):
                errors.append(f"candidate[{index}]: combined protocol/SAP upload is not eligible")
        duplicate_candidates = sorted(
            {value for value in candidate_ids if value and candidate_ids.count(value) > 1}
        )
        if duplicate_candidates:
            errors.append(f"duplicate candidate_id: {duplicate_candidates}")
        registered_nct_ids = {
            match.group(0)
            for study in studies
            for match in [re.search(r"NCT\d{8}", study.get("study_family_id", ""))]
            if match
        }
        overlaps = sorted(set(candidate_ids) & registered_nct_ids)
        if overlaps:
            errors.append(f"candidate catalog overlaps registered studies: {overlaps}")
        held_nct_ids = {
            item.get("candidate_id")
            for item in load_jsonl(BENCHMARK / "manifests" / "exclusions.jsonl")
            if item.get("status", "").startswith("hold_")
        }
        held_candidates = sorted(set(candidate_ids) & held_nct_ids)
        if held_candidates:
            errors.append(f"candidate catalog contains held studies: {held_candidates}")
        non_screened = sorted(
            candidate.get("candidate_id", "")
            for candidate in candidates
            if not candidate.get("status", "").startswith("screened_")
        )
        if non_screened:
            errors.append(f"candidate catalog contains non-screened statuses: {non_screened}")
        expected_candidates = config.get("scale_target", {}).get("screened_candidates")
        if expected_candidates is not None and candidate_count != expected_candidates:
            errors.append(
                f"candidate count {candidate_count} does not match configured target {expected_candidates}"
            )
    elif config.get("scale_target", {}).get("screened_candidates") not in {None, 0}:
        errors.append("configured screened candidate count is nonzero but no active candidate catalog exists")

    review_queue_path = BENCHMARK / config.get("review_queue", "screening/review_queue_v0.3.json")
    if review_queue_path.is_file():
        review_queue = load_json(review_queue_path)
        if review_queue.get("target_count") != len(review_queue.get("studies", [])):
            errors.append("review queue target_count does not match studies length")
        if config.get("scale_target", {}).get("collection_stopped_by_user") and review_queue.get("studies"):
            errors.append("collection is closed but the review queue is not empty")

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
                "screening_candidates": candidate_count,
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
