# Expert Review Packet — Batch 23

Batch 23 produced no promotable study. Five pairs failed the protocol-leakage gate and three pairs used retrospective, results-bearing, mismatched or otherwise incorrect document types.

## Screening decisions

- NCT03436810: `excluded_wrong_document_type`. Protocol physical page 1 uses completed-study language and reports the actual 40 participants plus observed group-level baseline summaries.
- NCT03181893: `excluded_combined_protocol_sap_leakage`. Protocol physical page 50 records an unblinded interim and physical pages 126-133 expose the core endpoint, population, sample-size and analysis strategy; SAP Version 5.0 also postdates actual primary completion.
- NCT04107935: `excluded_wrong_document_type`. Both documents postdate study completion; protocol physical page 2 is retrospective and SAP physical page 2 reports actual counts, selected controls, propensity matching and executed models.
- NCT03008460: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 56-59 disclose the noninferiority margin, power, sample size, hierarchy, confidence-interval rule, regression and secondary, safety and interim methods.
- NCT03248479: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 171-181 disclose analysis sets, cohort sample sizes, Simon two-stage rules, primary and secondary methods, PK and safety analysis.
- NCT03022045: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 58-63 disclose populations, descriptive methods, interim analyses, missing-data rules, feasibility sample size and randomization.
- NCT01900899: `excluded_combined_protocol_sap_leakage`. Despite an independent version-matched SAP, protocol physical pages 49-55 disclose the populations, sample sizes, exact intervals, immunogenicity models, ANOVA, safety analysis and analysis sequence.
- NCT03547869: `excluded_wrong_document_type`. The candidate NCT does not match the NCT on SAP physical page 1; the protocol is an IRB application and SAP physical page 4 is a COVID-termination post hoc deviation plan.

## Source audit

All 16 PDFs were downloaded from the ClinicalTrials.gov registry, hashed, page-counted and extracted by one-based physical page. Every decision-defining page was rendered at 144 DPI and visually inspected. Reference SAPs remain annotation-only acquisition artifacts under the gitignored source tree.

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT03436810 | wrong document type | 6 / 1 | `b676a0e5e97276e83e0d991ba184870d09fca09d0393244d84b37fd0883de8f1` | `638d8c4623f395ef7274e6a6d890b0ac3f6f3c6dae1736c3663b2973fe653665` |
| NCT03181893 | protocol leakage / post-primary SAP | 195 / 48 | `76080c0699693eeca21a9b4aa28472ae349b3d7c2d75db3a30c41497d08a21d0` | `a03ef99b147c05ebdad695adc9bc5e8789b7c0d0eb5fcbce988ead3217cb671d` |
| NCT04107935 | wrong document type | 4 / 2 | `7cdef26b6826a395ab6542ff29b71d74a239492e276ffdd0d8651038b62dc704` | `c15382d8d41a4671bb1af7fdff0635550eace4acd701daad48d1489d0660b890` |
| NCT03008460 | protocol leakage | 103 / 63 | `422fdc54d8598869838b59112973ca7e02219e59ab36314445eeb7937a4b65ce` | `dd3c9843183ea7f305f134ffd0fd6492385fde39ae6524e564372e34cbb431ec` |
| NCT03248479 | protocol leakage | 230 / 50 | `aa4a5bc0d408e33dfe270a3f9015834695c1c9e3419273a0f7b7d1553ace4d73` | `7f3b6af4882f109816d17b969d267a064e3b50c16b8a7e64f6e515cecf9b9ba6` |
| NCT03022045 | protocol leakage | 108 / 35 | `5717ac641d46c6613a29ff8c4bb2c6af6978c35beb5276b38c047b75a8358c93` | `38ddf612e70e0ba9305ab40cb00c05c326b45b28158aa870806cf70444f61bcd` |
| NCT01900899 | protocol leakage | 64 / 15 | `b3703e17adbc6de690c6d4133a5d74f373f14bc8667537efc10be4c0bf6e0d22` | `4ca6fe3777a2bd47738cb442d4cbea2fd0014f52a7aeffd50074677dced7594f` |
| NCT03547869 | mismatched / post hoc documents | 22 / 4 | `ea98dbe576803c420b16a8f1afda44cdca19803add21971ead05b0604ed6c33e` | `311440763797d3aff7555a80352ea93599b74d43c28616c2448024c754e8fdf4` |
