# Expert Review Packet - Batch 97

## Scope and decision boundary

Batch 97 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally and extracted page by page. Decisive identity, chronology, execution-language, sample-size-conflict and target-leakage pages were rendered and visually inspected. One family is promoted as a first-pass annotation draft and seven are excluded. Seven open slots are replenished so the intake remains 120 public families.

## Promotion

- `NCT03505658` -> `PUBLIC-ABRIENDO-CAMINOS2-001`. The 11-page protocol and independent three-page Statistical Analyses Plan share the exact Clearing the Path to Hispanic Children's Health title, Margarita Teran-Garcia principal investigator and 2018-04-06 date. Both were uploaded together during conduct, before the registry's then-estimated 2020 completion. The protocol describes the five-site family intervention, outcome constructs and three assessment occasions without disclosing the reference-only nested mixed model, multilevel mixture model or AIC/BIC selection. Twenty-five evidence-backed requirements were added. Because neither PDF prints NCT03505658 or protocol number 15503 and the trial began in 2015, the registry document association and original UIUC IRB or grant archive remain release gates. Protocol page 10 says 250 whole families, while SAP page 3 and registry metadata say 250 families per arm and 500 total; family-level allocation, site/cycle handling, analysis population, BMI-percentile derivation, estimand, missingness, multiplicity, safety and reproducible power remain expert-adjudication gates.

## Exclusions

- `NCT07280208` — completed-study reconstruction. The protocol is labelled Completed Study and the analysis document describes analyses performed, observed N=57 and results.
- `NCT03345836` — post-completion SAP. The 2021-11-15 SAP follows actual primary/final completion on 2021-08-11.
- `NCT03933397` — protocol leakage. Protocol pages 22-28 expose the primary regression and covariates, multiple imputation, best/worst sensitivity analyses, sample size/power and interim futility monitoring.
- `NCT02899962` — post-completion SAP. The 2019-07-15 SAP follows actual primary/final completion on 2019-06-26.
- `NCT02269917` — post-primary final-analysis SAP. The Week-96 final plan dated 2018-03-28 follows actual primary completion in February 2017.
- `NCT03918174` — retrospective preliminary-results package. The plan uses executed-method language and selects tests from observed non-normality.
- `NCT00250705` — retrospective executed-analysis note. It states that all analyses were conducted and defines the observed mITT/LOCF implementation.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT07280208 | retrospective completed study | 6 / 4 | e11186cfcbf6c88d99ca72dddbc989fe2b2b5903e13f58eaa752e8cc4e16aa1c | e917b0bf6829e73c6e0e1d417f3e9685d7bfc62f5ab5780f028cf748308575eb |
| NCT03505658 | promoted draft | 11 / 3 | fa7c67304989082cfac99ef2cf1f65f8236571a973b9eb1d1d45503bea7c620f | 88bac717b4aa1572cd45a278b6b6747047bd6468ff8b98a14dfce1ee6777de97 |
| NCT03345836 | post-completion SAP | 168 / 87 | 1afdb9d87d9c76a1e67bb8e2265beb929d597e220b26219029ceb30cd16e1003 | bbe8bd71478696c3eea3dad30d04501d45b514c2253b5c4e7903ca965326f76d |
| NCT03933397 | protocol leakage | 34 / 60 | 4fe18b895c90c8d2b5eea356da476fa27587c993029a70b7c0ac7a5a5e6041a0 | fe91b1ad7d34868f55dd763bd7074dd9952dc21b9f05eb6fb0f2b68818527a25 |
| NCT02899962 | post-completion SAP | 178 / 179 | 017b0a5b93b0498047978541acec6b4f6004a3ac3465024df0fe0b2d39c5c572 | f323690bc8ed95f753ba265c60b7e74320689f14418a8becfb8176c9af60049d |
| NCT02269917 | post-primary final SAP | 158 / 49 | ebed5c4bcfb62ebdd21090608b5eedf9c0682027d1489aeef88e9d48e57d248f | fd8260a2b913f4577058aa3d9b7bb890b99d99a23ffc11e41e6fc78bf8fdd9fd |
| NCT03918174 | retrospective preliminary results | 2 / 2 | dfe8db43d3a8835c6261e8b89e335cd134d7b692ad9ac2c3e18f0c656791630d | 311162e8718c0c86f73a3853b3f8d1c1dc12ee2d4148a452cd3d682d8a565a32 |
| NCT00250705 | retrospective executed analysis | 6 / 1 | d3ce4b4c5158bbdd069181d4065cd44484d208f3d7413eaa3a61d2b6b8277d55 | eb4216fa8871f3b6fa1b91cd3aa1f974c48b5ac5638eabb7506f2aef5eb1ec52 |

## Review gate

The promoted Abriendo Caminos 2 family remains `draft_needs_expert_review`; it is not expert-approved or split-frozen. Its reference Statistical Analyses Plan remains annotation-only and must never be model-visible. The excluded families do not enter the completed-question count.
