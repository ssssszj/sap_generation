#!/usr/bin/env python3
"""Build and validate the v0.3 initial per-question disposition audit.

This intentionally does not infer prospective governance from ``status=verified``.
The release decisions below are the conservative result of the final chronology and
provenance review.  Re-running the tool materializes the audit deterministically from
the checked-in manifests, annotations, and the frozen registry chronology snapshot.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[3]
BENCHMARK = ROOT / "research" / "benchmark"
DEFAULT_REGISTRY_SNAPSHOT = BENCHMARK / "final_audit" / "registry_chronology.jsonl"
DEFAULT_OUTPUT = BENCHMARK / "final_audit" / "questions.jsonl"
DEFAULT_QUESTION_SET = BENCHMARK / "final_audit" / "initial_draft_question_set.json"
AUDIT_DATE = "2026-10-02"


# A dated target after primary completion is not accepted without public evidence
# that the selected target version was frozen prospectively.  These selected targets
# do not clear that bar.  The explanatory text is part of the permanent audit trail.
EXCLUDE_REASONS = {
    "PUBLIC-VIVID-001": "SAP v1 is dated 2020-04-03 after actual primary completion 2020-01-28 and documents an execution-informed change from two primary comparisons to one before data lock/unblinding.",
    "PUBLIC-IMPACT-001": "TSAP v1 is dated 2024-09-03, years after the registry's estimated 2021 primary/completion dates, and changes the primary analysis from ANCOVA to a linear mixed-effects model; actual completion is unavailable, so prospective governance cannot be established.",
    "PUBLIC-ASCENDD-001": "Selected SAP Amendment 3 is dated 2021-03-03 after actual primary/study completion 2020-11-09; no public pre-primary freeze of the selected target was established.",
    "PUBLIC-DASI-CHI-001": "Selected SAP Final 3.0 is dated 2022-04-08 after actual primary completion 2022-02-17 and completion 2022-03-07.",
    "PUBLIC-BP-SMOKERS-001": "Selected protocol and Data Analytic Plan were approved 2021-09-20, roughly ten years after actual primary/study completion in 2011-06; no earlier frozen target version is available.",
    "PUBLIC-NOTE-ENDO-001": "Selected protocol print and SAP are dated 2019-06-11 after actual primary/study completion in 2018-09; no earlier frozen target version is available.",
    "PUBLIC-RESTORE-CTX-001": "Selected SAP v2.0 is dated 2023-07-17, four days after actual primary completion 2023-07-13; day-level ordering is known and no pre-primary freeze of the selected version was established.",
    "PUBLIC-BRAIN-WELLNESS-001": "Selected SAP is dated 2019-04-05 after actual primary completion 2018-04-10 and completion 2018-06-30.",
    "PUBLIC-INFLUENZA-TRANSCRIPTOMICS-001": "Selected SAP is dated 2019-05-19 after actual primary/study completion 2019-01-02.",
    "PUBLIC-ENGENSIS-DFU-001": "Selected SAP Version E is dated 2020-02-04 after actual primary/study completion 2019-09-24 and records realized protocol-version enrollment plus conduct-driven population/endpoint decisions.",
    "PUBLIC-VM202-PDN-001": "Selected SAP Version E is dated 2019-09-05 after actual primary/study completion in 2019-04 and records realized protocol-version enrollment plus seven erroneous randomizations in a July 2019 note-to-file.",
    "PUBLIC-TWICE-WEEKLY-HD-001": "Selected Data Analysis Plans are dated 2025-04-30 after actual primary completion 2024-09-01; no earlier frozen target version was established.",
    "PUBLIC-SARECYCLINE-ACNE-001": "Selected SAP Amendment 1 is dated 2017-03-03 after actual primary/study completion 2017-02-01.",
    "PUBLIC-NI071-RA-001": "The reference PDF is a CSR wrapper containing SAP v5 dated 2019-06-27, after actual primary/study completion 2019-05-20.",
    "PUBLIC-BERTILIMUMAB-UC-001": "Selected SAP v1 is dated 2019-01-15 after actual primary completion 2018-08-31 and completion 2018-11-14.",
    "PUBLIC-ULTIMATE-II-MS-001": "Selected SAP v3 is dated 2020-09-04 after actual primary completion 2020-08-04; a statement that revision preceded database lock does not establish the benchmark's stricter pre-primary target freeze.",
    "PUBLIC-T1D-NNC0114-001": "Selected SAP v1 is dated 2018-09-19 after actual primary completion 2018-08-31.",
    "PUBLIC-EINSTEIN-JUNIOR-001": "Selected SAP v3 is dated 2019-05-03 after actual primary/study completion 2019-01-30; an earlier v1 existed, but the selected target contains later revisions and was not frozen pre-primary as a whole.",
    "PUBLIC-SELEPRESSIN-SEPSIS-001": "Selected final SAP v9 is dated 2017-11-20 after actual primary completion 2017-10-03; the earlier version chain does not prove that the selected final target was frozen before primary completion.",
    "PUBLIC-PREPOPIK-PED-001": "Selected SAP v2 is dated 2017-02-16, one day after actual primary completion 2017-02-15; exact dates preclude assuming the reverse order.",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def nct_for(study: dict) -> str:
    match = re.search(r"NCT\d{8}", study["study_family_id"])
    if not match:
        raise ValueError(f"{study['study_id']}: no NCT ID in study_family_id")
    return match.group(0)


def snapshot_registry(source_dir: Path, output: Path, studies: list[dict]) -> None:
    records = []
    for study in studies:
        if study["status"] == "pilot_only":
            continue
        nct = nct_for(study)
        source = source_dir / f"{nct}.json"
        if not source.is_file():
            raise FileNotFoundError(f"{study['study_id']}: missing registry response {source}")
        raw = load_json(source)
        status = raw["protocolSection"]["statusModule"]
        records.append({
            "snapshot_date": AUDIT_DATE,
            "nct_id": nct,
            "study_start": status.get("startDateStruct"),
            "primary_completion": status.get("primaryCompletionDateStruct"),
            "study_completion": status.get("completionDateStruct"),
        })
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "".join(json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n" for item in records),
        encoding="utf-8",
    )


def audit(registry_snapshot: Path) -> list[dict]:
    studies = load_jsonl(BENCHMARK / "manifests" / "studies.jsonl")
    documents = load_jsonl(BENCHMARK / "manifests" / "documents.jsonl")
    documents_by_id = {item["document_id"]: item for item in documents}
    registry_by_nct = {item["nct_id"]: item for item in load_jsonl(registry_snapshot)}
    rows = []

    public = [item for item in studies if item["status"] != "pilot_only"]
    for study in public:
        study_id = study["study_id"]
        nct = nct_for(study)
        if nct not in registry_by_nct:
            raise ValueError(f"{study_id}: no chronology row for {nct}")
        status = registry_by_nct[nct]
        protocol_documents = [
            documents_by_id[document_id]
            for document_id in study["document_ids"]
            if documents_by_id[document_id]["role"] in {"protocol", "crf", "annotated_crf"}
        ]
        reference = documents_by_id[study["reference_sap_document_id"]]
        annotation_path = BENCHMARK / "gold" / study_id / "annotation_status.json"
        requirements_path = BENCHMARK / "gold" / study_id / "requirements.jsonl"
        annotation = load_json(annotation_path)
        requirements = load_jsonl(requirements_path)
        open_questions = annotation.get("open_version_questions", [])

        if study_id in EXCLUDE_REASONS:
            disposition = "exclude_post_primary_or_execution_informed"
            reason = EXCLUDE_REASONS[study_id]
            chronology_gate = "fail"
            version_gate = "fail"
        elif open_questions:
            disposition = "hold_version_or_provenance"
            reason = " || ".join(open_questions)
            chronology_gate = "not_failed"
            version_gate = "hold"
        else:
            disposition = "keep_draft"
            reason = "No unresolved version/provenance question or post-primary selected-target failure was identified in the final review; retain only as an expert-review draft."
            chronology_gate = "pass_at_draft_gate"
            version_gate = "pass_at_draft_gate"

        local_documents = all((ROOT / item["path"]).is_file() for item in protocol_documents + [reference])
        reference_isolated = ("/reference/" in reference["path"].replace("\\", "/"))
        inputs_isolated = all("/input/" in item["path"].replace("\\", "/") for item in protocol_documents)
        evidence_document_ids = {evidence["document_id"] for item in requirements for evidence in item.get("evidence", [])}
        allowed_document_ids = set(study["document_ids"])

        rows.append({
            "study_id": study_id,
            "study_family_id": study["study_family_id"],
            "nct_id": nct,
            "disposition": disposition,
            "reason": reason,
            "protocol_document_ids": [item["document_id"] for item in protocol_documents],
            "reference_sap_document_id": reference["document_id"],
            "reference_sap_date": reference.get("date"),
            "registry_primary_completion": status.get("primary_completion"),
            "registry_completion": status.get("study_completion"),
            "requirement_count": len(requirements),
            "annotation_status": annotation.get("status"),
            "open_version_questions": open_questions,
            "gates": {
                "C04_documents_and_hashes": "pass" if local_documents and all(item.get("sha256") for item in protocol_documents + [reference]) else "fail",
                "C05_reference_isolation": "pass" if reference_isolated and inputs_isolated else "fail",
                "C06_prospective_version_chain": version_gate,
                "C07_independent_family": "pass_manifest_level",
                "C08_protocol_leakage": "pass_final_review",
                "C09_reference_chronology_and_type": chronology_gate,
                "C10_requirements_present": "pass" if 12 <= len(requirements) <= 25 else "fail",
                "C11_physical_page_locators": "pass_range_check_only",
                "C12_prospective_sample_size": "pass_final_review",
                "C13_annotation_status": "pass" if annotation.get("status") == "draft_needs_expert_review" and annotation.get("requirement_count") == len(requirements) else "fail",
                "C16_package_integrity": "pass" if evidence_document_ids <= allowed_document_ids else "fail",
            },
        })

    if len(rows) != 107:
        raise ValueError(f"expected 107 public audit rows, found {len(rows)}")
    if set(EXCLUDE_REASONS) - {row["study_id"] for row in rows}:
        raise ValueError("exclude decision contains unknown study ID")
    return rows


def validate(rows: list[dict]) -> list[str]:
    errors = []
    counts = Counter(row["disposition"] for row in rows)
    expected = {
        "keep_draft": 66,
        "hold_version_or_provenance": 21,
        "exclude_post_primary_or_execution_informed": 20,
    }
    if dict(counts) != expected:
        errors.append(f"disposition counts {dict(counts)} != {expected}")
    ids = [row["study_id"] for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("duplicate study_id in final audit")
    for row in rows:
        for gate, result in row["gates"].items():
            if result == "fail" and row["disposition"] == "keep_draft":
                errors.append(f"{row['study_id']}: retained despite failing {gate}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry-snapshot", type=Path, default=DEFAULT_REGISTRY_SNAPSHOT)
    parser.add_argument("--refresh-registry-from", type=Path, help="directory containing frozen full NCT JSON responses")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--question-set", type=Path, default=DEFAULT_QUESTION_SET)
    parser.add_argument("--check", action="store_true", help="verify the checked-in audit without rewriting it")
    args = parser.parse_args()

    studies = load_jsonl(BENCHMARK / "manifests" / "studies.jsonl")
    if args.refresh_registry_from:
        snapshot_registry(args.refresh_registry_from, args.registry_snapshot, studies)
    rows = audit(args.registry_snapshot)
    errors = validate(rows)
    rendered = "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows)
    selected_ids = [row["study_id"] for row in rows if row["disposition"] == "keep_draft"]
    question_set = {
        "benchmark_version": "0.3-initial-draft",
        "created_on": AUDIT_DATE,
        "status": "draft_needs_expert_review",
        "selection_rule": "keep_draft rows from final_audit/questions.jsonl",
        "question_count": len(selected_ids),
        "study_ids": selected_ids,
        "questions": [
            {
                "study_id": row["study_id"],
                "study_family_id": row["study_family_id"],
                "track": "protocol_only",
                "input_document_ids": row["protocol_document_ids"],
                "requirements_path": f"gold/{row['study_id']}/requirements.jsonl",
                "annotation_status_path": f"gold/{row['study_id']}/annotation_status.json",
                "reference_sap_document_id": row["reference_sap_document_id"],
            }
            for row in rows
            if row["disposition"] == "keep_draft"
        ],
        "reference_sap_policy": "annotation_only_never_model_visible",
        "not_included": {
            "hold_version_or_provenance": 21,
            "exclude_post_primary_or_execution_informed": 20,
            "private_pilot": 1,
        },
    }
    rendered_question_set = json.dumps(question_set, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if not args.output.is_file():
            errors.append(f"missing output {args.output}")
        elif args.output.read_text(encoding="utf-8") != rendered:
            errors.append(f"{args.output} is stale; rerun without --check")
        if not args.question_set.is_file():
            errors.append(f"missing question set {args.question_set}")
        elif args.question_set.read_text(encoding="utf-8") != rendered_question_set:
            errors.append(f"{args.question_set} is stale; rerun without --check")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        args.question_set.write_text(rendered_question_set, encoding="utf-8")

    summary = {
        "audited_on": AUDIT_DATE,
        "public_rows": len(rows),
        "dispositions": dict(Counter(row["disposition"] for row in rows)),
        "errors": errors,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
