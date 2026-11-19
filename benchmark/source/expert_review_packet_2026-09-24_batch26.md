# Expert Review Packet — Batch 26

Batch 26 produced no promotable study. Three pairs failed the protocol-leakage gate, while five pairs used post-completion, CSR-oriented, retrospective or otherwise execution-informed documents.

## Screening decisions

- NCT03497897: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 95-103 disclose the Bayesian primary MMRM, decision thresholds, MAR handling, sample size and interim operating characteristics; the SAP also postdates completion.
- NCT03046927: `excluded_wrong_document_type`. Both files postdate completion, and the purported SAP is a one-page grant-strategy extract recording an implemented recruitment increase rather than an independently governed SAP.
- NCT03283085: `excluded_wrong_document_type`. Protocol Amendment 4 removes analyses after program discontinuation and limited sample size and reports actual enrollment; SAP Version 2.0 says it was edited to match actual data and adds event-triggered sensitivities.
- NCT01895777: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 68-75 disclose the noninferiority/superiority hierarchy, populations, models, missingness, randomization and simulation-based sample size.
- NCT03210961: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 112-118 disclose the efficacy and PK mixed models, confidence intervals, safety and interim analysis, and the amendment records an interim-result-driven dose change.
- NCT02386098: `excluded_wrong_document_type`. The post-completion SAP is explicitly for the Clinical Study Report and includes a large CSR presentation plan; the protocol also discloses mITT, snapshot, confidence-interval, futility and interim methods.
- NCT02655692: `excluded_wrong_document_type`. Both files postdate completion; the one-page SAP reports analyses already used, variable selection, responder analyses and observed sensitivity results.
- NCT06380634: `excluded_wrong_document_type`. Both files follow primary completion and state actual enrollment/randomization and statistical analyses already performed.

## Source audit

All 16 PDFs were obtained from ClinicalTrials.gov, SHA-256 hashed, page-counted and extracted by one-based physical page. Identity pages and all decision-defining statistical, timing, CSR, execution-informed and results pages were rendered at 120 DPI and visually inspected.

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT03497897 | protocol leakage / post-completion SAP | 112 / 32 | `fab7601efa6fe7ee0f1efa82d86e37d9c8771be6b04f184515dd137556f3c412` | `9a35dff63fc1b678096a98fb52025893c4cfac9204a291a8e7dcaf0cafae5809` |
| NCT03046927 | post-completion grant extract | 29 / 1 | `4da69b3e3d26e277937872b10a2c6bacca4917684dabde9b6c32661d09375a8a` | `38b2469fe5cdc8f16c7b547e3ab1991d8bf8037069c12c2fb7b18d91e2109943` |
| NCT03283085 | execution-informed amendment / SAP | 212 / 93 | `36ac47491003123df34e294725d1a48d0a5c42198ce94c949bd48efca2f1418b` | `d5052d4867d7dab0d25bdc032431acb54068ec695c33a9c7811d1501083f1e09` |
| NCT01895777 | protocol leakage | 147 / 39 | `6f007752e15672574cc7e0517dec4bf95e52a610fbe0c8a116c28e30f26a62f6` | `98534cc8a7fbefbba0def8acf122d5716f24257f313508353c7b5d7238895386` |
| NCT03210961 | protocol leakage / interim-informed amendment | 148 / 40 | `92c586ab2276f548ee56bd6f8b7c0e8e69b0db033a38d9b76b924372dd0d1c99` | `57382a0fb6934b54a149bfa1d79ebd8acad71ee159d89b31ed4eb02783e3ce65` |
| NCT02386098 | post-completion CSR package | 470 / 484 | `c4fc12eded245f71d20dab7ba7e11d1c627dd8621d66459b91272f2ece253fb8` | `37730f247b0ae7b1a154f5650b8cf026dbdf923a31a657bc2f404cec356f2a8e` |
| NCT02655692 | post-completion executed analysis | 39 / 1 | `64f35e0efc6f887ec71819e5f0b4d15f68ddb6ad79c7efe4493172b7441e5056` | `5ac124b380b5c8789bb824f594f3a679156a07530b09c4a3229ed87037532a3b` |
| NCT06380634 | retrospective completed-study documents | 8 / 12 | `dbec1691966b101f465a5256917fc120b3aa76d089dac579abe2ef4b644c606c` | `02c284cb80ba2a8fe8863657c912faa8f41abffc1c38feb70cdab38840ca79ce` |
