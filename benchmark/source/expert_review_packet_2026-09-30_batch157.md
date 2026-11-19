# Expert Review Packet: Batch 157

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 157 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 960 physical pages in the 16 selected PDFs, with full-page OCR used for the scan-only SAPs for NCT03266588, NCT03739593 and NCT04204083. A total of 92 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03639675 — exclude: Protocol Version 1.0 physical pages 39-43 already specify the PPS/FAS/SAF populations, primary and secondary endpoints, one-sample t test, 95% confidence interval and success threshold, Clopper-Pearson interval, LOCF, subgroup analyses, and sample-size/effect assumptions. SAP Version 1.0 physical pages 5, 7-8 and 10 substantially repeat that executable program, so the model-visible protocol can reconstruct the target analysis.
- NCT04731142 — exclude: SAP Version 0.2 is dated 2022-07-11, after actual primary completion on 2022-06-30. Physical page 23 explicitly removes the time-in-range benchmark pending a suitable reference and says it may be added post hoc; the approval signatures are blank. The selected target is post-primary and cannot be defended as an outcome-uninformed prospective plan.
- NCT05732454 — exclude: Protocol Amendment 2 physical pages 126-130 disclose the estimands and intercurrent-event strategies, analysis sets, CMH primary analysis, JTC Bayesian MMRM/multiple-imputation program, ANCOVA, absence of multiplicity adjustment, unblinded interim analysis and sample-size precision. SAP Version 2 physical pages 6-9 and 39 substantially reuse the same program and add an earlier unblinded interim, making the target reconstructable from the protocol.
- NCT03248882 — exclude: SAP Amendment 1 Version 2.0 is dated 2019-03-14, after actual primary completion on 2019-02-26. Its version history records an erroneous randomization-stratum instance, the realized Taiwan sample of six, actual clinical-database and oral-dosing-CRF structures, and an added plot for extreme post-randomization safety observations. Together with an unblinded interim based on observed safety and variability, the selected target is post-primary and observed-conduct-informed.
- NCT04204083 — exclude: SAP Version 2.0 is dated 2021-03-04 and signed 2021-03-09, after actual primary completion on 2021-02-26. It combines MON 18-01, MON 18-02 and MON 18-03, whereas the registry candidate is MON 18-01. The selected artifact is both post-primary and not a clean one-target study-family plan.
- NCT03266588 — exclude: the selected Protocol Version 5 is dated 2018-06-22, but SAP Version 6 is dated 2019-07-29, after actual primary/study completion on 2019-07-15, and explicitly cites unselected Protocol Version 6 dated 2018-12-20. Its version history uses realized conduct by reopening enrollment for about 20 CGRP-biologic users, defining a subgroup from actual dosing behavior, revising compliance around the clinical database and oral-dosing CRF, and deleting low-frequency adverse-event output. The target is post-completion, conduct-informed and governing-version-mismatched.
- NCT01997333 — exclude: Protocol Amendment 4 physical pages 51-53 already provide the PFS event/censoring rules, ITT/PP/safety populations, Kaplan-Meier analysis, stratified log-rank and Cox models, ORR CMH analysis, DOR/OS methods, and sample-size/event/effect assumptions. These provisions substantially reconstruct the target program; SAP Version 1.1 dated 2017-08-31 merely records an ORR-denominator change to baseline measurable disease.
- NCT03739593 — exclude: SAP Version 2 is dated 2020-06-10, after actual primary completion on 2020-05-14. It adds COVID-19 deviation and AE/SAE listings, and specifies an interim review after the first 20 randomized-period subjects complete Month 6 that examines safety, tolerability and efficacy to plan future studies, alongside multiple changes from the protocol. The selected target is post-primary and interim/COVID-informed.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03639675 | protocol leakage | 51 / 15 | `1134a038c7ca078a185d3960b02acd604dce672a65338ba9d34a5d965e028f0c` | `d40dba924ec93f16a7c419ca359c3d5be041adffd8e28ce7f0dc4c1f2ad01b3b` |
| NCT04731142 | post-primary/post-hoc-informed target | 28 / 27 | `ae676add2b2438c0fb4cd5a73fbaee46542df740c999c4a6779bda37758c7c18` | `a5cf476d2d67721e9439c154e1737b782fd54a152200ecce0078ee19bdcd6e72` |
| NCT05732454 | protocol leakage plus unblinded interim | 181 / 52 | `72d143a8c12451ff8ec7fd96fdb699b2a5588d2c6a720ee7a8b0607b1a2914cf` | `e4dc108642076f2ff75d058432e221d85a2962f0dbfb671f0d5611f466bddab1` |
| NCT03248882 | post-primary observed-conduct/unblinded-interim target | 103 / 83 | `49b4659da5987c936693eba364cba3c7b28ae33e34692286c8acbbdef13bb8b8` | `eb23651d2ab72c6938a0e472846c39866a26fa80f4f65e72f58dcf0769ebe8e0` |
| NCT04204083 | post-primary combined-study-family target | 39 / 12 | `301e522178d3e8f518890888ba9c88be53403fe20fdbf60da662951b4bb6dc5d` | `242fe7bb532395fd4d6539c57766bfce1e20754f367f7908b4853252d686c8f8` |
| NCT03266588 | post-completion conduct-informed version mismatch | 103 / 51 | `61749c6019d5ed259dc6d355ae161ced674fc068f65832cfe8568d994f807aef` | `28c658762da4a0f89da0d2bcf9b0cc6550df24cdc5bc1861dba8a334183131dc` |
| NCT01997333 | protocol leakage | 86 / 40 | `79d73b6db30be0a6ce5f4e0d25621061a61415dbe360a646c8180164557091ca` | `bb7a9844ca264bfe511379b386a90a0b951970558d2982ce46f9e5054d82e8ac` |
| NCT03739593 | post-primary interim/COVID-informed target | 59 / 30 | `4593a52c47655513031b3778f17490094d6858b6058b1b0f5c48f4978a2e4810` | `b82e8607978997629fe755fa8c2bdf289b0bffce0a219262cacdd6618aaf3e95` |

## Gate interpretation

- A protocol is disqualifying when it exposes enough populations, endpoint rules, estimands, tests, missing-data handling and decision thresholds to substantially reconstruct the target; a protocol need not be a verbatim SAP duplicate.
- A target dated after actual primary completion is not rescued by blank signatures or by being labeled a plan, especially when its own text documents a post-hoc change.
- Blinded operational facts, realized strata, country counts, CRF/database structures and observed safety or variability are execution information when they change the target plan.
- An analysis plan combining multiple protocols is not a clean target for a candidate registered under only one member of that study family.
- A later SAP that cites an unselected later protocol cannot be paired to an earlier selected protocol without a complete, reconciled governing-version chain.
- COVID-19 adaptations and interim efficacy reviews used for future-study planning make a target execution-informed even without final treatment unblinding.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
