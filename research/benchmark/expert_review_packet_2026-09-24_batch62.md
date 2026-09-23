# Expert Review Packet — Batch 62

## Scope

Batch 62 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent-target gate: every model-visible protocol exposes an executable target analysis. Four families have additional post-primary, post-completion, extension-family or non-independent-document defects. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. Every PDF had a usable embedded text layer.

## Decisions

- NCT02510794 — excluded: protocol pages 99-104 expose power, modified ITT as-treated handling, stratified log-rank/Cox and Kaplan-Meier analyses, LOCF, ANCOVA, safety and optional interim analyses; SAP is post-primary.
- NCT03757130 — excluded: protocol pages 66-68 expose sample-size probabilities, safety/PK/PD sets, no imputation, cohort pooling, descriptive analyses and early stopping.
- NCT02620046 — excluded: extension protocol pages 90-92 and 117 expose populations, efficacy/safety/resource-use analyses, confidence intervals, exposure-adjusted summaries, interim reporting and parent-study-derived sample size; SAP is post-completion and the family depends on two parent studies.
- NCT03285711 — excluded: protocol pages 81-85 expose analysis sets, imputation, efficacy and safety summaries, PK/biomarker analyses, power, DMC review and analysis timing.
- NCT03069365 — excluded: protocol pages 78-90 expose populations, no imputation, interval methods, Wilson sensitivity analysis, virologic endpoints, PK/exposure-response models and sample-size precision.
- NCT03368235 — excluded: protocol pages 44-47 expose the decision framework, populations, primary mixed model and thresholds, ANCOVA, PK and sensitivity analyses; SAP is post-completion.
- NCT02569398 — excluded: protocol pages 119-124 expose sample size, estimand, MMRM, Kenward-Roger inference, gatekeeping, adaptive modifications, futility, PK, biomarkers and safety.
- NCT03425656 — excluded: protocol pages 46 and 50-52 expose noninferiority assumptions, populations, missingness, primary interval/success rule, secondary and safety analyses; the same-day five-page SAP is not an independent hidden target.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02510794 | protocol leakage plus post-primary SAP | 234 / 53 | 436c315a9b35aa9b72c497721d6ccb724d2ec5546f383f25dbc1e4dccb20c499 | 9e15c08e71077a961d0c21afc14d94fba9ecda45ccd9f5ea540cff62501178a2 |
| NCT03757130 | protocol leakage | 114 / 28 | 97e8f7e8129141c12569dc1902ff2c0b52d1fa82c888b6b7be236206e0b3c61d | b7445f5a82a88bdb2d20484a12ee20b59f8aab899133c67fb0b18fab2012ad54 |
| NCT02620046 | protocol leakage plus post-completion extension SAP | 120 / 45 | 009197784d1b330e66166bd6c9e101e446fc2ad9f85b043eca186eac24648099 | a1de7ff697d843c3504a0f39d9fbe2c21f1064ac3a82cffe26e9c8a14bd90d27 |
| NCT03285711 | protocol leakage | 121 / 33 | d22d0a03b335afd1e0692a4036c79ff43915467b0bdb3287f1f729bca74ac52c | cf5a7f251801d81efc73c22e877e7cb73706f0ffd62297f4bd1005fac17b00b1 |
| NCT03069365 | protocol leakage | 116 / 51 | 64297c4feefc4d79d5185cefcbc94e84e80604ea2790e68a89b3296a82c4dd9d | 71472326523de108c55fbda73c9aefac8091db25bafd832eb735e567d8603137 |
| NCT03368235 | protocol leakage plus post-completion SAP | 55 / 42 | 20386350a7aaad557d6dcd2574f10301d99fb462ffbaf3d8be2f625bda308cf7 | d214e38fc2a859157e1e775ed4a988efcd3cdbe3318c27f1504be3f572677fa8 |
| NCT02569398 | protocol leakage | 163 / 70 | 39d67847a72404d81c4a57a69a697a86cbcd2ee1c393ca81d3b9ff3ce1843e91 | f27058c3b03ae606687e73545ce0a0a0cb85302ea0483736ac86cf2dab51418d |
| NCT03425656 | protocol leakage plus non-independent same-day SAP | 68 / 5 | 4324aae9e025347441ab3ab44fe82a3a55e3f8ef7cb775d22714818a2ffba74c | 10cdab452d7a7eb6bd28d7982eff0ee4c7746f2c476153638f90ff097ea5fc84 |

## Review gate

No Batch 62 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
