# Expert Review Packet — Batch 13

## PUBLIC-PRODERM-001

- 18 requirements; all remain draft_needs_expert_review.
- Confirm GAM10-08 Protocol Version 12 and SAP Final 4.0, both dated 2019-06-18.
- Verify TIS response, confirmed deterioration, FAS/PP1 membership and nonresponder rules.
- Adjudicate secondary multiplicity and the implementation of missing-data handling for continuous endpoints.

## PUBLIC-T1D-NNC0114-001

- 17 requirements; all remain draft_needs_expert_review.
- Confirm SAP Version 1.0 against NN9828-4150 Protocol Version 8.0 including Amendments 1–7; the registry wrapper is dated 2019-09-17, while Amendment 7 is dated 2018-03-23.
- Verify the relative C-peptide AUC derivation, MMRM terms, geometric mean ratios and four-arm contrasts.
- Adjudicate the estimand, post-discontinuation data handling and nominal interpretation without multiplicity control.

## PUBLIC-EINSTEIN-JUNIOR-001

- 16 requirements; all remain draft_needs_expert_review.
- Confirm integrated Protocol Version 5.0 and SAP Version 3.0 with Supplement 2.0 and the listed local amendments.
- Verify age-specific treatment windows, central adjudication, imaging imputation and censoring.
- Keep efficacy and safety comparisons descriptive or exploratory rather than treating the study as a powered non-inferiority trial.

## PUBLIC-RECAST-SLE-001

- 16 requirements; all remain draft_needs_expert_review.
- Confirm VIB7734.P2.S1 Protocol Version 2.0 and SAP Version 2.0, both dated 2022-02-10.
- Adjudicate the BICLA plus oral-glucocorticoid composite estimand, FAS country exclusions, LOCF and nonresponder handling.
- Confirm that alpha-0.10 comparisons remain exploratory and unadjusted for multiplicity.

## PUBLIC-DSM265-BA-001

- 15 requirements; all remain draft_needs_expert_review.
- Confirm B19-227 Protocol Version 1.0 and SAP Version 1.0, both dated 2018-08-13.
- Verify the noncompartmental PK endpoints, two test/reference contrasts, log-ANOVA and 0.80–1.25 interval rule.
- Adjudicate BLQ handling, PK evaluability, missing concentrations and model-diagnostic details.

## PUBLIC-OBTURATOR-TKA-001

- 14 requirements; all remain draft_needs_expert_review.
- Confirm the exact title, NCT identifier and 2017-09-29 date across the separate protocol and SAP.
- Resolve the primary opioid derivation, observation interval, analysis population and missing-data rule.
- Recover the sample-size inputs and result, and define multiplicity and distributional fallback rules.

## PUBLIC-HFO-EPILEPSY-001

- 14 requirements; all remain draft_needs_expert_review.
- Confirm the exact title, NCT identifier and Protocol Version Date 2017-10-26 across the separate protocol and SAP.
- Resolve the one-year versus two-year outcome hierarchy, censoring and event definition.
- Assess log-rank and Cox-model feasibility with N=30 and specify a missing-data sensitivity analysis.

## PUBLIC-SELEPRESSIN-SEPSIS-001

- 18 requirements; all remain draft_needs_expert_review.
- Confirm SAP Final Version 9.0 against the protocol dated 2016-07-08 including Amendments 1 and 2.
- Audit pooling across adaptive parts, P&VFD derivation, van Elteren strata and the joint treatment-effect model.
- Reproduce adaptive operating characteristics and verify futility, dose-selection and Hochberg thresholds.

## Version and source decisions

- NCT02728752: promoted. SAP Final 4.0 explicitly cites GAM10-08 Protocol Version 12; both documents are dated 2019-06-18.
- NCT02443155: promoted. SAP Version 1.0 explicitly states that it is based on Protocol Version 8.0 including Amendments 1–7. The registry wrapper date is later than the embedded governing amendment, and that distinction is retained in the manifest.
- NCT02234843: promoted. SAP Version 3.0 and Supplement 2.0 list the protocol chain through integrated Protocol Version 5.0 and later local amendments.
- NCT04925934: promoted. Protocol Version 2.0 and SAP Version 2.0 share study identifier VIB7734.P2.S1 and date 2022-02-10.
- NCT03637517: promoted. Protocol and SAP Version 1.0 share study identifier B19-227 and date 2018-08-13.
- NCT03326999: promoted. The two independent documents share the exact title, NCT identifier and date 2017-09-29; underspecified analysis choices remain confirmation requirements.
- NCT03790280: promoted. The two independent documents share the exact title, NCT identifier and Protocol Version Date 2017-10-26; underspecified censoring and hierarchy choices remain confirmation requirements.
- NCT02508649: promoted. SAP Final Version 9.0 explicitly states that it is based on the protocol dated 2016-07-08 including Amendments 1 and 2.
- NCT01709981, NCT03856164 and NCT01462253: excluded_combined_protocol_sap_leakage; their protocols reproduce the target statistical analysis in sufficient detail to leak the protocol-only answer.
- NCT02652767: hold_version_reconciliation; SAP Version 1.0 identifies the study but does not explicitly identify the governing protocol version or date.

