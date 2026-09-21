# Changelog

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
