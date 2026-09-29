# Expert Review Packet - Batch 116

## Scope and decision boundary

Batch 116 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen official PDFs and eight registry records were downloaded sequentially, byte-checked, SHA-256 frozen and extracted page by page. The scanned ten-page NCT02556788 protocol summary and 56-page NCT05718687 protocol required full-page OCR. One hundred fifty decisive identity, chronology, redaction, statistical-leakage and document-type pages were rendered from the original PDFs and visually inspected; all 150 thumbnails were produced despite four non-fatal JBIG2 end-of-stream warnings. No family is promoted: three selected plans are late or conduct-informed, three targets are already executable from the model-visible protocol, one governing protocol cannot be reconciled, one public release removes material timing context, and one purported SAP is actually a results report.

## Decisions

- NCT02007720 — exclude: RAP Module 3 dated 2017-08-23 follows actual primary completion on 2017-03-27 and final completion on 2017-06-16; Protocol Version 04 physical pages 65-72 already disclose the FAS primary analysis, trichotomous endpoint, ordered-logistic framework, secondary analyses, safety summaries, no formal efficacy interim analysis and sample-size re-estimation.
- NCT02556788 — hold: the final SAP dated 2015-10-05 says it is for Protocol RD.06.SPR.18252 dated 2015-07-21, but the only public model-visible document is Protocol Summary V02-19JAN2017, finalized 2017-03-10 after registry primary completion on 2017-02-07. The later summary cannot be assumed to be the SAP's governing protocol.
- NCT02732951 — exclude: the final SAP dated 2017-07-26 predates primary completion, but Trial Protocol physical pages 51-55 already specify the FAS, REML MMRM, fixed effects, unstructured covariance, Kenward-Roger inference, MAR missing-data handling, no interim analysis and the n=102 calculation.
- NCT03678545 — exclude: SAP Version 2.4 dated 2025-02-12 follows primary completion on 2024-03-04 and final completion on 2024-11-13; its revision history states that the primary and secondary analysis population was changed to complete-case ITT after observing similar imputed results and limited missingness. Protocol Version 6 physical pages 67-73 also disclose the analysis populations, primary model, missing-data strategy, sensitivity analyses and sample-size plan.
- NCT05718687 — exclude: SAP Version 1 dated 2023-05-01 is correctly tied to Protocol Version 3 dated 2023-03-13, but model-visible protocol physical pages 42-44 already define the safety and PK sets, noncompartmental analysis, PK parameters, missing-data conventions, descriptive summaries, absence of formal inferential testing and conventional 8-10 participant sample size.
- NCT02971683 — exclude: SAP Version 1 was last revised 2020-12-15 after primary completion on 2020-07-27 and physical pages 21-22 explicitly incorporate case-by-case review of observed COVID-19 deviations and the Week 24 database-lock analysis. Protocol physical pages 99-104 already disclose the prospective sample size, ITT/as-treated/per-protocol sets, logistic primary model, nonresponder handling and secondary MMRM program.
- NCT01751568 — hold: the public SAP states that author names, publication/writing-team membership and the analysis timeline were redacted. It is intended for protocol-team monitoring, full-cohort accrual reports and final reports, and the visible version table alone does not restore the removed chronology needed to verify when the operative analyses became final.
- NCT04011436 — exclude: the file labeled as an SAP contains observed baseline tables, post-intervention results, group medians, exact p-values, correlations and interpretive conclusions. It is an executed results report, not a prospective governing statistical analysis plan.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02007720 | post-completion SAP and protocol leakage | 88 / 29 | 7abc3110bc74251688e3fc16af6b4452cd0a93de40f2d4c6672f852addf889e5 | 931bb697d170d23a51dc4b20bb1857076c37df6df602aac7a4cec05162de0494 |
| NCT02556788 | governing-version hold | 10 / 39 | 09c93eedb92eb5114a0685e68a7740a99f791a7c8a590a27f84dab2ef9be8396 | 8bf487a8a166e79ce215e4c74a4657fe6d77af63226193725d234ef8271e94a0 |
| NCT02732951 | protocol leakage | 67 / 24 | 030796981335f6ecc367238f08481c324009f51f36190f452d9445b6d5135bcd | 2c749fadfa176fa00b8eea425035412139fb42081baee39ad94f18b83d17c564 |
| NCT03678545 | post-completion outcome-informed SAP and leakage | 81 / 17 | 53b90dbee6609adea1d50b3753dd06d37e2ddfc24dc401fdf309c4b4730f0c63 | c5ae3a67371ea18509cc553195752d41389b020502a5ad09f778ebbc3e421645 |
| NCT05718687 | protocol leakage | 56 / 30 | 22ffd30b26175ff8a6ca4e8ff26017ce69d86c16e89cf9e1aa28f729040376f7 | edd011b2ecec130505dd10e0820ab780864526c76bf7c0a11754087486487024 |
| NCT02971683 | post-primary conduct-informed SAP and leakage | 133 / 68 | aa06909ad54805ac26e9fa9e41efa1fff4e23e459c26b4e95102f12ca29eb42a | 3b7e435d40f44913cbcbf63f102fb80c634f3b0fd0f230b08232c804513cc7e8 |
| NCT01751568 | public-redaction hold | 4 / 9 | c55ea28fd4d04cbabc65af7e77e9af87ef85351209f66d075d29c8cd4ed5e83c | 419eb5952c38f0e20d2bbfc178d9c805b816bb5afa6737a9cfa2dbb6960d5647 |
| NCT04011436 | results-bearing wrong document type | 5 / 16 | efaac5f18c6889fb074157828b17ad13e4e3a107483fbb430b3100a02dcae548 | 8ed66852dffaadc65c9524b73f0d7e877ea3c9e44798f7aff930f71e5e368c59 |

## Review gate

No Batch 116 family enters the registered benchmark. The two holds remain outside the actionable queue and all eight slots must be replenished so the release intake remains 100 version-verified public drafts plus 20 actionable metadata candidates.
