# Expert Review Packet — Batch 18

## PUBLIC-FAM-ACT-DIABETES-001

- 23 requirements; all remain `draft_needs_expert_review`.
- Confirm the exact identity chain across protocol and SAP: University of Pittsburgh `STUDY20110344`, NCT03812614, title, version `v2.2.1 062222` and date 2022-06-22, before primary completion on 2023-12-31.
- Preserve the COVID-adapted design: the first 77 dyads followed the original 12-month intervention and later dyads followed the 6-month adapted protocol, with the primary contrast at 6 months.
- Verify the 268-dyad sample-size assumptions and the linear mixed model with repeated baseline, 6-month and 12-month HbA1c, arm-by-time interaction, specified covariates and 6-month contrast.
- Confirm every primary and supplementary strategy in the color-coded intercurrent-event table, especially home HbA1c, phone surveys, widened windows, noncompliance, delayed classes, Zoom delivery and support-person changes.
- Review the MAR and multiple-imputation approach, control-based MNAR sensitivity, instrumental-variable CACE analysis, compliance definitions and COVID-period heterogeneity analysis.
- Specify the safety-analysis summaries and patient/support-person denominators because the protocol defines collection and monitoring but not an executable safety analysis.

## Version and source decisions

- NCT03812614: promoted. The protocol and SAP share `STUDY20110344`, NCT03812614, title, version `v2.2.1 062222` and 2022-06-22 date. The protocol explicitly sends statistical considerations to the separate SAP and does not expose the executable target analysis.
- NCT02815280, NCT02906917, NCT02234310 and NCT02931838: `excluded_combined_protocol_sap_leakage`. Their protocols expose the core analysis populations, endpoint models, missing-data rules, interval methods, multiplicity or sample-size decisions. NCT02906917 also has a SAP dated after primary completion.
- NCT02646618 and NCT04979858: `excluded_wrong_document_type`. The analysis documents postdate completion and are preliminary, executed or results-bearing records rather than prospective governing SAPs.
- NCT03440320: `hold_version_reconciliation`. Registry metadata labels both documents 2021-03-12, but the protocol is an IRB print view dated 2021-06-17, after primary completion on 2021-05-12. A pre-completion governing protocol version has not been established.

## Source audit

All 16 PDFs were downloaded from the registry, hashed, page-counted and extracted by physical page. Title/version pages and the pages establishing promotion, leakage, retrospective timing or version ambiguity were visually checked. The scanned MY-Skills protocol was rendered and OCRed page by page, and all three MY-Skills SAP pages were visually inspected. For FAM-ACT, protocol cover/design/SAP-delegation pages and SAP cover/power/model/intercurrent-event pages were visually inspected.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT03812614 | protocol | 27 | cf9e5fdf9194aab3c316e23cb48b123a1512441943c4012af11fbe4894cca459 | [Prot_001.pdf](https://cdn.clinicaltrials.gov/large-docs/14/NCT03812614/Prot_001.pdf) |
| NCT03812614 | SAP | 11 | 24de750d7c500132b52d2c3a053a4b150a872ddd16f666c28c533e2f9a5d2aa2 | [SAP_002.pdf](https://cdn.clinicaltrials.gov/large-docs/14/NCT03812614/SAP_002.pdf) |
| NCT02815280 | protocol / SAP | 134 / 125 | 17c38fb5fdcdfa280c2d454c0027946c6c1fc608e1b5274c257e4fffeafe8408 / 8d2397c55130bc52e2b9e47c2e110e33b0839a0eedaf77cecfd48a6d7ef24dcf | [record](https://clinicaltrials.gov/study/NCT02815280) |
| NCT02906917 | protocol / SAP | 142 / 34 | 6ab1e5b66cedf13585c4c528d08649e6db1a45fb02a0e4efea82994eb667339c / 9c78e9c2d1c1bb1a74d2d60ec5e84e3b2e0ad060e7c2ade2dbb6fc64497f964e | [record](https://clinicaltrials.gov/study/NCT02906917) |
| NCT02646618 | protocol / SAP | 19 / 2 | eb920486137f2d3e9fa8e0d5877825d2e87d5368f2c4eac93d70965a094f8fe7 / c3b3004f4429a3cc17adf9810bc3b0ae8f8032ac81ec60c60ff3a4378687f50f | [record](https://clinicaltrials.gov/study/NCT02646618) |
| NCT02234310 | protocol / SAP | 99 / 65 | 3bc2093b0b86cd1a53ab25e97f131b7ec51e30b6b18d53eef4519d5754836dde / 612df63a26202d80a1a68b07b556217672e47e8b96c9386928e5f2fdbba569b3 | [record](https://clinicaltrials.gov/study/NCT02234310) |
| NCT02931838 | protocol / SAP | 96 / 33 | 78668b9ec7b6a0ae5024e2edd45c96c41b1baf94794f3caaf49a90759ae5d97e / dbbbb13a9912ba4d4537840617ed4cdd5a417e17ade308b4eaf8d3611e547ab2 | [record](https://clinicaltrials.gov/study/NCT02931838) |
| NCT04979858 | protocol / SAP | 4 / 40 | c3eb4437500e7c16b0b5515b5a6d60cd1b01ae2fd68bfca6fc9365c2b1285d91 / ece702110c03b82d4060928f2918d9d78404cc389a641c43e509338926aef24a | [record](https://clinicaltrials.gov/study/NCT04979858) |
| NCT03440320 | protocol / SAP | 11 / 3 | e68157d860e79833fc172100dde3b9765411a34ab2874801e11107c97f998635 / 1c598217069a1e98a997b1b46cd434fd870ff57372343a4e1bb5ec9a057c8c4c | [record](https://clinicaltrials.gov/study/NCT03440320) |

The local PDFs and registry snapshots are acquisition artifacts under the gitignored source tree. They are not committed, and reference SAPs remain annotation-only.
