# Expert Review Packet — Batch 83

## Scope

Batch 83 reviewed eight ClinicalTrials.gov document families. No family passed the protocol-only independence gate: six model-visible protocols already disclosed executable target analyses, one additional family combined protocol leakage with a post-termination final SAP, and one selected analysis document postdated study completion with an irreconcilable protocol date. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. The scan-only NCT04153981 SAP and image-encoded NCT04279613 protocol were OCRed before comparison.

## Decisions

- `NCT04153981` — excluded because protocol pages 39 and 41-45 already disclose populations, alpha, hypoglycaemia incidence and confidence interval, a negative-binomial event-rate model, LOCF/general-linear-model analyses, AE summaries and the ITSQ missing-item rule.
- `NCT02828917` — excluded because protocol pages 48-52 already disclose the TLF12 noninferiority hypotheses, Farrington-Manning statistic, propensity-score model/matching, populations, confidence intervals and power assumptions; the SAP also follows actual primary completion.
- `NCT04279613` — excluded because protocol pages 33-35 already disclose analytic groups and periods, the exposed population, pooled placebo cohorts, primary AE summaries, C-peptide AUC log transformation, comparisons, sample sizes and power.
- `NCT02933372` — excluded because SAP Version 1.0 is dated after actual completion, cites an impossible 2020 Protocol Version 9.0 date against the selected 2018 protocol, and contains executed-study wording.
- `NCT04365400` — excluded because protocol pages 69-77 already disclose dual primary endpoints, FAS/SAS/PPS, MMRM/ANCOVA, MI, LOCF, alpha and interim adaptation; Final SAP 2.0 also postdates termination/completion.
- `NCT03012334` — excluded because protocol pages 43-48 disclose the noninferiority margin, power, populations, sequential multiplicity, primary crossover mixed model, transformations, McNemar tests and contrasts; the uploaded SAP package follows completion and is embedded in CSR documentation.
- `NCT04629521` — excluded because protocol pages 44-53 contain the full long-term COMPASS follow-up analysis plan, including all endpoints, analysis set, interval methods, ECD summaries, missing-data rule and sample-size justification; it is also not independent of its COMPASS parent family.
- `NCT01953913` — excluded because protocol pages 50-52 disclose the treated set, TTSP derivation, Kaplan-Meier/Greenwood analysis, treatment-emergent window, safety summaries, interim trigger and missing-date rules.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT04153981 | protocol leakage | 64 / 86 | 909abb05b85a7aac25d31bef3dca1813ce300a246f7dc804307518ce4c7f7b9a | ac6685ca30607ce6e244d9b6db6a230f18fa338371226a040eb246482e2ad8c6 |
| NCT02828917 | protocol leakage | 83 / 32 | a12b7f7e4d76fdc6b7e8b9a489c40be92ab850517baf688547a4bde59c6b21da | 90fd11d3e1d28c2ba427c96d0cbcc027fc57837805b412bceb7886faa4c1cce5 |
| NCT04279613 | protocol leakage | 45 / 10 | 878968512e3c7e7fced66507a157482ca012f16af256f894042078a28315c3bd | 9c011f15481b62a30973d665b79c3228342dfbcbc695601da56eee92a3986774 |
| NCT02933372 | wrong document type/version chain | 27 / 6 | c0b9cf747d4af1b8207f5a77533fc8507b045db146a27ae7ce325c26e37a36c3 | 276abb10c81ee8a29762b5edcad7e3cd34c8ddfab19913ce49f424f2e7236198 |
| NCT04365400 | protocol leakage/post-termination SAP | 90 / 41 | 442a396d961658db214e334464a3424c3037756a0b3dc1663476081b26349b2d | 6e5e985864439ad47472d4ebeccf56e639a5bb861e3f16025eada60e2d478554 |
| NCT03012334 | protocol leakage/post-completion CSR SAP | 56 / 84 | b32e0be0886fcc2b1ba5bbf7c510380f6fd9b8b92b7a8919621845fad0a509fd | a4b075aba7e4d26f66c7e95fdd6069c84e3d8b6a7941dd9b85c1efacd5d00543 |
| NCT04629521 | protocol leakage/shared family | 60 / 24 | 51799517fee6961d96b26893db7f62f65812e3dbead49808418ee46831264bd5 | ddd0863acaed182c164e0139e0f236688f8d72c50a74d0210180c857e71b0815 |
| NCT01953913 | protocol leakage | 85 / 26 | f256dd6bb0a8b0c8add407f57d38a73d53352305210d35cccfb3de05b8890109 | 5e847baaad47cccf4477cf5121ef7a6afc25c8a27cabdd5baea23058e4f613cf |

## Review gate

None of these families should enter a protocol-only benchmark or receive requirements. Reference SAPs remain annotation evidence only. The eight decision records must remain outside the actionable candidate pool; replacement candidates must be screened before the public draft count can increase beyond 76.
