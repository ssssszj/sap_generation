# Changelog

## 0.3-development - 2026-09-23

- Set a 120-family release-eligible intake target, excluding the private pilot, with at least 100 retained families.
- Defined a 40/20/40 split at the 100-family floor and a 60/20/40 stretch split if all 120 eligible families pass.
- Expanded the acquisition catalog from seven study candidates to 116, yielding 120 eligible registered-plus-screened study families across 17 broad domains.
- Added a reproducible ClinicalTrials.gov API harvester that rejects combined protocol/SAP-only uploads and keeps all new records at metadata-screened status.
- Added a machine-readable pool summary and a 24-study document-level promotion queue.
- Separated the EMA document source pool from the study-question candidate catalog.
- Documented maturity layers, attrition allowance, subgroup limitations, and the tiered annotation budget.
- Added 18 first-pass requirements for SER-287, including protocol/SAP discrepancies around mITT and clinical-remission definitions.
- Added 22 first-pass requirements for ASCEND-D covering co-primary non-inferiority, estimands, ITT/PP/safety populations, Cox and ANCOVA analyses, missing data, gatekeeping, and Holm-Bonferroni multiplicity.
- Increased the registered-study requirement total from 56 to 96 and marked both new sets for independent expert review.
- Promoted NCT04172441 after verifying that SAP final v3.0 cites protocol ZP4207-17103 final v13.0/v14.0 dated 2021-06-04; added 22 crossover-study requirements.
- Promoted NCT00113074 after matching the protocol and Data Analytic Plan by NCT, title, and approval date; added 23 requirements covering the abstinence-conditioned population, ANCOVA, Fisher LSD, relapse, and missing-outcome uncertainty.
- Reduced the remaining metadata-screened pool from 116 to 114 while preserving the 120-family release intake, and increased the registered-study requirement total from 96 to 141.
- Placed NCT05133739 on a public-redaction hold because the available files obscure the protocol identifier and portions of the primary-analysis formula.
- Promoted NCT02513121, NCT02542410, and NCT02664415 after exact title/date or protocol-version matching; added 45 evidence-backed requirements across pediatric dietary intervention, endometriosis pilot, and HIV analytic-treatment-interruption designs.
- Excluded NCT03902392 because its uploads are a completed-study manuscript and retrospective statistics note, and excluded NCT03282916 because the protocol upload embeds the full reference SAP and would leak the target.
- Kept NCT00787722 on version-reconciliation hold because its concise SAP does not identify the governing internal protocol version.
- Added exclusion-aware candidate-pool refresh, replenished invalid candidates from the official registry API, and preserved the 120-family intake with nine registered public drafts plus 111 screened candidates.
- Increased the registered-study requirement total from 141 to 186.

## 0.2-development - 2026-09-21

- Registered four version-verified public study families: VIVID, IMPACT, SER-287, and ASCEND-D.
- Added 30 first-pass evidence-backed requirements for VIVID and IMPACT.
- Added an eight-entry screened candidate catalog covering device non-inferiority, crossover, repeated-measures, oncology time-to-event, and multiplicity cases.
- Added an explicit `candidate` split so unsplit studies cannot be confused with frozen train/dev/test data.
- Added remote-only public-document handling and SHA-256 verification support.
- Recorded NIS and upadacitinib as version-review holds rather than silently pairing mismatched documents.
- Documented source selection, redistribution, and combined protocol/SAP leakage policies.

## 0.1-pilot - 2026-09-11

- Created the benchmark specification, schemas, core rubric, ophthalmology extension, pilot manifests, and initial IOL annotations.
- Registered the existing Chinese ophthalmology study as `pilot_only` and permanently excluded it from future frozen test splits.
