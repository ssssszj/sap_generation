#!/usr/bin/env python3
"""Reconcile and materialize the user-authorized 100-question expansion.

The 34 IDs below are independent public study families with a separate protocol
and SAP. The selected SAP predates actual primary completion. This script is
idempotent: it removes only earlier expansion rows and rebuilds the selected set.
"""
from __future__ import annotations

from datetime import date, datetime
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
BENCH = ROOT / "research" / "benchmark"
BASELINE_COMMIT = "85c798a"
TMP_ROOTS = [
    Path("/private/tmp/sapbench_wave1"),
    Path("/private/tmp/sapbench_prestart_docs"),
    Path("/private/tmp/sapbench_prestart_docs2"),
    Path("/private/tmp/sapbench_prestart_docs3"),
    Path("/private/tmp/sapbench_second_docs"),
]
CANDIDATES = {
    row["candidate_id"]: row
    for row in map(json.loads, Path("/private/tmp/sapbench_candidates_1000.jsonl").read_text().splitlines())
}

# Exactly 34 independently reviewed families. The expansion ends at 100 keep
# questions (66 baseline + these 34); do not add more without a new decision.
SELECTED = [
    "NCT02593825", "NCT06814470", "NCT04755660", "NCT03701113",
    "NCT03198000", "NCT05516134", "NCT03256253",
    "NCT05016960", "NCT03231228", "NCT03212144", "NCT03954626",
    "NCT03744780", "NCT03835325", "NCT03876171", "NCT03835403",
    "NCT05430854", "NCT05307523", "NCT03397277", "NCT04239612",
    "NCT03332004", "NCT04674111", "NCT04126031", "NCT03324659",
    "NCT03805412", "NCT03210402", "NCT03529981", "NCT03704116",
    "NCT05001165", "NCT02041494", "NCT04026503", "NCT03308877",
    "NCT03691428", "NCT04786184", "NCT05319977",
]

