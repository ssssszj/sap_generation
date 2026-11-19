# Expert Review Packet - Batch 92

## Scope and decision boundary

Batch 92 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally and page-extracted; the scan-heavy 97-page NCT06700850 protocol was fully OCRed, and decisive identity, chronology, leakage and execution-stage pages were visually inspected. One family is promoted as a first-pass annotation draft and seven are excluded. The seven open slots are replenished so the intake remains 120 public families.

## Promotion

- `NCT04167566` -> `PUBLIC-PAKRO-MTTT-001`. The 29-page protocol and two-page SAP share the exact Pakro MTTT title and 2018-03-18 date and precede actual 2019-07-30 completion. The model-visible protocol describes design, intervention and prospective sample size but does not reproduce the reference-only t/Wilcoxon, ANOVA/Kruskal-Wallis, logistic/conditional-logistic, confounder-adjustment and trend-test details. Twenty-two evidence-backed requirements were added. The blank NCT fields, during-enrollment date, ambiguous arm/community language and unspecified clustering, estimands, missingness and multiplicity remain explicit expert-review gates.

## Exclusions

- `NCT04576897` — protocol leakage. Protocol page 9 already supplies descriptive statistics, t tests/ANOVA, Pearson correlation, multivariable analysis and AUROC, substantially duplicating the two-page analysis upload.
- `NCT06700850` — protocol leakage. Full OCR shows protocol pages 63-69 expose FAS/PP, Newcombe score, 15% non-inferiority margin, 97.5% CI, Bonferroni, 120 evaluable, LOCF, PP sensitivity and the testing hierarchy.
- `NCT05844137` — wrong document type and chronology. The grant/IRB pilot proposal and statistics excerpt are dated four months after study completion.
- `NCT02943447` — protocol leakage. Protocol pages 68-72 expose analysis sets and treatment attribution, the administrative interim, no-imputation convention, descriptive/CI analysis and sample-size rationale.
- `NCT03191799` — execution-stage final plan. SAP v3 is dated 14 days before completion, after planned interim analyses and multiple during-study revisions adding or revising surgery, COVID-19, biomarker, PK and event-definition analyses; outcome-uninformed provenance cannot be established.
- `NCT02709538` — protocol leakage. Protocol pages 57-58 expose the analysis sets, ANCOVA covariates, multiple imputation and confidence intervals; the SAP also conditions imputation on observed missingness.
- `NCT05373706` — wrong document type and chronology. Both two-page files postdate completion by about one year and describe executed recruitment, randomization, intervention and analysis methods.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT04576897 | protocol leakage | 12 / 2 | d376fa083453d25012adbbca577d42e680660e355214caea9099a24c39318c7a | d4c368d51a93294b5b58788e48e5f38e2fe7aec7b303d430a504c7ae14ba0f5b |
| NCT06700850 | protocol leakage | 97 / 71 | 2fb0a37d0557d1997aebb407c942486bd0947b54aec8d0914e2d9262975ff07d | 74d9044f59d0e8339d716384f3b33d2eae542de7ef68dcc06421792b4de72a7f |
| NCT05844137 | post-completion grant/IRB excerpt | 8 / 2 | 6294a8ded25ec1664226351f04e13fb9b16f0116ec7606ac090b9410a21c6b09 | 9e4e50b3916d5ccdb8bc24b41b19d8a5987d73912853b473fdad98cbcb1192fa |
| NCT02943447 | protocol leakage | 90 / 68 | c3e7b0bc49ae426a6abf5c0945b529a012db21a77a5a6e6d928090fe755af1b1 | 561fe338b8bb225cdbe635e6373164039f56aa5d70387f3e541ec9366ec6fa0d |
| NCT03191799 | execution-stage final SAP | 174 / 54 | 75723a1c96632c651b812568a082310fa5850df1d31731bcc63dcf222396c197 | cad09e53712104d2eff50d3e2846d12ff29a395273f3d532450e49c16525fb7c |
| NCT02709538 | protocol leakage | 91 / 152 | 1016be4cf09ffe74ad8bd5fe2ec134f3a9884b5d791dd04ff7f127fc10cdb0c6 | 2bf7a644fa25bca0f33d8a9d82e76c9c3bc1dc8940f9736db30714013a139d01 |
| NCT04167566 | promoted draft | 29 / 2 | 9cb8685abea57dfb21c54c277b71f07263543ee444b2e579cbebf4f19924f187 | 669909c04cb1f68c42039d8a2224f9ffaae5cf219a97b9223a87d57916e7348e |
| NCT05373706 | post-completion executed summary | 2 / 2 | 57ae82278bd1b229105a3f3a90af202d63160393be3fe0ba4898a5bdc1098959 | a8ef13e0d70fe4bd8eb3824b92cb830230f6d22575f0ef6e639b9b5846675f7f |

## Review gate

The promoted family remains `draft_needs_expert_review`; it is not expert-approved or split-frozen. Its reference SAP remains annotation-only and must never be model-visible. The seven excluded families do not enter the completed-question count.
