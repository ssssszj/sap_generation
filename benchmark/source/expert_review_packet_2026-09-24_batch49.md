# Expert Review Packet — Batch 49

## Scope

Batch 49 reviewed eight ClinicalTrials.gov protocol/SAP families. One family passed the independent prospective-target gate and received a 22-item first-pass annotation; six protocols expose executable target analyses, and one SAP is post-completion and execution-informed. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages.

## Promotion

- `NCT03458767` → `PUBLIC-PALMS-II-MS-001`. The separately uploaded protocol and SAP share the exact title and 2017-09-19 date and precede actual study start on 2017-10-09. The 12-page protocol defines a mixed-methods five-person qualitative adaptation phase and a 20-person randomized assessor-blind feasibility phase without exposing the independent SAP's generic ANCOVA, alpha 0.10 or reliability rule. The short reference plan leaves primary hierarchy, randomization details, analysis population, endpoint derivations, missing data and multiplicity unresolved; these are explicit `needs_confirmation` items.

## Exclusions

- `NCT02351856` — the rollover protocol pages 6 and 49 expose the population, descriptive analyses, timepoints and safety/efficacy/PK display rules.
- `NCT02973321` — protocol pages 8-10 and 84-88 expose power, populations, control-based multiple imputation, ANCOVA, CMH, multiplicity and interim analyses.
- `NCT05570006` — protocol pages 33-35 expose the historical-control Bayesian decision rule, NRI-MI, populations, safety, interim, multiplicity and power plan; later SAP versions incorporate the population enrolled.
- `NCT01286779` — protocol pages 11 and 92-94 expose populations, missingness, descriptive and PK methods, safety review and sample-size logic; SAP Version 2.0 is post-completion.
- `NCT03850483` — protocol pages 85-91 expose estimands, MI, sample size, populations, models, interim and unblinding; SAP Version 3.0 is post-completion.
- `NCT02738450` — SAP Final 2.0 is post-completion and incorporates observed COVID disruption and data collected under superseded protocol versions.
- `NCT02798211` — protocol pages 19-21 and 73-77 expose populations, logistic/CMH/ANCOVA analyses, nonresponder/LOCF rules and power; SAP Amendment 2.0 is post-completion.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02351856 | protocol leakage | 89 / 37 | `fba9d8fc03f7d504694e1d3123829ab35bc2bdeca3084e925219602273ec693a` | `d5c8cd1297b936551e993c25b7d7271d60f16fdb21da0180a57e07e8b054ceee` |
| NCT02973321 | protocol leakage | 107 / 61 | `5c40e895502b647a391c02e2e60d006e2e1e3c26feb685f4c0afc40f4be19b2e` | `c9d085f3baa8805fae32a3d2e3f93665b9605fc6177e85d7200e9a688de05421` |
| NCT05570006 | protocol leakage / enrolled-population update | 91 / 35 | `ad37c73e264a906ecdda4f82800fcb1dfc5699f2e20f305a6b4755686da4917f` | `544478eee690bc1e1a3cb5406be39de146fa81959520aa329976c91ae78773c3` |
| NCT01286779 | protocol leakage + post-completion SAP | 170 / 35 | `e01aa51b228453b769fc7cf128a3d8c59cce555e016521e84a289e13da00a107` | `9d241a328d82dffa4dc6d6bd65203f81aacfe3824f2f6636a9c30e1a85474940` |
| NCT03850483 | protocol leakage + post-completion SAP | 152 / 45 | `6ab3749ca08f29bec7e5e45bc03eb97904ab7eca9f6e6bb781b29ab8a21820ac` | `6be817a6811870944908914ac1a0e88f059295d082b3aef86cd283046d05d7ba` |
| NCT02738450 | post-completion execution-informed SAP | 8 / 75 | `66daefdcd2f0ab5b0610c6e853f56dada473f89a8adbec739f73b6e18f0e9f8e` | `0b55f430013a215a664ad22076e21a10640579b09c925ee574a6e882a6b838ba` |
| NCT02798211 | protocol leakage + post-completion SAP | 94 / 68 | `85e007b081eb6761d2e40e3f9c9bacba307cba0bbc86c455daa2254f3959dc77` | `f61c660bd901ad930d1065485f7144ba02963b92db993fac27e4bb7428ace233` |
| NCT03458767 | promoted draft | 12 / 2 | `6be48d823310e67d9867f95ceeb7bdd79a806007c575ed42f3c578abd553bbd0` | `79b1714b8bbaad8f5ff367cc06c45eb8a5b02ba8907676a81051ed61587883e9` |

## Review gate

The promoted family remains `draft_needs_expert_review`. The seven excluded candidates cannot enter train/dev/test and their slots must be replenished.