## Source audit

All admitted title/version pages and the pages supporting admission, hold or leakage decisions were visually inspected. Key design, endpoint, sample-size, model, multiplicity, missing-data and safety pages were inspected when present. Page counts and SHA-256 hashes were checked from the frozen local public PDFs.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT02728752 | protocol | 71 | a935360e3e9eace0a3c15bae9527c2665843f7f0fea4218b39aba69b1457424f | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/52/NCT02728752/Prot_000.pdf) |
| NCT02728752 | SAP | 27 | 98bab5f6bfb0411093729b855c561d3c09912cd6efb004914615257738f3b510 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/52/NCT02728752/SAP_001.pdf) |
| NCT02443155 | protocol | 255 | b2e9c6c6f19de5299a236e423b518639ec055bfdc96f0282dfad870da0dea264 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/55/NCT02443155/Prot_000.pdf) |
| NCT02443155 | SAP | 30 | a10825d669f19703d539e18eac191a725a84c5e2d942a71c6315c512d5b30177 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/55/NCT02443155/SAP_001.pdf) |
| NCT02234843 | protocol | 168 | 8025d7a21da9f3542de32165dd0d12255a7113a309f1a136617868d612e10f95 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/43/NCT02234843/Prot_000.pdf) |
| NCT02234843 | SAP | 44 | 583714becdb8b4d6e1006bc27394b590aa492ab32176a37670c55681868c870c | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/43/NCT02234843/SAP_001.pdf) |
| NCT04925934 | protocol | 106 | 0dcb5e6a63aeb81c33292c665c58b4582fba1af9e1b3bb0134e85e19a3da10ba | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/34/NCT04925934/Prot_000.pdf) |
| NCT04925934 | SAP | 52 | 0482ebaa7a8c3d891fe352bcbbf02d9b79451ee789c1ba59c37f45a1ec4524c7 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/34/NCT04925934/SAP_001.pdf) |
| NCT03637517 | protocol | 41 | f9b6a744f980b9e26069fbe0bb92d1e18fe74db452aefe085e3eefffc54db941 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/17/NCT03637517/Prot_000.pdf) |
| NCT03637517 | SAP | 10 | 8d4250ebcba0b4c9fa8418a7787e3dea9e5572a23daae56cd421fd7b491e0e4f | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/17/NCT03637517/SAP_001.pdf) |
| NCT03326999 | protocol | 7 | 1024d20dd35b4010f43048827c8e6abdd0870ac50629bbeb1b3cfe2b77461888 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/99/NCT03326999/Prot_000.pdf) |
| NCT03326999 | SAP | 2 | 4cab4958d6a2ebb92d440b34c923658ab1de77a2115284629932237a599f7ce1 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/99/NCT03326999/SAP_001.pdf) |
| NCT03790280 | protocol | 8 | e65f532bb6700685031384e0379fb0207f8963383a436ed58ebb6090ab3af53e | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/80/NCT03790280/Prot_000.pdf) |
| NCT03790280 | SAP | 1 | 57f77a56d424363c7f46d023d9389be772bbcf7d7bfb2a65a427e3cb6bf69889 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/80/NCT03790280/SAP_001.pdf) |
| NCT02508649 | protocol | 97 | 2ad65a21abd53ad7f85b5d2085ef9cc0699b28fab8fa860c0440a833c7554f50 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/49/NCT02508649/Prot_000.pdf) |
| NCT02508649 | SAP | 91 | 84a36c5f142acb28b279060e6705a6ab1e2926e5c1c51e7bf4e7697d64ecc870 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/49/NCT02508649/SAP_001.pdf) |
| NCT01709981 | protocol / SAP | 49 / 27 | 640bbe63498e3dbb7f8aef101283837d385a058cbd5aa753990b1a8765347b20 / fabaf8d4e404c349f12acdcaa494866043b1b8373a7687238cf8f8d61243f479 | [record](https://clinicaltrials.gov/study/NCT01709981) |
| NCT03856164 | protocol / SAP | 26 / 1 | 6d4dcb614fe66d0fe06fb789e1f7d046b2a6e83840a9c9cc0d1049dc2c6728d7 / 09f0beade74db10aa6d2417c707a90bfdec377538534ecd56fc0e274ffef719a | [record](https://clinicaltrials.gov/study/NCT03856164) |
| NCT01462253 | protocol / SAP | 63 / 8 | 59d047f63bed781d3e7dbe10f237b7e4d99ba457b8641fed8d6dd9879d64f665 / e2b197bfa9e436c533295e780d2c873d9ad4f4e22321a28904bb06e5cba17c0c | [record](https://clinicaltrials.gov/study/NCT01462253) |
| NCT02652767 | protocol / SAP | 65 / 19 | 978ef58cdc04a1e8c3d0eeeb0c830993b3c3d2c37e26f35775ef3e9dbb0084e8 / 4ee3d9723ae24fccb9aaaaf02487b2979a6a6ce99cd7037e7853e302cf1e7dd6 | [record](https://clinicaltrials.gov/study/NCT02652767) |

The local PDFs are acquisition artifacts under the gitignored source tree. They are not committed, and reference SAPs remain annotation-only.