REJECTED = {
    "NCT04122261": ("excluded_combined_protocol_sap_leakage", "Model-visible protocol reproduces the non-inferiority objective and core analysis framework of the short SAP."),
    "NCT03001817": ("excluded_combined_protocol_sap_leakage", "Protocol physical pages 9-11 specify the sample size, fixed-sequence multiplicity procedure, primary ANCOVA factors, imputation and nonparametric fallback, substantially reconstructing the target analysis."),
    "NCT03421379": ("excluded_combined_protocol_sap_leakage", "Protocol statistical sections specify the completer target, non-inferiority margin, alpha, power and primary analysis, substantially reconstructing the target SAP."),
    "NCT07289490": ("hold_version_reconciliation", "The SAP says the trial was not yet registered and does not print NCT07289490; title/date agreement alone is insufficient for strict registry provenance."),
    "NCT05715476": ("excluded_wrong_document_type", "The selected protocol is a three-page data-collection/follow-up form rather than a governing prospective study protocol, and its date follows the SAP date."),
    "NCT03459131": ("excluded_combined_protocol_sap_leakage", "The model-visible protocol contains an executable analysis plan including populations, missingness and multiplicity."),
    "NCT03232983": ("hold_version_reconciliation", "The selected files internally print NCT03233983 rather than registry ID NCT03232983."),
    "NCT05814042": ("excluded_combined_protocol_sap_leakage", "The selected input is explicitly a combined Study Protocol and Statistical Analysis Plan."),
    "NCT04432974": ("excluded_combined_protocol_sap_leakage", "The protocol and SAP have high textual containment and do not provide an independent hidden target."),
    "NCT04855513": ("excluded_wrong_document_type", "The selected protocol upload is a consent form and the selected SAP upload is a research protocol, not a protocol/SAP pair."),
    "NCT05116540": ("hold_version_reconciliation", "The SAP cover identifies a different governing protocol, HBPCOVID02, so study binding is unresolved."),
    "NCT05726136": ("hold_version_reconciliation", "The registry primary-completion date is still estimated, so the target cannot pass the strict actual-primary chronology gate."),
    "NCT07676110": ("hold_version_reconciliation", "The registry primary-completion date is month-level and still estimated, so strict prospective ordering against actual primary completion is not established."),
    "NCT02676895": ("hold_version_reconciliation", "The selected SAP states that it is based on protocol version 3.0, while the available model-visible protocol is version 1.0."),
    "NCT06340854": ("excluded_combined_protocol_sap_leakage", "The protocol contains enough of the target statistical analysis framework to substantially reconstruct the separate SAP."),
    "NCT05014919": ("excluded_combined_protocol_sap_leakage", "The protocol contains enough of the target statistical analysis framework to substantially reconstruct the separate SAP."),
    "NCT02746991": ("excluded_combined_protocol_sap_leakage", "The protocol contains enough of the target statistical analysis framework to substantially reconstruct the separate SAP."),
    "NCT02890381": ("excluded_combined_protocol_sap_leakage", "The protocol already specifies the core analysis populations, endpoint analyses, and inferential framework reproduced by the SAP."),
    "NCT03387813": ("excluded_conduct_informed_sap", "The SAP added a COVID-19 sensitivity analysis after study conduct had begun, so the target is not wholly prospective."),
    "NCT03422562": ("excluded_combined_protocol_sap_leakage", "The protocol already specifies Shannon diversity, Mann-Whitney with FDR, UniFrac/NMDS, PERMANOVA, negative-binomial models, and DESeq2; the two-page SAP is substantially reconstructable."),
    "NCT03911843": ("excluded_combined_protocol_sap_leakage", "The protocol specifies Wilcoxon, Mann-Whitney, repeated measures, Pearson correlation, multiple regression, and the significance threshold."),
    "NCT05252858": ("excluded_conduct_informed_sap", "The SAP uses completed-analysis language and the available protocol is a later post-start version, so prospective status cannot be established."),
    "NCT03718039": ("excluded_combined_protocol_sap_leakage", "The protocol already contains the substantive efficacy methods and clinical-results context."),
    "NCT04483011": ("excluded_conduct_informed_sap", "The SAP states that 18 participants had already been enrolled."),
    "NCT04774328": ("excluded_conduct_informed_sap", "Unblinded interim results from Part B informed dose and expansion decisions for Part C."),
    "NCT06001879": ("excluded_conduct_informed_protocol", "The protocol contains observed control and intervention result values from ongoing conduct."),
    "NCT03500159": ("excluded_combined_protocol_sap_leakage", "The protocol already contains the substantive statistical structure, leaving little independent SAP target."),
    "NCT03064438": ("excluded_combined_protocol_sap_leakage", "The protocol contains detailed statistical methods and the SAP has no reliably extractable public text."),
    "NCT02933502": ("excluded_conduct_informed_protocol", "The protocol plans an interim analysis after five participants and already specifies the primary and safety analyses."),
    "NCT03775434": ("excluded_combined_protocol_sap_leakage", "The protocol already specifies ITT, descriptive and efficacy methods, and the missing-data rule."),
    "NCT03525808": ("excluded_combined_protocol_sap_leakage", "The protocol and SAP substantially overlap on endpoints, success thresholds, Clopper-Pearson intervals, populations, and descriptive methods."),
    "NCT04460885": ("excluded_conduct_informed_sap", "The SAP records a post-first-visit missing-data imputation change made following FDA advice."),
    "NCT07016568": ("excluded_conduct_informed_sap", "The nominally pre-start SAP uses completed-analysis language such as data were extracted and software was used."),
    "NCT03978767": ("excluded_combined_protocol_sap_leakage", "The protocol already specifies the non-inferiority margin, alpha, sample size, ITT population, and primary tests."),
}

PROVENANCE_NOTES = {
    "NCT03231228": "SAP explicitly binds to protocol HC-G-H-1601 version 2.0 and states that analyses were defined before database lock.",
    "NCT05430854": "Protocol and SAP covers explicitly bind version 1; the SAP was finalized two days after actual start, has an empty revision history, and predates primary completion by more than two years.",
    "NCT05307523": "Binding relies on the same registry submission, identical official title and date, because the contemporaneous files leave the NCT field blank.",
    "NCT03332004": "Protocol and SAP share the same date, title, investigator, and protocol identifier 736513.A287/C.E./2013 and predate actual start by almost three years.",
    "NCT03324659": "Both registry-hosted files share the study title and predate actual start; the contemporaneous files state that an NCT number was not yet available.",
    "NCT05001165": "The SAP was uploaded before actual start. Binding relies on the same date, title, PI, institution, and registry record because both files state that the NCT number was not yet assigned; the protocol was uploaded later and is not used as chronology evidence.",
}

