# Expert Review Packet — Batch 43

## Scope

Batch 43 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent-target gate. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining statistical pages.

## Exclusions

- `NCT01243424` — protocol pages 70 and 75-81 expose the noninferiority/superiority hierarchy, FAS, Cox/log-rank, MMRM/ANCOVA, interim alpha, missing data and event-driven power.
- `NCT05589610` — protocol pages 71-72 expose safety/PK populations and detailed safety, efficacy and PK methods; the SAP is post-primary-completion.
- `NCT02597049` — protocol pages 49-55 expose estimands, ITT, MMRM/ANCOVA, LOCF, tipping-point and retrieved-dropout sensitivity analyses, multiplicity and sample size.
- `NCT05291689` — protocol pages 78-81 expose four analysis sets, endpoint analyses, cohort pooling and sample size; the SAP is post-primary-completion.
- `NCT03565237` — protocol pages 49-50 expose descriptive policy, EFAS/SAS, missing data, safety/efficacy summaries and no-interim rule; the SAP is post-completion.
- `NCT03610516` — protocol pages 92-98 expose analysis sets, the complete mixed model, censoring/MAR, safety, success criteria, power and interim reassessment; the SAP is post-completion.
- `NCT02414399` — protocol pages 15-17 expose Cox, Poisson/GEE, chi-square, propensity-score and interim adaptation methods; SAP Version 5 is post-primary and explicitly post-interim.
- `NCT02536833` — protocol pages 40-42 expose four analysis sets, interim timing, ANCOVA, logistic regression, safety and sample size.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01243424 | protocol leakage | 173 / 85 | `9d5524278a527b18215101089754ed11bbf01486894bcd077ff157afe074ddf6` | `9d3a1e3d2fc995750a9427e85fdbfab209693beb4bd61d5ff2f02294dc06a1db` |
| NCT05589610 | leakage + post-primary SAP | 93 / 42 | `b0deab1a161870bdc00db3697676f578b6ad4ef24884df8642171974fbb5ca6f` | `9fd376817ecfcc5ec458cd091652f788933a50a74b763c3e7e201927a08f9a09` |
| NCT02597049 | protocol leakage | 85 / 32 | `dbbddc56f1509c231be3d2ca44595cab04d02539c53eb32bb8249e59f67fb4bd` | `ed94ca0de7ead4d6bacced22b1d676f8172553a6b7442186efcc9596cea419d0` |
| NCT05291689 | leakage + post-primary SAP | 131 / 61 | `48cd7e5e2657bd765d07d67af6464f9aaeb8a545795fccf10507d9a0d1cf37dd` | `18f4c9b777bda8b02dbc280ea8e4bfd01a592c9928d084a34b2e81d226b8e4a6` |
| NCT03565237 | leakage + post-completion SAP | 144 / 34 | `ea0e7654c54c3cd6d56481394f70135512c2648b043f9ddf2a7c44eb4215d384` | `f4f544b1d605011c5440ce344f40dc8e67ccf1e80c8edfbdd5aa94f28156d91a` |
| NCT03610516 | leakage + post-completion SAP | 113 / 19 | `a7da5f4bae89c5ea3361faa9d174879667d20b3828929e9a89a0cc5e4407c46e` | `178853e994af5f75289a8fb539d33d76b78ed70c68581e4a8abf8d63777c3e64` |
| NCT02414399 | leakage + post-primary/post-interim SAP | 23 / 16 | `44fab736943a4d82a518574bb722ad73ef25d722be1f633aa3edfb6d964a94ad` | `591046efd2f6871336bcc265f21e5c2030d2239767729535ff8bb633f8388626` |
| NCT02536833 | protocol leakage | 64 / 20 | `e2cfc9b44aa99a63037238cf3c675e720a3ad3bc29febf2c94e89f06b9e292fe` | `d60aed895121f2d8cddd79ff6bad62edfbed72a614a60991413b6e7c733f2354` |

## Review gate

These eight candidates cannot enter train/dev/test. All eight slots must be replenished; no Batch 43 record is counted as a completed benchmark question.
