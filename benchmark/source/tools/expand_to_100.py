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
    Path("/private/tmp/sapbench_strict_docs"),
    Path("/private/tmp/sapbench_fresh_docs"),
    Path("/private/tmp/sapbench_replacement_fresh"),
    Path("/private/tmp/sapbench_replacement_round3"),
]
CANDIDATE_FILES = [
    Path("/private/tmp/sapbench_candidates_1000.jsonl"),
    Path("/private/tmp/new_candidate_rows.jsonl"),
]
CANDIDATES = {}
for candidate_file in CANDIDATE_FILES:
    for row in map(json.loads, candidate_file.read_text().splitlines()):
        CANDIDATES[row["candidate_id"]] = row
CANDIDATES["NCT04819113"] = {
    "candidate_id": "NCT04819113",
    "title": "Study to Evaluate the Safety and Immunogenicity of Nimenrix (Registered) in Healthy Infants, Given at 3 and 12 Months of Age",
    "source": "ClinicalTrials.gov",
    "study_type": "interventional",
    "domain": "infectious_disease",
    "conditions": ["Meningococcal Vaccine"],
    "intervention_type": "other",
    "design_tags": ["na", "single_group", "none", "phase_3"],
    "hypothesis_types": ["superiority_or_manual_review"],
    "endpoint_types": ["binary"],
    "primary_outcomes": [],
    "enrollment": 149,
    "overall_status": "completed",
    "has_results": True,
    "protocol_url": "https://cdn.clinicaltrials.gov/large-docs/13/NCT04819113/Prot_000.pdf",
    "protocol_document_date": "2020-10-23",
    "sap_url": "https://cdn.clinicaltrials.gov/large-docs/13/NCT04819113/SAP_001.pdf",
    "sap_document_date": "2021-03-24",
}

# Exactly 34 independently reviewed families. The expansion ends at 100 keep
# questions (66 baseline + these 34); do not add more without a new decision.
SELECTED = [
    "NCT06814470", "NCT04755660", "NCT03701113",
    "NCT03198000", "NCT05516134", "NCT03256253",
    "NCT05016960", "NCT03231228", "NCT03954626",
    "NCT03744780", "NCT03835325", "NCT03876171", "NCT04819113",
    "NCT04672083", "NCT05307523", "NCT03397277", "NCT04239612",
    "NCT03332004", "NCT04674111", "NCT04126031", "NCT03324659",
    "NCT03805412", "NCT05001165", "NCT04026503", "NCT03308877",
    "NCT03576976", "NCT04858035", "NCT04759157", "NCT03203291",
    "NCT04596085", "NCT05012657", "NCT05013762", "NCT02816723",
    "NCT05208593",
]

