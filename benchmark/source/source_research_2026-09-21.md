# Public Source Research for SAP Benchmark Expansion

Date: 2026-09-21

## Outcome

The first expansion round registered four public study families in addition to the existing private pilot. Two families now have evidence-backed draft annotations, and two high-complexity families are queued for annotation.

Raw public PDFs are deliberately not committed. The document manifest records stable URLs, internal versions and dates, byte-level SHA-256 hashes, and intended cache paths. Model-visible protocol/CRF files and reference SAPs are physically separated into `input/` and `reference/` directories. This avoids silently assuming redistribution rights while preserving reproducibility and reducing leakage risk.

## Source strategy

### ClinicalTrials.gov

ClinicalTrials.gov is the main source for randomized-trial protocol/SAP pairs. Its study-document metadata distinguishes protocol and SAP documents and provides stable NCT identifiers, dates, filenames, and download URLs. The benchmark still verifies the version cited inside the SAP because registry-level presence alone does not prove that the two uploaded files form the governing pair.

Recommended use:

- primary `protocol_only` benchmark source;
- clean protocol/SAP pairs with separate files;
- stratified selection by design and endpoint type;
- URLs and hashes in a release, with raw PDFs fetched by the user.

Do not use a combined `Prot_SAP` PDF directly as protocol-only input. It leaks the reference answer unless the protocol pages can be isolated deterministically and the split artifact is documented.

### Public trial websites

Study websites can supply CRFs that ClinicalTrials.gov does not accept as a standard study-document type. IMPACT is currently the strongest example: its TSAP explicitly names Clinical Study Protocol v2.0 dated 2020-09-24 and CRF v1.4 dated 2021-10-21, and all three files are public.

Recommended use:

- `protocol_only` versus `protocol_crf` paired comparison;
- CRF field-availability and visit-mapping requirements;
- testing whether a model distinguishes an observed exposure from randomized treatment.

IMPACT is observational, so it belongs in an auxiliary set rather than the primary randomized-trial score.

### CDISC synthetic packages

The CDISC SDTM/ADaM pilot and derivative eSubmission packages are useful for pipeline tests because they include synthetic data, CRFs, metadata, and outputs. They should remain development-only:

- the original CDISC terms require attribution and impose redistribution conditions;
- derivative repositories may contain newly authored protocol/SAP material rather than contemporaneous source documents;
- a synthetic package does not count as an independent real-world study family.

### EMA clinical data publication

EMA clinical-study-report packages are the best phase-two source for realistic protocol/SAP/CRF triplets. Published research reports that many trial packages contain all three document types. The trade-off is high retrieval, redaction, matching, and extraction cost, often across hundreds or thousands of pages.

## Registered families

| Study | Documents | Benchmark role | Main statistical coverage | Current decision |
|---|---|---|---|---|
| VIVID, NCT02819973 | protocol + SAP | primary-track candidate | binary endpoint, three arms collapsed to one contrast, change from co-primary to single primary | annotated draft |
| IMPACT, NCT04103723 | protocol + CRF + TSAP | auxiliary paired-track candidate | observational exposure, continuous endpoint, interactions, CRF field mapping | annotated draft |
| ASCEND-D, NCT02879305 | protocol + SAP | high-difficulty primary candidate | two co-primary non-inferiority endpoints, time-to-event MACE, gatekeeping, multiplicity, estimands | version verified; annotation queued |
| SER-287, NCT02618187 | protocol + SAP | missing-information challenge | phase 1b, multiple arms, safety/efficacy populations, several missing-data strategies | version verified; annotation queued |

## Important screening decisions

### NIS, NCT03347929: hold

The public protocol is v2.5 dated 2022-01-20. SAP v2 dated 2023-09-15 identifies protocol v2.6. The pair must not be promoted to gold until protocol v2.6 is obtained. This is exactly the kind of silent mismatch the benchmark should detect.

### Upadacitinib, NCT03104400: hold

The visible protocol upload is dated after the SAP. The correct governing amendment must be found before annotation.

### Combined protocol/SAP uploads: exclude by default

Combined documents are convenient for browsing but unsafe for a protocol-only task. Page-level splitting is permitted only if the protocol and SAP regions are unambiguous, the split procedure is reproducible, and the resulting protocol artifact contains no SAP-only content.

## Selection targets for the next round

Promote six more independent randomized study families so the registered set reaches 10-15. Preserve the following design coverage:

- binary: VIVID plus one confirmatory drug or device trial;
- continuous/repeated measures: AMPLIFY or a version-matched NIS pair;
- time to event: ASCEND-D plus an oncology progression-free-survival trial;
- non-inferiority: ASCEND-D plus one device trial;
- crossover: RESTORE or the pediatric dasiglucagon trial;
- multiplicity: ASCEND-D, AMPLIFY, or upadacitinib after version reconciliation;
- protocol+CRF: IMPACT now, followed by one interventional triplet from an EMA package.

## Annotation rule

Reference SAP text is used only to discover decisions and discrepancies. A requirement is marked `explicit` or `derivable` only when the model-visible protocol or CRF supports it. SAP-only choices become `needs_confirmation` or `proposed`; they are never converted into hidden facts the model was expected to guess.
