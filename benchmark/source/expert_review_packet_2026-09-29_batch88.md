# Expert Review Packet - Batch 88

## Scope and decision boundary

Batch 88 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally, every physical PDF page was text-extracted, and identity, chronology, redaction and decisive statistical pages were rendered for visual inspection. One family is promoted to a first-pass draft and seven are excluded. Promotion is not expert approval or a frozen release. The reference analysis document remains annotation-only and must never be included in model-visible input.

## Promotion

### `PUBLIC-HIV-NRT-001` / NCT02982772

- The eight-page protocol and three-page analysis document share the exact *Biobehavioral Intervention for Smokers Living With HIV* title, NCT02982772 and 2016-03-24 date. Registry chronology records a 2016-05 study start and 2021-05-31 primary/study completion, so the pair predates enrollment. Both documents use predominantly prospective language and report no outcomes.
- Protocol physical PDF pages 2-8 define the population, standard versus tailored NRT, statistician-generated permuted-block allocation, 3/6/12-month abstinence outcomes, biochemical verification, relapse/rescue procedures, secondary outcomes, safety and broad covariate intent. Full-text and visual comparison found no protocol copy of the reference's endpoint-specific logistic regression, repeated-binary GLMM, MNAR sensitivity, mediation sequence or PCA plan.
- The 25 requirements cover design, eligibility, randomization, treatment contrast, estimand, abstinence definitions and derivations, visits, secondary outcomes, hierarchy, population, regression and repeated modeling, covariates, missingness, MNAR sensitivity, mediation, PCA, sample size/power, safety, provenance and reference isolation.
- The protocol says 500 participants will be allocated 1:1, whereas the reference says 600 will be recruited so that 500 remain after 15% attrition. Both prospective source statements are preserved pending adjudication; the registry's later actual enrollment of 488 is not substituted for either target.
- The reference page 3 contains isolated past-tense phrases: the treatment-effect model "will have been conducted previously" within a future mediation sequence and "The full models included" listed covariates. The pre-start date and surrounding prospective language support retention, but release requires source-history confirmation that these are proposal/template tense rather than evidence of analysis of this trial.

The annotation remains `draft_needs_expert_review`.

## Exclusions

- `NCT02961894` — post-primary pair and protocol leakage. Protocol Version H/SAP Version 2.0 are dated 2019-08-01 after 2019-02-28 primary completion; protocol pages 22-28 already specify performance-goal hypotheses, exact-binomial tests, analysis groups, missingness, power/sample size and interim analysis.
- `NCT03743038` — protocol leakage. Protocol pages 40-42 already give pilot sample-size logic, endpoint derivations, safety/mITT/PP populations, compliance, descriptive efficacy analysis and detailed AE/LSR displays, closely reproducing the SAP; the SAP was finalized four days before completion.
- `NCT03922750` — post-completion pair and protocol leakage. The public cover date is 2020-05-28 and embedded SAP date is 2020-02-03, both after 2020-01-27 completion; protocol pages 49-52 expose the estimand, hypothetical strategy, FAS, multiple imputation, ANOVA/ANCOVA and Rubin pooling.
- `NCT02536404` — non-independent extension and post-completion SAP. Both files cover APD334-005, an extension of APD334-003, and SAP Version 1.2 is dated 2018-11-27 after 2018-11-01 completion.
- `NCT02913326` — protocol leakage. Protocol pages 72-76 expose the analysis sets and periods, ITT attribution, frequency/CI/HR analyses, ICH stratification, CMH testing, missing-data rules and sample size.
- `NCT02554019` — post-completion SAP and protocol leakage. SAP Version 5.0 is dated 2018-01-23 after 2017-10-25 completion; protocol pages 72-73 already provide analysis sets, descriptive methods, optional LOCF and safety summaries.
- `NCT03205488` — post-primary adaptive package and protocol leakage. The Cohort 1 SAP is dated after Cohort 1 primary completion; protocol pages 132-140 expose primary testing, chi-square/Poisson methods, the dose-selection algorithm, futility test, alpha, assumptions and power, while Cohort 1 results govern Cohort 2 dosing.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02961894 | post-primary / protocol leakage | 58 / 20 | ee286b14667f1294e7e3cd656788a1cdb47cc0405ca5ac0ebf05db1c172cd86d | 9152864ea72daee235b7ecf3c63cb38661500d54b734562d9c32eb237ac4db46 |
| NCT03743038 | protocol leakage | 61 / 15 | bd9fccedc9984a2f7533305720433d2ffe62ab61eed3335987725c38ea44c4a7 | fec27b1701283652cf06d332e4798837a4f30ec41baae9326f707c0931983a4b |
| NCT03922750 | post-completion / protocol leakage | 105 / 15 | 6785f6da6fce946fbf73ed15474c09b57bc20c7704f3eecc32791a40a535a8b6 | fcee4b4bfcc0b6c54451e7432d7a934aa2025245cdf00b4f00dc08c3c6a25b1f |
| NCT02536404 | extension / post-completion | 90 / 51 | 6446078120d84aea988f4c01b40e2c61ce274936d04904c7975405abc158d740 | db410ea6b283c024d381d04a4fef9c793df735b05608331290b76a5d39d11fd1 |
| NCT02913326 | protocol leakage | 97 / 30 | be847b55475085a5d62c6c0a115c805ac5f991a77501fc0986ef677e2b25bab1 | 99d8f635a02daef7d2ffcfaa8c56f44d987b1e811af9ce67938f065b1132b35a |
| NCT02554019 | post-completion / protocol leakage | 104 / 51 | ffcceef33a223e13f8274df13cbd806d40c3f44b5814a548e4379576c5c8dc4f | 696df17c6597e52d722c31c9db88048c8c51b2eff807acd4ca7f34f7ec561f87 |
| NCT02982772 | promoted with provenance and sample-size gates | 8 / 3 | 088f4fe30670b8eaf0d3d681a105d98d5586828851cf9489694a4be97e542daa | 03161df43da8f32db7ad02ba073167bc2e3f93c3d5cfe2259a2395f70c81d753 |
| NCT03205488 | post-primary adaptive package / protocol leakage | 198 / 20 | 7785125158fd19b27e9f17f6bb2a449f298760b1d0523c9201e2b66b931eee13 | 4f26f0fc1a3ab2ee14655bac6a566fa413bb4e9c77d9bd70dacf30b919f2c420 |

## Review gate

Only NCT02982772 enters the registered benchmark as a draft. The seven exclusions remain outside the actionable pool. After candidate refresh, rejected slots are replenished so the working collection remains exactly 120 public families across registered drafts and metadata candidates.
