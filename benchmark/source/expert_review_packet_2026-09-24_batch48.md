# Expert Review Packet — Batch 48

## Scope

Batch 48 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent prospective-target gate: seven packages expose executable target analyses in the model-visible protocol or use a non-independent SAP excerpt, while the remaining package is explicitly interim-informed, unblinded and post-completion. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining statistical pages.

## Exclusions

- `NCT02341534` — the protocol modification reports a completed interim analysis, observed reporting bias and changed termination/alpha strategy; post-completion SAP Version 3.0 states that its authors were unblinded.
- `NCT02835092` — protocol pages 33-34 expose power, populations, repeated-measures ANCOVA/GLM models, Dunnett correction, safety testing and imputation options.
- `NCT05156125` — protocol pages 98-103 expose populations, power, ten-test multiplicity, exact CMH primary analysis, missing-data/sensitivity structure and timing; the SAP is post-primary.
- `NCT04341662` — the post-completion public protocol uses accrued baseline data and pages 36-40 expose the sample-size update, mixed-effects primary model, marginal standardization, covariates, sensitivity, subgroup and missing-data plans.
- `NCT03230292` — protocol pages 61-64 expose analysis sets, exposure-adjusted safety analysis, efficacy handling, interim policy and sample-size basis; the SAP cites that exact amendment chain.
- `NCT02781571` — protocol pages 72-77 expose analysis sets, HCV-RNA imputation, exact primary analysis, secondary/safety summaries and sample size; the SAP is post-completion.
- `NCT02713178` — protocol pages 5, 11 and 63-68 expose primary analysis, populations, missingness, the complete multiplicity graph, sample size and observed interim PK findings.
- `NCT03341091` — the alleged SAP is a two-page extract of the same-dated protocol and repeats its tests, mixed-effects model and imputation policy rather than providing an independent target.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02341534 | interim-informed and post-completion | 10 / 74 | `fbb71ca5f24ddbce7818122d3899964973f2af33b775c34f61a43b327df62bb1` | `157df8aa193f5894bc3595e06aec98c65ada82530b61407dbef6fc381c9a53fe` |
| NCT02835092 | protocol leakage | 68 / 51 | `c1069d99b5c635e7a946e574b135050e0eeca673293cbb41e4a75a3b2bb8f34a` | `40122169c2a58fda8af6ff2df4e95fff7b5ba4cf259d48c9959b388b6b1fb77b` |
| NCT05156125 | protocol leakage plus post-primary SAP | 128 / 96 | `5905c9a5315a8c3db7fea1d6a60010d0e1089b2e2b5a7316c64de71792172687` | `9cfb988388b646650ff79f29bd8706c6d251fff08853f03673dc1ee30e89837e` |
| NCT04341662 | post-completion, baseline-informed protocol leakage | 51 / 53 | `83e0dc70be4a25304e36a393f0746c56c1c7b3dcb556be41f7f28927d769bdc0` | `49f85c56eb27e24c6b49262578e6fe4b29883d5453fcf8944432775a4dca260c` |
| NCT03230292 | protocol leakage | 79 / 58 | `a7a073c068c55080e4596fb53cfbf72a266e6fe73ae4dd18b8cf6a5b7ff2ffc4` | `8569047bf2d7937bbcaec4bb3a256e808a7a5feb3572fbde24d22d765b972080` |
| NCT02781571 | protocol leakage plus post-completion SAP | 117 / 40 | `11460c1dc497526358fa6b8e4bc6b5a991a2e43e1df5fe5119925eae7fc6dde7` | `73e63ea196de3671c12b02f06632661b4a70363052aa47e9a5d4f2f891c4f81a` |
| NCT02713178 | protocol leakage plus observed interim PK | 88 / 173 | `52f81063c71855ca987d411773acf1bc20ee38007a4e02b1d45278c2d689832d` | `72d31ba7590f27154677125144e24660de662361a731e09cc0936557a0445505` |
| NCT03341091 | duplicated non-independent SAP and leakage | 11 / 2 | `93b6f9347b6fb582c9b7f39411aa65ddd5126881e682b583d7c5505f1e06b1b7` | `c49f400c714ad8e5f5d7a65bedbb6d437b5728bc68ee4678b62b2f504591c90e` |

## Review gate

These eight candidates cannot enter train/dev/test. All eight slots must be replenished; no Batch 48 record is counted as a completed benchmark question.
