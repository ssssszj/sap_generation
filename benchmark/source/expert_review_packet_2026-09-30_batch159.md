# Expert Review Packet: Batch 159

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 159 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 1,005 physical pages in the 16 selected PDFs. Full-page OCR was also performed on the 97-page scan-only NCT03507790 protocol and the 22-page scan-only NCT03702608 SAP. A total of 87 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03702608 — exclude: Protocol Version 1.1 physical pages 41-43 already specify the sample-size/power basis, descriptive summaries, FAS/PP/safety populations, exact-binomial primary analysis, sensitivity MI definitions, secondary analyses, no multiplicity adjustment, no interim analysis, no subgroup analysis and no imputation. SAP Version 1.0 physical pages 8-13 substantially repeats that executable program and adds only refinements such as tipping-point and time-to-event details. The target is substantially reconstructable from the model-visible protocol.
- NCT04828785 — exclude: SAP physical page 1 says it was first created on 2025-06-27 to reflect analytic decisions made from enrollment and retention data. Physical page 4 explicitly responds to greater-than-anticipated missing follow-up data by making 100-dataset chained-equation multiple imputation the primary inference. The target is realized-enrollment/retention-informed even though it precedes actual primary completion.
- NCT05879718 — exclude: SAP Version 3 is dated 2025-11-25 and approved 2025-12-02, after actual primary completion on 2025-06-05 and actual study completion on 2025-11-18. Physical pages 5-8 record early termination based on a business decision, only 8/48 enrolled, only one SLE participant and analysis changes caused by those realized counts, including treatment-received summaries, removal of subgroup and time-to-event analyses, and descriptive-only efficacy outputs. The target is post-completion, termination- and realized-sample-informed.
- NCT03343626 — exclude: SAP Version 2.0 dated 2019-04-26 follows actual primary completion on 2018-12-28. Its governing Protocol Amendment 3 and the SAP specify interim immunogenicity/safety and dose-selection analyses; physical pages 37-38 state that unblinded statisticians will produce the analyses and that the sponsor study team will receive group-level unblinded results while subsequent conduct continues. The selected amended target is post-primary and sits after planned access to accumulated unblinded study evidence.
- NCT04482582 — exclude: Protocol dated 2023-09-27 physical page 3 says the ITT amendment was requested because weekend procedure scheduling affected enrollment and patients could not tolerate prone positioning. SAP revised 2023-09-28 physical page 3 says the ITT strategy was added to address high intervention-arm screen-failure rates. Both revisions occurred during conduct and encode realized operational and enrollment experience.
- NCT03507790 — exclude: SAP Final Version 2.0 dated 2024-05-23 is only six days before actual primary/study completion on 2024-05-29, after an unblinded interim of the first 24 participants and years of conduct. Physical pages 3-4 and 36-37 add the Completers/PK populations, remove the per-protocol population, expand final-analysis biomarker/subgroup work, and document an actual database derivation error discovered before lock. Protocol Version 6 also defines post-October-2021 Part C and COVID/dropout replacement. The target is accumulated-conduct-, interim- and database-informed.
- NCT02028455 — exclude: The 2021-02-09 SAP explicitly governs Phase II after Phase I and Cohort 2E analyses had already been performed. Physical pages 8-9 use completed Phase I selection of the recommended Phase II dose and the realized 27 SCRI-CAR19v2 products to define scope and exclusions. The 2020-06-04 protocol itself reports observed Phase I DLTs, response/persistence evidence and the resulting Phase II decision rule. The target is outcome-informed and inseparable from accumulated study-family conduct.
- NCT03791619 — exclude: Protocol Version 5 physical pages 44-47 already specifies the primary population, missing-data supportive analyses, two primary endpoints, confidence-interval reporting, descriptive secondary analyses, cylinder formula, interim reporting framework and 240-per-group/634-enrolled sample-size assumptions. SAP Version 1.0 physical pages 4-8 substantially repeats the same executable program, including redacted material in corresponding locations. The target is substantially reconstructable from the model-visible protocol.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03702608 | protocol leakage | 72 / 22 | `25858b066aa3b570f89e3d3b5d8daef6fb6b31b14970a0e0c2fa2913bb22a7c7` | `3f051bb85be8c8ed0e4be9ce1b826cbb49bfe2b053f1aae17420a37acb36c05e` |
| NCT04828785 | realized-enrollment/retention target | 98 / 13 | `2f49c1edc43f440385010927c546d90b039ff06443c022befa6ed86d65f23644` | `2f67bee88b03d54d89d896dcb47cbbc535c3b7f1f317cbf12fdf12f4b723144b` |
| NCT05879718 | post-completion early-termination target | 155 / 27 | `6c6e55dc5d55d7ceb689fa66205da452827a7923314d83635696e72f090b90fe` | `bf3fa78b3da7e2559b09b6be2c2422f0479c9e2d6527a72ae26281f6e974b5a9` |
| NCT03343626 | post-primary unblinded-interim target | 110 / 55 | `3ee43e5077e1f9be997b3210f36d7bdb86ebbd9fc2b91d13240fd627db595be7` | `1b64fd21b35905412cf7530b1d5476523acb066dbbfa4d5c354dce12217e7c43` |
| NCT04482582 | realized-operational/enrollment target | 11 / 4 | `b51ed93df0f63d43eca66583a67fd9e388896bdafe30cc1e6064f3bffef930ec` | `5ba8f6e9747213dae32562eef3a6bd6a7d0f5bada4f17b95e69cceed7bf0fb4a` |
| NCT03507790 | interim/database/conduct-informed target | 97 / 38 | `5dbd31947cb463550453da084948400e2dada765d8c15231d178a02c6aedf4f9` | `5c45667752ca61c9c35f7cf8ea9268599a260b12bfffd5e76059d6a8ae020feb` |
| NCT02028455 | completed-phase outcome-informed target | 107 / 20 | `86a35a140afd53c920c4c7b42a9ee093c3b377ac0bcff00d8bc28a663c96c25f` | `a4492f71fd26d6e57dee173a0e12ffd2f864a18421c38cf50d9fb3be29385dc3` |
| NCT03791619 | protocol leakage | 62 / 14 | `f8ef0b59466ce93a676c2e8d7f589ce380c6a38c68f12844ae2c64a38841e6b7` | `d3f3290bbf45797ea961c78a53720244758e737f3cebdc868c16979b2812d954` |

## Gate interpretation

- A plan created before primary completion is still execution-informed when it explicitly reacts to realized missingness, retention, screen failures or operational barriers.
- A post-primary amendment is not rescued by a statement that its changes merely clarify the protocol when planned unblinded interim outputs were available to the sponsor during continuing conduct.
- A final plan only days before completion is not outcome-uninformed when it follows an unblinded interim and records actual database errors, population changes and final-analysis additions.
- An adaptive phase 1/2 target is outcome-informed when the selected phase, dose, decision rule or excluded cohort is defined from already completed analyses and observed outcomes in the same study family.
- Protocol leakage is assessed by substantive reconstructability across populations, endpoints, models, missingness, sensitivity analyses, thresholds and sample-size logic, not by verbatim duplication or the mere presence of an endpoint and sample size.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
