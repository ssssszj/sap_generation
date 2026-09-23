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
- Promoted NCT00738894 REDUCE and NCT05352893 imsidolimab after exact protocol/SAP identity and date matching; added 35 evidence-backed requirements for device co-primary testing and Phase 3 estimand/multiplicity/MI evaluation.
- Excluded NCT02348775 as a retrospective post-study summary rather than a prospective protocol/SAP pair.
- Put NCT03734588 on hold for an internal governing-protocol date conflict and formalized the existing public-redaction hold for NCT05133739.
- Refreshed and replenished the candidate pool to 109, preserving 120 release-intake families, and increased the registered requirement total from 186 to 221.
- Promoted NCT04925570 Anchor/W-SUDs after exact title, NCT, and date matching; added 14 requirements for digital-intervention outcomes, retention weighting, item-level missingness, and adherence-defined sensitivity analysis.
- Promoted NCT04270682 RESTORE after verifying that SAP v2.0 cites protocol Amendment 6 dated 2023-04-04; added 18 requirements for rare-disease crossover analysis, rescue handling, Holm-Bonferroni testing, MAR multiple imputation, and separate pediatric analyses.
- Refreshed the candidate pool to 107, preserving 120 release-intake families, and increased the registered requirement total from 221 to 253.
- Promoted NCT02600637 after exact title, NCT, and date matching; added 17 requirements that preserve the pilot's descriptive analysis and separate it from an illustrative future-efficacy mixed model.
- Promoted NCT03603509 after matching protocol Version 7 and the SAP by exact title, NCT, and 2019-05-19 date; added 15 requirements for HAI change, Wilcoxon comparison, laboratory blocking, CQN normalization, and exploratory transcriptomic analyses.
- Excluded NCT03856047, NCT05025345, NCT02176018, and NCT04707014 for protocol-embedded SAP leakage, and excluded NCT03556293 and NCT04697836 as retrospective analysis summaries rather than prospective protocol/SAP pairs.
- Put NCT02796677, NCT02407054, NCT02301897, and NCT00928447 on version-reconciliation hold, and NCT02173379 on public-redaction hold; holds remain outside the review queue.
- Refreshed and replenished the candidate pool to 105, preserving 120 release-intake families, and increased the registered requirement total from 253 to 285.
- Removed held studies from the actionable candidate-count denominator, replenished all ten held slots, recorded the two legacy version holds in the decision manifest, and added validator checks preventing held or non-screened records from re-entering the candidate catalog.
- Promoted NCT02341417 after verifying SAP v2.0 against the complete protocol Amendment 3 and a later superseding amendment restricted to administrative/typographical safety-threshold corrections; added 23 requirements for descriptive safety incidence, analysis sets, iPTH derivations, IPW and repeated-measures sensitivity analyses, growth, and combined parent-study summaries.
- Excluded NCT01682356, NCT03955055, and NCT02075437 for wrong document type, and NCT00116337 and NCT03342027 for protocol-embedded analysis leakage.
- Put NCT02279173 on version-reconciliation hold because its complete governing original protocol is absent, and NCT04435600 on public-redaction hold because material treatment doses are obscured.
- Refreshed and replenished the candidate pool to 104, preserving 120 release-intake families, and increased the registered requirement total from 285 to 308.
- Promoted NCT02563522 after exact Protocol Version I/SAP Version E matching and added 21 requirements for the early-terminated Engensis diabetic-foot-ulcer trial.
- Promoted NCT02657564 as an auxiliary observational safety case after exact title/NCT/date matching and added 16 requirements that preserve unresolved population, reversibility, repeated-measure, missing-data, and multiplicity decisions.
- Excluded NCT02866669, NCT05464914, and NCT03634488 as wrong document types; excluded NCT03435783 and NCT02015455 for protocol-embedded target leakage; and put NCT05540665 on version-reconciliation hold.
- Refreshed and replenished the candidate pool to 102, preserving 120 release-intake families, and increased the registered requirement total from 308 to 345.

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
