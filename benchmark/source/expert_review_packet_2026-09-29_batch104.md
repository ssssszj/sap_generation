# Expert Review Packet - Batch 104

## Scope and decision boundary

Batch 104 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were downloaded sequentially, matched byte-for-byte to the registry sizes, SHA-256 frozen and parsed page by page. Scanned or unusually encoded pages for NCT03528551 were independently OCR'd. Protocol and SAP covers and all decisive chronology, version, executed-analysis and leakage pages were rendered from the original PDFs and visually inspected. Seven families are excluded and one is held; none enters the completed-question count. Their eight slots are replenished so the intake remains 96 public first-pass drafts plus 24 actionable metadata candidates.

## Exclusions

- NCT04083456 — the 2026-03-02 pair follows actual 2025-05-31 completion. SAP physical page 2 reports below-target enrollment, underpowering, abandonment of the planned futility test and analyses already performed and reported.
- NCT03224598 — the 2019-02-19 SAP follows actual 2019-01-08 completion. Protocol physical pages 12-13 and its later analysis text also expose endpoint summaries, population and missing-data conventions and safety methods, so the pair additionally fails the hidden-target gate.
- NCT04465799 — although both files claim 2017-01-31, the registry start is 2016-11-20 and protocol physical pages 4-6 describe consent, random assignment, intervention delivery and measurements in executed tense and report current-sample reliability. It is not a clean prospective protocol.
- NCT02836470 — SAP physical page 19 records an already-performed efficacy/safety interim analysis and sponsor tables from 2020. Page 24 records later changes to the primary endpoint, alpha, confidence intervals, covariates and analyses; the plan is conduct- and outcome-informed.
- NCT03528551 — protocol physical pages 55-59 disclose the analysis sets, treatment attribution, bleeding derivation, Poisson/negative-binomial and repeated-measures models, imputation, subgroup and PK rules. SAP physical page 13 explicitly says its statistical text is identical to the protocol.
- NCT02533570 — protocol physical pages 60-65 expose FAS/ITT, PP, Safety and PK populations, missingness, exact-binomial/Fisher and ANCOVA analyses, nominal alpha, subgroup policy and detailed safety summaries. The separate SAP is substantially reconstructable.
- NCT05210023 — the 2021-09-30 pair was written after recruitment had been carried out and was uploaded only after 2021-12-22 completion. Its SAP mixes future tense with an already-performed ANCOVA statement, so the public record cannot establish an outcome-uninformed prospective freeze.

## Hold

- NCT04646109 — the original covers visibly print 04.05.2020, naturally read as 2020-05-04 in the Turkish source, while registry metadata reports 2020-04-05. The protocol is Version 4 without the SAP's IVMC_03 identifier, while the SAP is Version 3 and cites no governing protocol version. The exact governing-version chain must be established from authoritative version history before the otherwise prerecruitment pair can be reconsidered.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT04083456 | post-completion outcome-informed methods | 5 / 2 | d7d68aed1dd24b00a2af4142f4ba9243db63ddf26ab91a730ef159e344342c20 | 4cd1b0525f7ba166fdbafc6785c449975ac74a6a24fdd7a9cb0c24dea4d58060 |
| NCT03224598 | post-completion SAP and protocol leakage | 60 / 26 | 7183af9ecd336d5e91766a5d51e47f8e6b94bcefd50c9b5930cad6711a9e4681 | 70ee50ce3f53353c796475bc2ba4e54fa87f3edeae8bfdad6564579799d63395 |
| NCT04465799 | retrospective executed methods | 10 / 2 | 95c3851dde98f42d452ee2a74c0fd33b6661cfebbfede48b02e1b6c2588c44a9 | ca43d517d5efa7f9260c063bd9628efef4c07e1fc04bf1c1b77a31615e8f0b17 |
| NCT02836470 | outcome-informed interim and revisions | 75 / 24 | 066c77e9efbc58598b66bc597f3a9e8f6d6fa9706e2841bea8682fd8e9919676 | 8bc4fa31d621bb878f191d8651fc662401edff3b702c5cadbb4e188ceb8a8d43 |
| NCT03528551 | protocol leakage identical to SAP | 98 / 13 | cb6b50e77ed31eb57fdb3a2bc18f3e25e5132d9a9f54f3acb673c62f77ba7c48 | 31681a888e9a2d8facb2240e8380ff8b990637606840d3b371abfe77c40b0956 |
| NCT02533570 | protocol leakage | 109 / 41 | c1759c5b643849cdbe0a597c6ab33a22ab054c5dc8e6ee9420e65200e2152563 | 59773925952e6f06bdcc59a9edf868736c51917e79517ae35474e9f57bd6ed51 |
| NCT04646109 | hold: date and version reconciliation | 11 / 2 | e9ca4b1fef31a87b937f13c3be29111ac059580b180e64166e0cc3c0d32f1691 | 268d5beef9a37eae4f8b51c594f30041423077d35e1c7ceb2883637765e1106a |
| NCT05210023 | conduct/completion-informed methods | 5 / 2 | 765350c7db269b11d75c4818a871d902e9fbf05814d9f6af58b4c7ddcad0ffa6 | 35ee526c2009368d199c4140fefd2106516f68dc3de01be249408327dc053f62 |

## Review gate

None of these eight families enters the completed-question count, train/dev/test or a frozen release. NCT04646109 remains outside the actionable queue unless authoritative version history resolves its date and governing-protocol chain. All rejected and held slots must be replaced by newly screened public candidates; every reference PDF remains an annotation-only acquisition artifact and must never be model-visible.
