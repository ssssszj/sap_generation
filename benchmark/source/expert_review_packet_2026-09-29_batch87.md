# Expert Review Packet - Batch 87

## Scope and decision boundary

Batch 87 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally, every physical PDF page was text-extracted, the two scan-only protocols were OCRed, and identity, chronology and decisive statistical pages were rendered for visual inspection. One family is promoted to a first-pass draft and seven are excluded. Promotion is not expert approval or a frozen release. The reference SAP remains annotation-only and must never be included in model-visible input.

## Promotion

### `PUBLIC-ROKHYT-001` / NCT03515681

- The eight-page ROKHyT protocol and one-page SAP share the exact Retail Outlet Health Kiosk Hypertension Trial title, NCT03515681 and 2019-04-15 protocol-version date. Registry chronology records a 2019-03-06 start and 2020-07-30 primary/study completion. Both documents use prospective language and report no outcomes.
- Because the pair follows first enrollment and the protocol includes a vanguard phase, release requires source-history confirmation that neither document incorporated observed vanguard or randomized-trial outcomes. This remains an explicit provenance gate in requirement R021 and `annotation_status.json`.
- Protocol physical PDF pages 1-7 define the pretest, vanguard and 140-person main trial, 1:1 DCC randomization stratified by sex, age and region, intervention/control, visits, eligibility, blood-pressure control and a descriptive pilot-analysis intent. Full-text and visual comparison found no protocol copy of the SAP's stratification-adjusted Mantel-Haenszel relative risk.
- The 22 requirements cover design and phase separation, eligibility, intervention, randomization, masking, prospective sample size, visit schedule, primary and secondary outcomes, estimation, population, estimand, missingness, feasibility denominators, intervention engagement, safety, provenance and reference isolation.
- Open decisions include role-specific masking, derivation from three kiosk readings, analysis population and estimand, missing-data sensitivity, confidence intervals, safety applicability and feasibility denominators. The SAP introduction's `<149/90` is treated as an unresolved source typo because the same page later defines systolic `<140` and diastolic `<90`, matching the protocol and registry.

The annotation remains `draft_needs_expert_review`.

## Exclusions

- `NCT03229759` — protocol leakage. Protocol pages 29-32 already provide mITT/per-protocol rules, no imputation, superiority hypotheses and margin, covariate-adjusted linear regression with an interaction decision rule, confidence intervals, safety Fisher testing and exploratory ANOVA.
- `NCT03687827` — protocol leakage and post-completion package. Protocol pages 39-41 expose power, analysis sets, linear mixed modeling, estimand, noninferiority confidence-interval rules and sensitivity weighting; the selected public files are CSR appendices after completion and embed a post-completion SAP.
- `NCT02047318` — non-independent extension and protocol leakage. Both files explicitly cover the LUM001-303 extension/optional-extension family, while protocol pages 95-97 already give populations, Week-48 efficacy variables, ANCOVA and categorical methods.
- `NCT02846532` — protocol leakage and execution-informed two-part revision. Protocol pages 55-57 disclose the analysis sets, periods, combined Part A/B summaries, Kaplan-Meier and efficacy rules; SAP Amendment 1 follows the Part A review that governed progression to Part B and updates the Part B PK/PD plan.
- `NCT02185040` — post-primary non-independent extension SAP. The selected reference is explicitly for the Active Treatment Extension Phase and postdates actual primary/study completion.
- `NCT05017493` — retrospective results-stage document. The protocol calls the study retrospective, and the post-completion SAP reports observed group sizes, P-values, outcome-driven early stopping and analyses already carried out.
- `NCT04062123` — execution-stage methods record. The near-completion analysis uses past tense, reports mixed models already fit, scanner upgrades encountered during the study and detailed FSL processing choices.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03515681 | promoted with provenance and endpoint-definition gates | 8 / 1 | 158b4d3a3293272d60830b43e51f24d6799d15878891e1bb570674b4a86f92ac | 3efd363db43578d1ba7af42695d10bd331703dd1148186b98cf0d00f4d5a51e8 |
| NCT03229759 | protocol leakage | 53 / 18 | 8823d599ea6fc7dcfda3ade91e07a35004f62210e310e49be9d4006d0a73f171 | 69d4dd07fd5fcc1773677c2c277a3890e0730f98b6d1ae80f44977fdc44950cd |
| NCT03687827 | leakage / post-completion CSR package | 71 / 19 | eef87e6c2ffb774ad5613c8bda3fefd349befdcc4cbb6682abf1f29338de1ace | 19fed40f382402c4d2552cba4df313878d4f18e5a12bf8f2109592d9565b948c |
| NCT02047318 | extension / protocol leakage | 212 / 90 | 869c5c1b2b999e41a5db1e24667c9e1893ca3238a1367c9c8f3117c317a1552a | 09f1d227a7cb25afb2ff59742d4103199756257db6e13db4fde375af59d5d3af |
| NCT02846532 | leakage / execution-informed amendment | 88 / 21 | a71e300bfb1e2359efab78d667e576b39913795525e304aec140722ec1f03b9a | 6786514ab350a082ff4de6c5ba91778a97ede16ba631c2a5c6f0e63df936a9cd |
| NCT02185040 | post-primary ATEP extension | 154 / 48 | 43985f5f5148b1a7866581d535c879945c6301d8926ad26b473295d23175890f | 1b806b7ecae3a42dde38f308709cc75d4294b2dbc30200f2d9b5d7a404e6da50 |
| NCT05017493 | retrospective/results-stage | 12 / 3 | 8809209698c19c03be4145b52ad8fd6b5898eb3b25300ab3a12f8dca72af3149 | 4567adb0b38ed13bf8b72ce0b9d52a692c91b43a0f035348f36a5bf69939f79e |
| NCT04062123 | execution-stage methods | 4 / 2 | a95d7aacf03e5c701b1e721ac264ebdddb67a38aa4dae36da5825e7447badf65 | 0173b579fea669e8fc0632789e6cdc3f904306339cda08731b670c3c6284b10e |

## Review gate

Only NCT03515681 enters the registered benchmark as a draft. The seven exclusions remain outside the actionable pool. After candidate refresh, rejected slots are replenished so the working collection remains exactly 120 public families across registered drafts and metadata candidates.
