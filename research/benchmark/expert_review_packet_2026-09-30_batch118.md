# Expert Review Packet - Batch 118

## Scope and decision boundary

Batch 118 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen official PDFs and eight official registry records were downloaded sequentially, size-checked and SHA-256 frozen. Native text was extracted from all 1,131 physical PDF pages; 26 scan-only or otherwise empty-text pages in the NCT01954017 pair were separately OCRed. Decisive identity, chronology, version, conduct and leakage pages were rendered into 18 contact sheets and visually compared with the original PDFs. No candidate survives the complete prompt-to-reference boundary: five have post-primary, post-completion or conduct-informed target material, two expose detailed executable plans in the protocol, and the otherwise prerecruitment NCT04220489 pair exposes the entirety of its minimal SAP in the model-visible protocol.

## Decisions

- NCT01566695 — exclude: the 2022 protocol amendment reports the finalized primary CSR, the 2019-01-25 data cut, 216 analyzed patients and sponsor unblinding. The 2019-03-27 SAP also postdates primary completion, and the protocol exposes the executable program.
- NCT01936831 — exclude: SAP Version 3 dated 2022-05-05 follows 2021-09-22 primary completion and incorporates recultured results, an early-terminated arm and observed reporting issues.
- NCT01954017 — exclude: Final SAP Version 3 dated 2018-10-31 follows primary completion and was finalized nine days after study completion; protocol pages 50-53 expose populations, sample size, descriptive analysis, missing/repeated-data and interim decisions.
- NCT02065791 — exclude: protocol pages 91-94 disclose ITT/safety sets, event-driven N=4,200, stratified Cox analysis, interim alpha/stopping, hierarchy/multiplicity and safety summaries.
- NCT02833857 — exclude: protocol pages 44-45 substantially reproduce the analysis set, practical N=10, descriptive/no-formal-test approach and AE/PK/PD program. The public protocol date also does not match the date cited by the SAP.
- NCT03025542 — exclude: SAP Amendment 1 says it added tables and figures generated for Interim Analysis 3 and changed content after interim data cuts; protocol pages 72-74 also expose populations, analyses, nonresponder imputation, data cuts and sample size.
- NCT03781414 — exclude: post-completion SAP Amendment 3 describes interim-driven termination, unfavorable risk-benefit and termination-driven analysis changes; protocol pages 109-121 expose the Bayesian primary, FAS, missingness, MMRM and sample-size framework.
- NCT04220489 — exclude after final leakage reconciliation: the pair has exact prerecruitment identity and chronology, but the two-page reference SAP's only substantive content is a descriptive-statistics/possible-two-sample-t-test statement. Protocol physical page 15 reproduces it verbatim. Because the full target plan is reconstructable from the prompt, exact version matching cannot make it eligible. The COVID-19 termination and registry actual N=1 are conduct context only; prospective N=20 is not enough to overcome the leakage boundary.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01566695 | post-primary/outcome-aware wrong pair and leakage | 160 / 64 | fe416fccf9ef13670096ceb7744b08a4411303fd7956ba30ca1550b4a585ba1a | 5f2c02213be418b2fbfe648a1746d4f8ed4a54fdc73e36889f0bbc02e2fee7e3 |
| NCT01936831 | post-primary and conduct-informed | 104 / 14 | b781727c6d967c88afc9c86cbaf22509ea1eee17e26f520b350e3707acfa9bab | f73dda394851cf70ebff7ab1a41adb6a5ea388a8448034143fd824f72061f965 |
| NCT01954017 | post-completion and protocol leakage | 74 / 41 | ee34490311eecc11500aa42bf2039e2a9c2fa7103cb605a62a6721dd7a34fc00 | e9d2a476b6ac4c03bd112f76a17557fbf77d09941a1e9d73c07a8a388368ac8c |
| NCT02065791 | protocol leakage | 129 / 52 | 44e972d5baa07d3672e5153c6410de855b827c5fc06df58464e9a1879d570959 | 23e15ceeb56be453b23515b811db0b57c137d4fdbd63110d1635e8a9a985fa9c |
| NCT02833857 | protocol leakage and version-date mismatch | 64 / 20 | 37aaf2d0c66696dfd073f79be6a94e332a62cd3bab1f29f5c03a4da620db8656 | e7652ccefcc26ceb01046508734f8bd6c690efa267b3dc41b30672878ef2d4b6 |
| NCT03025542 | interim-informed and protocol leakage | 117 / 68 | 8094bbf36d94fb79f61beed8181d98b806728ae83fa8dd8fb453542c4d9135ee | 7c0a1491147de92537ec71347cb67859cc13433f0b907fd97d1fefb9065ab7cc |
| NCT03781414 | termination-informed and protocol leakage | 136 / 48 | 33c5cd5c1db538f188329bb0df4a3a0cb122f0472d6ad3ae9b91f140dbc666d9 | 59510b1ba05f5f29b87b4e4a816c2bc37c5d393594e6048702fa2d9673dd7d12 |
| NCT04220489 | complete target leakage in protocol | 38 / 2 | 3edb01401bbb1329d2050bb4a86c38205b0ab47c7ad29712bfd80373c7377ba9 | 28e35c510a1062b72966c3c60620d315f436b7283ac2117568c982eb7567a2c4 |

## Review gate

No Batch 118 candidate enters the registered benchmark. All eight slots must be replenished from the official registry pool, leaving the benchmark at 101 public first-pass drafts plus 19 actionable candidates. In particular, NCT04220489 must not be promoted merely because its documents are prerecruitment and exactly matched: eligibility also requires the prompt not to reproduce the target SAP.
