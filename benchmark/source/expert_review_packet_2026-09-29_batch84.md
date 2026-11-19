# Expert Review Packet — Batch 84

## Scope

Batch 84 reviewed eight ClinicalTrials.gov document families. One family, NCT04984590, passed the protocol-only independence and prospective version-chain gates and was promoted as `PUBLIC-IOPCL-AMD-MAG-001`; 23 evidence-backed requirements were created. Five families were excluded because the model-visible protocol already disclosed an executable analysis target, two of those also had post-primary SAP revisions, one family was excluded because both selected documents postdated study completion, one family was excluded because its SAP was written after primary completion and incorporated observed conduct, and one family was held because public identifiers and the single-arm versus randomized analysis-set descriptions cannot be reconciled.

All 16 PDFs and eight registry records were downloaded and hash-frozen. Text was extracted by one-based physical page; the character-corrupted NCT04984590 and NCT04753606 SAPs were rendered and OCRed. Identity, chronology and decision-defining pages were visually inspected. Reference SAPs remain annotation evidence only and are never model-visible.

## Promotion

### `PUBLIC-IOPCL-AMD-MAG-001` / NCT04984590

- Protocol Rev 5 and SAP Version 1.3 have the same NCT, full study title, sponsor, product and 2022-12-06 date, before actual primary/study completion on 2024-03-20.
- Visual inspection confirmed that `IOPCL AMD-20`, `IOPCL AMD-020` and the `IOPCL-AMD-2020` running footer are internal formatting variants in the same document family.
- The 31-page model-visible protocol names `Appendix 6 – Statistical Analysis Plan` only in its final appendix list; Appendix 6 is not included. It therefore does not expose the reference SAP's analysis population, available-data convention, interim timing or output-specific summaries.
- The 23 requirements cover study-eye unit of analysis, sample-size target, effectiveness and safety populations, visual-acuity responders and derivations, positional stability, adverse events, secondary surgery, visit windows, missing data, intercurrent events, multiplicity, interim review, exploratory reading outcomes, ophthalmic assessments and VFQ-25 scoring.
- The annotation remains `draft_needs_expert_review`; six critical items require statistician adjudication. Promotion is a first-pass benchmark draft, not expert approval.

## Exclusions and hold

- `NCT01953926` — excluded for protocol leakage. Protocol physical PDF pages 75-77 visibly disclose cohort-specific Simon two-stage assumptions and stopping rules, analysis populations, ORR/ORRfirst definitions, RECIST response, exact Clopper-Pearson intervals, Kaplan-Meier DOR/PFS and safety summaries.
- `NCT07608367` — held for version reconciliation. The protocol cover visibly says `NCT Number: Not applicable`, the registry organization ID is `SDSYKYY202510-1`, and the SAP cover identifies `ChiCTR2600122083`; no public document links these identifiers to one governing version chain. SAP physical pages 9-10 also define Randomized, FAS and PPS populations despite the registry and documents describing a single-group study.
- `NCT03108469` — excluded for protocol leakage. Protocol physical PDF page 46 visibly gives 1:1 unstratified randomization, two-sided alpha 0.05, chi-square and repeated-measures ANOVA, mITT and safety populations, LOCF and the non-headache rule for an unrecorded diary day.
- `NCT01966445` — excluded for protocol leakage. Protocol physical PDF pages 115-121 visibly disclose the descriptive Part 1 strategy, N-CRM simulations, the Part 2 predictive-probability design, futility and success boundaries, analysis populations, missing-data convention, transformations, interim monitoring and stopping table.
- `NCT01468844` — excluded as a post-completion document package. The protocol cover is dated 2018-09-19 and the SAP cover is Version 1.0 dated 2020-04-14; SAP page 5 says it is based on Protocol Version 22.0 dated 2019-12-10. Registry actual primary and study completion were 2015-03-04 and 2015-05-13.
- `NCT04753606` — excluded for protocol leakage and chronology. Protocol physical PDF pages 35-36 visibly disclose ITT, mITT, PP, PK and safety populations, primary MMRM, unstructured covariance, Dunnett adjustment, multiple imputation with Rubin combination, no interim analysis and power assumptions. The SAP cover is Version 2.0 dated 2021-07-07, after actual primary completion on 2021-05-24.
- `NCT05478018` — excluded as an execution-informed post-primary SAP. The SAP cover is dated 2024-06-24, after actual primary completion on 2024-04-16. Physical pages 7, 17 and 18 visibly report recruitment stopping after 40 completers, 55 included participants, added questionnaires for the last 25 participants and a specific pregnancy-screening mistake. Protocol page 43 additionally discloses the primary ANCOVA and power assumptions.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT04984590 | promoted | 31 / 15 | e6681b99155bdda0e1dfcee9e5f45d66622bea0704b2289335fabbc7b67e00d4 | d1ea019c2064c980eb276ecadbe806bc48779161c8c2cf29c5f2c86a071d961d |
| NCT01953926 | protocol leakage | 121 / 40 | 0127f5e7d837befa726c229a57ebb9c5f0dfb1ded13e828cc3a9a74a9bf26639 | 44f806d752820ee04360e839986fe301be98a4c84992b85589ed49a094295515 |
| NCT07608367 | version hold | 43 / 11 | 7fdf92aa04f41363729881ec33899dd535c31d2e34b41277f9803d135307b31f | c60fa4f41f6084cd650ad0110b077089f488faca9179374f34666ca9ab3d3596 |
| NCT03108469 | protocol leakage | 54 / 20 | fd2fe24a8ca8d4880dd50f80d99b5ee8274bba47f55cb5e58fd6ffdf98147ff1 | 772af400288bf14265edae172b0703176fc049de8b2f365f6be7516ee68d0724 |
| NCT01966445 | protocol leakage | 266 / 62 | 1e1a9aaad1b2035af98cccba1007bdf127867b28a02ba475ecd4f6c48d550197 | cb55d4b209f7daf278f4e43d55e6a01388bccdf681f2ac74bc8bbe9adcff9db7 |
| NCT01468844 | post-completion documents | 59 / 43 | b645bb3fb4e1ea3435a5647d325959be7053eabc25e3e41aafa52c4b98c01e79 | b914988b2576a7f54d8fc73326c335f23e207e3f98de1b5a6f4534a3e0bbaddb |
| NCT04753606 | protocol leakage / post-primary SAP | 47 / 24 | 7364ad2c8535506348f9e0334afd558fb995fc1dbf5becb7084996311070148f | 4557458606b6458c8d2e9ba338a710e082f401f00fd6a3fc9756fef8a40564b0 |
| NCT05478018 | execution-informed post-primary SAP | 52 / 30 | 26dbdd12013815e09f65e5c3f01a37c9cc477d0174f0dc256c4d6a6db47817ca | c54af5fc687aa0634986f264bb9fb1b4457e3f9b571420d6f35ac86883fdc056 |

## Review gate

Only NCT04984590 enters the registered benchmark. Its reference SAP must remain in the annotation-only `reference/` path and must not be supplied to a generation model. The seven decision records remain outside the actionable candidate pool; the held family cannot be promoted without authoritative identity and design reconciliation. Replacement candidates must be screened until all 120 public families have first-pass requirements.
