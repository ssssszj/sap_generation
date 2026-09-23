# Expert Review Packet — Batch 09

## PUBLIC-TARGETED-STROKE-001

- 16 requirements; all remain `draft_needs_expert_review`.
- Confirm that NCT01819506 Protocol Version 4.0 and the separate SAP, both dated 2016-08-01, form the correct governing pair.
- Adjudicate the protocol percent-change ANOVA against the later SAP's repeated-measures mixed ANOVA; the latter is a confirmed decision and must not be presented as a protocol-only fact.
- Verify the sample-size arithmetic, analysis populations, Aim 1 estimand, multiplicity threshold, and severity-by-treatment interpretation.
- Specify executable multiple-imputation and sensitivity-analysis rules before freezing the rubric.

## PUBLIC-ALCOHOL-PATHWAYS-001

- 17 requirements; all remain `draft_needs_expert_review`.
- Preserve the nonrandomized design: AALD/AUD and AUD-only are clinical-status cohorts, not randomized treatment arms, and all participants receive the intervention.
- Verify all six feasibility thresholds and make their denominators executable.
- Retain the pragmatic N=44 rationale and do not imply confirmatory power.
- Define the exploratory longitudinal models, missing-data handling, analysis populations, and multiplicity policy before freezing.

## PUBLIC-TKA-NMES-001

- 16 requirements; all remain `draft_needs_expert_review`.
- Confirm the same-day protocol and separate two-page prospective analysis plan dated 2022-03-23 as the governing pair.
- Adjudicate the primary-outcome hierarchy across the numerous fiber-level, mitochondrial, and functional measures.
- Specify analysis populations, covariance and degrees-of-freedom choices, multiplicity, and the study-level success rule.
- Operationalize dropout sensitivity values and covariate-selection rules before freezing.

## PUBLIC-PED-IDA-FCM-001

- 18 requirements; all remain `draft_needs_expert_review`.
- Confirm SAP v2.0 dated 2020-07-15 against protocol 1VIT17044 Administrative Change 1 dated 2019-09-26, which is physically present in the public protocol bundle.
- Adjudicate the protocol-to-SAP switch from mITT to ITT and whether the later mITT analysis should remain sensitivity-only.
- Review LOCF, worst-value imputation, MMRM covariance fallback, and multiplicity.
- Confirm the laboratory grading change to DAIDS and the SAP omission of the protocol's IBD and CKD subgroup analyses.

## Version and source decisions

- NCT01819506: promoted. The protocol and independent SAP both identify Version 4.0 and 2016-08-01. The protocol does not reproduce the later SAP's full repeated-measures, missing-data, or sensitivity strategy.
- NCT05135767: promoted. The independent protocol and SAP share the exact title, NCT identifier, and 2023-05-25 date. The study is a prospective nonrandomized feasibility intervention with clinical-status cohorts.
- NCT03051984: promoted. The protocol and separate prospective analysis plan share the exact title, NCT identifier, and 2022-03-23 date.
- NCT03523117: promoted. SAP v2.0 explicitly cites 1VIT17044 Administrative Change 1 dated 2019-09-26, and that complete version is present in the public protocol bundle.
- NCT01831804: `hold_version_reconciliation`; the 2017 reporting and analysis plan has a confusing RAP/protocol revision chronology and does not cleanly identify the governing protocol revision.
- NCT02849080: `hold_version_reconciliation`; the protocol bundle contains the original protocol plus amendments, while the extension SAP does not explicitly reconcile its governing complete protocol version.
- NCT05763082: `hold_public_redaction`; material sample sizes, allocation ratio, and core primary equivalence or superiority details are visibly redacted.
- NCT01980771: `excluded_wrong_document_type`; the purported SAP describes already completed analyses in the past tense.

## Source audit

For every candidate below, title/version pages and the pages supporting admission, hold, redaction, or retrospective-document decisions were visually inspected. Page counts and SHA-256 hashes were checked from the frozen public PDFs.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT01819506 | protocol | 33 | 6d8fd88183c48bde7eced8b61808ced13affe1b0c077806eb9d5a69e06f4c595 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/06/NCT01819506/Prot_000.pdf) |
| NCT01819506 | SAP | 2 | 3e0512819a1efc34f7200c3502d5fa8c103c1451ddaa0e95c2fcc08afbe754b4 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/06/NCT01819506/SAP_001.pdf) |
| NCT01831804 | protocol | 205 | 9779492e29ba473b1cc96ea295fc61343f4642131d973216db9a49fe80bdee6d | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/04/NCT01831804/Prot_000.pdf) |
| NCT01831804 | reporting and analysis plan | 57 | 5bbe8acf62d95af462b75e7bf906eb1c3d2e1768c5318d338757891c007d53bc | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/04/NCT01831804/SAP_001.pdf) |
| NCT02849080 | protocol bundle | 209 | 5d753657ab128f4d3923e72e5cb8b42e17ad2503c50f1796a13f5d8e9657d884 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/80/NCT02849080/Prot_000.pdf) |
| NCT02849080 | SAP | 43 | b860ccb83f48d69a5bd9526da4c83618fec28b90f0afa06fa67b36c17c2b5626 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/80/NCT02849080/SAP_001.pdf) |
| NCT05135767 | protocol | 16 | 721b4a8419561fddeea38ca2e07c7bbcb3a0d91db3e087b83295e654842a00d4 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/67/NCT05135767/Prot_000.pdf) |
| NCT05135767 | SAP | 2 | 3e70002b90581bfb24e5633cd9d7df4b44c777445d9b604a3d1d1565306acf04 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/67/NCT05135767/SAP_001.pdf) |
| NCT03523117 | protocol bundle | 94 | efb10b792021859b219643ca7d2fe644fb4d4d7fe3b09aabbc52579e8f4c1362 | [Prot_003.pdf](https://cdn.clinicaltrials.gov/large-docs/17/NCT03523117/Prot_003.pdf) |
| NCT03523117 | SAP | 32 | d08637bc3524611fdba98c288dff1f4bf08f4aa39b6214f6e0c93cba69e59a90 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/17/NCT03523117/SAP_001.pdf) |
| NCT05763082 | redacted protocol | 60 | 3086aeec5b169cd529ed300afd34023ee320f8af3cc2e768b8254596ef2a366a | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/82/NCT05763082/Prot_000.pdf) |
| NCT05763082 | redacted SAP | 14 | 01a2300f626ca20f9b019545413eab5fb5527ea880063d93d709c43a7853b939 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/82/NCT05763082/SAP_001.pdf) |
| NCT01980771 | protocol | 11 | 2ecd46490c5cebb9fe0b651616a3557fefef334598487eb7c4b0437f27f4537d | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/71/NCT01980771/Prot_000.pdf) |
| NCT01980771 | uploaded SAP slot | 2 | 14cdc6893b3b09398f748f367ed01cbcc2e5809ea00bd57f05690e48d334cd0f | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/71/NCT01980771/SAP_001.pdf) |
| NCT03051984 | protocol | 15 | 4af44af690addcc9ed7cb9b735f03ed7c8f1e4655a6a55a9f9b98fdd8d69f739 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/84/NCT03051984/Prot_000.pdf) |
| NCT03051984 | SAP | 2 | ee92f512c2314d0930e57743780f11c1ea21c94eb375909272d07f79052f0159 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/84/NCT03051984/SAP_001.pdf) |

The local PDFs are acquisition artifacts under the gitignored source tree. Their URLs, hashes, and page counts are recorded here or in the manifest; PDFs are not committed.
