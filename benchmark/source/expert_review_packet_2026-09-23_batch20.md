# Expert Review Packet — Batch 20

Batch 20 promoted one version-verified study and rejected seven pairs at a hard source-admissibility gate.

## Promoted study

### PUBLIC-ACTIVE-DUTY-LBP-001 / NCT03502187

- Study: *Home-based Approaches for Subacute Low Back Pain in Active Duty: Randomized, Controlled Trial*.
- Version chain: the independent six-page protocol and two-page SAP share the exact official title, NCT03502187 and 2018-04-17 date. Both predate the 2020-05-28 primary completion.
- Leakage check: protocol physical page 6 says `Statistical Methods – See Statistical Analysis Plan`; it does not reveal the SAP's longitudinal mixed model, active-versus-usual-care rate-of-change contrasts or missing-data language.
- Annotation: 22 atomic evidence-backed requirements cover the three-arm design, four visits, strength/activity/function and patient-reported outcomes, prospective sample target, adherence, longitudinal models, contrasts and unresolved estimand, model, missingness, multiplicity and safety decisions.
- Review focus: confirm the broad primary-outcome hierarchy, complete the mixed-model specification, and adjudicate missing-data, multiplicity, effect-reporting and safety rules.

## Rejected pairs

- NCT04118270: `excluded_combined_protocol_sap_leakage`. Protocol physical page 7 reproduces the complete two-page SAP analysis content.
- NCT03028363: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 34-41 expose the endpoints, ANCOVA/logistic methods, center pooling, MCMC multiple imputation and sensitivity analysis; the SAP is also post-primary-completion.
- NCT02911948: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 72-81 expose populations, sample size, ANCOVA, LOCF and sensitivity analyses; the SAP postdates primary completion.
- NCT02903966: `excluded_wrong_document_type`. The 110-page Reporting and Analysis Plan became effective after primary completion and contains interim/final analysis changes.
- NCT02548143: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 57-59 expose populations, exact primary analysis, safety summaries and interim plan; SAP Version 2 is also post-completion.
- NCT02962960: `excluded_wrong_document_type`. SAP Edition 2 postdates primary completion and records execution-sensitive early-discontinuation, exposure and event-definition changes.
- NCT07084948: `excluded_wrong_document_type`. Both files postdate primary completion; the SAP reports actual enrollment, completed follow-up timing and an already performed DMC review.

## Source audit

All 16 PDFs were downloaded from the ClinicalTrials.gov registry, hashed, page-counted and extracted by one-based physical page. The promoted pair's cover and substantive pages and every exclusion-defining page were rendered for visual inspection. Reference SAPs remain annotation-only artifacts under the gitignored source tree.

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT04118270 | protocol leakage | 15 / 2 | `4530649a42e16189d1b3bd1fe4e870101bc191ec8c58054ec6cef9a474f78a7d` | `99c323f79282cf8ebc9b71f39286c9da915e86a81a9792b841c188f331fe0f2e` |
| NCT03028363 | protocol leakage | 52 / 27 | `a4032703323b61a8e8857f3febeab185fcdd6027796308597acf5331e7f4d89f` | `c7e395c0408791d1cb1685cf4673b29daab60813bc400471e051d4599315d4f7` |
| NCT02911948 | protocol leakage | 131 / 16 | `c1b1bb1d20598e3cde9095e530426a54a75b32bb8338f226442272d46623531d` | `68d2d0dfa2bfbb092e5642b26d8f3b5d1a19b87343c51264431196498da05d95` |
| NCT02903966 | wrong document type | 111 / 110 | `83e7b18823f1cfef5ef69fae59da193a31282d671d2e3c1c901c90d5bd77129c` | `f6626394649288fab35a52d97225e9a8c0043092b8576e2b2b09e741b643ee6d` |
| NCT02548143 | protocol leakage | 69 / 24 | `23ce6efd7bad743eaf5c4a19425cd83b667f4d155f0fd91d5e0b5363f0dd614a` | `6fba5cdefe4db2fde428c22f74c5c9577123c59139e89b004eb60468774e39c6` |
| NCT02962960 | wrong document type | 131 / 49 | `808150869808082e5f1d5c6ee44bf8bf26be537c232862b7332a55f9bcb94528` | `ffb56b05f5834691635a10bc8591500a82cfa6dd8623204d662de53979ba4491` |
| NCT07084948 | wrong document type | 5 / 2 | `0ded2627af1f731eed200ae00ba7b4b6d55007ba122a5c59781450780e6c4062` | `69037cddf6d12018d0256c0e8f600aac691a67086bb0c3b36de2f9443cc5e9cb` |
| NCT03502187 | promoted | 6 / 2 | `36f724a1513a07bc2c0b43f6d9a137e4411dff3e2b7feb8dace1b620096a192e` | `4fe9dc39e3a289f7b41469616c7cf7d761be2aa9ec260e9cb6254e1ddc40f738` |
