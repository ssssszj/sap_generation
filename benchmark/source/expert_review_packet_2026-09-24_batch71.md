# Expert Review Packet — Batch 71

## Scope

Batch 71 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the public, prospective, version-matched, independent-hidden-target gate: six model-visible protocols expose executable target analyses, and the other two selected references are post-primary or post-completion execution-stage plans. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology, statistical, redaction and decision-defining pages.

## Exclusions

- NCT02917031 — post-completion Protocol Version 5 pages 69-74 expose the complete noninferiority, population, ANCOVA, imputation, MMRM and sensitivity plan; the SAP is also post-completion.
- NCT02471404 — protocol pages 85-92 expose the noninferiority margin, sample size, analysis sets, full hierarchy, MMRM, rescue handling, sensitivity analyses and secondary models; the SAP postdates completion.
- NCT02022826 — protocol pages 54-58 expose the precision design, interim, PPA/NPA methods, confidence intervals, bootstrap analyses, missing-data summaries and stopping rule.
- NCT05999799 — protocol pages 99-104 expose the Bayesian estimand, analysis sets, repeated-measures and logistic models, intercurrent-event handling, imputation and interim logic; pages 104-106 also obscure the sample-size content.
- NCT03235349 — protocol pages 96-104 and 108 expose populations, imputation, SVR estimands, confidence intervals, subgroup and resistance analyses, PRO handling, PK models and sample-size rationale.
- NCT03952377 — the CSR-stage SAP bundle postdates primary completion, reports the observed 55-patient termination, replaces planned efficacy tests with descriptive analyses and adds a topline analysis.
- NCT02975349 — the public protocol is a 2023 late amendment after 2018 primary completion, while the Final Analysis Integrated Analysis Plan was signed after 2024 study completion.
- NCT01797120 — protocol pages 84-85 expose the PFS definition, stratified log-rank design, alpha, power, event/sample-size targets, Kaplan-Meier, Fisher exact and safety-precision analyses.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02917031 | protocol leakage plus post-completion documents | 82 / 46 | 1b95533ea42dcc63cc8e7fb1fad8ebe229e2b30da271102ab9ec270e91bcf44d | f78b4d4789f176582e1628cd8723146ca5b55344da9b0664f07fe3bfc2f16363 |
| NCT02471404 | protocol leakage plus post-completion SAP | 123 / 74 | ae9ef6c186719c3f5ab8f4a5814cfcb71930be45892d7d373a00573b98c8beea | 19d579762bbb6b54e79977a81f63753bdcf438546b6e36d1a807a5a64b28800b |
| NCT02022826 | protocol analysis leakage | 111 / 21 | d4a7188127ce4bf628ec12299eb0667f95a768905ec5d14553d11a79f6fefcff | 41f2a578c58a726acbdd6c0015dc2c07ba260276c5797f5ea7ae8bb4d0b52d59 |
| NCT05999799 | protocol leakage plus material redaction | 141 / 84 | 547b8c0b23d5c8161887a62ff3ea7962dad3978389beabc98e27b096d838ef34 | 12c8ee905eed4e220fa3d0d2619fc875c47d48ab9ac23e81bc767f3a7c6a39a5 |
| NCT03235349 | protocol analysis leakage | 129 / 61 | da0985034fc9dd7a72ba124094aaa388ec27ff2a1792e63b2ec4e0b60293f6ba | 663cae1c67d0cde4475f8264f1accc7b46af31d0dd9d43c3e397778742c34abe |
| NCT03952377 | execution-informed CSR-stage plan | 148 / 62 | e4f4506608562a09ce49082542f4fbf9f5bbf2b730f6f2d82a2ba7e89bfb074c | db36fb1f00ef503e30e891ba7b686dd4455b6fa48311fc362cf4c53902fad5a1 |
| NCT02975349 | post-completion final-analysis package | 131 / 62 | d40bd638e93040b4efaa3abd3d63254d1f76dd613dc7472507dcd99e35ad4add | 94badbff8f339a3802a2de09eac7e1c724affa391a5b322a75b1cb0c8766907b |
| NCT01797120 | protocol analysis leakage | 115 / 36 | ce891945ed16f875345d2781bd287c51e2a28a99008cc5dd46a2b949e7a3000c | 22f3b11e4724428082e03d51ef328be872c4d49b56a01397d110793cc66d1397 |

## Review gate

None of these eight families may enter train/dev/test. Six fail prompt/reference independence and two fail prospective-governing-plan provenance. Batch 71 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
