# Expert Review Packet - Batch 96

## Scope and decision boundary

Batch 96 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally and extracted page by page; the 56-page scan-only NCT02871479 protocol was fully OCRed. Decisive identity, chronology, endpoint-conflict and target-leakage pages were rendered and visually inspected. One family is promoted as a first-pass annotation draft, one is held for version reconciliation and six are excluded. Seven open slots are replenished so the intake remains 120 public families.

## Promotion

- `NCT04203147` -> `PUBLIC-HOME-DMBAT-001`. The seven-page protocol and independent two-page Analysis Plan share exact title, NCT and 2021-06-02 date and predate actual 2025-06-30 primary completion. The protocol defines the older low-income Black/Hispanic type-2-diabetes population, HOME DM-BAT and GHE/ST conditions, 200-person target, assessment schedule, HbA1c objective and stratified randomization without exposing the reference-only longitudinal mixed-effects framework or candidate covariates. Twenty evidence-backed requirements were added. Because both files were uploaded after completion, original unmodified MCW IRB or grant provenance remains a release gate. The control description, masking, estimand, model, missingness, multiplicity and safety specifications also require expert adjudication.

## Hold

- `NCT03431467` — same-date endpoint conflict. Both documents are dated 2017-12-20, but the protocol defines recovery at 30 days and the one-page SAP uses 45 days. No amendment chain resolves which endpoint governed, so the pair is held rather than guessed.

## Exclusions

- `NCT04438174` — protocol leakage plus version mismatch. The public protocol is Version 5.00 dated 2022-02-02, while SAP Version 1.0 explicitly governs Protocol Version 3.00 dated 2020-10-14. Protocol pages 23-26 also reproduce the central analyses, missing-data and sensitivity rules, subgroup plan and sample-size justification.
- `NCT03234907` — post-completion SAP. The 2020-10-05 plan follows actual primary/final completion on 2020-08-14.
- `NCT03745287` — protocol leakage. Protocol Version 6.11 pages 76-83 expose analysis sets, missing-data rules, exact binary inference, Kaplan-Meier methods, group-sequential interim design, alpha and efficacy boundaries.
- `NCT02871479` — post-completion SAP. The 2018-10-11 final SAP Implementation Document follows actual primary/final completion on 2018-08-31.
- `NCT00799864` — final-analysis, post-completion SAP. The cohort-2 final-analysis plan is dated 2022-10-07 after actual primary/final completion in August 2022.
- `NCT03010254` — protocol leakage. Protocol Version 4.0 pages 65-74 contain the complete analysis plan, hypotheses, alpha, noninferiority margins, missing-data sensitivity analyses and power assumptions.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03431467 | version hold | 23 / 1 | 5d61a47720f0d3587d658a49eff1273f152eb882c85c4aac6017aa7b98430ab8 | 30c7d15ec3023b6977ae54d21914c506953fb0d9771c023bd965bfd66918d68e |
| NCT04438174 | protocol leakage/version mismatch | 31 / 26 | 3d2e088334ecd74dd784b024797b1bf6600448d2de0416b01cd95c9a54a0b34d | 197b32163a59e9f05d0ce877ebd32cdfce48abea9228f5773aa6c039f326cea1 |
| NCT04203147 | promoted draft | 7 / 2 | 96d071a593f2109d4c2e1220772a4670f7c7c5c791cd5995d4aad8862cb9c20d | 507a74f289f2361946dd6a72903ef8eba92546fb17aa995ed85556e462948a61 |
| NCT03234907 | post-completion SAP | 99 / 55 | cda47e4b2a25b616c661728e362bb99348454c0d3c07cd4acb8a75cd79362c4f | 68cf35394c60f6eb72d719cbd2143a3a680e0d1d5c3088d9ef82c84dec0d5ac2 |
| NCT03745287 | protocol leakage | 102 / 59 | 6c1b197eb9229f1075578ac22f8bb813ead7249ac4a3c957cfad51fcc92903a2 | 63ea8a7258e4fbf718b0a79be68f6d08b90e56fbef6041400f6c5365bd1e060e |
| NCT02871479 | post-completion SAP | 56 / 18 | 390fbfa4a5dc97a7a9d52bcf5e913f6008df9ceb4a4f6ec8c9289fa0fc42e9f0 | a6aadf6f05b53daea43cbb69a4d9a262c50cb087552cb43200d1f10b623a846e |
| NCT00799864 | final-analysis post-completion SAP | 234 / 39 | 37ea7e700ccc86ad05047054646da0a2425a7de0eb6efd838960abe94e78cb4f | 488c0674d342e20fe4b82903fd1847ddca208168d81c05ae160aa82022bb29c1 |
| NCT03010254 | protocol leakage | 81 / 39 | 68082669747b537fd5aea763c07304838101e0d57c2d7d4cc1166240de22dc6e | d0160e309667339fedd216c9362ead5cec118176028f2091d12a7edf9039c33e |

## Review gate

The promoted HOME DM-BAT family remains `draft_needs_expert_review`; it is not expert-approved or split-frozen. Its reference Analysis Plan remains annotation-only and must never be model-visible. The held and excluded families do not enter the completed-question count.
