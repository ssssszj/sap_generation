# Expert Review Packet — Batch 69

## Scope

Batch 69 reviewed eight ClinicalTrials.gov protocol/SAP families. No family passed the public, prospective, version-matched, independent-hidden-target gate: seven model-visible protocols contain enough executable statistical content to make the reference SAP non-independent, and the remaining otherwise prospective pair has material public redactions plus unresolved document identifiers. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology, formula and decision-defining pages.

## Exclusions

- NCT02862600 — protocol pages 42-44 expose endpoints, t tests, assumptions, power, populations, analyses and a data snapshot; SAP is post-completion and internally cites both Protocol v11 and v10.
- NCT02060383 — protocol pages 79-85 expose populations, models, covariates, missing/rescue handling and sample size; SAP is post-completion and records technical-data and analysis changes.
- NCT04168385 — protocol pages 75-77 expose the descriptive extension plan; the rollover depends on predecessor-study baselines and its SAP is post-completion.
- NCT03389893 — protocol pages 73-78 expose populations, ANCOVA, sensitivity analyses, repeated-measures models, multiplicity, hypotheses and sample size; SAP is post-completion.
- NCT03231943 — protocol pages 68-72 expose sample size, populations, PK/safety analyses and Bayesian dose-escalation models and include observed SAD/MAD data.
- NCT02844465 — protocol pages 59-66 expose power, populations, primary performance criteria, the full hierarchical secondary sequence, interim rule and multiple imputation.
- NCT01767857 — protocol pages 60-64 expose the complete group-sequential survival and secondary plan; the public SAP bundle adds post-completion patient-level hard-coding decisions.

## Hold

- NCT03908476 — SAP pages 4-7 redact the analysis population, endpoint-test specifications, sample-size calculation, interim analysis, success rule and multiplicity decisions; registry, protocol, SAP cover and SAP headers also disagree on the governing document identifier.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02862600 | protocol leakage plus post-completion/version-defective SAP | 58 / 31 | 110067038c46363e3bffa7197600dff43d4e40b712d754cd8f6d1fad87c05933 | 5583e4cd837a796b29c69fcf6e76e5029d347e3b084f02546c969d322d1c4040 |
| NCT02060383 | protocol leakage plus post-completion SAP | 94 / 27 | a654376544451ddbad67c5252aaf41eb8788e502c53462f9e82f86a9f59653ce | acf891a79e24cee7aa6d28425a2dc13c9eb702553cdeaee2eda035a75a4f8b95 |
| NCT04168385 | non-independent rollover leakage plus post-completion SAP | 117 / 38 | 3f98162171a3a716bae9e49a31a3c16f495fc76a26970f06ac3eaf04767c65f0 | b5eee6631f547845f643c6f6f970fc265fad1c530a23786c8d90265ec22c1295 |
| NCT03389893 | protocol leakage plus post-completion SAP | 91 / 25 | 02d87ff5e7484cd6c6c349d1d4599ec20f7b9691b5747d2b9932b32f6dfb7493 | abdc09f9ea3176a383de5c69d325ea98fc27a648de1cc17a3dca70b71cac2b92 |
| NCT03231943 | protocol analysis leakage using observed dose-escalation data | 151 / 81 | 509c298ecee1550f0bb19d8a307481c72576f0fa4653496fbabd21ce182445d8 | 42bf0b03b635aa130334f5425bea39d92e1d7f1344d1f504af9b705a69760807 |
| NCT03908476 | public-redaction and identifier-reconciliation hold | 38 / 9 | 6d0b334049557f6ad958135b5a91c116a2f3d97563573f7c71280a0b1abf66b8 | 0507469dc1498c15dbb64e8bd95ca3fe2bf41df954c5104daebaef268e22dd88 |
| NCT02844465 | protocol analysis leakage | 86 / 24 | 630a27597ad95d9be05faf4b7bd05409ff5f531edc96b2099b51350567b608fe | 01c72cc00ff2f2cf2073d388b20f34ee4605a7071291d3b64f5c4ddc1c012033 |
| NCT01767857 | protocol leakage plus execution-informed SAP bundle | 74 / 43 | fa4710f91942413532bbfac15458325057ba5e8af058a5691df09b8e972d01aa | f590213cd0a922351ce135b99c9b8a873363d8e2c7266bac4a9ab05293929246 |

## Review gate

None of these eight families may enter train/dev/test. Seven fail prompt/reference independence, with additional chronology, execution-informed or study-family defects where noted. One remains on hold because critical public content is redacted and the document chain is inconsistent. Batch 69 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
