# Expert Review Packet — Batch 57

## Scope

Batch 57 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent-target gate. Every model-visible protocol exposes executable target-analysis content; NCT02065622 additionally pairs the full study protocol with a Japan-sub-study-only SAP, and NCT06338592 labels a near-verbatim extract of the protocol statistical section as the SAP. Four families have additional post-primary or post-completion chronology defects. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. The scan-only NCT02274857 protocol was fully OCRed before visual confirmation.

## Decisions

- NCT02274857 — excluded: protocol pages 44-47 expose ITT/PP populations, hypotheses, chi-square, Kaplan-Meier, Hochberg correction and the interim trigger.
- NCT03338023 — excluded: protocol pages 47-54 expose noninferiority power, sample-size re-estimation, populations, MMRM/ANCOVA, LOCF, gatekeeping, safety, subgroups and interim analysis.
- NCT02065622 — excluded: protocol pages 279-289 and 306-312 expose the main and Japan-sub-study plans; the selected SAP is only for the Maintenance Japan Sub-Study and is post-primary.
- NCT04444752 — excluded: protocol pages 68-73 expose preliminary-data-informed power, hierarchical testing, populations, ANOVA, safety and LOCF/WOCF; SAP is post-completion.
- NCT02992418 — excluded: protocol pages 84-93 expose noninferiority hypotheses/margins, interval methods, global rules, analysis sets, missingness, interims and power.
- NCT03104374 — excluded: protocol pages 117-125 expose analysis sets, CMH, NRI/OC/MMRM, graphical multiplicity, safety, PK and power; SAP is post-primary.
- NCT02284906 — excluded: protocol pages 74-78 expose MMRM/Cox, analysis sets, MAR multiple imputation, censoring and safety; SAP is post-completion.
- NCT06338592 — excluded: protocol pages 27-30 expose GEE, weighting, ITT, missingness, subgroups and power; the four-page post-primary SAP reproduces that section and identifies itself as protocol content.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02274857 | protocol leakage | 49 / 11 | fd879563181704c68f6c0a81fa2bd92079f1bb9abbd4977c471647a2d9a1b16d | d93f90ab987c25b01237324ea8d6ee785f67879652055b3b8714edf1a3cf0e4c |
| NCT03338023 | protocol leakage | 87 / 35 | 95481b327f2074b1454629e981cc7ea789add715d0731471083bac06e7807a8a | 7753531ed85afb0cb1256a9413b9278efa2c90b64dce313a4411e06e2feaccd4 |
| NCT02065622 | protocol leakage plus wrong-scope post-primary SAP | 313 / 77 | 4984652dfe5252cec9f606093d494b71563cd657aba73e745092174910a17312 | fe61451d807a6c1fadccfc217114510e7b478e9a0870f3c086b245e17ba13677 |
| NCT04444752 | protocol leakage plus post-completion SAP | 93 / 32 | 30a5f668afd6cf088ffec2d80defee04a138d39a22f241bb35b0d657693975bd | 6c18f934c0c7493b5bdecda3e762ae3ee48537a83f610a5d5b9dfeedb80b5bd8 |
| NCT02992418 | protocol leakage | 102 / 40 | d385f6778800ce8899187d512be69e7001df01e60a1d2191f7035c7c7f4a9463 | 24a4d7ea7e88f65e87c08d5b6560f0221f843d230cb5949d0a636b5c86977017 |
| NCT03104374 | protocol leakage plus post-primary SAP | 159 / 87 | 4602a5efc6a9a4508798b077620ea697fba3f0301f9a6e2aadb996a6f03c56d8 | 6a2a93e603e2db0aa4251881a48673a5c3ef890737b934516b0e19b78ed73344 |
| NCT02284906 | protocol leakage plus post-completion SAP | 125 / 38 | 8f5f459a8600aacfdea443f538ae8017e92b96f2934d9857705e644c90f06695 | a86532f3711770cc50b16942eed3526b0a123d6fec807b6386d4057b79256c51 |
| NCT06338592 | duplicated protocol section plus post-primary upload | 31 / 4 | 7ef2e78c6918237047e9d76f1718a2f25e8dccf8e713a981deac3d1f688c5f8a | 815594f6be07addddfbf90ab8c7218fcba596c0b2d438a5532138c9cefc0119d |

## Review gate

No Batch 57 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
