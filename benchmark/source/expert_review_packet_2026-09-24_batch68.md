# Expert Review Packet — Batch 68

## Scope

Batch 68 reviewed eight ClinicalTrials.gov protocol/SAP families. No family passed the public, prospective, version-matched, independent-hidden-target gate: six model-visible protocols contain enough executable statistical content to make the reference SAP non-independent, while two remaining public pairs cannot be reconciled to a governing prospective protocol/SAP version without guessing. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. The weak text layer in the NCT03840993 pair was resolved by full-page OCR before review.

## Exclusions

- NCT02816736 — protocol pages 33-36 expose populations, sample size, endpoint transformation, imputation/sensitivity rules, GLM, survival, win-ratio and interim analyses; SAP uses observed COVID-era enrollment status.
- NCT04278417 — protocol pages 59-67 expose populations, ANCOVA, noninferiority, CMH, hierarchy, estimands and missingness; SAP is post-primary and records observed-data-driven changes.
- NCT05540717 — protocol pages 2 and 5-6 expose the adaptive group-sequential design, mixed model, multiple imputation, Pocock boundary and multiplicity.
- NCT03227861 — protocol pages 61-64 expose populations, precision target, snapshot/TLOVR and downstream analyses; SAP is post-completion.
- NCT03840993 — protocol pages 12-14 expose populations, power, repeated-measures ANCOVA, covariance, imputation and survival/categorical methods; SAP is post-primary and changes endpoints.
- NCT01581840 — protocol pages 25-29 expose populations, Simon design, stopping rules, survival, quality-of-life and safety-interim analyses; SAP is post-primary and reports the observed interim result.

## Holds

- NCT04104438 — public protocol page 18 says statistical analysis is TBD, while the purported earlier SAP is a one-page retrospective methods narrative without a governing protocol version or core prospective design elements.
- NCT02721069 — public prompt is Protocol v4, but SAP cites unavailable Protocol v3; the available SAP v1.1 is post-primary, explicitly adds analyses, and the prospective v1.0 is unavailable.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02816736 | protocol leakage plus execution-informed SAP | 41 / 32 | 879fdbc08cd346d13114e6be8b7cfcaa24f73fd8b076d39f2d02bfe5f2a6801d | d24fbb155a75199eafa6f74a3ad139693c8ecf701a16beab2d95ad6a19c48dcb |
| NCT04278417 | protocol leakage plus post-primary execution-informed SAP | 74 / 53 | 16e1d2d4bfaa68776572bc33bd65cbb612d9527640b17c3b21eec2527b6091bd | bcbd66a0b0e2474921c866487048a3f4cdfd13825f16420ef4fc51c2f5415f40 |
| NCT04104438 | governing-version hold | 25 / 2 | ae37d748949dbf16d3d6f5795951b16354cea3037cc5208fede3e261ab098649 | 01caac54012ba5c1f9a667caafc924a6c9f16c1480257f8f6f0fa181f50242d4 |
| NCT05540717 | protocol analysis leakage | 9 / 26 | 0614e995d81918d6e5915c68a72ff24fbaa3b23fdadc075b1a63ce879f4ff449 | 5f0786fc2c338b2a4e580a5452f32d30863d26737f1aaa2cd7dc29ae39a18b8e |
| NCT03227861 | protocol leakage plus post-completion SAP | 122 / 45 | 6f5c678ea1790ab7eb8578ee26e8adbe526322345d706af06dd94bdefdbb78ff | a2008a0f7211367996c348ce3c58efe7fd4f8bad0bd739979e2e9c43b8cc4d13 |
| NCT03840993 | protocol leakage plus post-primary SAP | 104 / 40 | 0498de7ea5df7eedd2b34cbad4a5aa948a64294eb512fefbde55498811452d3f | 7ee983c219e88befedd54f6361830e0978f1f5d54f4df4e57d1aef93c051ed16 |
| NCT02721069 | governing-version hold | 98 / 62 | 728a4d7445c66998522f104d574830c602f270fa1ba4a988385cd3525802b21e | 235550adfc1c97c2c600a9f27392ba01e5e562eb86098cccaf02eb3b09a7756a |
| NCT01581840 | protocol leakage plus execution-informed post-primary SAP | 34 / 15 | c02e439ac810e3804a19256ed001401023c63a933278a3514db578edc308cb50 | 0c586aca8ea01a3d31228090c0ab970ed3b21181a22e26d7ef0abc88e779bf71 |

## Review gate

None of these eight families may enter train/dev/test. Six fail prompt/reference independence because the model-visible protocol discloses executable target-analysis content. Two remain on hold because the public files do not establish a version-matched governing prospective pair. Batch 68 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
