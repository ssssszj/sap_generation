# Expert Review Packet: Batch 171

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 171 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 1,008 one-based physical pages; native text extraction recovered content from 788 pages, and all 118 scan-only SAP pages for NCT04281472 were OCRed. A total of 54 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT04484220 — exclude: SAP Revision 2.0 dated 2023-02-15 matches Clinical Investigation Plan Version 4.0 dated 2022-10-13 and precedes actual completion, but model-visible protocol physical pages 41-42 and 50 already define the Safety and Treated populations, missing/censoring and competing-risk rules, Bonferroni-adjusted 97.5% confidence intervals, endpoint analyses and N=134 with 25% dropout. SAP physical page 4 also records an FDA-requested analysis addition. The protocol substantially reconstructs the target plan.
- NCT05510245 — exclude: SAP Version 1 dated 2022-09-06 identifies Original Protocol C3991007 dated 2022-06-03 and predates actual study start, but model-visible protocol physical pages 62-63 already define the safety and PK analysis sets and the log-PK ANOVA with renal-impairment group as a fixed effect, adjusted geometric means, ratios and 90% confidence intervals. The protocol substantially reconstructs the target analysis.
- NCT03702270 — exclude: the selected SAP is dated 2024-08-05, after actual primary completion on 2021-12-11 and study completion on 2023-05-11. It cannot serve as a prospective target.
- NCT03635788 — exclude: SAP Version 6.0 dated 2024-08-05 follows actual primary completion on 2024-02-12. Physical pages 5-7 state that revisions incorporated the 2024-02-12 DSMB recommendation after an interim efficacy review, stopped Step 2 randomization and changed the study design. The target is post-primary and interim/execution-informed.
- NCT05553366 — exclude: SAP Version 1.0 dated 2023-12-19 follows actual primary/study completion on 2023-12-15. The selected target is post-completion.
- NCT04281472 — exclude: Final SAP 1.0 dated 2023-06-09 follows actual primary/study completion on 2023-05-11. Scan-only physical page 20 further states that an interim analysis was conducted after 30 Stage A participants reached EOSA and that a "Go" decision was announced. The target is post-completion and interim-informed.
- NCT02232074 — exclude: revised SAP dated 2018-02-07 and Protocol Version 5 dated 2017-09-01 precede actual primary completion, but model-visible protocol physical pages 19 and 22-23 already specify N=117 per arm, power, multiple logistic regression, Kaplan-Meier/log-rank/Cox analyses, ANCOVA/multiple linear regression, candidate covariates and no interim analysis. The protocol substantially reconstructs the target plan.
- NCT05285644 — exclude: SAP Version 1.0 dated 2023-07-07 identifies Protocol Version 2 dated 2022-05-13 and precedes actual primary completion, but model-visible protocol physical pages 9 and 62-67 already define ITT/PP/Safety populations, study-eye selection, discontinuation-triggered available-data and multiple-imputation estimands, MAR/MNAR sensitivity with 30 imputations, LOCF and trimmed-mean analyses, hypotheses, power and the primary analysis. The protocol substantially reconstructs the target plan.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT04484220 | executable protocol leakage | 65 / 26 | `fcecd8903d6552fb7148df60afca6657b146cbe8df653467358eeb4b6f4e2b97` | `0b7dbd005faaac47dc29b172abd7f1fc23232df36f593b11f3d69e00d24a5d8d` |
| NCT05510245 | executable protocol leakage | 106 / 24 | `fb1e86df9c4f2cce6c5988c8cb06cf41b6287cf6a655be0825d19ca1a4f40ea2` | `a1a13a1caec2b6af76cfd33a967b0dabc0b40b1bba3d15278356b72f01605161` |
| NCT03702270 | post-completion target | 10 / 10 | `205c3d7169dd69cbd9732ba3b13c234f05839e8cd5a60039719950a199cf76ee` | `4fe45b0360d2da62084a80523c806295711578159e3ba9f9bfb577765136908a` |
| NCT03635788 | post-primary/interim-informed target | 172 / 27 | `a11dd43e59b9c694e7f51ec8160ec2b1400b235cde488ae21b89364ca6603eb4` | `67f6157942ed1c331bed6d51563c0e4225f6cf691c05f9af2edb5ed58f84db6a` |
| NCT05553366 | post-completion target | 57 / 28 | `61dd3c1abb14f73ffdb35b16c177ec13bced8504a6b2a8a15f5f0d3460688fcc` | `7af094a3c5ab220e106547616564b35e7e7f8c1518e15baf0cf2d6c32d8c5974` |
| NCT04281472 | post-completion/interim-informed target | 163 / 118 | `bbf9e1195f6961e848b2c5210010a545d0050cf9caf335d64372c393da4fa31d` | `56e981efeaa2015bd1576436f1890a0ab10467d13c56a6f71c0b8d20afc0f540` |
| NCT02232074 | executable protocol leakage | 34 / 11 | `11a71912471aefbe94a4b3ac788afcb747f2938490a4969227a0ce5189bf6e1b` | `11633bdc996b2d5ea7ac85e256bb3b2a898160557c60f881ee32f79da782efc0` |
| NCT05285644 | executable protocol leakage | 91 / 66 | `7cdb273e411a433bec103977d7565978c2fd2a9d27ca65bec300f650e07be75f` | `6f0016b1d07183629ad73de74f831f1a6195afc5fbc071a7e22c36c498a3501e` |

## Gate interpretation

- A target dated after actual primary or study completion is not prospective, even if the delay is only four days.
- A DSMB recommendation already acted upon, stopped randomization, an announced stage-progression decision and regulator-requested analysis changes are execution information rather than protocol-only inference.
- Protocol descriptions become disqualifying leakage when they jointly expose analysis populations, models/effect measures, missing-data or estimand rules, multiplicity, hypotheses and prospective sample-size decisions sufficiently to reconstruct the target.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