DOMAIN_MAP = {
    "cardiovascular": "cardiovascular", "mental_and_behavioral_health": "behavioral_health",
    "neurological": "neurology", "metabolic_endocrine": "metabolic_endocrine",
    "respiratory": "respiratory", "infectious_disease": "infectious_disease",
    "oncology": "oncology", "musculoskeletal": "musculoskeletal",
}

def jsonl(path: Path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]

def dump_jsonl(path: Path, rows):
    path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows))

def baseline_jsonl(relative: str):
    text = subprocess.check_output(["git", "show", f"{BASELINE_COMMIT}:research/benchmark/{relative}"], cwd=ROOT, text=True)
    return [json.loads(line) for line in text.splitlines() if line.strip()]

def nct_of_study(study):
    match = re.search(r"NCT\d{8}", study.get("study_family_id", ""))
    return match.group(0) if match else None

def source_dir(nct):
    for root in TMP_ROOTS:
        path = root / nct
        if (path / "input" / "protocol.pdf").is_file() and (path / "reference" / "sap.pdf").is_file():
            return path
    raise FileNotFoundError(nct)

def pdf_pages(path):
    pages = [(index, (page.extract_text() or "")) for index, page in enumerate(PdfReader(path).pages, 1)]
    # A few official registry PDFs are image scans.  Earlier manual review used
    # page-aligned OCR sidecars; use those only when the embedded page is blank.
    source = path.parents[1]
    ocr_dir = source / ("ocr_protocol" if path.parent.name == "input" else "ocr_stats")
    if ocr_dir.is_dir():
        pages = [
            (page, (ocr_dir / f"page-{page:03d}.txt").read_text(errors="replace")
             if not clean(text) and (ocr_dir / f"page-{page:03d}.txt").is_file() else text)
            for page, text in pages
        ]
    return pages

def clean(text):
    return re.sub(r"\s+", " ", text).strip()

def first_hit(items, patterns, fallback=1, width=260):
    for pattern in patterns:
        rx = re.compile(pattern, re.I)
        for page, raw in items:
            text = clean(raw)
            match = rx.search(text)
            if match:
                start = max(0, match.start() - 70)
                return page, text[start:min(len(text), match.end() + width)]
    by_page = dict(items)
    text = clean(by_page.get(fallback, ""))
    if text:
        return fallback, text[:width]
    for page, raw in items:
        text = clean(raw)
        if text:
            return page, text[:width]
    return fallback, "No extractable text on the cited page; verify against the PDF image."

def hits(items, pattern, limit=6):
    rx = re.compile(pattern, re.I)
    values = []
    for page, raw in items:
        text = clean(raw)
        for match in rx.finditer(text):
            context = text[max(0, match.start()-70):min(len(text), match.end()+360)]
            toc_like = (
                "table of contents" in text.lower()
                or len(re.findall(r"\.{4,}", context)) >= 1
                or len(re.findall(r"\b\d+(?:\.\d+){1,3}\b", context)) >= 5
            )
            substantive = bool(re.search(
                r"(?i)\b(?:will|shall|defined as|includes?|consists?|using|based on|summari[sz]ed|analy[sz]ed|estimated|calculated|imputed|randomi[sz]ed)\b",
                context,
            ))
            if toc_like:
                continue
            values.append((not substantive, page, context))
    values.sort(key=lambda item: (item[0], item[1]))
    return [(page, context) for _, page, context in values[:limit]]

def parse_date(value):
    if not value or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"day-level date required, got {value!r}")
    return date.fromisoformat(value)

def evidence(document_id, item):
    page, text = item
    return [{"document_id": document_id, "locator": f"physical PDF page {page}", "text": text}]

def concise(item, limit=280):
    text = clean(item[1])
    if len(text) <= limit:
        return text
    clipped = text[:limit].rsplit(" ", 1)[0]
    return clipped + "…"

def requirement(study_id, index, rubric, severity, text, values, doc_id, hit, status="explicit", tracks=None, notes=None):
    row = {
        "requirement_id": f"{study_id}-R{index:03d}", "study_id": study_id,
        "rubric_id": rubric, "tracks": tracks or ["protocol_only", "confirmed_decisions"],
        "applies": True, "status": status, "severity": severity,
        "requirement": text, "acceptable_values": values, "evidence": evidence(doc_id, hit),
    }
    if notes:
        row["notes"] = notes
    return row

def primary_outcomes(registry):
    return registry.get("outcomesModule", {}).get("primaryOutcomes", [])

