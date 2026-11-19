# Expert Review Packet - Batch 112

## Scope and decision boundary

Batch 112 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen official PDFs and eight registry records were downloaded sequentially, byte-checked, SHA-256 frozen and extracted page by page. Ninety decisive identity, chronology, statistical, sample-size, missing-data, interim and document-type pages were rendered from the original PDFs and visually inspected. No family is promoted: four expose or duplicate the executable target in the protocol, three use post-primary, manuscript-stage or interim-informed plans and also leak the target, and one is a core-study-dependent extension whose protocol discloses its program.

## Decisions

- NCT05897073 — exclude: protocol pages 36-37 reproduce allocation, power, ITT constrained-baseline mixed modeling, covariates, pairwise comparisons, practical-benefit reporting and sex interactions; the 2024 amendment is also near primary completion.
- NCT05368103 — exclude: protocol pages 57-60 disclose n=30, probability targets, safety/PK sets, Week-24 SALT percent change, 95% intervals, prohibited-medication and discontinuation rules, LOCF/nonresponder missingness and safety analyses.
- NCT02634333 — exclude: SAP Version 3 says it followed submission of the primary two-year manuscript and changed the COVID visit window; protocol pages 37-43 also expose the executable time-to-event, visual-acuity, multiplicity, missingness and power program.
- NCT03255174 — exclude: protocol pages 26-27 reproduce the ten-page SAP's four analysis sets, descriptive effectiveness and safety program, confidence intervals and missing-data rules.
- NCT04132050 — exclude: SAP Version 3 follows primary completion; protocol pages 80-87 expose populations, endpoint response, Fisher/Clopper-Pearson, multiple-imputation sensitivity and safety.
- NCT02770170 — exclude: the revised SAP follows primary completion and records post-interim endpoint-derivation changes; protocol pages 61-66 expose MCPMod/logistic analysis, alpha, interim, NCF missingness and power.
- NCT07137026 — exclude: the complete two-page plan is copied verbatim into protocol pages 11-12, including mixed models, interrupted-time-series Poisson models, covariates and power.
- NCT01197300 — exclude: this extension depends on the core trial's randomized groups and baselines; protocol pages 52-61 also expose its analysis sets, group comparisons, models, missingness, intervals and sample-size rationale.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT05897073 | protocol leakage and near-primary amendment | 43 / 33 | fc628da53cb4ea7c43ca51e3e0c29d99d0b6b4903626029c205b42976bed5d04 | 270d73d7627bc93697aca8822a0517269639e47eabf977a28f6c6d3d3dc93e2a |
| NCT05368103 | protocol leakage | 75 / 26 | 55629cdd422a754987f031820bbc91cdd68fb061129e0b8dbe0b328166089c97 | a789fe39ae4f4de7d5907873c3c9aa0bd750044c72353a31f4b6f696235242db |
| NCT02634333 | manuscript-stage SAP and leakage | 48 / 15 | a19dd12e5d1cfa5458040ce3a81f18b1461a315fe89449ba1e509b7beb3866bc | ccba608a65e659a335b0c2ed504e7e340c4e6d943c2eddc02e42352f6ebb71c5 |
| NCT03255174 | protocol/SAP duplication | 37 / 10 | 6acf3ddafdbb9cd7335538ff7678181315c2f3ce97656959f12fc93b67241f10 | 01a3c64ee6cbc8129c260b3dae99d4c8d8da94de761653418d695abf8d2ad122 |
| NCT04132050 | post-primary SAP and leakage | 100 / 35 | d7eb3926e3241928bda0a532326db271018a4254cf126bc3f68e52f0de21a003 | eb0e2b9d45fe03d0fc41f0c5093e1006f1c1b49a5e1b822ffb5b973c93bf53f5 |
| NCT02770170 | interim-informed post-primary SAP and leakage | 118 / 39 | fcfcd1745027bb431d8a3a7b6030fb30f8e7beae8a598b581c11521fc6f26c40 | 3ccb6bb927bda52153b54bde8ff52aa04d81f711029e5b33e65c739deeaf9928 |
| NCT07137026 | protocol/SAP duplication | 12 / 2 | 18f7bd0426a78325f068f919a8bc8267ea00d47bc69fac7d0ccb95d3ceae9bd9 | 2b4a13011933fcc7a4674c0542b3ef9dfb884028f94c565258104795e9fe40b0 |
| NCT01197300 | related extension family and leakage | 79 / 22 | 5d72e679a69bc48500ee2d2da477f79cd4b194ee41b230263ab64465aad33f99 | f53f32291f27cb82b9e6d9077a88d7b2824b7f8fc08e03124739636f1243c242 |

## Review gate

No Batch 112 family enters the registered benchmark. All eight slots must be replenished so the release intake remains 100 version-verified public drafts plus 20 actionable metadata candidates.
