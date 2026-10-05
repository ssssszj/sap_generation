#!/usr/bin/env python3
"""Independent completion audit for the initial benchmark delivery.

This is intentionally separate from the ordinary structural validator.  It checks
the prompt-to-artifact chain for all 141 audited public drafts and verifies PDF
evidence page bounds against the locally frozen source files.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re
import sys

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[3]
BENCHMARK = ROOT / "research" / "benchmark"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def locator_pages(locator: str) -> list[int]:
    # Evidence locators use one-based physical/PDF/page wording.  Paragraph,
    # section, table and appendix numbers are deliberately ignored here.
    if not re.search(r"(?i)\b(?:physical\s+pdf\s+pages?|pdf\s+pages?|pages?)\b", locator):
        return []
    pages = []
    for chunk in re.findall(r"(?i)(?:physical\s+pdf\s+pages?|pdf\s+pages?|pages?)\s+([^;]+)", locator):
        chunk = re.split(r"(?i)\b(?:section|table|appendix|paragraph|figure|row)\b", chunk)[0]
        for start, end in re.findall(r"(\d+)(?:\s*[-–]\s*(\d+))?", chunk):
            first = int(start)
            last = int(end) if end else first
            if last >= first and last - first <= 500:
                pages.extend(range(first, last + 1))
    return pages


def main() -> int:
    errors = []
    studies = load_jsonl(BENCHMARK / "manifests" / "studies.jsonl")
    documents = load_jsonl(BENCHMARK / "manifests" / "documents.jsonl")
    audit_rows = load_jsonl(BENCHMARK / "final_audit" / "questions.jsonl")
    question_set = load_json(BENCHMARK / "final_audit" / "initial_draft_question_set.json")
    documents_by_id = {item["document_id"]: item for item in documents}
    studies_by_id = {item["study_id"]: item for item in studies}
    public_ids = {item["study_id"] for item in studies if item["status"] != "pilot_only"}

    if len(audit_rows) != 141 or {item["study_id"] for item in audit_rows} != public_ids:
        errors.append("C01: audit does not exactly cover 141 public drafts")
    dispositions = Counter(item["disposition"] for item in audit_rows)
    expected = Counter({
        "keep_draft": 100,
        "hold_version_or_provenance": 21,
        "exclude_post_primary_or_execution_informed": 20,
    })
    if dispositions != expected:
        errors.append(f"C02/C07/C10: unexpected dispositions {dict(dispositions)}")
    if question_set.get("question_count") != 100:
        errors.append("C02: initial question set does not contain 100 studies")
    if list((BENCHMARK / "screening").glob("candidate_catalog.jsonl")):
        errors.append("C03: active candidate catalog still exists")
    queue = load_json(BENCHMARK / "screening" / "review_queue_v0.3.json")
    if queue.get("studies") or queue.get("target_count") != 0:
        errors.append("C03: actionable review queue is not empty")
    if set(question_set.get("study_ids", [])) & {"PILOT-IOL-001"}:
        errors.append("C04: private pilot appears in initial question set")

    page_counts = {}
    public_requirement_total = 0
    requirement_status_counts = Counter()
    question_requirement_total = 0
    question_ids = set(question_set.get("study_ids", []))
    for row in audit_rows:
        study_id = row["study_id"]
        study = studies_by_id[study_id]
        requirements = load_jsonl(BENCHMARK / "gold" / study_id / "requirements.jsonl")
        annotation = load_json(BENCHMARK / "gold" / study_id / "annotation_status.json")
        public_requirement_total += len(requirements)
        requirement_status_counts.update(item["status"] for item in requirements)
        if study_id in question_ids:
            question_requirement_total += len(requirements)
        if not 12 <= len(requirements) <= 25:
            errors.append(f"C11 {study_id}: requirement count {len(requirements)} outside 12-25")
        if annotation.get("status") != "draft_needs_expert_review":
            errors.append(f"C14 {study_id}: status is {annotation.get('status')}")
        if annotation.get("requirement_count") != len(requirements):
            errors.append(f"C14 {study_id}: annotation count mismatch")

        input_ids = set(row["protocol_document_ids"])
        reference_id = row["reference_sap_document_id"]
        if reference_id in input_ids:
            errors.append(f"C06 {study_id}: reference SAP appears in model-visible inputs")
        for document_id in input_ids | {reference_id}:
            document = documents_by_id.get(document_id)
            if not document or document.get("study_id") != study_id:
                errors.append(f"C05/C15 {study_id}: invalid document binding {document_id}")
                continue
            path = ROOT / document["path"]
            if not path.is_file():
                errors.append(f"C05 {study_id}: frozen source missing {path}")
            elif document.get("format") == "pdf" and document_id not in page_counts:
                page_counts[document_id] = len(PdfReader(path).pages)

        for requirement in requirements:
            if not requirement.get("evidence"):
                errors.append(f"C11 {requirement.get('requirement_id')}: no evidence")
            for evidence in requirement.get("evidence", []):
                document_id = evidence.get("document_id")
                if document_id not in set(study["document_ids"]):
                    errors.append(f"C15 {requirement.get('requirement_id')}: cross-study evidence {document_id}")
                    continue
                pages = locator_pages(evidence.get("locator", ""))
                if pages and document_id in page_counts and max(pages) > page_counts[document_id]:
                    errors.append(
                        f"C12 {requirement.get('requirement_id')}: page {max(pages)} exceeds {document_id} page count {page_counts[document_id]}"
                    )

    audited_requirement_total = sum(row.get("requirement_count", 0) for row in audit_rows)
    if public_requirement_total != audited_requirement_total:
        errors.append(
            f"C11: public requirement total {public_requirement_total} differs from audit total {audited_requirement_total}"
        )
    if set(question_set.get("study_ids", [])) != {
        item["study_id"] for item in audit_rows if item["disposition"] == "keep_draft"
    }:
        errors.append("C02: question set differs from keep_draft audit rows")

    summary = {
        "public_drafts_audited": len(audit_rows),
        "dispositions": dict(dispositions),
        "initial_question_count": question_set.get("question_count"),
        "public_requirements": public_requirement_total,
        "initial_question_requirements": question_requirement_total,
        "requirement_statuses": dict(requirement_status_counts),
        "public_pdf_page_counts_checked": len(page_counts),
        "errors": errors,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