def secondary_outcomes(registry):
    return registry.get("outcomesModule", {}).get("secondaryOutcomes", [])

def make_requirements(study_id, nct, candidate, registry, ppages, spages, protocol_id, sap_id):
    design = registry.get("designModule", {})
    info = design.get("designInfo", {})
    arms = registry.get("armsInterventionsModule", {}).get("armGroups", [])
    prim = primary_outcomes(registry)
    sec = secondary_outcomes(registry)
    target_hits = hits(ppages, r"(?:target|planned|proposed|approximately|up to|aim.{0,20}recruit|sample size).{0,120}?(?:\b\d{2,5}\b|patients?|participants?|subjects?)")
    sap_population_hits = hits(spages, r"intent.to.treat|full analysis set|analysis population|efficacy population|all (?:randomized|enrolled)", 2)
    sap_population = sap_population_hits[0] if sap_population_hits else first_hit(spages, [r"statistical analysis plan|data analysis plan"] )
    sap_method_hits = hits(spages, r"primary analysis.{0,220}|mixed.effects?|generalized estimating|analysis of covariance|ANCOVA|logistic regression|fisher.?s exact|mcnemar|wilcoxon|paired.{0,15}t.test|repeated.measures.{0,30}(?:ANOVA|MANOVA)|receiver operating characteristic|sensitivity.{0,80}specificity|descriptive statistics", 3)
    sap_method = sap_method_hits[0] if sap_method_hits else first_hit(spages, [r"statistical analysis plan|data analysis plan"] )
    sap_missing_hits = hits(spages, r"missing data|missing values?|imputation|complete.case|available.case|last observation")
    sap_mult_hits = hits(spages, r"multiplicity|multiple comparisons?|family.wise|bonferroni|hierarch|fixed sequential|no (?:adjustment|correction).{0,30}multip")
    sap_alpha_hits = hits(spages, r"two.sided|one.sided|alpha.{0,25}0?\.0[125]|significance.{0,25}0?\.0[125]|95% (?:confidence|CI)")
    sap_safety_hits = hits(spages, r"adverse events?|safety (?:analysis|population|set|outcome|endpoint)|tolerability")
    sap_sensitivity_hits = hits(spages, r"sensitivity analys|supportive analys|per.protocol|completer analys")
    group_values = [a.get("label") for a in arms if a.get("label")]
    model_design = [str(x).lower() for x in [info.get("allocation"), info.get("interventionModel"), info.get("maskingInfo", {}).get("masking")] if x]
    phase = registry.get("designModule", {}).get("phases", [])
    model_design += [str(x).lower() for x in phase]
    rows = []
    def add(rubric, severity, text, values, doc, hit, status="explicit", tracks=None, notes=None):
        rows.append(requirement(study_id, len(rows)+1, rubric, severity, text, values, doc, hit, status, tracks, notes))

    add("CORE-PROV-001", "critical", f"Identify the analysis as belonging to {candidate['title']} ({nct}).", [candidate["title"], nct], protocol_id, first_hit(ppages, [re.escape(nct), re.escape(candidate["title"][:35])]))
    add("CORE-DESIGN-001", "critical", f"Preserve the study design as {', '.join(model_design) or 'an interventional study'}.", model_design or ["interventional"], protocol_id, first_hit(ppages, [r"study design|randomi[sz]ed|single.arm|parallel|crossover|open.label|double.blind"]))
    if group_values:
        add("CORE-RAND-001", "major", f"Name the planned treatment groups without inventing additional arms: {'; '.join(group_values)}.", group_values, protocol_id, first_hit(ppages, [r"treatment groups?|study arms?|randomi[sz].{0,100}(?:group|arm)|intervention group|control group"]))
    if target_hits:
        add("CORE-SAMPLE-001", "major", f"Use the prospective protocol sample-size statement and its planning assumptions: {concise(target_hits[0])}", [concise(target_hits[0]), "do not substitute registry actual enrollment"], protocol_id, target_hits[0], notes="Registry actual enrollment is conduct context only, never the prospective target.")
    elif len(rows) < 4:
        add("CORE-SAMPLE-001", "major", "State that the prospective target sample size still requires confirmation; do not substitute registry actual enrollment.", ["needs confirmation", "actual enrollment is not the target"], protocol_id, first_hit(ppages, [r"participants?|subjects?|enroll"]), "needs_confirmation")
    primary_names = [o.get("measure") for o in prim if o.get("measure")]
    primary_times = [o.get("timeFrame") for o in prim if o.get("timeFrame")]
    add("CORE-ENDPT-001", "critical", f"Define the primary outcome family as: {'; '.join(primary_names) or 'the protocol-specified primary outcome'}.", primary_names or ["protocol-specified primary outcome"], protocol_id, first_hit(ppages, [r"primary (?:endpoint|outcome|objective)"]))
    if primary_times:
        add("CORE-VISIT-001", "critical", f"Use the primary assessment timing: {'; '.join(primary_times)}.", primary_times, protocol_id, first_hit(ppages, [re.escape(primary_times[0][:35]), r"primary (?:endpoint|outcome)"]))
    secondary_names = [o.get("measure") for o in sec[:5] if o.get("measure")]
    if secondary_names:
        add("CORE-ENDPT-002", "major", f"Cover the prespecified secondary outcome family without promoting it above the primary outcome: {'; '.join(secondary_names)}.", secondary_names, protocol_id, first_hit(ppages, [r"secondary (?:endpoint|outcome|objective)"]))
    if sap_population_hits:
        add("CORE-POP-FAS-001", "critical", f"Define the main analysis population using the reference rule: {concise(sap_population)}", [concise(sap_population)], sap_id, sap_population, tracks=["confirmed_decisions"], notes="Do not infer a generic ITT/FAS rule when the cited SAP defines a different population.")
    else:
        add("CORE-POP-FAS-001", "critical", "Flag the main analysis-population inclusion and treatment-attribution rules as unresolved; do not invent an ITT, FAS, or evaluable-set definition.", ["needs confirmation", "population inclusion rule", "treatment attribution"], sap_id, sap_population, status="needs_confirmation", tracks=["protocol_only", "confirmed_decisions"])
    if sap_sensitivity_hits:
        add("CORE-POP-PPS-001", "major", f"Define the supportive or sensitivity population using the reference rule and keep it subordinate to the primary analysis: {concise(sap_sensitivity_hits[0])}", [concise(sap_sensitivity_hits[0])], sap_id, sap_sensitivity_hits[0], tracks=["confirmed_decisions"] )
    else:
        add("CORE-UNCERT-001", "major", "Flag any per-protocol or completer analysis as unresolved unless the protocol independently specifies it.", ["needs confirmation", "do not invent exclusions"], sap_id, sap_population, "needs_confirmation", ["protocol_only", "confirmed_decisions"] )
    if sap_method_hits:
        add("CORE-METHOD-001", "critical", f"Use the primary statistical method and comparison structure specified in the reference plan: {concise(sap_method)}", [concise(sap_method)], sap_id, sap_method, tracks=["confirmed_decisions"] )
    else:
        add("CORE-METHOD-001", "critical", "Flag the primary statistical model, comparison, covariates, and repeated/paired structure as unresolved rather than inventing them.", ["needs confirmation", "model", "comparison", "covariates"], sap_id, sap_method, status="needs_confirmation", tracks=["protocol_only", "confirmed_decisions"] )
    if sap_alpha_hits:
        add("CORE-ALPHA-001", "critical", f"Use the inferential sidedness, alpha, or confidence-interval rule stated here: {concise(sap_alpha_hits[0])}", [concise(sap_alpha_hits[0])], sap_id, sap_alpha_hits[0], tracks=["confirmed_decisions"] )
    else:
        add("CORE-ALPHA-001", "critical", "Expose the inferential sidedness, alpha, and confidence-interval level as decisions requiring confirmation rather than inventing values.", ["needs confirmation"], sap_id, sap_method, "needs_confirmation", ["protocol_only", "confirmed_decisions"] )
    if sap_missing_hits:
        add("CORE-MISS-001", "critical", f"Apply the reference plan's missing-data rule and assumptions: {concise(sap_missing_hits[0])}", [concise(sap_missing_hits[0])], sap_id, sap_missing_hits[0], tracks=["confirmed_decisions"] )
    else:
        add("CORE-MISS-001", "critical", "Flag primary-outcome missing-data handling as unresolved; do not silently invent an imputation rule.", ["needs confirmation", "no invented imputation"], sap_id, sap_method, "needs_confirmation", ["protocol_only", "confirmed_decisions"] )
    if sap_mult_hits:
        add("CORE-MULT-001", "critical", f"Apply the multiplicity policy or testing order stated in the reference plan: {concise(sap_mult_hits[0])}", [concise(sap_mult_hits[0])], sap_id, sap_mult_hits[0], tracks=["confirmed_decisions"] )
    else:
        add("CORE-MULT-001", "critical", "Flag multiplicity control across the outcome family as unresolved; do not claim adjustment or no adjustment without support.", ["needs confirmation", "no unsupported multiplicity claim"], sap_id, sap_method, "needs_confirmation", ["protocol_only", "confirmed_decisions"] )
    if sap_sensitivity_hits and len(rows) < 15:
        add("CORE-SENS-001", "major", f"Include the prespecified supportive or sensitivity analysis represented by this reference rule: {concise(sap_sensitivity_hits[0])}", [concise(sap_sensitivity_hits[0])], sap_id, sap_sensitivity_hits[0], tracks=["confirmed_decisions"] )
    if sap_safety_hits and len(rows) < 15:
        add("CORE-SAFE-001", "major", f"Use the safety population, periods, denominators, and categories indicated by the reference rule: {concise(sap_safety_hits[0])}", [concise(sap_safety_hits[0])], sap_id, sap_safety_hits[0], tracks=["confirmed_decisions"] )
    add("CORE-CONSIST-001", "critical", "Keep endpoint labels, treatment groups, visits, populations, and methods internally consistent across the generated SAP.", ["consistent endpoints", "consistent groups", "consistent visits", "consistent populations"], sap_id, sap_method, tracks=["confirmed_decisions"] )
    add("CORE-COVER-001", "major", "Provide traceable sections for design, endpoints, populations, primary methods, missing data, multiplicity, safety where applicable, and planned outputs.", ["design", "endpoints", "populations", "methods", "missing data", "multiplicity"], sap_id, first_hit(spages, [r"table of contents|statistical analysis plan|statistical plan|data analysis plan|analysis strategy"]), tracks=["confirmed_decisions"] )
    while len(rows) < 12:
        add("CORE-UNCERT-001", "major", "Separate protocol-supported facts from reference-only confirmed decisions and explicitly surface unresolved choices.", ["protocol-supported", "confirmed decision", "needs confirmation"], sap_id, sap_method, "needs_confirmation")
    if len(rows) > 25:
        raise ValueError(f"{nct}: too many requirements")
    return rows

