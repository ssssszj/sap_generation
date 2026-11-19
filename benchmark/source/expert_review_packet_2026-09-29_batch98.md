# Expert Review Packet - Batch 98

## Scope and decision boundary

Batch 98 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally and extracted page by page. Decisive identity, chronology, scope, execution-stage and target-leakage pages were rendered and visually inspected. Two families are promoted as first-pass annotation drafts and six are excluded. Six open slots are replenished so the intake remains 120 public families.

## Promotions

- `NCT01458990` -> `PUBLIC-PPI-DYSBIOSIS-CIRRHOSIS-001`. The three-page protocol and independent one-page plan print the same NCT, title and 2017-11-29 date and precede actual February 2018 completion. The protocol expressly covers only the decompensated-cirrhosis portion and says the compensated-cirrhosis and healthy-control portion was already published, so this question excludes those cohorts. It defines PPI initiation/withdrawal and paired specimens while deferring statistics to the separate plan; the reference-only Wilcoxon and Kruskal-Wallis methods are not leaked. Twenty requirements were added. VCU/VA prospective provenance, exact subcohort binding, missing numeric target, microbiota feature derivation, exact Kruskal-Wallis contrast, nonrandomized confounding, missing specimens, multiplicity and safety remain expert-review gates.
- `NCT07493655` -> `PUBLIC-TDM-MMF-LUPUS-NEPHRITIS-001`. The six-page protocol and three-page independent SAP have the exact title and 2026-01-29 date and precede the estimated 2026-07-01 start. The protocol gives the randomized TDM-versus-standard design, blocks, interventions, endpoints and broad sample-size assumptions but not the reference-only ITT rule, chi-square/Fisher comparison, adjusted logistic covariates, MPA test selection or STATA/JASP choice. Twenty-three requirements were added. Because neither PDF prints the NCT or formal version, UFMA ethics provenance remains a gate. The registry's sequential label conflicts with the apparent parallel design; masking roles, remission classification, primary analysis hierarchy, alpha 0.10 versus 0.05, 49-per-group plus attrition arithmetic, missingness, multiplicity, safety and data-contingent exploratory models also require adjudication.

## Exclusions

- `NCT02575833` — protocol leakage. The protocol exposes analysis populations, ANOVA/stratum, a 90% confidence interval and -90-second safety boundary, Kaplan-Meier/log-rank methods and safety summaries; the pair is also wrapped in a CSR package.
- `NCT03915860` — protocol leakage. Protocol pages 62-65 expose ITT, baseline and descriptive conventions, safety tables, subgroup factors, LOCF, binary nonresponder imputation, 95% intervals and the 50-subject estimation design.
- `NCT02827708` — post-completion analysis documentation dated 2018-12-13 after primary completion on 2018-04-10 and final completion on 2018-05-15.
- `NCT02515630` — internally dated final-analysis SAP from 2017-10-16 after July/August 2017 completion; registry metadata incorrectly repeats the protocol date, and protocol pages 58-61 also leak executable methods.
- `NCT02876926` — both documents dated 2018-09-15 after actual primary and final completion on 2018-02-15.
- `NCT03869268` — execution-informed COVID amendment containing the observed 46 participants/83 endotoxin visits, interim analysis, termination rule and missing-period analyses; the protocol reproduces the detailed plan.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02575833 | protocol leakage | 169 / 52 | a86d212afb3c2148723e00586211a4bb46a97a7f9b20aa7acefd93ef7614615e | b00e9cd772508c5c246b2c720cab03fa72e3465df31e6f1895cbb7b5d81f680b |
| NCT03915860 | protocol leakage | 88 / 50 | b2a8bcc216181e59aa7b4112198bdb13138af96b30f751129ec1de8549e469d4 | 0fab509b00172dcc66aa20d0a56601851d2145abc9b76add3163fd4f5a6e2fab |
| NCT02827708 | post-completion analysis | 168 / 37 | bf983edda7eb52c2c786a46ce8b82344c45e1bae521edcb689eacf0dfff6a681 | f9b1f16d7ba716570d6c5ea6a3a70bcb871d06f15416e1104c51022bb0c4b87e |
| NCT01458990 | promoted scoped draft | 3 / 1 | 9865543befe141c79964e13852054c97e137f71622a8a180a809952bb5a504c2 | 77179a207107ec2c40dbcde090fc0f15785331fc30c74f3674cd2b7551895aec |
| NCT02515630 | post-completion final SAP and leakage | 80 / 133 | 70d5a268d4c94a2cfaec16d1897ae7b712b134ae28d53c00c9eda693aeac8183 | 1b33b2e47ec1c3fbea856f881cae2d116a8f4535adc265b5121641f032255b1c |
| NCT07493655 | promoted prerecruitment draft | 6 / 3 | 1fe2aebd642dd7f52ff8551d9efc72403d4cbc3f112ef1a401833807a078ca10 | 655eca17400c7be3bd58d11add8bb621e3fb837e86fbefa0566f1e2b94460e68 |
| NCT02876926 | post-completion pair | 15 / 2 | fa035ef5c9e9fac134e579d502dc7f6d2d687e02d20f23748e0ed5e95748982a | 17c3792639a7404c98e03f1af7fff1e2eb519dc8e33a9f8b5b2adfde18b92e2f |
| NCT03869268 | execution-informed COVID/interim plan | 62 / 9 | 26e39c8074691b2b8968a1f734832441c8375909598039f8582070b4dab111be | 062e4121a202b6efa85faee5994b44147142f9f8654957da1110d0155997b0aa |

## Review gate

Both promoted families remain `draft_needs_expert_review`; neither is expert-approved or split-frozen. Their reference SAPs remain annotation-only and must never be model-visible. The six excluded families do not enter the completed-question count.
