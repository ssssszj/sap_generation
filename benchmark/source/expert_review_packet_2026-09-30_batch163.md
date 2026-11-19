# Expert Review Packet: Batch 163

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 163 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 1,008 one-based physical pages; text extraction recovered content from 946 pages. A total of 46 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT04049266 — exclude: SAP Version 1.0 dated 2022-02-03 follows actual primary completion on 2021-11-17. SAP physical page 31 also defines the ICH E9(R1) estimand and sensitivity strategy that supersedes the protocol-level analysis description. The selected target is post-primary and lacks an outcome-uninformed prospective finalization chain.
- NCT04964986 — exclude: SAP Version 3.0 dated 2022-12-12 states on physical page 3 that preliminary data analysis and the timing of the first protocol-defined interim analysis changed the analysis plan. Version 3 adds a Sponsor note-to-file governing the second interim and final analysis; physical page 10 also records closed recruitment and realized French and Belgian enrollment. The target is interim-, preliminary-data- and realized-conduct-informed.
- NCT06447506 — exclude: SAP Amendment 1 dated 2025-06-19 explicitly responds to early termination and parent-study futility. Physical pages 21, 26-27, 49, 51 and 53 revise analyses around actual erroneous administration, dose escalation, termination decisions and treatment received in the parent study. The target is termination-, parent-study- and conduct-informed.
- NCT03393754 — exclude: SAP Final Version 4.0 dated 2019-05-13 follows actual primary/study completion on 2019-04-08. Its revision history also records removal of an analysis after no adverse events of special interest were identified. The target is post-completion and outcome-informed.
- NCT04810962 — exclude: Protocol physical pages 84-88 already specify ITT, PP and Safety populations, LOCF and rescue handling, the Pearson chi-square primary test, fixed-sequence testing, ANCOVA, sample-size determination, tipping-point analysis and PP supportive analysis. This substantially reconstructs the target; SAP Amendment 1 further records LOCF/observed-case changes made in response to 2021-11-03 FDA comments.
- NCT03763058 — exclude: Protocol physical pages 8 and 16 specify the planned sample size, ITT population, paired-Wilcoxon primary analysis, secondary Wilcoxon and McNemar tests and descriptive summaries. Those elements substantially reconstruct the six-page SAP, despite the SAP being dated before enrollment.
- NCT02089334 — exclude: the official/final SAP is dated 2018-12-07, and its cover gives an analysis-plan date of 2018-05-29; both follow actual primary completion on 2018-04-26, while the cover date also follows study completion on 2018-05-17. The selected target is post-completion.
- NCT03889886 — exclude: Protocol physical pages 48-50 already specify ITT, PP and Safety populations, the primary MMRM with baseline, treatment and visit terms, MAR handling, LOCF and observed-case sensitivity analyses and the SANDE/TBUT fixed hierarchy. This substantially reconstructs the target; SAP physical page 25 additionally records deletion of the TBUT hierarchy during study conduct.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT04049266 | post-primary target | 81 / 44 | `0554ade0ad6d8b40b01c629790e1abc6ef192606fff96ee1a8558250ce408f33` | `d82e121164644cd189f5da13e9e6a91befb4dd73e84edce3017de43ee1419df6` |
| NCT04964986 | interim/preliminary-data-informed target | 174 / 51 | `8d4ce2940dd4434ae6613f4e40ffd79b6d5aa06d4ecbd6d93505f0ef86e24887` | `fa453226faf458c32b56e529602ed716e3b1e736c5c3808e8687850939be52e0` |
| NCT06447506 | termination/parent-study/conduct-informed target | 105 / 62 | `c0fc409d91cb60ce8af5b773924396b9aabe1e200c5146c3b0b2e32a7dbd00f0` | `47d520a6987583ad85811481cb55b23ca0e61d579306c832d2dbfd31da29c3e0` |
| NCT03393754 | post-completion/outcome-informed target | 87 / 42 | `3bff1e957e235c501d03d3d28f0901c6f3e917ef82438539ed4b0c946e2356c9` | `609bb745988ee3555c18fd7597a27b74856d9d2348d4aedc228a51409fd61d49` |
| NCT04810962 | protocol leakage and regulator-informed revision | 95 / 28 | `8bfff96ceb5cf78b8961ab0e05254d6d682a8be710cd1b6ff921c477aaa6f8f9` | `18532d2c863e22e676242959dacc0b61a0f1051d075b5a110abddb3271e77ea8` |
| NCT03763058 | protocol leakage | 25 / 6 | `d5e903214a1d4a9a16d98353ad6b789dadf429f40c7773cbf00fabbc05ec70d3` | `a7a6e5309bb33984d1d8cf872859a58cad993e3b07d2245df563308b87272a00` |
| NCT02089334 | post-completion target | 81 / 39 | `efaa21076ef647e04ef95be6f9fda53b221aee9a06c996614ca5b4b03156530b` | `f087d389f611a377feb06485cebad5ba009e2b41f914300684cb6a3eb898ddf7` |
| NCT03889886 | protocol leakage and during-conduct revision | 59 / 29 | `544f722c82bfd83cee97359c8613bf777012a5e4ac3eaa0977672174273f048b` | `388e1cb47e1a9f520f91f58fcf64e894197fdea011636bf358976bacbd1cdca9` |

## Gate interpretation

- A target finalized after actual primary completion is excluded even when it is described as final or predates overall study completion.
- Preliminary-data review, completed interim analyses, realized recruitment, early termination, actual treatment errors and parent-study futility are execution information that invalidates prospective generation.
- Protocol leakage requires substantive reconstructability. Here the affected protocols jointly expose populations, endpoints, models or tests, missing-data or rescue handling, sensitivities and multiplicity; endpoint names or sample-size statements alone would not have triggered exclusion.
- Regulatory comments do not rescue a leaked target and may independently make a later amendment unsuitable when they change the executable analysis program.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
