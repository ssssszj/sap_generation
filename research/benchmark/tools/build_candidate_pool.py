#!/usr/bin/env python3
"""Build a stratified SAP benchmark candidate pool from ClinicalTrials.gov.

This script performs metadata screening only. It requires separate uploaded protocol
and SAP files, excludes already registered study families, and never marks a pair as
version verified. Promotion still requires document download, hash freezing, internal
version-chain review, extraction QA, and a second reviewer.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import re
import urllib.parse
import urllib.request


ROOT = Path(__file__).resolve().parents[3]
BENCHMARK = ROOT / "research" / "benchmark"
API = "https://clinicaltrials.gov/api/v2/studies"
VERSION_API = "https://clinicaltrials.gov/api/v2/version"
QUERY = (
    "AREA[LargeDocHasProtocol]true AND AREA[LargeDocHasSAP]true "
    "AND AREA[StudyType]INTERVENTIONAL"
)
FIELDS = ",".join(
    [
        "NCTId",
        "BriefTitle",
        "OverallStatus",
        "Phase",
        "Condition",
        "InterventionType",
        "DesignAllocation",
        "DesignInterventionModel",
        "DesignMasking",
        "EnrollmentCount",
        "PrimaryOutcomeMeasure",
        "LargeDoc",
        "HasResults",
    ]
)


DOMAIN_RULES = [
    ("oncology", r"cancer|carcinoma|tumou?r|neoplasm|lymphoma|leukemia|myeloma|melanoma|metast"),
    ("cardiovascular", r"cardi|heart|coronary|hypertension|stroke|vascular|atrial|myocard"),
    ("respiratory", r"asthma|copd|pulmonary|lung disease|respiratory|bronch"),
    ("neurology", r"alzheimer|parkinson|epilep|multiple sclerosis|neuropath|neurolog|migraine|dementia"),
    ("psychiatry", r"depress|anxiety|schizoph|bipolar|mental|stress|ptsd|autism|insomnia"),
    ("infectious_disease", r"covid|influenza|infection|hiv|tuberculosis|malaria|hepatitis|vaccine"),
    ("endocrine_metabolic", r"diabet|obesity|metabolic|thyroid|lipid|hypergly|osteopor"),
    ("gastroenterology_hepatology", r"colitis|crohn|bowel|gastro|liver|cirrhos|intestinal|pancrea"),
    ("renal_urology", r"kidney|renal|dialysis|urolog|urinary|prostate|bladder"),
    ("musculoskeletal_pain", r"arthritis|pain|musculoskeletal|osteoarth|back|sciatica|fracture|fibromyalgia"),
    ("immunology_rheumatology", r"lupus|rheumat|autoimmune|psoria|atopic|allerg"),
    ("dermatology", r"skin|dermat|acne|alopecia|wound|scar"),
    ("ophthalmology", r"eye|ocular|retina|glaucoma|cataract|macular|vision"),
    ("reproductive_maternal", r"pregnan|maternal|fertil|contracep|endometri|ovarian|postpartum"),
    ("hematology", r"anemia|haem|hemat|sickle|hemoph|thromb|coagula"),
    ("perioperative_critical_care", r"surg|perioper|anesth|intensive care|critical care|sepsis"),
]

MANUAL_DOMAIN_OVERRIDES = {
    "NCT05133739": "dermatology",
    "NCT04270682": "endocrine_metabolic",
    "NCT04172441": "endocrine_metabolic",
    "NCT02407054": "oncology",
    "NCT02796677": "respiratory",
    "NCT03347929": "musculoskeletal_pain",
    "NCT03104400": "immunology_rheumatology",
}


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def fetch_json(url: str, params: dict[str, str] | None = None) -> dict:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "sap-generation-benchmark/0.3"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def collect(max_pages: int) -> tuple[list[dict], dict]:
    studies: list[dict] = []
    token = None
    total_count = None
    for _ in range(max_pages):
        params = {
            "query.term": QUERY,
            "format": "json",
            "pageSize": "1000",
            "countTotal": "true",
            "fields": FIELDS,
        }
        if token:
            params["pageToken"] = token
        payload = fetch_json(API, params)
        studies.extend(payload.get("studies", []))
        total_count = payload.get("totalCount", total_count)
        token = payload.get("nextPageToken")
        if not token:
            break
    return studies, {"query_total": total_count, "pages_fetched": min(max_pages, (len(studies) + 999) // 1000)}


def doc_url(nct_id: str, filename: str) -> str:
    return f"https://cdn.clinicaltrials.gov/large-docs/{nct_id[-2:]}/{nct_id}/{filename}"


def parse_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def choose_pair(protocols: list[dict], saps: list[dict]) -> tuple[dict, dict, str]:
    ranked = []
    for protocol in protocols:
        for sap in saps:
            protocol_date = parse_date(protocol.get("date"))
            sap_date = parse_date(sap.get("date"))
            if protocol_date and sap_date:
                delta = (sap_date - protocol_date).days
                if delta == 0:
                    rank = (0, 0)
                    state = "exact_document_date_match"
                elif 0 < delta <= 1095:
                    rank = (1, delta)
                    state = "plausible_date_order"
                else:
                    rank = (2, abs(delta))
                    state = "needs_version_review"
            else:
                rank = (3, 999999)
                state = "missing_document_date"
            ranked.append((rank, protocol, sap, state))
    _, protocol, sap, state = min(ranked, key=lambda item: item[0])
    return protocol, sap, state


def domain_for(text: str) -> str:
    lowered = text.lower()
    for domain, pattern in DOMAIN_RULES:
        if re.search(pattern, lowered):
            return domain
    return "other_clinical"


def endpoint_types(measures: list[str]) -> list[str]:
    text = " ".join(measures).lower()
    labels = []
    if re.search(r"survival|time to|progression.free|hazard|event.free|mortality", text):
        labels.append("time_to_event")
    if re.search(r"proportion|percentage|incidence|response rate|remission|responder|occurrence|yes/no", text):
        labels.append("binary")
    if re.search(r"count|number of|frequency|rate per", text):
        labels.append("count_or_rate")
    if re.search(r"change from baseline|score|level|concentration|weight|pressure|volume|distance", text):
        labels.append("continuous")
    return labels or ["other_or_manual_review"]


def intervention_type(values: list[str]) -> str:
    normalized = {value.lower() for value in values}
    if len(normalized) > 1:
        return "mixed"
    value = next(iter(normalized), "other")
    if value in {"drug", "device", "behavioral", "procedure"}:
        return value
    return "other"


def to_candidate(study: dict) -> dict | None:
    protocol = study.get("protocolSection", {})
    identification = protocol.get("identificationModule", {})
    design = protocol.get("designModule", {})
    design_info = design.get("designInfo", {})
    status = protocol.get("statusModule", {})
    conditions = protocol.get("conditionsModule", {}).get("conditions", [])
    interventions = protocol.get("armsInterventionsModule", {}).get("interventions", [])
    measures = [item.get("measure", "") for item in protocol.get("outcomesModule", {}).get("primaryOutcomes", [])]
    documents = study.get("documentSection", {}).get("largeDocumentModule", {}).get("largeDocs", [])
    protocols = [item for item in documents if item.get("hasProtocol") and not item.get("hasSap")]
    saps = [item for item in documents if item.get("hasSap") and not item.get("hasProtocol")]
    if not protocols or not saps:
        return None
    nct_id = identification.get("nctId")
    if not nct_id or not measures:
        return None
    chosen_protocol, chosen_sap, pairing_state = choose_pair(protocols, saps)
    title = identification.get("briefTitle", nct_id)
    condition_text = " ".join(conditions + [title])
    tags = [
        value.lower()
        for value in [
            design_info.get("allocation"),
            design_info.get("interventionModel"),
            design_info.get("maskingInfo", {}).get("masking"),
        ]
        if value
    ]
    tags.extend(value.lower().replace("phase", "phase_") for value in design.get("phases", []))
    primary_text = " ".join(measures).lower()
    if "non-infer" in primary_text or "noninfer" in primary_text or "non-infer" in title.lower():
        hypothesis = ["non_inferiority"]
    elif "equivalen" in primary_text or "equivalen" in title.lower():
        hypothesis = ["equivalence"]
    else:
        hypothesis = ["superiority_or_manual_review"]
    return {
        "candidate_id": nct_id,
        "title": title,
        "source": "ClinicalTrials.gov",
        "study_type": design.get("studyType", "INTERVENTIONAL").lower(),
        "domain": domain_for(condition_text),
        "conditions": conditions,
        "intervention_type": intervention_type([item.get("type", "OTHER") for item in interventions]),
        "design_tags": tags,
        "hypothesis_types": hypothesis,
        "endpoint_types": endpoint_types(measures),
        "primary_outcomes": measures,
        "enrollment": design.get("enrollmentInfo", {}).get("count"),
        "overall_status": status.get("overallStatus", "UNKNOWN").lower(),
        "has_results": bool(study.get("hasResults")),
        "protocol_url": doc_url(nct_id, chosen_protocol["filename"]),
        "protocol_document_date": chosen_protocol.get("date"),
        "sap_url": doc_url(nct_id, chosen_sap["filename"]),
        "sap_document_date": chosen_sap.get("date"),
        "crf_url": None,
        "pairing_state": pairing_state,
        "protocol_document_count": len(protocols),
        "sap_document_count": len(saps),
        "status": "screened_metadata",
        "priority": 2,
        "reason": "Separate protocol and SAP uploads; selected for stratified benchmark coverage from official registry metadata.",
        "blockers": [
            "Download files and freeze SHA-256 hashes",
            "Confirm the SAP-internal protocol identifier, amendment, version, and date",
            "Check text/table extraction quality and redistribution constraints",
            "Independent second reviewer required before split assignment",
        ],
        "screening_level": "metadata_only",
    }


def round_robin_select(records: list[dict], target: int, excluded: set[str]) -> list[dict]:
    eligible = [record for record in records if record["candidate_id"] not in excluded]
    eligible.sort(
        key=lambda record: (
            record["pairing_state"] != "exact_document_date_match",
            not record["has_results"],
            record["pairing_state"] != "plausible_date_order",
            record["candidate_id"],
        )
    )
    buckets: dict[str, list[dict]] = defaultdict(list)
    for record in eligible:
        buckets[record["domain"]].append(record)
    selected = []
    domains = sorted(buckets)
    while len(selected) < target and any(buckets.values()):
        for domain in domains:
            if buckets[domain] and len(selected) < target:
                selected.append(buckets[domain].pop(0))
    return selected


def build_review_queue(records: list[dict], target: int = 24) -> list[dict]:
    eligible = [record for record in records if not record.get("status", "").startswith("hold_")]
    eligible.sort(
        key=lambda record: (
            record.get("priority", 9),
            record.get("pairing_state") != "exact_document_date_match",
            not record.get("has_results", False),
            record.get("endpoint_types") == ["other_or_manual_review"],
            "randomized" not in record.get("design_tags", []),
            record["candidate_id"],
        )
    )
    buckets: dict[str, list[dict]] = defaultdict(list)
    for record in eligible:
        buckets[record.get("domain", "other_clinical")].append(record)
    chosen = []
    domains = sorted(buckets, key=lambda domain: (domain == "other_clinical", domain))
    while len(chosen) < target and any(buckets.values()):
        for domain in domains:
            if buckets[domain] and len(chosen) < target:
                chosen.append(buckets[domain].pop(0))
    return [
        {
            "queue_rank": index,
            "candidate_id": record["candidate_id"],
            "domain": record.get("domain"),
            "title": record["title"],
            "pairing_state": record.get("pairing_state"),
            "design_tags": record.get("design_tags", []),
            "endpoint_types": record.get("endpoint_types", []),
            "protocol_url": record.get("protocol_url"),
            "sap_url": record.get("sap_url"),
            "next_action": "Download, hash, extract title pages, and verify the SAP-internal protocol version citation.",
        }
        for index, record in enumerate(chosen, start=1)
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=int, default=116, help="Number of screened study candidates")
    parser.add_argument("--max-pages", type=int, default=6, help="Maximum 1000-record API pages")
    parser.add_argument(
        "--output",
        type=Path,
        default=BENCHMARK / "screening" / "candidate_catalog.jsonl",
    )
    parser.add_argument(
        "--summary",
        type=Path,
        default=BENCHMARK / "screening" / "candidate_pool_summary.json",
    )
    parser.add_argument(
        "--queue",
        type=Path,
        default=BENCHMARK / "screening" / "review_queue_v0.3.json",
    )
    args = parser.parse_args()

    registered = load_jsonl(BENCHMARK / "manifests" / "studies.jsonl")
    registered_nct = {
        match.group(0)
        for item in registered
        for match in [re.search(r"NCT\d{8}", item.get("study_family_id", ""))]
        if match
    }
    screening_decisions = load_jsonl(BENCHMARK / "manifests" / "exclusions.jsonl")
    excluded_nct = {
        item["candidate_id"]
        for item in screening_decisions
        if re.fullmatch(r"NCT\d{8}", item.get("candidate_id", ""))
        and item.get("status", "").startswith("excluded_")
    }
    holds_by_id = {
        item["candidate_id"]: item
        for item in screening_decisions
        if re.fullmatch(r"NCT\d{8}", item.get("candidate_id", ""))
        and item.get("status", "").startswith("hold_")
    }
    # Holds are decisions, not active acquisition candidates. Keeping them in the
    # target-sized catalog would make the nominal 120-family intake include
    # records that cannot be promoted and would leave fewer than 120 actionable
    # study families. Preserve them in exclusions.jsonl and replenish the catalog.
    existing = [
        item
        for item in load_jsonl(args.output)
        if re.fullmatch(r"NCT\d{8}", item.get("candidate_id", ""))
        and item["candidate_id"] not in excluded_nct
        and item["candidate_id"] not in holds_by_id
    ]
    existing_by_id = {item["candidate_id"]: item for item in existing if item["candidate_id"] not in registered_nct}

    raw_studies, api_stats = collect(args.max_pages)
    converted = [record for study in raw_studies if (record := to_candidate(study))]
    converted_by_id = {item["candidate_id"]: item for item in converted}
    # Enrich manually curated legacy rows with the normalized metadata fields while
    # retaining their human-written priority, status, reason, and blockers.
    for candidate_id, existing_record in list(existing_by_id.items()):
        if candidate_id in converted_by_id:
            enriched = converted_by_id[candidate_id].copy()
            enriched.update(existing_record)
            existing_by_id[candidate_id] = enriched
        else:
            existing_record.setdefault(
                "domain",
                domain_for(" ".join(existing_record.get("conditions", [])) + " " + existing_record.get("title", "")),
            )
            existing_record.setdefault("has_results", False)
            existing_record.setdefault("pairing_state", "legacy_manual_screen")
            existing_record.setdefault("screening_level", "manual_web_screen")
        if candidate_id in MANUAL_DOMAIN_OVERRIDES:
            existing_by_id[candidate_id]["domain"] = MANUAL_DOMAIN_OVERRIDES[candidate_id]
    needed = max(0, args.target - len(existing_by_id))
    discovered = round_robin_select(
        converted,
        needed,
        set(existing_by_id) | registered_nct | excluded_nct | set(holds_by_id),
    )
    final = list(existing_by_id.values()) + discovered
    final = final[: args.target]
    if len(final) < args.target:
        raise RuntimeError(f"Only {len(final)} eligible candidates found; target was {args.target}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "".join(json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n" for item in final),
        encoding="utf-8",
    )
    version = fetch_json(VERSION_API)
    summary = {
        "generated_on": date.today().isoformat(),
        "source": "ClinicalTrials.gov API v2",
        "api_data_timestamp": version.get("dataTimestamp"),
        "query": QUERY,
        "query_total": api_stats["query_total"],
        "pages_fetched": api_stats["pages_fetched"],
        "records_screened": len(raw_studies),
        "eligible_separate_protocol_sap_pairs": len(converted),
        "registered_studies_including_pilot": len(registered),
        "registered_release_eligible": sum(item.get("status") != "pilot_only" for item in registered),
        "screened_candidates": len(final),
        "total_release_eligible": sum(item.get("status") != "pilot_only" for item in registered) + len(final),
        "total_including_pilot": len(registered) + len(final),
        "domain_distribution": dict(sorted(Counter(item["domain"] for item in final).items())),
        "intervention_distribution": dict(
            sorted(Counter(item["intervention_type"] for item in final).items())
        ),
        "endpoint_distribution_multi_label": dict(
            sorted(Counter(label for item in final for label in item["endpoint_types"]).items())
        ),
        "pairing_state_distribution": dict(
            sorted(Counter(item.get("pairing_state", "legacy_manual_screen") for item in final).items())
        ),
        "warning": (
            "This is a metadata-screened candidate pool, not a frozen benchmark. No candidate is "
            "version verified until its SAP-internal protocol citation has been checked. Excluded "
            "and held studies are decision records outside this actionable pool."
        ),
    }
    args.summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    queue = {
        "version": "0.3-development",
        "purpose": "First document-level promotion sprint; rank is operational, not benchmark difficulty.",
        "target_count": 24,
        "studies": build_review_queue(final),
    }
    args.queue.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
