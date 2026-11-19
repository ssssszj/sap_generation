# Expert Review Packet: Batch 124

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 124 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,084 physical pages. Every page was text-extracted, and 30 decisive physical pages were rendered and visually inspected. No pair survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT02611778 — exclude: final SAP v01 dated 2018-04-16 follows actual primary completion in 2017-12 and identifies the main-analysis last-patient-last-visit as 2017-12-21. Protocol physical pages 53-58 independently expose the analysis populations, noninferiority ANCOVA and confidence intervals, missing-data approach, sensitivity analyses, sample size and no-interim decision.
- NCT02963766 — exclude: Protocol Amendment (e) is execution-informed; physical page 100 says the sample-size re-estimation was performed in 2019. Physical pages 101-105 also expose the estimands, MMRM/ANCOVA, copy-reference imputation, binary analysis, multiplicity, subgroup/safety methods and database-lock unblinding.
- NCT03226067 — exclude: Protocol Final 4.0 physical pages 73-80 expose hypotheses, N=102, Hochberg testing, the unblinded development-decision interim, ITT/PP/Safety populations, endpoint hierarchy, stepwise ANCOVA/Wilcoxon analysis, repeated measures, intervals, safety and MAR/MNAR handling.
- NCT03020160 — exclude: SAP Version 1 is dated 2017-06-20, but the only selected model-visible protocol is Version 5 dated 2019-12-20, two years after actual primary completion on 2017-12-15. The governing pair cannot be aligned without inventing or substituting an unavailable earlier protocol.
- NCT03451422 — exclude: SAP Amendment 3 dated 2021-11-09 follows actual primary and study completion on 2021-10-12. Its revision table records method changes on 2021-10-26 and laboratory-result changes on 2021-11-09.
- NCT02416453 — exclude: SAP dated 2018-05-30 follows actual primary/study completion on 2018-01-19. Protocol Amendment 5 physical page 49 says Group 3 randomization was not resumed and enrollment would be stopped, making the selected prompt conduct-informed as well.
- NCT01709747 — exclude: SAP Version 4.0 dated 2019-02-04 follows completion in 2018-02. Physical page 7 explicitly records cleaned data through 2018-01-08, database lock on 2018-02-07 and sponsor decisions first to analyze selected safety data and later to proceed with the full analysis.
- NCT02188719 — exclude: SAP Version 1.0 dated 2020-05-06 follows actual primary and study completion on 2019-06-18 by nearly eleven months and cannot be certified as the prospective frozen primary-analysis plan.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02611778 | excluded | 89 / 51 | `5c32d8c40e9ab9cd3fdfc5523dc844f4519bed604dca089402b320e2181c1547` | `e13dd89de056ac7e1c3b537b4ab35bc5a7833b77c0701b3409a222a9fd37f190` |
| NCT02963766 | excluded | 107 / 42 | `2123e62f4e88af437d080bda03e56a6773455d24ab5c6590b7a6500a313955c1` | `111d9288154281c1d8e0ca0d6978490d05fb1b22489df6ad4216fd44f663b972` |
| NCT03226067 | excluded | 113 / 35 | `a14183f3c714a08552b42a9a422c89654dcfbc42766312ca8bee586fade32be0` | `29fa9979aa6c1428f726e5bdb32e1c62674ad2ca525b43e38376ecd62880b0c9` |
| NCT03020160 | excluded | 130 / 42 | `ebf5dfe2b2285b60759a070117219ade303841b222fc1b8bca4dbb9226631cff` | `094aeb184d5b5dbfbaff04cce044c08abe221e325e0c3ff7809f3bd862a7b5a1` |
| NCT03451422 | excluded | 104 / 34 | `e687a6f299c5e96709623c8a6b462e2348c5ef8a45d0a45c4332fca91e1beec6` | `12fd8438ac1736d69e62762175a7765f106cdfe1612b74d530cabbff75cab01a` |
| NCT02416453 | excluded | 114 / 34 | `cfb6e00110708163a78f22ff10f892588fcabebe6045ecd0eee5a8a6a41ab063` | `c170e95447bc8459fb58013b95d811a76e6431483a945c0d1a9c3a862607e2ee` |
| NCT01709747 | excluded | 64 / 31 | `6342ba8bf71b17bee150990df0f0e8089698330ed8ecee52e60bdb5a3dd49619` | `3d5bc24dc4e6d26235bd900fc77abc01c0214fead5ec8732ae787e65a68f4923` |
| NCT02188719 | excluded | 80 / 14 | `9b2750ebb6b219bad506fdda5bf70b0f7f0573776a2e98704b75c9480dcb7cd0` | `211aa83ec32506d5bb229553b80a23fcc1d63926cae38a1a6846177b6b73488a` |

## Replenishment

All eight excluded slots were replenished from the official API. The release-eligible intake remains 120: 103 public first-pass drafts and 17 actionable metadata candidates. The next queue starts with NCT02695420, NCT03010319, NCT04673357, NCT03103542, NCT03482011, NCT02167945, NCT02151682 and NCT05421624.
