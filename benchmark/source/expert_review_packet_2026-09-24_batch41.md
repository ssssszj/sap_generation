# Expert Review Packet — Batch 41

## Scope

Batch 41 reviewed eight ClinicalTrials.gov protocol/SAP families. One family passed the independent-target gate and received a 20-item first-pass annotation; seven were excluded. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity and decision-defining pages.

## Promotion

- `NCT02469610` → `PUBLIC-INTERCOSTAL-BLOCK-TIMING-001`. The independent protocol and SAP share the exact title, investigator and Carmel Medical Center site. Their dates, 2016-06-28 and 2016-10-01, precede actual primary completion on 2017-01-30. The five-page protocol defines the prospective randomized beginning-versus-end intercostal-block comparison, 30-per-arm target and outcomes but contains no statistical tests. The two-page reference SAP adds t, chi-square and two-proportion tests. Its unresolved endpoint hierarchy, repeated pain derivation, analysis population, missing data, multiplicity and questionable use of categorical tests for unspecified pain data are exposed as `needs_confirmation` items rather than hidden required facts.

## Exclusions

- `NCT01927367` — protocol pages 25 and 28-29 expose cluster-adjusted power, ITT, multiple imputation, GEE, alpha and sensitivity analyses; SAP is post-completion.
- `NCT05041803` — protocol page 47 exposes populations and descriptive methods; SAP Version 2.0 is post-completion.
- `NCT02582814` — protocol pages 17 and 90-96 expose analysis sets, MMRM, LOCF, multiplicity policy and sample-size reasoning.
- `NCT03920254` — protocol pages 58-59 expose descriptive methods, the safety set, subgroups and sample-size logic; SAP is post-termination/completion.
- `NCT03395223` — protocol pages 46-47 expose populations, missing-data and outcome summaries; the reference is a later pooled Data Summary Plan spanning a second registry.
- `NCT03590613` — the compound protocol exposes descriptive, exact-binomial, Bayesian and PK precision analyses plus analysis populations on pages 37-39 and repeated amendment pages.
- `NCT02628600` — the reference is a CSR appendix containing a final post-completion SAP and explicitly describes second/final analyses.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01927367 | leakage + post-completion SAP | 48 / 19 | `b0d4930f9f64dbde8c33a95227c0a7e0b61019e518a30e2721e6495d8ffd3cb8` | `c1a4835d4dec5287060f537e733beab53629bcfd65669fe70a4f5a0b3297a763` |
| NCT05041803 | leakage + post-completion SAP | 59 / 44 | `97f491b3ef1d8a329179bae8535480e77887b513a9cb6ebcc54fc4ea3e4de401` | `e9b83e0d4989b6a8a7d4046ed5fe4f7f2548ac75fbc77b026e2b19fb6d1df405` |
| NCT02582814 | protocol leakage | 110 / 59 | `0eadf48d1f48b70a2f68e547c5b8e8f2a2bc7024e1260637a55579cfa7d0f8fc` | `bee6fc4df64ba80ab84e8d9368fcfac2c02f4e03848b3f03fc30f7b247f6050d` |
| NCT03920254 | leakage + post-completion SAP | 84 / 29 | `22cb9f9b8655be394e63372bf3f1c5f53f0f7917eeff2367257d4d5208a35853` | `d6b074afc8483414df4d98163256ab10dfdacbb0c1b0ad315e8268b9f6aea48e` |
| NCT03395223 | leakage + pooled post-completion plan | 67 / 35 | `7949c9ec5a4b047623e0b1b88467ad1acdc90e78603d0ad4dc9dfab8cce16dcb` | `23c4c83391dcf7084a5dcb6ba6ef51953371eabfcb578c6183f094044f0237f1` |
| NCT03590613 | protocol leakage | 152 / 50 | `a44b96f762feab32da16cb6276f03f0c332dcc63719b99f6c26bcdb18aa8aca6` | `a80739c2d28f82a469ff5ad7c58cd2893d85be56b14200f38172755b05814df2` |
| NCT02628600 | CSR / execution-informed plan | 93 / 83 | `4235db963fd7c79f4b54f94225bbf078903a4b2e33bd7d00bfae3c5a0e1b31ca` | `4ecad1fd1712bb01218b5f70c393d34bb456139f6d4fee2e51f8a40ba74e1cb6` |
| NCT02469610 | promoted draft | 5 / 2 | `00ef1b78786317644adad7be800eefbd60a8ce51018a6af4a0068e4364994e89` | `0ac80cee0f1ea71d4eb36cc654a17ce02337178a28d011f6bb9bb02732182369` |

## Review gate

The promoted family remains `draft_needs_expert_review`. The seven excluded candidates cannot enter train/dev/test and their slots must be replenished.