REJECTED = {
    "NCT03917927": ("hold_version_reconciliation", "The short protocol synopsis and statistical plan share Protocol 1601 ROSE QUARTZ, but the SAP does not identify the governing protocol version/date and its planned sample size differs from the synopsis; the exact version chain is unresolved."),
    "NCT04320407": ("excluded_combined_protocol_sap_leakage", "The protocol already specifies the one-sided 0.025 paired t-test, ITT population, multiple imputation, sample-size assumptions, primary analysis, safety summaries, and interim timing, substantially reconstructing the SAP."),
    "NCT04230122": ("excluded_combined_protocol_sap_leakage", "The protocol already specifies the PK populations, noncompartmental and nonlinear mixed-effects analyses, log-linear dose proportionality and bioavailability models, 90% confidence intervals, and permits unblinded safety/PK review during conduct."),
    "NCT04435639": ("hold_chronology_reconciliation", "The protocol and SAP are prospective paired documents, but the current registry records both study start and primary completion as estimated rather than actual."),
    "NCT03547869": ("excluded_wrong_study_binding", "The uploaded SAP identifies NCT03312920 rather than NCT03547869 and its PDF was generated after the candidate study completed."),
    "NCT04466215": ("excluded_unextractable_source", "The protocol and SAP are image-only scans with effectively no extractable text, preventing reproducible page-level evidence annotation."),
    "NCT03036592": ("excluded_conduct_informed_sap", "The purported SAP was generated after study conduct and uses completed-analysis wording rather than preserving a demonstrably frozen prospective plan."),
    "NCT04716010": ("excluded_combined_protocol_sap_leakage", "The protocol reproduces the SAP's primary models, moderation analyses, power assumptions, and outlier/exclusion rules, leaving insufficient independent target content."),
    "NCT03374306": ("excluded_conduct_informed_sap", "The SAP explicitly adapts analyses for COVID-19-related delayed visits and reports observed normality-test results, so it is conduct-informed."),
    "NCT03763058": ("excluded_combined_protocol_sap_leakage", "The protocol already specifies the primary comparison, McNemar test, alpha, and core statistical framework reproduced by the short SAP."),
    "NCT05964166": ("excluded_conduct_informed_sap", "The SAP uses completed-analysis language and reports the observed data distribution and tests performed; the public file was generated after primary completion."),
    "NCT05534061": ("excluded_conduct_informed_sap", "The SAP describes preliminary analyses and models in the past tense and its PDF was generated after study conduct began."),
    "NCT05767437": ("excluded_conduct_informed_sap", "The uploaded protocol and SAP PDFs were generated after study completion and report observed distributional results and realized recruitment."),
    "NCT05124704": ("excluded_conduct_informed_documents", "Both PDFs were generated after study completion and the protocol describes the completed conduct and realized enrollment in the past tense."),
    "NCT02234284": ("excluded_conduct_informed_sap", "The SAP was uploaded after completion and describes analyses as performed, including completed sensitivity and subgroup analyses."),
    "NCT03074500": ("hold_prospective_provenance", "Although the displayed plan date precedes start, the PDF was generated after study completion and the start margin is only two days, so the frozen pre-start artifact cannot be established."),
    "NCT02352090": ("excluded_version_date_conflict", "Although the registry labels both files 2014-04-21, the SAP names SPSS versions 25 and 27 and Prism 9 and the later-added wrapper cites 2020-2021 publications; the public artifact cannot be established as the original pre-start SAP."),
    "NCT03835403": ("excluded_conduct_informed_sap", "The SAP was finalized about 19 months after actual study start, and the two-page model-visible file is a conduct-era protocol change log rather than a complete governing protocol; a prospective, outcome-uninformed protocol/SAP pair cannot be established."),
    "NCT05430854": ("excluded_conduct_informed_sap", "The SAP was finalized two days after actual study start and lacks affirmative provenance establishing that it was outcome-uninformed throughout those two days of conduct."),
    "NCT02593825": ("hold_version_reconciliation", "Actual study start is recorded only at month precision, so strict ordering against the SAP cannot be established."),
    "NCT02041494": ("excluded_conduct_informed_sap", "The SAP is later than the month-level actual study start and no affirmative pre-unblinding, conduct-independent provenance was established."),
    "NCT04786184": ("excluded_conduct_informed_sap", "The post-start target lacks affirmative evidence that it was finalized before unblinding and without access to accumulating outcomes."),
    "NCT03704116": ("excluded_conduct_informed_sap", "The post-start target lacks affirmative evidence that it was finalized before unblinding and without access to accumulating outcomes."),
    "NCT05319977": ("excluded_conduct_informed_sap", "The post-start target lacks affirmative evidence that it was finalized before unblinding and without access to accumulating outcomes."),
    "NCT03210402": ("excluded_conduct_informed_sap", "The post-start target lacks affirmative evidence that it was finalized before unblinding and without access to accumulating outcomes."),
    "NCT03691428": ("excluded_conduct_informed_sap", "The post-start target lacks affirmative evidence that it was finalized before unblinding and without access to accumulating outcomes."),
    "NCT03212144": ("excluded_conduct_informed_sap", "The post-start target lacks affirmative evidence that it was finalized before unblinding and without access to accumulating outcomes."),
    "NCT03529981": ("excluded_conduct_informed_sap", "The post-start target lacks affirmative evidence that it was finalized before unblinding and without access to accumulating outcomes."),
    "NCT02680847": ("excluded_combined_protocol_sap_leakage", "The available model-visible protocol is a post-start revision and already discloses detailed PK and safety analysis rules."),
    "NCT04841577": ("excluded_combined_protocol_sap_leakage", "The protocol directly discloses the ANCOVA, covariates, missing-data, non-inferiority, and interim framework."),
    "NCT05695391": ("excluded_conduct_informed_protocol", "The available protocol is a post-start version and substantially discloses the target analysis and interim stopping rules."),
    "NCT05979207": ("excluded_conduct_informed_protocol", "The protocol substantially discloses the PK/PD model and permits adaptive cohort decisions after safety and PK review."),
    "NCT05365217": ("excluded_combined_protocol_sap_leakage", "The protocol substantially reproduces the analysis populations, endpoint definition, models, and missing-data rule."),
    "NCT04231318": ("excluded_combined_protocol_sap_leakage", "The protocol discloses the primary and secondary ANOVA, covariates, repeated-measures model, populations, missing-data assumptions, and GEE."),
    "NCT03349632": ("excluded_combined_protocol_sap_leakage", "The protocol discloses the safety set, primary descriptive analysis, missing-data and multiplicity rules, leaving insufficient independent target content."),
    "NCT03392532": ("excluded_combined_protocol_sap_leakage", "The protocol discloses the analysis populations, primary definition, confidence interval, threshold, missingness, safety, and sample-size plan."),
    "NCT04091061": ("excluded_conduct_informed_protocol", "The protocol discloses the PK populations and ANOVA with 90% confidence intervals and permits sponsor unblinded safety and PK-model review during conduct."),
    "NCT04953442": ("excluded_conduct_informed_protocol", "The available protocol is a later IRB report stating that data collection concluded and reporting realized enrollment."),
    "NCT03102034": ("excluded_conduct_informed_sap", "The SAP explicitly plans an interim safety analysis."),
    "NCT02581631": ("excluded_conduct_informed_sap", "The SAP postdates actual start and describes analyses by completed cohort."),
    "NCT03856996": ("excluded_conduct_informed_sap", "The SAP postdates actual start and plans repeated unblinded safety analyses."),
    "NCT02816710": ("excluded_conduct_informed_sap", "The analysis document uses completed-analysis or results-state language."),
    "NCT03564080": ("excluded_conduct_informed_sap", "The analysis document uses completed-analysis or results-state language."),
    "NCT05791435": ("excluded_conduct_informed_sap", "The analysis document uses completed-analysis or results-state language."),
    "NCT03660787": ("excluded_combined_protocol_sap_leakage", "The protocol already specifies the primary test, confidence intervals, analysis populations, safety analysis, and power calculation."),
    "NCT03868631": ("excluded_conduct_informed_sap", "The nominally pre-start files describe realized recruitment, completed analyses, model convergence, and observed analysis-set sizes."),
    "NCT03918174": ("excluded_conduct_informed_sap", "The documents are written as a completed preliminary-results report and use completed-analysis language."),
    "NCT05052138": ("excluded_conduct_informed_sap", "Both protocol and SAP use completed-data and completed-analysis language rather than a prospective plan."),
    "NCT07330232": ("excluded_conduct_informed_sap", "The SAP internal date is 2025-12-29, after actual primary completion, despite an inconsistent registry document date of 2021-07-30."),
    "NCT04966910": ("excluded_conduct_informed_sap", "The SAP reports realized sample sizes, sphericity results, and an observed missing-data decision."),
    "NCT03925220": ("hold_version_reconciliation", "The SAP cover contains irreconcilable dates, stating Document Date August 10, 2023 and Revised November 11, 2018."),
    "NCT05039528": ("excluded_conduct_informed_protocol", "The protocol plans annual interim efficacy review by a DSMB."),
    "NCT04226742": ("excluded_conduct_informed_sap", "The SAP uses completed-analysis language for inclusion, imputation, and model adjustment despite its nominal pre-start date."),
    "NCT02657564": ("excluded_duplicate_study_family", "The family is already represented by baseline study PUBLIC-PEG-RENAL-SAFETY-001."),
    "NCT05421624": ("excluded_duplicate_study_family", "The family is already represented by baseline study PUBLIC-AMPED-PD-001."),
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

# Earlier exploratory screening briefly classified this existing baseline family
# as conduct-informed merely because its plan contains a prespecified interim
# analysis.  The dated plan predates actual study start, so that rejection was
# withdrawn and must be removed on every deterministic rebuild.
RETRACTED_REJECTIONS = {"NCT05187013"}

PROVENANCE_NOTES = {
    "NCT03231228": "SAP explicitly binds to protocol HC-G-H-1601 version 2.0 and states that analyses were defined before database lock.",
    "NCT04819113": "Final protocol C0921062 dated 2020-10-23 and SAP version 1 dated 2021-03-24 share the same sponsor study code and title; the SAP states that no interim analysis is planned, and both files predate actual study start.",
    "NCT04672083": "Final SAP version 1 dated 2020-08-13 explicitly states that it is based on final protocol version 4 dated 2020-07-27; both identify study CPT31-001 and predate actual study start.",
    "NCT05307523": "Binding relies on the same registry submission, identical official title and date, because the contemporaneous files leave the NCT field blank.",
    "NCT03332004": "Protocol and SAP share the same date, title, investigator, and protocol identifier 736513.A287/C.E./2013 and predate actual start by almost three years.",
    "NCT03324659": "Both registry-hosted files share the study title and predate actual start; the contemporaneous files state that an NCT number was not yet available.",
    "NCT05001165": "The SAP was uploaded before actual start. Binding relies on the same date, title, PI, institution, and registry record because both files state that the NCT number was not yet assigned; the protocol was uploaded later and is not used as chronology evidence.",
    "NCT03805412": "The SAP predates the selected protocol by one day; both registry-hosted files share the same title and study identifier, and both predate actual start.",
    "NCT04759157": "The SAP predates the selected protocol revision; both files explicitly identify NCT04759157 and both predate actual start.",
    "NCT03203291": "The SAP predates the selected protocol revision; both files explicitly identify NCT03203291 and both predate actual start.",
    "NCT04596085": "The SAP predates the selected protocol revision; both files explicitly bind to protocol NS-VC-CT01-20 and both predate actual start.",
    "NCT05208593": "The contemporaneous protocol and SAP share exact date, title, and unique protocol ID IRB20201070D; both state that the NCT number was not yet assigned and predate actual start.",
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


def isolate_reference_only_requirements(studies, documents):
    """Remove protocol-only scoring from facts evidenced only by the hidden SAP."""
    document_roles = {row["document_id"]: row["role"] for row in documents}
    for study in studies:
        requirement_path = BENCH / "gold" / study["study_id"] / "requirements.jsonl"
        if not requirement_path.is_file():
            continue
        rows = jsonl(requirement_path)
        changed = False
        for row in rows:
            if row.get("status") != "explicit" or "protocol_only" not in row.get("tracks", []):
                continue
            evidence_roles = {
                document_roles.get(item.get("document_id"))
                for item in row.get("evidence", [])
            }
            if evidence_roles and evidence_roles <= {"reference_sap"}:
                row["tracks"] = [track for track in row["tracks"] if track != "protocol_only"]
                if "confirmed_decisions" not in row["tracks"]:
                    row["tracks"].append("confirmed_decisions")
                changed = True
        if changed:
            dump_jsonl(requirement_path, rows)

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


def toc_like(text, context):
    """Return true when a match is a contents/index entry, not evidence."""
    return (
        "table of contents" in text.lower()
        or bool(re.search(r"\.{4,}", context))
        or len(re.findall(r"\b\d+(?:\.\d+){1,3}\b", context)) >= 5
    )


def first_hit(items, patterns, fallback=1, width=260):
    for pattern in patterns:
        rx = re.compile(pattern, re.I)
        for page, raw in items:
            text = clean(raw)
            match = rx.search(text)
            if match:
                start = max(0, match.start() - 70)
                context = text[start:min(len(text), match.end() + width)]
                if toc_like(text, context):
                    continue
                return page, context
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
            is_toc = toc_like(text, context)
            substantive = bool(re.search(
                r"(?i)\b(?:will|shall|defined as|includes?|consists?|using|based on|summari[sz]ed|analy[sz]ed|estimated|calculated|imputed|randomi[sz]ed)\b",
                context,
            ))
            if is_toc:
                continue
            values.append((not substantive, page, context))
    values.sort(key=lambda item: (item[0], item[1]))
    return [(page, context) for _, page, context in values[:limit]]


VALUE_STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "on",
    "for", "with", "from", "by", "at", "as", "is", "are", "was",
    "were", "be", "this", "that", "study", "participants", "participant",
    "number", "change", "baseline", "through", "about", "approximately",
    "assessed", "assessment", "measure", "score", "treatment", "group",
    "groups", "week", "weeks", "day", "days",
}


def value_tokens(text):
    return {
        token for token in re.findall(r"[a-z0-9]+", text.lower())
        if len(token) >= 2 and token not in VALUE_STOPWORDS
    }


def best_value_hit(items, value, width=520):
    """Find a non-TOC passage that substantively overlaps one source value."""
    wanted = value_tokens(value)
    best = (0.0, None)
    for page, raw in items:
        text = clean(raw)
        if not text:
            continue
        starts = [
            match.start()
            # Sets have process-randomized iteration order.  Sorting here keeps
            # equal-scoring passage selection stable across rebuilds.
            for token in sorted(wanted)
            for match in re.finditer(re.escape(token), text.lower())
        ] or [0]
        for start in starts:
            context = text[max(0, start - 180):min(len(text), start + width)]
            if toc_like(text, context):
                continue
            score = len(wanted & value_tokens(context)) / len(wanted) if wanted else 1.0
            if score > best[0]:
                best = (score, (page, context))
    return best


def source_hits_for_values(items, values, minimum=0.5):
    """Return one source passage per value only when every value is supported."""
    selected = []
    for value in values:
        score, hit = best_value_hit(items, value)
        if hit is None or score < minimum:
            return []
        if hit not in selected:
            selected.append(hit)
    return selected


def prospective_sample_hits(items):
    candidates = hits(
        items,
        r"(?:sample(?: size)?\s*(?:is|of|:)?|target (?:sample size|enrollment)\s*(?:is|of|:)?|"
        r"(?:estimated )?total of|the participant group will be\s*|"
        r"(?:plan|aim|expect|propos|intend)[a-z]* to (?:enroll|recruit|randomi[sz]e|include))"
        r".{0,80}?\b\d{1,5}\b[^.;]{0,80}?(?:participants?|patients?|subjects?|children|couples|veterans|adults?|individuals|cases)",
        12,
    )
    retained = []
    for item in candidates:
        text = clean(item[1])
        if re.search(r"(?i)\b(?:were|was|had been) (?:enrolled|recruited|randomi[sz]ed|included|treated|completed)\b", text):
            continue
        if not re.search(r"(?i)\b(?:will|shall|plan|aim|expect|propos|intend|target|sample size|approximately|estimated|anticipated)\b", text):
            continue
        retained.append(item)
    return retained

def parse_date(value):
    if not value or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"day-level date required, got {value!r}")
    return date.fromisoformat(value)

