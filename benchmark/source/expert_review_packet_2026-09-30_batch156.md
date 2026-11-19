# Expert Review Packet: Batch 156

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 156 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 1,679 physical pages in the 16 selected PDFs. A total of 110 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03613649 — exclude: the selected Protocol Version 4.0 is prospective, but physical pages 74-79 disclose the hypotheses, power assumptions, analysis populations, linear mixed model, 18 one-sided confidence intervals, decision threshold, assay-sensitivity rule and concentration-QTcF program. The appended final ECG SAP is dated 2018-09-18 and explicitly says it is based on Protocol Version 1.0 dated 2018-06-18 rather than the selected Version 4.0, so the otherwise prospective target also lacks a reconciled governing-version chain.
- NCT04707313 — exclude: SAP Version 2.0 is dated 2023-10-25, after actual study completion on 2023-10-11, and its version history says updates were based on ongoing blinded review of tables. The SAP and Protocol Amendment 2 also incorporate newly added Cohort 3 and its separate 32-week estimand/analysis. The protocol independently exposes the MMRM, fixed effects, covariance, missingness, confidence interval, Cohort 3 sample size and annual unblinded interim machinery.
- NCT05724199 — exclude: the public target is SAP Amendment 1 (v2.0), dated 2024-09-27 after actual primary completion on 2024-09-15. Its version history adds/changes endpoints, race/ethnicity subgroups, diary rules, supportive estimand imputation and the US submission's coprimary endpoint ordering after FDA advice. Although original SAP v1.0 is listed as 2024-01-24, that document is not the selected public target. Protocol Amendment 5 already exposes the populations, covariates, estimands, analysis timing, missing-data strategies and principal efficacy methods.
- NCT03239483 — exclude: SAP Version 1.0 is dated 2019-01-03, after actual primary/study completion on 2018-09-20, and the public approval page has blank signatures/dates. It also says a safety monitoring review occurred on 2018-05-14 and writes retrospective study-conduct facts. Protocol Version 2.0 already exposes the endpoints, sample size/power, blinding, monitoring, populations, exact-binomial/Fisher analyses and PK summaries.
- NCT04203537 — exclude: SAP v3.0 was signed 2020-11-12/13, after actual primary/study completion on 2020-10-26. Its version history says v2.0 followed blinded TLF review and v3.0 updated the per-protocol population before lock/unblinding; it also incorporates COVID deviations and pools realized Part A/Part B cohorts. The SAP's repeated page headers incorrectly display 12NOV2010, adding an internal date defect.
- NCT03238781 — exclude: SAP Amendment v2.0 is dated 2018-10-31, after actual primary completion on 2018-10-16. It specifies up to five independent unblinded interim analyses after about 50% reach Week 12, using interim primary effect sizes for future study planning, with individual assignments available to an internal unblinded team. The selected target is post-primary and interim-informed.
- NCT01970865 — exclude: the selected protocol is Amendment 8 dated 2019-01-23, after actual primary completion on 2017-03-15, while SAP v6.0 is dated 2019-03-15 and says it is based on Amendment 6 dated 2016-07-15. The SAP nevertheless says v6 was updated to Amendment 8 and records that central radiology review stopped because endpoint data were sufficient. Its version history incorporates FDA feedback, ongoing Phase 2 changes, dose/response-informed development, revised pooling/sample sizes and an EXP-6 interim futility program.
- NCT03710564 — exclude: SAP Amendment 4.0 was released 2021-04-30, after actual primary completion on 2020-12-21. It adds COVID-exposure sensitivity analyses and protocol-deviation handling, identifies Week 52 as the primary interim analysis/unmasking point, and uses the current observed dropout rate to increase randomized sample size from 513 to 533. The target is post-primary and explicitly observed-conduct-informed.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03613649 | protocol leakage plus governing-version mismatch | 111 / 175 | `d0add2304ede0c08d27078690cbb5b9b4da1e41896a81f50b2d109ef8930330c` | `d12ac5f809b3957979aa82cef39c9929585ac862b5f329dbe70934ddca9d4637` |
| NCT04707313 | post-completion/blinded-review/interim-informed plus leakage | 135 / 61 | `32d255478ee4ef6782e32d2bcfad47e54f21c5409fe9a44a0c1f18af1516e10a` | `59c4dd41df1a46ac02350ac577f0edc831deefaac209a1aa0ddc2e0d9381b0e8` |
| NCT05724199 | post-primary regulatory/analysis revision plus leakage | 162 / 70 | `f222fc7ce846da04136929f27b38bf79d17924bb6e48d8742c8135a7f019eb81` | `bd730cbe216864416193cf0d605cac2011ece06a1e405c71bf7de815e5925d3e` |
| NCT03239483 | post-completion and monitoring-informed plus leakage | 115 / 14 | `823a4d02d0eca592071aa4fabf7137e942af3157dfff52a0bfefdd716d0d1438` | `2d51eaecf7c2fc04b4f5048fef3e634621c99dee243870df5165e97d8f062c43` |
| NCT04203537 | post-completion/blinded-TLF/COVID-informed target | 135 / 70 | `56d0b3eec9326f67dad5d3078e780722b35324fee04c5880b3d01ed8ebaeaed5` | `e4737dc94b3bc2a5970df6e00725e03ae2cd58cb94a21f3c5a3123f00c24c662` |
| NCT03238781 | post-primary unblinded-interim-informed target | 132 / 82 | `5e7e3486c6a6f98e255109f12b12416f1ac43b2786971de06eee868d11ddb47a` | `e47283593915a8c4fbfe936fb3e4083c2c8129f5421514c1867297113dadd1e9` |
| NCT01970865 | post-primary version mismatch and accumulated-conduct target | 208 / 89 | `3d804930163bab89b6812b7c410d23e27887917d0b4142b9c0b0e3b97661bade` | `23f6ad0bdd4ffd50a1134a4e07929ef210b22b40f4bdefe81f88257d6366154b` |
| NCT03710564 | post-primary observed-dropout/COVID-informed target | 71 / 49 | `134e928aefe6aa91757236223d7b6cd89fc4c7ecfc32e3410402dd9028f1906e` | `38d19b27f702e185b03055d291c0530d0cf6ebbd2d2dd1df576e790f2ac09b52` |

## Gate interpretation

- A prospective sub-plan does not become a valid target when it explicitly cites a superseded protocol and the public package supplies no reconciliation to the selected governing version.
- Blinded aggregate review can still make a late target execution-informed when it changes tables, populations, endpoints or cohort reporting.
- A late amendment cannot stand in for an earlier version merely because its version history lists that earlier plan; the actual selected artifact and its changes govern screening.
- Post-primary regulatory advice that changes coprimary endpoint ordering, estimands or sensitivity analyses is not a clean prospective target.
- An unblinded interim team separated from the operational study team still makes the resulting target interim-informed when effect sizes support future development decisions.
- A sample-size update calculated from observed study dropout is execution-informed even when treatment masking remains intact.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
