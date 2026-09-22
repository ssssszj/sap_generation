# Changelog

## 0.3-development - 2026-09-22

- Set a 120-family release-eligible intake target, excluding the private pilot, with at least 100 retained families.
- Defined a 40/20/40 split at the 100-family floor and a 60/20/40 stretch split if all 120 eligible families pass.
- Expanded the acquisition catalog from seven study candidates to 116, yielding 120 eligible registered-plus-screened study families across 17 broad domains.
- Added a reproducible ClinicalTrials.gov API harvester that rejects combined protocol/SAP-only uploads and keeps all new records at metadata-screened status.
- Added a machine-readable pool summary and a 24-study document-level promotion queue.
- Separated the EMA document source pool from the study-question candidate catalog.
- Documented maturity layers, attrition allowance, subgroup limitations, and the tiered annotation budget.

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
