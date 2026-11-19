# Expert Review Packet - Batch 93

## Scope and decision boundary

Batch 93 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally and page-extracted, and decisive identity, chronology, leakage and execution-stage pages were rendered and visually inspected. Two families are promoted as first-pass annotation drafts and six are excluded. The six open slots are replenished so the intake remains 120 public families.

## Promotions

- `NCT05473767` -> `PUBLIC-ENRICH-FCU-HEART-001`. The four-page protocol and independent two-page Data Analysis Plan share the exact ENRICH title and 2022-04-05 date and predate the 2022-11-18 study start. The model-visible protocol describes the arms, cardiovascular and implementation measures and six-month assessment but does not expose the reference-only 100:50 target, t-based 95% confidence interval, race-stratum repetition, power assumptions or analyzed-as-randomized rule. Twenty evidence-backed requirements were added. The post-completion upload of nominally pre-start documents, registry-versus-plan endpoint hierarchy, masking, race-stratum role, estimands, missingness and multiplicity remain explicit expert-review gates.
- `NCT05472740` -> `PUBLIC-TENS-EMB-001`. The three-page protocol and independent one-page plan share the exact title, Duke identifier, Version 1.9 and 2023-08-23 date and predate 2023-12-26 completion. The protocol exposes the 160 target, VAS timepoints and broad between-arm intent but not the reference-only 15-mm difference, SD 30, 64-per-arm power result or baseline-adjusted linear regression. Twenty-one evidence-backed requirements were added. The during-study Version 1.9 provenance, unexplained baseline-pain covariate, population, estimand, missingness and multiplicity remain explicit expert-review gates.

## Exclusions

- `NCT02798120` — protocol leakage. Protocol pages 37-39 expose the safety population, TEAE definitions and summaries, exposure windows, tolerability, efficacy summaries and target.
- `NCT02964247` — protocol leakage. Protocol pages 67-78 expose estimands, analysis sets, sample size, hierarchical testing, ANCOVA, MI, MMRM, placebo MI and tipping-point analyses.
- `NCT03123120` — interim-informed plan. SAP v3 records actual screening cessation, randomized and completed counts, interim availability, cutoff and an early project decision; the protocol also exposes extensive executable methods.
- `NCT03369444` — post-completion plan. SAP v1.2 follows actual termination/completion, while protocol pages 86-88 expose analysis sets, response endpoints and sensitivity, safety and FIX analyses.
- `NCT02725515` — protocol leakage. Protocol pages 90-95 expose populations, power, Fisher exact testing, exact intervals, Kaplan-Meier/log-rank, safety, PK/PD and interim methods.
- `NCT06925620` — invalid retrospective source chain. The files claim a 2022 date but print an NCT identifier not submitted or posted until 2025, after 2022 completion, and were uploaded in 2025.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT05473767 | promoted draft | 4 / 2 | f11cd236f85f656fd0e385d53ad5b7e90ab5ad63077365646f92818a1aa275a8 | 7c88c5468081a87033704a6493f7d4c37880a6594195a1a81beb771f81304098 |
| NCT02798120 | protocol leakage | 47 / 62 | 318e1f72b8d33e7757729871feb99eeffbfafc96abe919562352b83f2a2daac6 | 74914ccc55ffaeb8c18f45f99aee99feb1793346b3ef1d9cf41f59aa56fd0585 |
| NCT02964247 | protocol leakage | 112 / 24 | 21e4192269bdace05ef8d971956cfe5fe9372ef8589979b31c96c217b9f1bf93 | 72c4032dbb21b18119d82281edbbf8ca055c64802ce8beb10002fc4da561211a |
| NCT03123120 | interim-informed plan | 104 / 67 | af407c0c694f0a5b91e79f755a385407eb6f6b43dff070772343c2ccf1105a06 | 228d1420b955a0b8b9f1566fbfd56d25048bc63f79e75afe716f1b537518292e |
| NCT03369444 | post-completion plan | 119 / 81 | 874711c6d22fed5404c71867b77f736438575cc5d5ee599e2ba2bd4178a48a1e | eb9d7edfa9648d038803216931a23e85f885cd20d826aab3660b2b1758cd4d5e |
| NCT02725515 | protocol leakage | 132 / 32 | 3047a0903c6d90b6e49da65ef828df2802ef10985bd9921bcabb4726217a52f9 | 97cb1fe9d79da73c4a1b93cdcf088428cc6609a75eaec6df01c9893449deba6e |
| NCT06925620 | invalid post-completion source chain | 2 / 2 | a23f4a12d7e03a59370f5b19e676ea0660c095f955f14145c4a6a39884d1b792 | ab7a5f506b75e8c5118f09ec85c59ad0b2341f9525973883cdbee1798fe80e2f |
| NCT05472740 | promoted draft | 3 / 1 | 6a91c29d88a597f7001ae6c54a88279757a0d57c8155574a97039a4596d00c85 | 39987da967636f24de781695ed634c730bdf636a16a930978c15b0ab3527f35a |

## Review gate

Both promoted families remain `draft_needs_expert_review`; neither is expert-approved or split-frozen. Their reference SAPs remain annotation-only and must never be model-visible. The six excluded families do not enter the completed-question count.
