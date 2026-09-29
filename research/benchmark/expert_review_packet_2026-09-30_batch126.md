# Expert Review Packet: Batch 126

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 126 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,176 physical pages. Every page was text-extracted; all 45 scan-only NCT02703454 protocol pages were OCRed; and 56 decisive physical pages were rendered and visually inspected in eight contact sheets. Seven pairs were excluded and one was placed on version-reconciliation hold. No pair survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT02376790 — exclude: SAP Version 2.0 dated 2018-06-06 follows actual primary completion on 2018-01-09. Protocol physical pages 50-55 independently expose the analysis sets, prospective N=840, Bonferroni gatekeeping, stratified CMH, nonresponder imputation, covariates, subgroup rules and safety conventions.
- NCT02422524 — exclude: SAP Version 2.0 dated 2024-05-08 follows primary and study completion in 2023, and its history explicitly updates the plan for protocol changes, a second site and collected conduct data. Protocol physical pages 78-80 also expose hypotheses, precision, cohort assignment, interim review, analysis sets and PK methods.
- NCT02703454 — exclude: OCR and visual review confirmed that protocol physical pages 41-44 reproduce essentially the complete 14-page SAP, including ITT/PP sets, the 15% noninferiority rule, confidence intervals, Kaplan-Meier, chi-square, prospective N=170, censoring, center-adjusted Cox/CMH and no interim analysis.
- NCT03014479 — exclude: SAP Version 2.0 dated 2017-12-28 follows completion on 2017-10-21. Protocol physical pages 14-17 and 55-58 already disclose FAS/safety sets, exact DTR-QOL ANCOVA and covariates, alpha, secondary analyses, questionnaire missing-item rules, sample size and no interim analysis.
- NCT03533751 — exclude: during-recruitment Protocol Amendment 3 states that it changed the statistical approach, endpoint hierarchy and Week-16 interim. Protocol physical pages 53-59 expose analysis sets, ANCOVA, hierarchical testing, rescue handling, imputation, sensitivity and interim/final logic; SAP Version 1.1 also adds or revises analyses during conduct.
- NCT03855280 — exclude: SAP Version 2.1 dated 2023-03-28 follows completion on 2022-07-04 and physical pages 5-6 state that no surgeries had occurred at the update, incorporating realized conduct. Protocol physical pages 60-62 independently expose the descriptive efficacy, PK, safety and interim-report program.
- NCT05014672 — exclude: SAP Version 4.0 dated 2024-06-27 follows primary completion on 2024-05-31 and records two June dry runs. During-conduct Protocol Amendment 5 records slow enrollment, endpoint/sample-size changes and removal of the interim/extension; protocol physical pages 21-22 also disclose estimand, missingness and MMRM details.
- NCT05992467 — hold for version reconciliation: the protocol and SAP covers show an IRB approval date of 2023-08-31, but SAP physical page 2 requires R 4.4.1, which CRAN dates to 2024-06-14. The files were uploaded in 2025 and contain no revision or sign-off chain that can establish a prerecruitment, outcome-uninformed SAP. The chronology is internally impossible as printed, so prospective status is held rather than guessed.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02376790 | excluded | 85 / 56 | `b8d4068f5e1ad3a6f843ae46acb9dde168b257689d15e5cfe8f3564eec085bf2` | `34551e6b47c15582daa09927af7973ac3908e0915f134988fb4555ca12baf030` |
| NCT02422524 | excluded | 108 / 212 | `4d4c1001dbe3476f697fdf00f6ddebc12c3b1d8c515b410bdcc1340793001d01` | `b3054dd5148221eb20c2fb6860138acd24be9aea2cb5ca4f7acae5378ee6d679` |
| NCT02703454 | excluded | 45 / 14 | `7f517844fa620995cca9cd804c121a3c1e0fab97c3a8ffa235164a70c9eca5ca` | `eb76c7c620c4298181ab584d165b7fd774258108d494081c21178d1cee0717bc` |
| NCT03014479 | excluded | 133 / 25 | `cbe9e14df2564d004e4eb21dd95cf2ac07a209294d8f3c5f638d7fea61c145cf` | `7b93379498e2a25ab63069aad5a748aaf4abdd1939f525a811df3f604554c973` |
| NCT03533751 | excluded | 106 / 64 | `0e13e8e0f7c37a7da226cede0cf763f93c244561be0967b94e35658f56b9e7f6` | `98bd6c74c58b488cb36ea14afbe64e7cdc9083206a6ee170dfaa9a04cbfd2ef1` |
| NCT03855280 | excluded | 68 / 23 | `c9c8861cde1c8e03dbd3a8cb0f128692003befd491668583e06531abf8b8ebd9` | `e6016855e29157836e57361fdbcb2d7c29ca3fecd09b19dd66616fd29eeee4d2` |
| NCT05014672 | excluded | 127 / 55 | `91b66a58ccda5f65b3fb99ae1f3b84b1d1274e2b0463d416ed11319f06855f7c` | `2cad601e9421df83539745eb7326428de88021661128e70df6cd449730adfd76` |
| NCT05992467 | hold | 5 / 2 | `bb87211cbbaf98114df5612b06c4b8a4a6679c1911c834f8c7c2240c5ae373af` | `7d69aaf493c66bb57ddf2e31d43d478255c6ed926452a5b64ea3ec6f81cb6d22` |

## Gate interpretation

- Registry actual enrollment was not used as a substitute for any prospective sample-size target.
- Protocol disclosure of design, outcomes or sample size alone was not treated as leakage. Exclusions based on leakage require an executable analysis program or essentially complete target reconstruction.
- Post-primary, post-completion, dry-run, observed-conduct and during-conduct revision evidence was treated as outcome/execution-informed unless a defensible earlier governing chain existed.
- NCT05992467 remains a hold, not an exclusion: a later signed revision could resolve its chronology, but the public package does not currently provide one. CRAN's source index records `R-4.4.1.tar.gz` as modified on 2024-06-14.

## Replenishment

All eight non-promotable slots were replenished from the official API. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates. The next queue starts with NCT02712008, NCT03094416, NCT05175131, NCT04370054, NCT02945657, NCT02532283, NCT02585258 and NCT03765489.
