# Expert Review Packet: Batch 123

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 123 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 914 physical pages. All pages were text-extracted; the 74-page NCT03211247 SAP had no embedded text and was OCRed page by page. Ninety-nine decisive physical pages were rendered into contact sheets and visually inspected. This remains first-pass work requiring independent expert review.

## Decisions

- NCT05832918 — promote as `PUBLIC-CORE-DUAL-TASK-LBP-001`: the official five-page protocol and independent one-page analysis document share the exact title and 2023-03-27 date and predate actual start on 2023-05-02. Neither PDF prints the NCT, so registry binding remains explicit for second review. The protocol defines the randomized exercise design, endpoints, N=34 prospective target and COP derivations without exposing the reference-only SPSS/Stata, mixed ANOVA, Bonferroni or Friedman choices.
- NCT02476006 — exclude: protocol physical pages 67-72 disclose the precision target, populations, periods, compliance, safety/Kaplan-Meier, efficacy summaries and interim decision; the reference adds only implementation detail.
- NCT02944383 — exclude: SAP approval 2018-05-02 is after primary completion 2018-01-11; protocol physical pages 57-60 also disclose FAS/PPS/SAS, LOCF, ANCOVA, least-squares means, alpha, confidence intervals, PPS confirmation and secondary models.
- NCT04375878 — exclude: final SAP 2021-05-21 is after primary/study completion 2021-04-08; protocol physical pages 55-57 disclose analysis sets, no replacement, CFA derivation, descriptive/non-inferiority analyses and sample-size basis.
- NCT03263091 — exclude: SAP 2023-04-10 is after primary completion 2023-03-09; protocol physical pages 71-75 disclose power, FAS/Safety, sequential testing, CMH, MMRM/ANCOVA, Cox and safety methods.
- NCT03211247 — exclude: Protocol Version 7.0 dated 2019-11-15 and SAP Version 4.0 dated 2022-03-15 both postdate primary completion 2019-08-20; the protocol embeds the completed Part A safety/dose decision and the SAP records pandemic and later modification history.
- NCT02409290 — exclude: final SAP 2022-09-09 is after primary completion 2022-05-13 and has extensive during-trial revisions; protocol physical pages 68-78 expose outcome derivations, analysis sets, non-inferiority, interim re-estimation and primary/safety models and cite preliminary Stage 1 results.
- NCT05015478 — exclude: both documents dated 2024-02-01 postdate completion 2023-09-12; protocol physical pages 2-5 contain pilot results and the full paired-condition mixed model and Sidak testing program.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02476006 | excluded | 111 / 60 | `6efd19c3d26868952fa3ed25cb5755a459ff882caf43aa01a4ccfd91837ce478` | `56a111d7801a8bed83637070bf05129f843ce18c5b0982db1b8be295e497bb7e` |
| NCT02944383 | excluded | 79 / 35 | `baa50e39511c94c417da3af43c669209e291ded05039cb8f0c9ff3ccd0f48865` | `38aa2172d0c75a1a44ed6c2c5e0fce716231b0533cf57f3146b1a9829a58acd1` |
| NCT04375878 | excluded | 79 / 46 | `1b6681698fab737d7ce7e07f2ea081a7430c7765f66354b24af3fc87250e9fbe` | `ce7bd51bb2b80654dfd9b9054be6939850fe6c188934ae74c524245e368d832a` |
| NCT03263091 | excluded | 105 / 77 | `1caa40bb5ccd763f445bf2dcf220170c1c6d76d9c4758412ca8e70eb1fa447c6` | `46df9a0f39a314aa6c812383c83582c800ae959765de36cd2971a49309bc87e1` |
| NCT03211247 | excluded | 145 / 74 | `0d02cf8b117a3ae12335b3b0d1af78a32685b9b05ef26b33ca71570726115100` | `33fb1a2c4893c5db5c023dd7ba00e2d1e403e6d5ab0bed31517a64565dee9c98` |
| NCT02409290 | excluded | 106 / 37 | `2a5f5a997329d08b39a02b3582dba90e0cc6fa3351524de68d6ae6d8eabf2e27` | `036ad52849d17ffdde6a7b78986175127e5dc96ae6e4400db6e0b691544c9158` |
| NCT05832918 | promoted | 5 / 1 | `e3bc27997232c468ead3bad629d82093314886c925369248ccf5ddb30c7715f0` | `b749763aca0c9f6b4ed8e943e58b6c1a11b15b3a69d38d860ca5167b575991f7` |
| NCT05015478 | excluded | 5 / 3 | `768eb9adfc1de96a03b475e092c1c82c385a681c98c828fd819e5ed6c43d2b6e` | `30f701e4920122a7749beb8913dbc84db2e430f3d0fb77514bf7c2ec21bfddfe` |

## Annotation and replenishment

`PUBLIC-CORE-DUAL-TASK-LBP-001` has 24 atomic first-pass requirements. They retain the prospective 26-analyzable/34-enrolled target rather than the later registry target, preserve direct randomized group-by-time inference, and expose the missing NCT-in-PDF binding, 16-session schedule conflict, VAS/ODI hierarchy, analysis populations, estimand, missingness, multiplicity, robust inference, effect intervals and safety as expert-review gates.

The seven excluded slots were replenished from the official API after exclusions and the promotion were registered. The release-eligible intake remains 120: 103 public first-pass drafts and 17 actionable metadata candidates.
