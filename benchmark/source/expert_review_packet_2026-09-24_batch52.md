# Expert Review Packet — Batch 52

## Scope

Batch 52 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed all prospective-version, identity and independent-target gates: seven model-visible protocols expose executable target analysis content, and the remaining family has an unresolved governing-protocol mismatch plus substantial leakage in the substituted public version. Four selected SAP chains also have post-primary, post-completion or execution-informed defects. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. The scan-only NCT06007781 protocol received a full 160-dpi OCR pass before its decisive pages were visually confirmed.

## Decisions

- NCT02439775 — excluded: protocol pages 81-86 expose ITT/mITT/PP/as-treated sets, LOCF, exact-binomial safety testing, Bayesian power-prior ANCOVA, posterior decisions, interim operating characteristics and secondary methods.
- NCT03131687 — excluded: protocol pages 55-61 expose Bayesian dose-response priors, populations, MMRM, ANCOVA/LOCF, superiority/noninferiority bounds, secondary tests and sample-size probabilities.
- NCT06007781 — excluded: OCR-confirmed protocol pages 59-61 expose SAF/FAS/PPS, GMT/95% CI, exact seroresponse intervals, safety summaries and analysis timing; SAP is post-completion.
- NCT04565236 — hold for governing-version reconciliation: SAP v2.0 explicitly cites Protocol v2.0 dated 2020-10-22, but the public prompt is Amendment 2 v4.0 dated 2023-05-12. The substituted v4 also leaks sample size, populations, ABR derivation, missingness and interim intent on pages 60-64.
- NCT04181762 — excluded: protocol pages 198, 203 and 207-210 expose estimands, models, multiplicity, interim boundaries and power; post-completion SAP Amendment 3 says it updates analysis for early termination.
- NCT02880865 — excluded: protocol pages 54-57 expose ITT/safety/multiple PP sets, dual noninferiority hypotheses, Farrington-Manning and log-transformed analyses, staged timing and power; SAP is post-primary.
- NCT02960490 — excluded: protocol pages 9-11 and 61-63 expose populations, logistic primary analysis, nonresponder handling, ANCOVA and descriptive efficacy/PK/safety methods; the extension SAP is post-completion and execution-informed.
- NCT01931566 — excluded: protocol pages 98-100 and 152-153 expose FAS/PP, Cox/ANCOVA/MMRM, alpha and hierarchy, MAR multiple imputation, censoring, subgroups and detailed futility analyses.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02439775 | protocol leakage | 111 / 40 | 5b1c73f9f3c3c2a4ec7b457476209837ad2710da40a9e6532de306474eb1ba57 | c7d738fda0feda0698e837f06b385d71c0b366b28b93435eaa3caaddb0135a73 |
| NCT03131687 | protocol leakage | 89 / 62 | 037e811f53445c83e26674fec6fd75514a5fc7f96a5eb56d85fa3032956fb726 | efa292e4f98331fe39b462353fff03ccf2b04f5b8cca1252951c1605a8bcf83f |
| NCT06007781 | protocol leakage plus post-completion SAP | 73 / 29 | 6ae533173dd8e11e41db61b61c9787f15e1a1667f2352813524c27c210fa9e3e | bf897b0add9a37690079f846ff222d5bf356bfdf5811adddacc37fcc41e902c8 |
| NCT04565236 | governing-version hold plus protocol leakage | 106 / 16 | 7614bff9e5fbcdb05e6a563fe471308c97aa077502c11914f971fa89feb131e8 | 2d54f13e4e39d0ca2fbdec80e2c6692831e07068819b392831d4efe9bc4722aa |
| NCT04181762 | protocol leakage plus execution-informed SAP | 233 / 46 | 2125588b49b4df032b0e2c27c385c0db2bd138c206c7c02d8556859b92fc6c92 | 86d1a52df0eec7e3f7ef1b434c26bbc2a53a5c4adac32bb3d984c104e1f3f8a9 |
| NCT02880865 | protocol leakage plus post-primary SAP | 68 / 21 | 63f9083437ad23eb62bafcaf914d2d1ea7fc809a830e6b7193984ce12c6de985 | 3a806af686962e76a42383052bec6def0fb6ca5630600cdeb93f77503eb69807 |
| NCT02960490 | protocol leakage plus post-completion extension SAP | 100 / 34 | 2c47d044df2934a5fbe8738228a6609acd350bf4fd4b8f07a10dc894be44f365 | 04c9434411472f2da11acc4b96e865dfec8a3f083cd9472ee8679e830bfaa796 |
| NCT01931566 | protocol leakage | 160 / 73 | 4374842e077be116284c3b408cfaaa0a48827a31904904f4d80fea978eaf9b1c | 7b389807f38891768432d0c01922c685f063611b09546427cd22d68ee1cbe708 |

## Review gate

No Batch 52 family may enter train/dev/test. The version hold remains outside the actionable queue, and all eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
