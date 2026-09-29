# Expert Review Packet — Batch 82

## Scope

Batch 82 reviewed eight ClinicalTrials.gov document families. No family passed the protocol-only independence gate: seven model-visible protocols already disclosed executable target analyses, and one selected analysis upload was a retrospective post-completion methods summary. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages.

## Decisions

- `NCT02379819` — excluded because Protocol Version 8 pages 37-38 already specify repeated-measures mixed models, rank fallback, exact-binomial and patient-time safety summaries, Kaplan-Meier, proportional hazards and cross-cohort pooling.
- `NCT03091673` — excluded because Protocol Version 1.3 pages 38-39 already specify the age-cohort t tests, LOCF, PK/PD summaries, safety analyses and sample-size assumptions restated by SAP Version 1.0.
- `NCT03246152` — excluded because the two-page analysis upload is dated 2019-05-16 after 2018-12-24 study completion and retrospectively describes tests already used; it is not a prospective governing SAP.
- `NCT03466099` — excluded because protocol pages 10-11 and 48-54 expose FAS/PPS, ANCOVA, MMRM sensitivity, multiplicity and power decisions; SAP Version 2.0 also postdates study completion.
- `NCT02525783` — excluded because protocol pages 42-46 expose the complete performance-goal noninferiority analysis, missing-data sensitivities, gated Hochberg secondary tests, propensity analysis and poolability rule; the SAP also contains an internal Version 5/Version 6 scope inconsistency.
- `NCT03760068` — excluded because protocol pages 51-56 expose the TEAR equivalence margin rule, Wald interval, ITT attribution, baseline-dependent MI/CCMV, tipping point, MMRM and analysis sets; SAP Final 3.0 postdates completion.
- `NCT03844789` — excluded because Protocol Version 2.5 pages 61-68 already disclose the primary mixed model, missing-data sensitivities, hierarchical testing, secondary models and safety attribution; SAP Version 2.1 is dated on actual primary completion.
- `NCT04016662` — excluded because Protocol Version 5.01 pages 52-59 already disclose the full crossover analysis, data thresholds, direct likelihood, MI, carryover assessment, covariance structure, alpha allocation, recycling and FDR control.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02379819 | protocol leakage | 47 / 11 | e9d87990f8a6327e4bab4fa668ebb47dd76eb01430c1cfe292ab412b47fb5a52 | 2d54867936496429c485acab725a465b2a4086b7b93093f929fc88e2382d9cbb |
| NCT03091673 | protocol leakage | 53 / 55 | 8f7a07d9d584c71f6e7b736d8ff65ce549136c88310efd4c53a80a4650794f1e | 9c9f77201369a7a52cf2b13687f8517cc21025908c49024f3b5c1ed821efe5ce |
| NCT03246152 | wrong document type | 7 / 2 | 35b2baea3ae2bb32deaa2188ea2a35343cdafb44da332b2755913716526f5ae6 | 8e3fc8bb2c20c72e60e7323192d52db76bed0a354bbf0151d6c4b523209b2338 |
| NCT03466099 | protocol leakage | 66 / 37 | 2c9d108e879dc9c62791418065fa7af02acae853330af63af118b5ff0f7956b6 | 62b01042322a48203d4b236eef00751b6831478a7ec748d80877e65997583d37 |
| NCT02525783 | protocol leakage | 76 / 19 | d6b377c032b0f74e74ad8a73b3ded96a6c71d38180bebb659d61a1a0ac07b19f | 9162137c0e8a752c3cebd034f62dc11e786f1c873efa6cf5b637cb3257a59b79 |
| NCT03760068 | protocol leakage | 71 / 69 | c0dac7187fffb6a5dda79d606ebdab12f0c5cc0e4e72268ba2aba24c902e4257 | dc590fcdc95a883e636ba6fea387437887b0ecfb44dad8d4338d9c4390566cf5 |
| NCT03844789 | protocol leakage | 76 / 19 | 46b905eccd9ee999c341ace166ca1068eb77ce70ffdc663f8c13d9480dce57f5 | 0721d4c000256891d83c2108adc4d865e49fba10d6869f6eb87717837af53be7 |
| NCT04016662 | protocol leakage | 67 / 15 | aba46d6e1a28daf6dfd5f1ae10ec36a41bd756e5188eb7bec5f7c97c2495d339 | e2b543c104bfbee00676370782709dd220463e9dfb9a48f543e98e6ffb481c3f |

## Review gate

None of these families should enter a protocol-only benchmark or receive requirements. Reference SAPs remain annotation evidence only. The eight decision records must remain outside the actionable candidate pool; replacement candidates must be screened before the public draft count can increase beyond 76.