def evidence(document_id, item):
    page, text = item
    return [{"document_id": document_id, "locator": f"physical PDF page {page}", "text": concise(item, 420)}]


def evidence_from_hits(document_id, items):
    return [
        {"document_id": document_id, "locator": f"physical PDF page {page}", "text": concise((page, text), 420)}
        for page, text in items
    ]

def concise(item, limit=280):
    text = clean(item[1])
    if len(text) <= limit:
        return text
    clipped = text[:limit].rsplit(" ", 1)[0]
    return clipped + "…"


def page_hit(items, page, pattern, width=520, before=0):
    """Return a deterministic, exact excerpt from one physical PDF page."""
    by_page = {number: clean(text) for number, text in items}
    text = by_page.get(page, "")
    match = re.search(pattern, text, re.I)
    if not match:
        raise ValueError(f"manual evidence anchor not found on physical page {page}: {pattern}")
    start = max(0, match.start() - before)
    return page, text[start:min(len(text), match.start() + width)]

def requirement(study_id, index, rubric, severity, text, values, doc_id, hit, status="explicit", tracks=None, notes=None):
    row = {
        "requirement_id": f"{study_id}-R{index:03d}", "study_id": study_id,
        "rubric_id": rubric, "tracks": tracks or ["protocol_only", "confirmed_decisions"],
        "applies": True, "status": status, "severity": severity,
        "requirement": text, "acceptable_values": values,
        "evidence": evidence_from_hits(doc_id, hit) if isinstance(hit, list) else evidence(doc_id, hit),
    }
    if notes:
        row["notes"] = notes
    return row


