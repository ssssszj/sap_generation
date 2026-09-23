# Expert Review Packet — Batch 28

Batch 28 produced no promotion. Five protocols expose the core target analysis, and three purported SAPs are retrospective, execution-informed or finalized after primary completion. All 16 source PDFs were obtained from ClinicalTrials.gov, hashed, page-counted, text-extracted and visually checked at the cover and decision-defining pages.

## Screening decisions

- NCT04941482: excluded_wrong_document_type. The SAP says that 92 participants were randomized, no interim analyses were conducted, and all analyses were specified after data collection was finalized.
- NCT03709654: excluded_combined_protocol_sap_leakage. Protocol physical pages 51-54 disclose populations, endpoint derivations, compliance, safety summaries, ANCOVA, CMH, LOCF, site stratification and the no-interim decision.
- NCT03235024: excluded_combined_protocol_sap_leakage. Protocol physical pages 42-44 disclose sample-size assumptions, analysis populations, safety summaries, mixed repeated-measures ANOVA, supportive t tests, alpha levels, missingness and multiplicity.
- NCT05071807: excluded_wrong_document_type. Its two-page analysis document reports analyses already performed, diagnostics already checked, assumptions already met and a nonsignificant interaction removed from the final model.
- NCT03938792: excluded_combined_protocol_sap_leakage. Protocol physical pages 109-114 disclose estimands, success thresholds, intercurrent-event handling, missingness, power, populations, negative-binomial GEE models and secondary methods.
- NCT03124160: excluded_combined_protocol_sap_leakage. Protocol physical pages 50-52 disclose Pearl Index and Poisson methods, life tables, Kaplan-Meier, log-rank, power, competing risks, categorical tests and no multiplicity adjustment.
- NCT05037851: excluded_wrong_document_type. SAP Version 2.4 is dated 2024-01-03, after actual primary completion on 2023-10-19 and study completion on 2023-11-13; material public SAP content is also redacted.
- NCT05120193: excluded_combined_protocol_sap_leakage. Protocol physical pages 61-63 disclose Farrington-Manning thresholds, site pooling, multiple imputation, tipping points, subgroups, sample size, power and secondary gating.

## Source audit

Identity covers and all cited decision pages were visually rendered in addition to text extraction. The files remain local, gitignored screening artifacts and are not model inputs.

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT04941482 | execution-informed document | 10 / 8 | 1436475b4cd5a22b69394b6f0a0c31edd3c0e4fccf875f44cb5ab780136fb61c | 873edf5d9b53f39ca1debb35af35c342e68031b3d93d7cad1a2ada970b1c5da3 |
| NCT03709654 | protocol leakage | 70 / 22 | 906f22de043c2f6bfdc5e4e73263bd9ad8c2d4651317abe10df4c45576bb825c | 2e75d4c11165b7c3dad98e3f750b8ff3a140be19b8ae4a4dfcab21d4a9e2cc6a |
| NCT03235024 | protocol leakage | 80 / 69 | 4b67bb1d451ac9664335a128f509f6fe5271e7a40c4b8254cc76abd9e55f14d6 | fdfed77c17437a965eb1e2da80b21bd7d77a868fd2aced81577a582b9167b071 |
| NCT05071807 | execution-informed document | 45 / 2 | a6524044d54eeeffdab449409513618fc15810f518f9f251544cdbbba1accc13 | 7aaa68e510afadf52e9f6862d83bc4f21a0f14d63a34204cfeea3affa398145a |
| NCT03938792 | protocol leakage | 243 / 65 | c7ccba36fba5a4e0c3b617786aa8ddbaa4c515b5b3218ac2e9849132f0506508 | 697f26d567f8adc851755ed9e840390807fbb15b9abcf9d2db0783878ee5fcc4 |
| NCT03124160 | protocol leakage | 76 / 20 | 5dd11c0fd80ed73a41f5c4bc878fb46f962f62756501fd296d7dbb600dcbc6cc | 7b567bfdc3dc0d970ee0a9f8c925a8d30a0d6fdc3a462b497392575bc8fce857 |
| NCT05037851 | post-completion SAP | 124 / 20 | 66c4bac80fe7c9432d078cdc1bdca473d047a5ccc64e2aab0454590f75490476 | ec0deecb012814659c784b02288876a2d6f89831c12aeeb723a7010f4ab95120 |
| NCT05120193 | protocol leakage | 86 / 24 | 8067f7d5b3b52e92b922c3da00f0190647f5110882fc32cc1707446d9050b7fe | 99859d397912428399b82a11a9b968dfcf836c15e833d46f0c52eab538f69c9f |
