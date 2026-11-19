# Expert Review Packet: Batch 140

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 140 review-queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,099 physical pages. Native text was extracted from every file except the 67-page NCT03030235 protocol, which was fully OCRed. A total of 178 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. Seven pairs were excluded, one was placed on version-reconciliation hold, and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT02018367 — exclude: the alleged one-page SAP is only physical page 6 of the model-visible Baylor IRB Human Protocol Report, duplicated verbatim; that report also contains preliminary pilot performance and the complete generalized-linear mixed-model analysis.
- NCT02417935 — exclude: SAP Version 2 postdates actual primary/study completion, was approved only before final database lock and updates the sample-size rationale from a conduct-era protocol amendment; the selected protocol already exposes the MMRM, noninferiority margin, covariance structure and LOCF/BOCF sensitivity program.
- NCT02931539 — exclude: SAP Amendment 3 postdates primary/study completion and adds report-preparation clarifications and COVID-19 analyses; the conduct-era protocol already exposes populations, sample-size, multiplicity and executable efficacy methods.
- NCT03028870 — exclude: the SAP postdates actual primary and study completion, while the prerecruitment protocol already discloses the MMRM, treatment-by-time structure, analysis populations, missingness, multiplicity and interim efficacy/futility design.
- NCT03030235 — exclude: Protocol Version 3.0 was issued three years after enrollment began, and the final SAP is dated one day before actual completion; the protocol and SAP expose the same ANCOVA endpoint, covariates, prospective N=320 and substantial population/sensitivity program without a clean prospective amendment chain.
- NCT03610646 — exclude: Final SAP Version 3.0 follows actual primary completion and incorporates COVID-19 disruption analyses plus an FDA-requested FAS-to-ITT change; the conduct-era protocol independently exposes the equivalence margin, MMRM, covariance, populations and sensitivity program.
- NCT04664153 — exclude: although the protocol is prerecruitment, it exposes the estimands, mITT/safety sets, ANCOVA, copy-to-control multiple imputation with Rubin combination, exact risk-difference intervals and no-interim rule that form the executable SAP core.
- NCT06400498 — hold: prerecruitment Protocol Version 2.0 postdates SAP Version 1.0 and no governing amendment chain reconciles their substantive Stage 2 primary-analysis conflict: the protocol specifies a Wilcoxon rank-sum test while the SAP specifies a covariate-adjusted proportional-odds likelihood-ratio test.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02018367 | duplicate protocol/SAP plus pilot-result leakage | 12 / 1 | `09dcea009df989ee674587faeeaacbe6a14420b4617f006ecc095b7508b33207` | `e619e3cbbd8cff5d1294f9ec302a605499c6f444c73e8c0df6b9d18dd30ff9f2` |
| NCT02417935 | post-completion/conduct-amended target plus leakage | 67 / 21 | `a5f5ae19fa048ddcfbe1bba60dcde9113e25b6b2c1a07fdb8566111034c8a523` | `0c56d72226e7bd6dc7f80f4c3f47b91661ab94215ca65a3eff83652f914635ee` |
| NCT02931539 | post-completion/COVID-informed target plus leakage | 199 / 84 | `efae9bdcaba0223df9b023cfd93d587195c4524a019db986256cbf048e1d691b` | `79c7cba4f7c515e55dfe511b9547508293272e8b420f020937d3e420570f68fc` |
| NCT03028870 | post-completion target plus leakage | 173 / 80 | `a7df75bebcea08ea67586ac351950f95625f87bc7d6ee1a7ae523803815d8c16` | `e8d3e7fc5c4216e37c8e18cedfe3af934ca686b4a7c9d9d59b653c1a531f45b8` |
| NCT03030235 | near-completion target and conduct-era protocol leakage | 67 / 35 | `876324fec5b766b83ef94ad28a09f06822bc63cceb88e50edbe9157aabadbaba` | `aae73c543f89d8a7b38dc1c92146319c5d16dfe81a03a19b9b0384f614f942e9` |
| NCT03610646 | post-primary/FDA- and COVID-informed target plus leakage | 79 / 48 | `2b3968f8d6b2103ba744fab1912f4e73168aa410c1e1946483adb724c11cfab5` | `e2655532067b7653aad2e22138bd27456f320dddb90afe369d845db87272eb37` |
| NCT04664153 | protocol-embedded target leakage | 131 / 63 | `992ce59220699f8b95939dadb9b6a6b8ea4ff8935053d32abd528cb768f40c8f` | `7709157222072a4c919eede8b53c79e21bdc40de38f59ae3567ca0f9270c58b8` |
| NCT06400498 | unreconciled governing-version and primary-model conflict | 30 / 9 | `4719bd024c0c3d845e55d25f1f8f0affb51e74989066197f44b2090786bdde65` | `50e3444051365f61ed302acd1f8fc3b32e2344e183e5ce23bb1bc6a4843b7600` |

## Gate interpretation

- A file labeled SAP by the registry is not an eligible hidden target when it is merely a page copied from the protocol. Preliminary pilot performance in the same model-visible package is outcome leakage.
- Approval before database lock is not equivalent to prospective governance when the selected SAP follows primary/study completion or explicitly incorporates conduct-era amendments, COVID-19 disruptions, regulatory feedback or report preparation.
- Protocol disclosure of endpoints and sample size alone is permitted. These pairs fail where the model-visible protocol additionally fixes populations, estimands, models, covariance, imputation, multiplicity, interim rules or sensitivity analyses sufficient to reconstruct the target.
- A prerecruitment protocol/SAP pair is not promoted when the dated governing chain is reversed and the documents disagree on the primary analysis. NCT06400498 remains a hold rather than an exclusion because an authoritative amendment history could in principle reconcile the May and July 2024 documents.
- Registry actual enrollment was used only as conduct context and never substituted for a prospective sample-size target.

## Replenishment

All eight rejected or held slots are replenished from the official API. The release-eligible intake remains 120: 105 public first-pass drafts and 15 actionable metadata candidates.
