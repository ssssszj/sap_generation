# Expert Review Packet: Batch 127

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 127 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 894 physical pages. Every page was text-extracted; all 78 scan-only NCT03094416 protocol pages were OCRed; and 59 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT02712008 — exclude: the SAP follows completion, while protocol physical pages 6-7 expose group-specific sample size, populations, LOCF, sensitivity, direct contrasts and confidence-interval conventions; the during-conduct amendment also changed timepoints and analysis.
- NCT03094416 — exclude: the SAP follows completion and records COVID-19 early termination after realized treatment/completion counts. OCR-confirmed protocol physical pages 49-50 expose populations, LOCF, repeated-measures models, covariates, sample size and no-interim logic.
- NCT05175131 — exclude: the SAP follows completion and says the interim was removed because rapid realized recruitment made it futile. Protocol physical pages 68-72 expose sample size, populations, endpoint derivations, ANCOVA, superiority, LOCF and safety analyses.
- NCT04370054 — exclude: the during-conduct Amendment 10/SAP Version 6 follow multiple interim/regulatory revisions and change data-cutoff timeframes, populations, sample size and analyses. Protocol physical pages 96-104 independently expose the executable program.
- NCT02945657 — exclude: although the SAP predates completion and binds Amended Protocol 1, protocol physical pages 68-70 already disclose the core short descriptive target, including populations, PK/NCA, BLQ, trapezoidal AUC, safety tabulation and no interim.
- NCT02532283 — exclude: SAP Version 2 follows study completion; its amendment and pre-lock section change analyses based on actually measured variables. Protocol physical pages 13-15 and 59-64 also expose precision, populations, models and interim/final logic.
- NCT02585258 — exclude: the SAP follows completion and incorporates a blinded mid-trial sample-size recalculation. Protocol Version 4 states recruitment had closed at 452, uses observed pooled event rates and exposes the executable primary models.
- NCT03765489 — exclude: the alleged SAP is an executed-analysis excerpt titled as the results of a pilot randomized study and states that analyses were performed and tests were used. The same pre-start date on these past-tense documents is internally impossible and does not establish a prospective plan.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02712008 | excluded | 58 / 41 | `d3eb5f97234aba6278287ae5ab02a3bc58dfd96aabbb7767a747534ddf644ce5` | `7277f661f991131088db2aeef630fcebddf5ae8464ea89b590c27d10abfba8c0` |
| NCT03094416 | excluded | 78 / 27 | `ce2483493b50728559524157cfd66d2d6ae185882eb1a444a492b4d6f69b484e` | `b4eaa837968d8c5ac8505c3633871f8adfc7ab0ce76832779d82a7a8c7b00c9d` |
| NCT05175131 | excluded | 80 / 32 | `4bb34132bd679bfd4e9c530d5f32c5928c976cd750f9835ccd0bd9a2348739dc` | `55bf8b8ae8578eecdb391b410f92b91db19d757116fd5fbb0af3e2c7eeb7a96f` |
| NCT04370054 | excluded | 165 / 81 | `8abdce890cb1233e5ba0a1196ed723b06b3867721dee9a719a0d578229155dfc` | `6ac0750eb75c31845601c10d873920c3c45f01adb734f3ef405a31c20503f60c` |
| NCT02945657 | excluded | 92 / 22 | `7bf0273e51dc09a2d3ded5d1e33bb49778172c4bf774162a24455ff58c968b63` | `80096e575eed5562dec992b6c818b8f154a6a357d6607718953496b31a7a913a` |
| NCT02532283 | excluded | 104 / 53 | `c2796eac412cdb530714f865c1c7f5c9684c50b6f6b00824e06cb2dc4d1248dc` | `0d22955af807ed30a8a4942f33c61f94b3331f89f1827523c045cc0d495c7b43` |
| NCT02585258 | excluded | 76 / 94 | `a80754814a434c81b808c028b4382d534d4fb2ab2fd5cc475d06f54465fe68f6` | `35b64be1f69f180fbb48fb4f0d306e40773b1bcf64d8f885d101ed38ca8e319c` |
| NCT03765489 | excluded | 3 / 2 | `8ae7131afe94826dd6a45cba50ac98d5941bc2c9f0cb027b17bb021efd3a43e7` | `c28fd581bce3255cca20ef977193ed00fe7f19301b0d3fdbb244a79ab55e0e75` |

## Gate interpretation

- A document date before primary completion was not sufficient where the model-visible protocol already reconstructed the executable target, as in NCT02945657.
- Claims that a plan was finalized before database lock were not accepted when the selected version itself was post-completion or explicitly used realized recruitment, termination, measurement or data-cutoff information.
- A registry label of `Statistical Analysis Plan` was not accepted over contrary document-internal evidence. NCT03765489 is an executed methods/results excerpt.
- Registry actual enrollment remained conduct context only and was never substituted for a prospective sample-size target.

## Replenishment

All eight excluded slots were replenished from the official API. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates. The next queue starts with NCT02827500, NCT03163511, NCT04604652, NCT04700345, NCT03569293, NCT02589795, NCT02640612 and NCT07716553.
