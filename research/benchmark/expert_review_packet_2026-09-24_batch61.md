# Expert Review Packet — Batch 61

## Scope

Batch 61 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent-target gate: NCT02570113 has an unresolved CR0001/CR0002 governing-protocol conflict, while the other seven model-visible protocols expose executable target analyses. Several selected plans also have post-primary or post-completion chronology, one is only a technical supplement, and PA0009 is a rollover family dependent on PA0008. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. Every PDF had a usable embedded text layer.

## Decisions

- NCT02570113 — hold: protocol and SAP cover identify CR0001, but SAP content pages identify CR0002; public evidence cannot establish whether this is a clerical error or a different governing protocol.
- NCT03552757 — excluded: protocol pages 57-64 expose hierarchy, power, populations, estimands, ANCOVA/logistic models, success criteria, multiple imputation and sensitivities; SAP is post-completion.
- NCT02589665 — excluded: protocol pages 55-59 expose power, populations, attribution, logistic models, PK/PD, safety and interim analyses; SAP is post-primary.
- NCT04823130 — excluded: protocol pages 62-70 expose populations, endpoint methods, confidence intervals, missingness, safety and interim rules; post-completion upload is only a Statistical Technical Document modifying that analysis.
- NCT03057119 — excluded: protocol page 11 exposes feasibility and acceptability rules, ITT, covariate screening, chi-square, repeated-measures ANOVA and missing-data handling; three-page plan is post-completion and duplicative.
- NCT03347110 — excluded: rollover protocol pages 66-68 expose PA0008-dependent attribution/baselines, populations, safety rates, efficacy, imputation and sample size; SAP amendment is post-completion and the family is not self-contained.
- NCT02565186 — excluded: protocol pages 40-46 expose populations, attribution, safety and efficacy rules, endpoint derivations, nonresponder imputation and sensitivity analysis.
- NCT02508389 — excluded: protocol pages 79-84 expose sample size, populations, endpoints, van Elteren primary analysis, sequential multiplicity, missingness and secondary models; protocol amendment and SAP are post-primary.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02570113 | governing-protocol ID hold | 5 / 4 | 39a9f4b7e1181ed4a7e522ae6f6ed33847af75ff34c8696266f16c22cd49bafd | 620a7681c5a7fbe46579fc8f23dcf86f7d3d9eceee081c3b7a082fdd8ad7112d |
| NCT03552757 | protocol leakage plus post-completion SAP | 169 / 39 | 4fcca9c7b0d755f72cc9bddfaee37326f81ac8df10251ee9b222a2430e5ea0e4 | c30ec7689ba50519bdd6de3d5cdec401f289233dec4f570e4ff6e84809c4aa8a |
| NCT02589665 | protocol leakage plus post-primary SAP | 82 / 69 | 537091ae2c78bc569272ae8ac29edefb28c565846971c0f0783c84515747b813 | b7a6e47713579b270a56d60e3916d94d8831543bb7eb5c3cda1d6389a9e15740 |
| NCT04823130 | protocol leakage plus post-completion technical supplement | 90 / 13 | 869046ad5be1e23d5ceaf125d161026187918ff5479d7fd63a522fc1efe060f6 | 4a4d8cbabf9aa6bae7479dd77bb86c110c26506bd55e05fd86a58be4d8895622 |
| NCT03057119 | protocol leakage plus post-completion duplicate | 16 / 3 | 5d959265c40c0281f93f694115178fcb5422a1b46917758e3b1c22d6fdcbd65a | 674966f4dac8852be079a74f31cb528bdc44bf2c8968f6ff840367c50176f8c0 |
| NCT03347110 | protocol leakage plus post-completion rollover SAP | 117 / 113 | 6eb4d147cfad2216c4dfa9d4952ed0a2720fa4a48ea967aa130961be7f166f02 | 443f9acd48300f2442491fc656062e0c738d9c266ee7b10ea21984b6ca92ab03 |
| NCT02565186 | protocol leakage | 75 / 51 | 500dd31a7f5d360102962d1723e1d99e6ac342ec02c10f88e1f357db0660b01b | 79340d7dd420f6fb372926f442e99b0126a7718fc1b3039b9171a695dac3e1fc |
| NCT02508389 | protocol leakage plus post-primary documents | 105 / 47 | 14f784a8d2e65af5ad9a7faf54a7a11dc8c9e1d912de1cccac95853408eb0ba0 | c32f1beb5b530a93d3b977adbe243e6d56818a98763c7a66b77baa625b0cd556 |

## Review gate

No Batch 61 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
