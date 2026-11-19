# Expert Review Packet — Batch 59

## Scope

Batch 59 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent-target gate because every model-visible protocol exposes an executable target analysis. Five selected SAPs are additionally post-primary or post-completion, and both public NCT03503370 documents are retrospective. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. The 637-page NCT02477800 protocol has no usable embedded text, so its identity pages and governing Version 6.0 statistical section were OCRed and then confirmed against the rendered originals.

## Decisions

- NCT02541591 — excluded: protocol pages 32-33 expose populations, ANOVA, imputation, endpoint-specific models, Kaplan-Meier/log-rank, subgroups, sample size and the no-interim rule; SAP is post-completion.
- NCT03503370 — excluded: protocol pages 17-18 expose ITT time-to-event, Kaplan-Meier/log-rank, censoring, Cox/competing-risk sensitivity analyses, adherence moderation, Wilcoxon and power; both public documents are post-completion.
- NCT02401035 — excluded: protocol pages 50-51 expose simulation power, population-PK model structure and covariates, safety and no-interim analysis; SAP is post-completion and revision-aligned to that protocol.
- NCT04652245 — excluded: protocol pages 60-63 expose populations, baselines, primary model, hierarchical testing, sensitivities, missingness, safety and no-interim analysis; SAP is post-completion.
- NCT03008070 — excluded: protocol pages 65-72 expose power, sets, CMH, Hochberg, nonresponder imputation, heterogeneity, sensitivity and secondary models; SAP is post-completion.
- NCT03254459 — excluded: protocol pages 37-39 expose safety endpoints, population, sample-size rationale and all descriptive safety analyses.
- NCT02477800 — excluded: scan-only governing Version 6.0 pages 623-628 expose ITT, MMRM, closed testing, adaptation, interims and sample-size re-estimation.
- NCT03719300 — excluded: protocol pages 51-54 expose populations, exact-binomial power/analysis, response derivation, Kaplan-Meier, futility, time-to-event, missingness and safety.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02541591 | protocol leakage plus post-completion SAP | 40 / 15 | 72fb9155f0b8a2a8216b45769eeb343f9bca1affa89073e648e1a7ac7dcc4e88 | 5c6240d096cedc6c92dd8836a2cd04b167d695cc2ec6f6872cc15c1abc8e3fda |
| NCT03503370 | protocol leakage plus retrospective pair | 24 / 3 | eb869004968545a566975bb0978edba4a67bfca84d8842c1d024d4e9fc3d2d0c | 6aed2ab5dbb580fe958b092789db87955385bb7120f5fb7f096db52507aa04b9 |
| NCT02401035 | protocol leakage plus post-completion SAP | 61 / 14 | 29c5304b0438e85503c7714262aa46742377f0f697ccba5683fd3937fc8dc14f | 2bc2b70a382d2c7c005c1b4671a5dadc3cf471fe4bc941143d763d8b496ec0be |
| NCT04652245 | protocol leakage plus post-completion SAP | 81 / 23 | 503e1b1a6b444284eef906ed3d2da05c40f95285947a1256b1d69194d3e4d6d2 | ce6aacb7f72296574584f59088b328de797c33101bb7bcc53e9cc11e8bbda9b6 |
| NCT03008070 | protocol leakage plus post-completion SAP | 106 / 106 | 67d3afab381f1edb7e3ef9438e5b0cfb4567f4a5da0e8ee49d2d0e5affd66cd3 | 8c0e9a1e57992f7a9118c4e729f680fbbda070253feb6ea83e21be529a6f56f4 |
| NCT03254459 | protocol leakage | 60 / 96 | cba21373cf93902c3970798f8b7ba1f00eddbf33c33344bd799a08a33ec674c7 | 91afe440e175210f8b1bec046b09da6d7ab61750a7711361e3d6ea201a9cbb83 |
| NCT02477800 | scan-only governing-protocol leakage | 637 / 91 | 5efc05f5ac2f2fe55f305d924b9fb0b23fec8829ab0b91fb8aebd54b44b5dc45 | b50c49d90ad339ed1bd5c07bd2b9c550c743b3ac7119e838bd1063eb64414afe |
| NCT03719300 | protocol leakage | 63 / 38 | 1df42e5185a3185595a6fd97f085d824a6c44b2096ddfc1aedf5a3ab9b1d338a | b94361c7c9484b6b3febb6235333eedf4ac800253479fb9f7ef120354794c792 |

## Review gate

No Batch 59 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
