# Expert Review Packet - Batch 89

## Scope and decision boundary

Batch 89 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally, every physical PDF page was text-extracted, and identity, chronology, execution-language, redaction and decisive statistical pages were rendered for visual inspection. No family is promoted: four fail the protocol-only leakage boundary, and four have retrospective, post-completion or within-study-outcome-informed reference packages. These decisions do not reduce the 120-family intake; all eight slots are replenished.

## Exclusions

- `NCT03680742` — protocol leakage. Protocol Revision F and SAP Revision A share the exact CERUS identity and 2019-02-05 date, but protocol pages 41-44 already provide the ITT/PP populations, primary endpoint proportions, missing-data rule, summary statistics, software, interim rule and sample-size rationale found in the nine-page SAP.
- `NCT04183335` — protocol leakage. Protocol pages 65-68 expose CMH testing and strata, rescue/prohibited-medication and missing-data handling, sensitivity/subgroup analyses, Cox/Kaplan-Meier methods, WOCF/multiple imputation and multiplicity. The protocol also records changes based on observed companion-study EFC16460 results; the final SAP is dated one day before primary completion.
- `NCT03968003` — post-completion publication methods. Both uploads are dated 2025-05-20, almost five years after completion. The protocol reports actual enrollment and executed microbiome processing, while the analysis file repeatedly says analyses were conducted or performed.
- `NCT02621892` — protocol leakage. Protocol pages 43-57 contain Fisher-exact powering, blocked randomization, analysis sets, missing-week rules, LOCF, site pooling, alpha control, responder definitions, sensitivity analyses and detailed output plans.
- `NCT02309411` — post-completion, execution-informed SAP. Version 2.0 is dated after completion and explicitly incorporates blind-review decisions, unavailable visit-level accountability data and an event-triggered informative-dropout sensitivity analysis.
- `NCT02618967` — within-study-outcome-informed adaptive package. Amendment 4 and SAP Version 3.0 use interim PK/PD data from the ongoing first-in-human study to add a seventh 700 mg cohort and revise dose expectations.
- `NCT03068767` — retrospective methods package. The nominally 2017 cover conflicts with retrospective conduct language and a later 2017-2018 recruitment interval; the protocol reports conducted methods and the one-page analysis file says analyses were performed.
- `NCT01990534` — protocol leakage. Protocol pages 54-59 expose the analysis populations, exact-binomial ORR method, confidence intervals, covariate displays, Kaplan-Meier and Brookmeyer-Crowley analyses, safety summaries and interim rule. The visible redaction does not hide the decisive target content.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03680742 | protocol leakage | 106 / 9 | 4fee507f9362dca2815c1958c6e2d949faee79fbe8c6575888f1168550d71295 | b2aadf410539472a78179c31f40c4922b432aabe0b2fa6a61564f3344d9e0972 |
| NCT04183335 | protocol leakage | 116 / 64 | 6d3eb1fbf9de30df9f017b1c103473aae443f5e704f55178c6a9dfe24980aa38 | 4f8a4789a085802c921b0eeaef5ae3afc734a1c4f38ee30d4e5d16b223aa63ea |
| NCT03968003 | post-completion methods | 9 / 3 | a1d386036ceb4276c77cb34653211c5f1db26802136fb24e613d661df5bb0921 | bbb5556308c340a65cc08f8e997760466adde4f316057001c752672033ea0c5c |
| NCT02621892 | protocol leakage | 74 / 79 | 4c54bbab87f7869a34ca3d6bd6690461776c68de0ada581b76da3af007ad22be | 3796a25cbff028e5d3b4aab01aeca0b98f31b3f7600980a3e6858b0ad9a8bcae |
| NCT02309411 | post-completion / blind-review-informed | 80 / 20 | 6dec45ae8245642ccbd92e3da65d9d88a50c50e62ba8308a0107bb35652d59aa | 3749c1cbb6bf94248b3bd42c2d0921a4a4e5558ccb1a860e5b6d0af09507ce5e |
| NCT02618967 | within-study interim-informed | 87 / 31 | 9ca1ee3d9d2145e0384ada17dc685de62a1b6e1168cec9ab978285f180dd0833 | daa8a183805ae5ae194aba4fbf440e2f6c50a270f79951733121542cd866a04a |
| NCT03068767 | retrospective methods | 12 / 1 | 715d6ded4f02b9de7c747ba2145d6c5492d52c7e960f9255627431da40e2ecf3 | cee9480f17c863fab3c1fa8aaa408c75d34632f0dba5a1c6b77242f6478c559e |
| NCT01990534 | protocol leakage | 85 / 24 | 48a802d482b82e04759f1eed3dcf42717fe0cf122b5f4efa08d05cf8c205f3ae | 3cff37b751b840033a8098a0bd2819311dc8ad32054f199145d9a15393b296bb |

## Visual review

Rendered one-based physical PDF pages confirmed each decisive finding: CERUS protocol page 42, LIBERTY-PN PRIME protocol page 65, Thai prebiotic SAP page 2, TEN-01-301 protocol page 44, EINSTEIN Junior SAP page 18, AMG 570 protocol page 83, vitamin-D/HBV SAP page 1 and brentuximab protocol page 56. No decisive statement depended on truncated OCR. The page-56 Takeda redaction obscures one secondary phrase only; the exact-binomial primary ORR method and analysis populations remain visible.

## Review gate

None of the eight families enters the registered benchmark. Their slots remain outside the completed-question count and are replenished so that the working collection continues to contain exactly 120 public families across registered drafts and metadata candidates.