def replace_requirement(rows, rubric, *, text, values, doc_id, hits_, status="explicit", notes=None):
    """Replace one generated requirement while retaining its stable ID/tracks."""
    matches = [row for row in rows if row["rubric_id"] == rubric]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one {rubric} requirement, found {len(matches)}")
    row = matches[0]
    row.update({
        "requirement": text,
        "acceptable_values": values,
        "status": status,
        "evidence": evidence_from_hits(doc_id, hits_),
    })
    if notes is None:
        row.pop("notes", None)
    else:
        row["notes"] = notes


def apply_manual_requirement_overrides(rows, nct, ppages, spages, protocol_id, sap_id):
    """Apply page-reviewed overrides for candidates that defeat generic extraction.

    These overrides live in the generator, rather than only in generated JSONL, so
    rebuilding the benchmark preserves the reviewed annotations exactly.
    """
    if nct == "NCT04672083":
        replace_requirement(
            rows,
            "CORE-DESIGN-001",
            text=(
                "Preserve the protocol-defined Phase 1a, placebo-controlled, double-blind, single-dose, "
                "sequential-group dose-escalation design in healthy adults."
            ),
            values=[
                "Phase 1a",
                "placebo-controlled",
                "double-blind",
                "single-dose sequential-group dose escalation",
                "healthy adults",
            ],
            doc_id=protocol_id,
            hits_=[page_hit(ppages, 6, r"This study will comprise a placebo-controlled", 520)],
        )
        replace_requirement(
            rows,
            "CORE-RAND-001",
            text=(
                "Use 4 dose-level groups (A1 to A4) at 0.01, 0.04, 0.12, and 0.24 mg/kg; "
                "within each group allocate 6 subjects to CPT31 and 2 to matching placebo, split into "
                "two cohorts with sentinel dosing in the first cohort."
            ),
            values=[
                "Groups A1 to A4",
                "0.01, 0.04, 0.12, and 0.24 mg/kg",
                "6 CPT31 and 2 matching placebo per group",
                "two cohorts per group with sentinel dosing in cohort 1",
            ],
            doc_id=protocol_id,
            hits_=[
                page_hit(ppages, 6, r"It is planned for 6 subjects per dose level group", 620),
                page_hit(ppages, 6, r"Proposed dose levels", 220),
            ],
        )
        replace_requirement(
            rows,
            "CORE-SAMPLE-001",
            text=(
                "Plan for 32 healthy subjects in 4 dose-level groups (Groups A1 to A4), "
                "with 8 subjects per group: 6 receiving CPT31 and 2 receiving matching placebo."
            ),
            values=[
                "32 healthy subjects",
                "4 dose-level groups (Groups A1 to A4)",
                "6 CPT31 and 2 placebo subjects per group",
            ],
            doc_id=protocol_id,
            hits_=[
                page_hit(ppages, 6, r"It is planned for 6 subjects per dose level group", 360),
                page_hit(ppages, 6, r"Number of subjects:\s*32 healthy subjects", 180),
            ],
            notes="This is the prospective protocol target, not registry actual enrollment.",
        )
        replace_requirement(
            rows,
            "CORE-ENDPT-001",
            text=(
                "Define the primary safety and tolerability outcome family to include adverse events, "
                "clinical laboratory evaluations, 12-lead ECGs, vital signs, physical examinations, "
                "and anti-CPT31 antibodies."
            ),
            values=[
                "adverse events",
                "clinical laboratory evaluations",
                "12-lead electrocardiograms",
                "vital signs",
                "physical examinations",
                "anti-CPT31 antibodies",
            ],
            doc_id=protocol_id,
            hits_=[page_hit(ppages, 7, r"Safety:\s*Adverse events", 420)],
        )
        replace_requirement(
            rows,
            "CORE-ENDPT-002",
            text=(
                "Cover the secondary pharmacokinetic and immunogenicity families: plasma and urinary "
                "CPT31 concentrations; AUC0-infinity, AUC0-tlast, Cmax, Tmax, terminal half-life, CL/F, "
                "Vz/F, Ae, Fe, and CLR; and anti-CPT31 antibodies."
            ),
            values=[
                "plasma and urinary CPT31 concentrations",
                "AUC0-infinity, AUC0-tlast, Cmax, Tmax, terminal half-life, CL/F, Vz/F, Ae, Fe, and CLR",
                "anti-CPT31 antibodies",
            ],
            doc_id=protocol_id,
            hits_=[
                page_hit(ppages, 7, r"Endpoints:\s*Pharmacokinetics", 920),
                page_hit(ppages, 7, r"Safety:\s*Adverse events", 420),
            ],
        )
        replace_requirement(
            rows,
            "CORE-POP-FAS-001",
            text=(
                "Use the safety population for safety and immunogenicity summaries and the PK population "
                "for pharmacokinetic summaries and modeling: respectively, all subjects receiving at least "
                "1 dose of CPT31 or placebo, and CPT31 recipients with evaluable PK data."
            ),
            values=[
                "safety population: all subjects receiving at least 1 dose of CPT31 or placebo",
                "PK population: CPT31 recipients with evaluable PK data",
            ],
            doc_id=sap_id,
            hits_=[page_hit(spages, 11, r"7\.2\. Safety Population", 430)],
            notes="These reference-only population definitions must not be exposed in the protocol-only input.",
        )
        replace_requirement(
            rows,
            "CORE-METHOD-001",
            text=(
                "Use objective-specific methods: summarize safety descriptively; derive PK parameters by "
                "noncompartmental analysis; and assess Cmax, AUC0-tlast, and AUC0-infinity dose "
                "proportionality with the prespecified power model or ANOVA as appropriate."
            ),
            values=[
                "descriptive safety summaries",
                "noncompartmental PK analysis",
                "power model or ANOVA for dose proportionality of Cmax, AUC0-tlast, and AUC0-infinity",
            ],
            doc_id=sap_id,
            hits_=[
                page_hit(spages, 14, r"8\.5\.1\. Pharmacokinetic Analysis", 440),
                page_hit(spages, 17, r"Where data are available, CPT31 dose proportionality", 720),
                page_hit(spages, 21, r"8\.6\.6\. Safety and Tolerability Statistical Methodology", 180),
            ],
        )
        replace_requirement(
            rows,
            "CORE-ALPHA-001",
            text=(
                "For each dose-proportionality PK parameter, report the pooled slope estimate with its "
                "95% confidence interval and between-subject coefficient of variation; do not introduce "
                "an inferential safety test because none is planned."
            ),
            values=[
                "pooled slope estimate",
                "95% confidence interval",
                "between-subject coefficient of variation",
                "no inferential safety analysis",
            ],
            doc_id=sap_id,
            hits_=[
                page_hit(spages, 17, r"For each PK parameter separately, a pooled estimate", 520),
                page_hit(spages, 21, r"8\.6\.6\. Safety and Tolerability Statistical Methodology", 180),
            ],
        )
        replace_requirement(
            rows,
            "CORE-SAFE-001",
            text=(
                "Implement the SAP's safety outputs: derive and summarize TEAEs by treatment, "
                "summarize laboratory and vital-sign changes from baseline by treatment and timepoint, "
                "and summarize 12-lead ECG changes and prespecified QTc outlier categories."
            ),
            values=[
                "TEAE definition and summaries by treatment",
                "clinical laboratory changes from baseline",
                "vital-sign changes from baseline",
                "12-lead ECG changes from baseline and QTc outlier categories",
            ],
            doc_id=sap_id,
            hits_=[
                page_hit(spages, 19, r"A treatment-emergent adverse event \(TEAE\) will be defined", 520),
                page_hit(spages, 20, r"8\.6\.2\. Clinical Laboratory Parameters", 620),
                page_hit(spages, 21, r"8\.6\.4\. 12-lead Electrocardiogram Parameters", 620),
            ],
        )

    if nct == "NCT04819113":
        replace_requirement(
            rows,
            "CORE-DESIGN-001",
            text=(
                "Preserve the Phase 3b, multicenter, open-label, single-arm design in which healthy infants "
                "receive Nimenrix at 3 and 12 months of age."
            ),
            values=[
                "Phase 3b",
                "multicenter",
                "open-label",
                "single-arm",
                "Nimenrix at 3 and 12 months of age",
            ],
            doc_id=protocol_id,
            hits_=[page_hit(ppages, 12, r"Overall Design", 500)],
        )
        replace_requirement(
            rows,
            "CORE-SAMPLE-001",
            text=(
                "Plan to enroll approximately 150 participants in the single open-label vaccine group, "
                "yielding approximately 130 evaluable participants after allowing for up to about 15% exclusion."
            ),
            values=[
                "approximately 150 enrolled participants",
                "approximately 130 evaluable participants",
                "up to approximately 15% exclusion from the applicable evaluable population",
            ],
            doc_id=protocol_id,
            hits_=[
                page_hit(ppages, 54, r"9\.2\. Sample Size Determination", 620),
            ],
            notes="This is the prospective protocol target; do not substitute registry actual enrollment.",
        )
        replace_requirement(
            rows,
            "CORE-ENDPT-001",
            text=(
                "Preserve both primary outcome families: post-Dose 2 safety (local reactions, systemic "
                "events, antipyretic use, AEs, SAEs, NDCMCs, and immediate AEs) and post-Dose 2 "
                "immunogenicity (rSBA titers >=1:8 and GMTs for MenA, MenC, MenW-135, and MenY)."
            ),
            values=[
                "post-Dose 2 local reactions, systemic events, antipyretic use, AEs, SAEs, NDCMCs, and immediate AEs",
                "post-Dose 2 rSBA titers >=1:8 and GMTs for MenA, MenC, MenW-135, and MenY",
            ],
            doc_id=protocol_id,
            hits_=[
                page_hit(ppages, 9, r"Primary \(Safety\):", 680),
                page_hit(ppages, 9, r"Primary \(Immunogenicity\):", 760),
            ],
        )
        replace_requirement(
            rows,
            "CORE-ENDPT-002",
            text=(
                "Preserve the secondary outcome families: post-Dose 1 safety/reactogenicity and the "
                "post-Dose 1 and post-Dose 2 supportive immunogenicity measures using rSBA and hSBA "
                "thresholds and GMTs for MenA, MenC, MenW-135, and MenY."
            ),
            values=[
                "post-Dose 1 local reactions, systemic events, antipyretic use, AEs, SAEs, NDCMCs, and immediate AEs",
                "post-Dose 1 rSBA titers >=1:8 and >=1:128 and GMTs",
                "post-Dose 1 and post-Dose 2 hSBA titers >=1:4 and >=1:8 and GMTs",
                "post-Dose 2 rSBA titers >=1:128",
            ],
            doc_id=protocol_id,
            hits_=[
                page_hit(ppages, 10, r"Secondary:\s*Secondary:\s*Secondary:", 980),
                page_hit(ppages, 11, r"Percentage of participants with hSBA-MenA", 880),
            ],
        )
        replace_requirement(
            rows,
            "CORE-POP-FAS-001",
            text=(
                "Use the post-Dose 2 evaluable immunogenicity population for the primary immunogenicity "
                "analysis and the visit-specific Dose 2 safety population for primary safety analyses, "
                "applying the SAP's receipt, assay, timing, prohibited-medication, deviation, and safety-data criteria."
            ),
            values=[
                "post-Dose 2 evaluable immunogenicity population",
                "Dose 2 safety population",
                "SAP-defined inclusion and exclusion criteria",
            ],
            doc_id=sap_id,
            hits_=[
                page_hit(spages, 26, r"Post.Dose 2 evaluable immunogenicity population", 820),
                page_hit(spages, 27, r"Dose 2 safety population", 300),
            ],
            notes="These are reference-only confirmed decisions and must not be exposed in the protocol-only input.",
        )
        replace_requirement(
            rows,
            "CORE-POP-PPS-001",
            text=(
                "Define the post-Dose 2 mITT population as participants receiving 2 doses with at least "
                "1 valid determinate MenACWY assay result at Visit 4, and use it for the supportive analysis "
                "only when it differs from the evaluable population by more than 10%."
            ),
            values=[
                "post-Dose 2 mITT population",
                "2 doses and at least 1 valid determinate MenACWY result at Visit 4",
                "supportive analysis triggered by a difference greater than 10%",
            ],
            doc_id=sap_id,
            hits_=[
                page_hit(spages, 26, r"Post.Dose 2 mITT", 300),
                page_hit(spages, 32, r"Sensitivity/Supplementary Analyses", 320),
            ],
        )
        replace_requirement(
            rows,
            "CORE-MISS-001",
            text=(
                "Apply the SAP's missing-data rules: use Pfizer rules for missing AE start dates and do not "
                "otherwise impute safety data; analyze observed determinate immunogenicity results without "
                "imputation, set results below LLOQ to 0.5 x LLOQ, and treat QNS, indeterminate, not-done, "
                "and no-blood-draw results as missing."
            ),
            values=[
                "Pfizer rules for missing AE start dates",
                "no other safety imputation",
                "observed determinate immunogenicity data with no imputation",
                "below-LLOQ results set to 0.5 x LLOQ",
                "QNS, indeterminate, not done, and no blood draw treated as missing",
            ],
            doc_id=sap_id,
            hits_=[
                page_hit(spages, 28, r"5\.3\. Methods to Manage Missing Data", 360),
                page_hit(spages, 29, r"5\.3\.2\. Immunogenicity Data", 820),
            ],
        )
        replace_requirement(
            rows,
            "CORE-METHOD-001",
            text=(
                "Use descriptive estimation: report n and percentages for binary endpoints with exact "
                "2-sided 95% Clopper-Pearson intervals, and compute serogroup GMTs on the natural-log "
                "scale with 2-sided 95% intervals based on the Student t distribution."
            ),
            values=[
                "n and percentage for binary endpoints",
                "exact 2-sided 95% Clopper-Pearson confidence intervals",
                "natural-log GMT analysis with exponentiated Student t confidence limits",
            ],
            doc_id=sap_id,
            hits_=[
                page_hit(spages, 27, r"5\.2\.1\. Analyses for Binary Endpoints", 620),
                page_hit(spages, 28, r"5\.2\.2\.1\. Geometric Mean Titers", 720),
            ],
        )
        replace_requirement(
            rows,
            "CORE-ALPHA-001",
            text=(
                "Report exact 2-sided 95% Clopper-Pearson confidence intervals for percentages and "
                "2-sided 95% Student-t-based confidence intervals for log-scale GMT analyses."
            ),
            values=[
                "exact 2-sided 95% Clopper-Pearson confidence intervals for percentages",
                "2-sided 95% Student-t-based confidence intervals for GMTs",
            ],
            doc_id=sap_id,
            hits_=[
                page_hit(spages, 27, r"The exact 2-sided 95% CIs for percentages", 420),
                page_hit(spages, 28, r"The associated exact 2-sided 95% CIs", 360),
            ],
        )
        replace_requirement(
            rows,
            "CORE-MULT-001",
            text=(
                "Do not invent a multiplicity-controlled hypothesis-testing hierarchy: this is an "
                "estimation study with no specific hypotheses, and all endpoints are summarized descriptively."
            ),
            values=[
                "no specific hypotheses tested",
                "estimation and descriptive summaries",
                "no invented multiplicity hierarchy",
            ],
            doc_id=protocol_id,
            hits_=[page_hit(ppages, 54, r"9\.1\. Estimands and Statistical Hypotheses", 360)],
        )
        replace_requirement(
            rows,
            "CORE-SENS-001",
            text=(
                "Repeat the main post-Dose 2 immunogenicity analysis on the corresponding mITT population "
                "only if the evaluable and mITT populations differ by more than 10%."
            ),
            values=[
                "mITT sensitivity analysis",
                "triggered only when the population-size difference is greater than 10%",
            ],
            doc_id=sap_id,
            hits_=[page_hit(spages, 32, r"Sensitivity/Supplementary Analyses", 320)],
        )
        replace_requirement(
            rows,
            "CORE-SAFE-001",
            text=(
                "Use the visit-specific safety populations and summarize primary safety endpoints by vaccine "
                "group with n, percentage, and exact 2-sided 95% Clopper-Pearson intervals; do not impute "
                "missing e-diary data and handle missing AE dates under Pfizer safety rules."
            ),
            values=[
                "visit-specific safety population",
                "n, percentage, and exact 2-sided 95% Clopper-Pearson confidence interval",
                "no imputation of missing e-diary data",
                "Pfizer safety rules for missing AE dates",
            ],
            doc_id=sap_id,
            hits_=[
                page_hit(spages, 27, r"Dose 1 safety population", 460),
                page_hit(spages, 29, r"6\.1\.1\. Primary Safety Endpoints", 620),
                page_hit(spages, 31, r"6\.1\.1\.5\. Adverse Events", 620),
            ],
        )

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
    # Keep sample-size extraction deliberately narrow.  Earlier versions
    # matched phrases such as "target population" followed much later by a
    # session count, which produced requirements unsupported by the excerpt.
    target_hits = prospective_sample_hits(ppages)
    sap_population_hits = hits(spages, r"intent.to.treat|full analysis set|analysis population|efficacy population|all (?:randomized|enrolled)", 2)
    sap_population = sap_population_hits[0] if sap_population_hits else first_hit(spages, [r"statistical analysis plan|data analysis plan"] )
    sap_method_hits = hits(
        spages,
        r"primary analysis.{0,220}|linear mixed models?|mixed.effects?|multilevel structural equation|"
        r"structural equation model|randomization test|two one.sided equivalence test|\bTOST\b|"
        r"pass/fail|analysis of variance|generalized estimating|analysis of covariance|ANCOVA|"
        r"logistic regression|fisher.?s exact|mcnemar|wilcoxon|paired.{0,15}t.test|"
        r"repeated.measures.{0,30}(?:ANOVA|MANOVA)|receiver operating characteristic|"
        r"sensitivity.{0,80}specificity|descriptive statistics",
        3,
    )
    sap_method = sap_method_hits[0] if sap_method_hits else first_hit(spages, [r"statistical analysis plan|data analysis plan"] )
    sap_missing_hits = hits(spages, r"missing data|missing values?|imputation|complete.case|available.case|last observation")
    sap_mult_hits = hits(spages, r"multiplicity|multiple comparisons?|family.wise|bonferroni|hierarch|fixed sequential|no (?:adjustment|correction).{0,30}multip")
    sap_alpha_hits = hits(spages, r"two.sided|one.sided|alpha.{0,25}0?\.0[125]|significance.{0,25}0?\.0[125]|p.?value.{0,12}0?\.0[125]|95% (?:confidence|CI)")
    sap_safety_hits = hits(spages, r"adverse events?|safety (?:analysis|population|set|outcome|endpoint)|tolerability")
    sap_sensitivity_hits = hits(spages, r"sensitivity analys|supportive analys|per.protocol|completer analys")
    group_values = [a.get("label") for a in arms if a.get("label")]
    model_design = [str(x).lower() for x in [info.get("allocation"), info.get("interventionModel"), info.get("maskingInfo", {}).get("masking")] if x]
    phase = registry.get("designModule", {}).get("phases", [])
    model_design += [str(x).lower() for x in phase]
    rows = []
    protocol_uncertainty = first_hit(
        ppages,
        [r"statistical analys|data analys|primary (?:endpoint|outcome|objective)|study design"],
    )
    group_values = list(dict.fromkeys(group_values))
    primary_names = list(dict.fromkeys(o.get("measure") for o in prim if o.get("measure")))
    primary_times = list(dict.fromkeys(o.get("timeFrame") for o in prim if o.get("timeFrame")))
    secondary_names = list(dict.fromkeys(o.get("measure") for o in sec[:5] if o.get("measure")))
    group_hits = source_hits_for_values(ppages, group_values) if group_values else []
    primary_hits = source_hits_for_values(ppages, primary_names) if primary_names else []
    timing_hits = source_hits_for_values(ppages, primary_times) if primary_times else []
    secondary_hits = source_hits_for_values(ppages, secondary_names) if secondary_names else []
    def add(rubric, severity, text, values, doc, hit, status="explicit", tracks=None, notes=None):
        rows.append(requirement(study_id, len(rows)+1, rubric, severity, text, values, doc, hit, status, tracks, notes))

    protocol_text = " ".join(clean(text) for _, text in ppages)
    provenance_values = [candidate["title"]] + ([nct] if re.search(re.escape(nct), protocol_text, re.I) else [])
    provenance_label = f"{candidate['title']} ({nct})" if len(provenance_values) == 2 else candidate["title"]
    add("CORE-PROV-001", "critical", f"Identify the analysis as belonging to {provenance_label}.", provenance_values, protocol_id, first_hit(ppages, [re.escape(nct), re.escape(candidate["title"][:35])]))
    add("CORE-DESIGN-001", "critical", f"Preserve the study design as {', '.join(model_design) or 'an interventional study'}.", model_design or ["interventional"], protocol_id, first_hit(ppages, [r"study design|randomi[sz]ed|single.arm|parallel|crossover|open.label|double.blind"]))
    if group_values and group_hits:
        add("CORE-RAND-001", "major", f"Name the planned treatment groups without inventing additional arms: {'; '.join(group_values)}.", group_values, protocol_id, group_hits)
    elif group_values:
        group_context = first_hit(ppages, [r"treatment groups?|study arms?|randomi[sz].{0,140}(?:group|arm)|intervention group|control group"])
        add("CORE-RAND-001", "major", f"Preserve the protocol-defined treatment-group structure in this source passage and flag registry-only arm labels for confirmation: {concise(group_context)}", [concise(group_context), "confirm exact arm labels"], protocol_id, group_context, "needs_confirmation")
    if target_hits:
        add("CORE-SAMPLE-001", "major", f"Use the prospective protocol sample-size statement and its planning assumptions: {concise(target_hits[0])}", [concise(target_hits[0]), "do not substitute registry actual enrollment"], protocol_id, target_hits[0], notes="Registry actual enrollment is conduct context only, never the prospective target.")
    elif len(rows) < 4:
        add("CORE-SAMPLE-001", "major", "State that the prospective target sample size still requires confirmation; do not substitute registry actual enrollment.", ["needs confirmation", "actual enrollment is not the target"], protocol_id, first_hit(ppages, [r"participants?|subjects?|enroll"]), "needs_confirmation")
    primary_context = first_hit(ppages, [r"primary (?:endpoint|outcome|objective)"])
    if primary_names and primary_hits:
        add("CORE-ENDPT-001", "critical", f"Define the primary outcome family as: {'; '.join(primary_names)}.", primary_names, protocol_id, primary_hits)
    else:
        add("CORE-ENDPT-001", "critical", f"Define the primary outcome/objective using the protocol's own prospective statement and flag any later registry-only operational wording for confirmation: {concise(primary_context)}", [concise(primary_context), "confirm any exact operational definition not stated in the protocol"], protocol_id, primary_context, "needs_confirmation")
    if primary_times and timing_hits:
        add("CORE-VISIT-001", "critical", f"Use the primary assessment timing: {'; '.join(primary_times)}.", primary_times, protocol_id, timing_hits)
    elif primary_times:
        add("CORE-VISIT-001", "critical", "Use only protocol-supported primary assessment timing and flag the exact analysis time point or window for confirmation when the protocol does not state it.", ["protocol-supported timing", "needs confirmation"], protocol_id, primary_context, "needs_confirmation", notes="The current registry timing was not used as gold because it was not fully supported by the frozen protocol text.")
    if secondary_names and secondary_hits:
        add("CORE-ENDPT-002", "major", f"Cover the prespecified secondary outcome family without promoting it above the primary outcome: {'; '.join(secondary_names)}.", secondary_names, protocol_id, secondary_hits)
    elif secondary_names:
        secondary_context = first_hit(ppages, [r"secondary (?:endpoint|outcome|objective)", r"exploratory (?:endpoint|outcome|objective)"])
        add("CORE-ENDPT-002", "major", f"Cover the secondary outcome/objective family stated in the protocol and flag later registry-only operational wording for confirmation: {concise(secondary_context)}", [concise(secondary_context), "confirm any exact operational definition not stated in the protocol"], protocol_id, secondary_context, "needs_confirmation")
    if sap_population_hits:
        add("CORE-POP-FAS-001", "critical", f"Define the main analysis population using the reference rule: {concise(sap_population)}", [concise(sap_population)], sap_id, sap_population, tracks=["confirmed_decisions"], notes="Do not infer a generic ITT/FAS rule when the cited SAP defines a different population.")
    else:
        add("CORE-POP-FAS-001", "critical", "Flag the main analysis-population inclusion and treatment-attribution rules as unresolved; do not invent an ITT, FAS, or evaluable-set definition.", ["needs confirmation", "population inclusion rule", "treatment attribution"], protocol_id, protocol_uncertainty, status="needs_confirmation", tracks=["protocol_only", "confirmed_decisions"], notes="No governing analysis-population rule was located in either source; the cited protocol passage anchors the study context, not an inferred rule.")
    if sap_sensitivity_hits:
        add("CORE-POP-PPS-001", "major", f"Define the supportive or sensitivity population using the reference rule and keep it subordinate to the primary analysis: {concise(sap_sensitivity_hits[0])}", [concise(sap_sensitivity_hits[0])], sap_id, sap_sensitivity_hits[0], tracks=["confirmed_decisions"] )
    else:
        add("CORE-UNCERT-001", "major", "Flag any per-protocol or completer analysis as unresolved unless the protocol independently specifies it.", ["needs confirmation", "do not invent exclusions"], protocol_id, protocol_uncertainty, "needs_confirmation", ["protocol_only", "confirmed_decisions"], "No supportive-population rule was located in either source; the cited protocol passage anchors the study context, not an inferred rule.")
    if sap_method_hits:
        add("CORE-METHOD-001", "critical", f"Use the primary statistical method and comparison structure specified in the reference plan: {concise(sap_method)}", [concise(sap_method)], sap_id, sap_method, tracks=["confirmed_decisions"] )
    else:
        add("CORE-METHOD-001", "critical", "Flag the primary statistical model, comparison, covariates, and repeated/paired structure as unresolved rather than inventing them.", ["needs confirmation", "model", "comparison", "covariates"], protocol_id, protocol_uncertainty, status="needs_confirmation", tracks=["protocol_only", "confirmed_decisions"], notes="No executable primary method was located in either source; the cited protocol passage anchors the study context, not an inferred method.")
    if sap_alpha_hits:
        add("CORE-ALPHA-001", "critical", f"Use the inferential sidedness, alpha, or confidence-interval rule stated here: {concise(sap_alpha_hits[0])}", [concise(sap_alpha_hits[0])], sap_id, sap_alpha_hits[0], tracks=["confirmed_decisions"] )
    else:
        add("CORE-ALPHA-001", "critical", "Expose the inferential sidedness, alpha, and confidence-interval level as decisions requiring confirmation rather than inventing values.", ["needs confirmation"], protocol_id, protocol_uncertainty, "needs_confirmation", ["protocol_only", "confirmed_decisions"], "No inferential threshold was located in either source; the cited protocol passage anchors the study context, not an inferred threshold.")
    if sap_missing_hits:
        add("CORE-MISS-001", "critical", f"Apply the reference plan's missing-data rule and assumptions: {concise(sap_missing_hits[0])}", [concise(sap_missing_hits[0])], sap_id, sap_missing_hits[0], tracks=["confirmed_decisions"] )
    else:
        add("CORE-MISS-001", "critical", "Flag primary-outcome missing-data handling as unresolved; do not silently invent an imputation rule.", ["needs confirmation", "no invented imputation"], protocol_id, protocol_uncertainty, "needs_confirmation", ["protocol_only", "confirmed_decisions"], "No missing-data rule was located in either source; the cited protocol passage anchors the study context, not an inferred rule.")
    if sap_mult_hits:
        add("CORE-MULT-001", "critical", f"Apply the multiplicity policy or testing order stated in the reference plan: {concise(sap_mult_hits[0])}", [concise(sap_mult_hits[0])], sap_id, sap_mult_hits[0], tracks=["confirmed_decisions"] )
    else:
        add("CORE-MULT-001", "critical", "Flag multiplicity control across the outcome family as unresolved; do not claim adjustment or no adjustment without support.", ["needs confirmation", "no unsupported multiplicity claim"], protocol_id, protocol_uncertainty, "needs_confirmation", ["protocol_only", "confirmed_decisions"], "No multiplicity policy was located in either source; the cited protocol passage anchors the outcome context, not an inferred policy.")
    if sap_sensitivity_hits and len(rows) < 15:
        add("CORE-SENS-001", "major", f"Include the prespecified supportive or sensitivity analysis represented by this reference rule: {concise(sap_sensitivity_hits[0])}", [concise(sap_sensitivity_hits[0])], sap_id, sap_sensitivity_hits[0], tracks=["confirmed_decisions"] )
    if sap_safety_hits and len(rows) < 15:
        add("CORE-SAFE-001", "major", f"Use the safety population, periods, denominators, and categories indicated by the reference rule: {concise(sap_safety_hits[0])}", [concise(sap_safety_hits[0])], sap_id, sap_safety_hits[0], tracks=["confirmed_decisions"] )
    add("CORE-CONSIST-001", "critical", "Keep endpoint labels, treatment groups, visits, populations, and methods internally consistent across the generated SAP.", ["consistent endpoints", "consistent groups", "consistent visits", "consistent populations"], sap_id, sap_method, tracks=["confirmed_decisions"] )
    add("CORE-COVER-001", "major", "Provide traceable sections for design, endpoints, populations, primary methods, missing data, multiplicity, safety where applicable, and planned outputs.", ["design", "endpoints", "populations", "methods", "missing data", "multiplicity"], sap_id, first_hit(spages, [r"table of contents|statistical analysis plan|statistical plan|data analysis plan|analysis strategy"]), tracks=["confirmed_decisions"] )
    while len(rows) < 12:
        add("CORE-UNCERT-001", "major", "Separate protocol-supported facts from reference-only confirmed decisions and explicitly surface unresolved choices.", ["protocol-supported", "confirmed decision", "needs confirmation"], protocol_id, protocol_uncertainty, "needs_confirmation", ["protocol_only", "confirmed_decisions"], "The cited protocol passage anchors the study context; reference-only decisions remain excluded from the protocol-only track.")
    apply_manual_requirement_overrides(rows, nct, ppages, spages, protocol_id, sap_id)
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
    baseline_ncts = {nct for row in studies if (nct := nct_of_study(row))}
    overlap = baseline_ncts & set(SELECTED)
    if overlap:
        raise ValueError(f"SELECTED duplicates baseline study families: {sorted(overlap)}")
    for path in (BENCH / "gold").glob("PUBLIC-*"):
        if path.name not in baseline_ids:
            shutil.rmtree(path)
    for nct in SELECTED:
        candidate = CANDIDATES[nct]
        source = source_dir(nct)
        registry = json.loads((Path("/private/tmp/sapbench_candidate_registry") / f"{nct}.json").read_text())["protocolSection"]
        status = registry["statusModule"]
        start = status.get("startDateStruct", {})
        primary = status.get("primaryCompletionDateStruct", {})
        sap_date = parse_date(candidate["sap_document_date"])
        start_date = parse_date(start.get("date"))
        if start.get("type") != "ACTUAL":
            raise ValueError(f"{nct}: study start is not actual")
        if sap_date >= start_date:
            raise ValueError(f"{nct}: SAP does not strictly predate actual study start")
        if primary.get("type") != "ACTUAL" or sap_date >= parse_date(primary.get("date")):
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
    isolate_reference_only_requirements(studies, documents)
    dump_jsonl(BENCH / "manifests" / "studies.jsonl", studies)
    dump_jsonl(BENCH / "manifests" / "documents.jsonl", documents)
    dump_jsonl(BENCH / "final_audit" / "registry_chronology.jsonl", registry_rows)
    exclusions = [
        row for row in jsonl(BENCH / "manifests" / "exclusions.jsonl")
        if row.get("candidate_id") not in RETRACTED_REJECTIONS
    ]
    existing = {row.get("candidate_id") for row in exclusions}
    for nct, (status_name, reason) in REJECTED.items():
        if nct not in existing:
            exclusions.append({"candidate_id": nct, "reason": reason, "status": status_name})
    dump_jsonl(BENCH / "manifests" / "exclusions.jsonl", exclusions)
    print(json.dumps({"selected": len(SELECTED), "studies": len(studies), "documents": len(documents), "requirements": sum(len(jsonl(BENCH / 'gold' / row['study_id'] / 'requirements.jsonl')) for row in studies)}, indent=2))

if __name__ == "__main__":
    main()