def main():
    if len(SELECTED) != 34 or len(set(SELECTED)) != 34:
        raise ValueError("SELECTED must contain exactly 34 unique NCT IDs")
    studies = baseline_jsonl("manifests/studies.jsonl")
    documents = baseline_jsonl("manifests/documents.jsonl")
    registry_rows = baseline_jsonl("final_audit/registry_chronology.jsonl")
    baseline_ids = {row["study_id"] for row in studies}
    for path in (BENCH / "gold").glob("PUBLIC-*"):
        if path.name not in baseline_ids:
            shutil.rmtree(path)
    for nct in SELECTED:
        candidate = CANDIDATES[nct]
        source = source_dir(nct)
        registry = json.loads((Path("/private/tmp/sapbench_candidate_registry") / f"{nct}.json").read_text())["protocolSection"]
        status = registry["statusModule"]
        primary = status.get("primaryCompletionDateStruct", {})
        if primary.get("type") != "ACTUAL" or parse_date(candidate["sap_document_date"]) >= parse_date(primary.get("date")):
            raise ValueError(f"{nct}: SAP does not strictly predate actual primary completion")
        slug = re.sub(r"[^A-Z0-9]+", "-", candidate["title"].upper()).strip("-")[:42]
        study_id = f"PUBLIC-{slug}-{nct[-4:]}"
        protocol_id = f"doc-{nct.lower()}-protocol-{candidate['protocol_document_date']}"
        sap_id = f"doc-{nct.lower()}-reference-sap-{candidate['sap_document_date']}"
        protocol_source = source / "input" / "protocol.pdf"
        sap_source = source / "reference" / "sap.pdf"
        ppages, spages = pdf_pages(protocol_source), pdf_pages(sap_source)
        if not any(clean(text) for _, text in ppages) or not any(clean(text) for _, text in spages):
            raise ValueError(f"{nct}: protocol or SAP has no extractable text")
        info = registry.get("designModule", {}).get("designInfo", {})
        phases = registry.get("designModule", {}).get("phases", [])
        design = [x for x in [info.get("allocation"), info.get("interventionModel"), info.get("maskingInfo", {}).get("masking")] if x] + phases
        studies.append({
            "study_id": study_id, "study_family_id": f"{nct}-{slug[:28]}", "title": candidate["title"],
            "language": "en", "domain": DOMAIN_MAP.get(candidate.get("domain"), candidate.get("domain", "other")),
            "intervention_type": candidate.get("intervention_type", "other"), "design": [str(x).lower() for x in design],
            "hypothesis_types": candidate.get("hypothesis_types", []), "endpoint_types": candidate.get("endpoint_types", []),
            "document_ids": [protocol_id, sap_id], "reference_sap_document_id": sap_id,
            "split": "candidate", "status": "verified",
            "notes": f"ClinicalTrials.gov pair for {nct}; SAP {candidate['sap_document_date']} strictly predates actual primary completion {primary['date']}. {PROVENANCE_NOTES.get(nct, '')} Draft pending independent expert adjudication.".replace("  ", " "),
        })
        for role, doc_id, local, doc_date, url in [
            ("protocol", protocol_id, protocol_source, candidate["protocol_document_date"], candidate["protocol_url"]),
            ("reference_sap", sap_id, sap_source, candidate["sap_document_date"], candidate["sap_url"]),
        ]:
            relative = f"research/benchmark/sources/public/{nct}/{'input/Prot_000.pdf' if role == 'protocol' else 'reference/SAP_001.pdf'}"
            destination = ROOT / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(local, destination)
            documents.append({
                "document_id": doc_id, "study_id": study_id, "role": role, "format": "pdf", "path": relative,
                "sha256": hashlib.sha256(local.read_bytes()).hexdigest(), "version": "selected registry document", "date": doc_date,
                "version_match_status": "verified", "availability": "public", "source_url": url,
                "notes": (("Reference-only annotation aid; never model-visible. " if role == "reference_sap" else "Model-visible protocol selected from the official registry document record. ") + PROVENANCE_NOTES.get(nct, "")).strip(),
            })
        requirements = make_requirements(study_id, nct, candidate, registry, ppages, spages, protocol_id, sap_id)
        gold = BENCH / "gold" / study_id
        gold.mkdir(parents=True, exist_ok=True)
        dump_jsonl(gold / "requirements.jsonl", requirements)
        critical = [row["requirement_id"] for row in requirements if row["severity"] == "critical"]
        annotation = {
            "study_id": study_id, "annotation_version": "0.3-draft", "status": "draft_needs_expert_review",
            "annotator": "traecode_first_pass_2026-10-05", "requirement_count": len(requirements),
            "critical_items_requiring_statistician_adjudication": critical, "open_version_questions": [],
            "review_requirements": [
                "Independently verify the governing protocol/SAP identity, version binding, and chronology.",
                "Recheck every evidence quotation against the cited one-based physical PDF page.",
                "Adjudicate all reference-only and needs-confirmation decisions before freezing.",
            ] + ([PROVENANCE_NOTES[nct]] if nct in PROVENANCE_NOTES else []),
        }
        (gold / "annotation_status.json").write_text(json.dumps(annotation, ensure_ascii=False, separators=(",", ":")) + "\n")
        registry_rows.append({"snapshot_date": "2026-10-05", "nct_id": nct, "study_start": status.get("startDateStruct"), "primary_completion": primary, "study_completion": status.get("completionDateStruct")})
    dump_jsonl(BENCH / "manifests" / "studies.jsonl", studies)
    dump_jsonl(BENCH / "manifests" / "documents.jsonl", documents)
    dump_jsonl(BENCH / "final_audit" / "registry_chronology.jsonl", registry_rows)
    exclusions = jsonl(BENCH / "manifests" / "exclusions.jsonl")
    existing = {row.get("candidate_id") for row in exclusions}
    for nct, (status_name, reason) in REJECTED.items():
        if nct not in existing:
            exclusions.append({"candidate_id": nct, "reason": reason, "status": status_name})
    dump_jsonl(BENCH / "manifests" / "exclusions.jsonl", exclusions)
    print(json.dumps({"selected": len(SELECTED), "studies": len(studies), "documents": len(documents), "requirements": sum(len(jsonl(BENCH / 'gold' / row['study_id'] / 'requirements.jsonl')) for row in studies)}, indent=2))

if __name__ == "__main__":
    main()
