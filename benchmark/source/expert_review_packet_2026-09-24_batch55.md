# Expert Review Packet — Batch 55

## Scope

Batch 55 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent-target gate: every model-visible protocol exposes executable statistical methods, and four document chains have additional post-primary, post-completion or governing-version defects. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. Visual review confirmed the statistical content despite the malformed NCT01529034 SAP text layer.

## Decisions

- NCT02506244 — excluded: protocol pages 13-16 expose cohort comparisons, Bayesian analysis, event-rate assumptions, powered sample sizes and log-rank design.
- NCT03320941 — excluded: protocol pages 54-62 expose five analysis sets, MCP-Mod contrasts, multiplicity, ANCOVA, multiple imputation, responder and repeated-measures models, safety and power; SAP is post-completion.
- NCT01029353 — excluded: protocol pages 2-3 and 12-14 expose logistic, Bayesian, propensity-score and comprehensive-cohort analyses, multiplicity, sample size, stopping and sequential-monitoring rules; SAP cites the original rather than revised protocol and was last revised in the completion month.
- NCT04294667 — excluded: protocol pages 96-106 expose analysis sets, primary and sensitivity analyses, missingness, full multiplicity hierarchy, survival/subgroup/safety methods, monitoring and power; SAP Amendment 3 is post-completion.
- NCT02939989 — excluded: protocol pages 98-107 and 197-200 expose populations, imputation, exact interval switching, sensitivity/subgroup/resistance/safety methods, interim intent and revised sample size.
- NCT03025308 — excluded: protocol pages 73-77 expose analysis set, data handling, efficacy/safety outputs and analysis schedule and disclose that a prespecified interim analysis was already performed; final SAP is post-completion.
- NCT01529034 — excluded: protocol pages 78-83 expose analysis populations, safety summaries, generalized-linear mixed and Kaplan-Meier analyses, and sample-size rationale; SAP is post-primary-completion.
- NCT02627963 — excluded: protocol pages 63-67 expose event-driven power, analysis sets, log-rank/Kaplan-Meier, alpha spending, futility, censoring, CMH and subgroup analyses.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02506244 | protocol leakage | 23 / 24 | b2393adf5a0ba86264deb281a88334c68cec2f382de3f2ff131baba371d28805 | 97f0dd55d540ee740645e7febc986c0dd2c2db3116f4d22b875eaea39c3eb035 |
| NCT03320941 | protocol leakage plus post-completion SAP | 69 / 45 | 8a378349061139dd562f57868faf69af776d804c9650e66f619f01b7059c6747 | d3f84d9165cf75c747301c9f87c3f5ba69e13bf38d15388116d1d4de61857418 |
| NCT01029353 | protocol leakage plus version mismatch | 16 / 30 | 38edae080613c69e2dbea35ed4a562d0a4e5c29cf5baba15786589d60824716a | 9bf428ef6e51b68b20c3976d2631c0c0bd24ef0ee818972e9099e375d3865f1d |
| NCT04294667 | protocol leakage plus post-completion SAP | 186 / 155 | f434ef797bc2e0daccb1f00c7f1878ed280ffadf5f0ca857f2adbf1e28e149f9 | 295a72c2ae1cbf563f51805f169f22d59e76c9e17b8baa23452a0ac6c0c6ed5d |
| NCT02939989 | protocol leakage | 214 / 51 | df6babafd02a5e72a42375a8e8c05cac4c04646d806791a0ed56fc943001a82d | f5e37057f7e90f0333f00eea8ee4bdb8420431959d2073264b149f3347a011be |
| NCT03025308 | protocol leakage plus execution-informed post-completion SAP | 102 / 66 | d4cd2591e180fbe4fb15905fd9edbdd41fae27f9220cc3ec667de48b50a6f12d | 092c3f8b79b9834b224e3ce67cc958fc0dfeef18d08004dda31367007e320cf1 |
| NCT01529034 | protocol leakage plus post-primary SAP | 124 / 91 | 5d8d8608525eeaa52d6f0ecc7ea9efa8b7e9a9819dd595862bd191f631bc4ea6 | d70569604da09283174442a86267f59710f196d91a048305ab20dabad1721dcf |
| NCT02627963 | protocol leakage | 111 / 33 | 8e1d444995e8bb0e8511ebc67e54a2c2826afe480ad959a2a1aaf5c9fb262b32 | c94d5c8f69f018232c95d67431b5b9d8bf2e10a883f7261cd7a3546063c30356 |

## Review gate

No Batch 55 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
