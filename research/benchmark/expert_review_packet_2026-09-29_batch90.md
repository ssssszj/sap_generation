# Expert Review Packet - Batch 90

## Scope and decision boundary

Batch 90 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally, every physical PDF page was text-extracted, and identity, chronology, execution-language and decisive statistical pages were rendered for visual inspection. No family is promoted: seven fail the protocol-only leakage boundary, including two with post-primary or post-completion reference plans, and one is a post-completion execution-stage methods package. These decisions do not reduce the 120-family intake; all eight slots are replenished.

## Exclusions

- `NCT04074941` — protocol leakage. Protocol pages 27-30 reproduce the SAP's baseline-adjusted linear regression, ITT and Wald test, subgroup and on-treatment analyses, sensitivity analysis and missing-data checks.
- `NCT04556734` — protocol leakage. Protocol pages 12 and 71-75 expose the sample-size assumptions, MMRM factors and covariates, unstructured covariance, CMH test, nonresponder imputation, analysis sets and output plan.
- `NCT02825251` — post-completion SAP plus protocol leakage. Internal SAP Version 1.0 is dated after both primary and study completion, while protocol page 108 exposes the noninferiority margin, fixed-sequence hierarchy and estimand.
- `NCT02762500` — protocol leakage. Protocol pages 70-71 expose the power assumptions, full-analysis and safety sets, one-sided Pearson chi-square comparison and 90% confidence interval.
- `NCT01151423` — protocol leakage. Protocol pages 111-112 expose exact sample-size assumptions, the one-sided log-rank test, Kaplan-Meier estimation, stratification, ITT/PP populations and censoring.
- `NCT02635776` — post-primary SAP plus protocol leakage. SAP Final Version 2.0 follows actual primary completion, and protocol pages 93 onward already contain detailed populations and an executable statistical plan.
- `NCT04336332` — protocol leakage. Protocol pages 13-14 expose external-pilot-based power, the uncorrected chi-square method, Kaplan-Meier/log-rank analysis and exact allocation and sample sizes.
- `NCT04864210` — post-completion execution-stage methods. Both uploads follow study completion; the protocol is a registry export with actual enrollment, and the analysis note describes endpoints already analyzed and tests already used.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT04074941 | protocol leakage | 36 / 10 | 293aabffd6f10d3b56399d120a995ad05190fabdcf2347b89fbf111cc48b93dd | d10aa65ab53261a612c865d4b3185d40633bb47774fc5f4dea9359198d1961d7 |
| NCT04556734 | protocol leakage | 100 / 72 | ca6c7e9cae9838c941ed6a10c7a77de92e28b9941a036de86efbc316faabcb6f | a925f7e208471ab774f0aa8f22e8f6cdcb31e5a04257af803d7f39a4777294b8 |
| NCT02825251 | post-completion / protocol leakage | 158 / 33 | a416499d17e8ff4e7850dbcdb540816b0ef360cacb923efdafa1138493b2470e | 254af33ab50dfcd9975c0581b860297969128fb6a69acace6dcdd164245b0411 |
| NCT02762500 | protocol leakage | 91 / 27 | 92247634485a4078a490a9036c63608056935b5bb344e712f23083dd4b679b95 | 182d68edcc5cde5cd5abb671ead1025519aff384a59819f32d60142c182ab10f |
| NCT01151423 | protocol leakage | 128 / 61 | d88ef429a442453464aa9e603556aee5759a462fb36a3512aa1df6447a211684 | 1bf8262a727ab54707a2605058f5be9872067c99f85a8f4647e9cb02f0b7a06e |
| NCT02635776 | post-primary / protocol leakage | 127 / 81 | 09f0a25ccc9c0c013c3bd7095a8df96f9a8bf1f4569df7bf7cf9be507c5b8e14 | 601acfd821dfa5ea5f7eb3ab2f685783b18eceb5b79721310689c89df79d8549 |
| NCT04336332 | protocol leakage | 32 / 18 | e4bda2d4d46f842627059950a6bd2968ec576ffc57fc1ffa4f8b6fddb4adf9db | 54edadc58aefc0ba175b0ce334667edefab4eaed1ff636464c8ad75e48074fcf |
| NCT04864210 | post-completion methods | 11 / 2 | e16c036a21d8ac78efb93e9a2619428e716886e78aed66976c14b45eefd5f66f | 919ac34dbd581f3f702057fc0800a00e39399f7d3dce38bf6c00addf41e60d4f |

## Visual review

Rendered one-based physical PDF pages confirmed each decisive finding: sodium-reduction protocol page 28, etrasimod protocol page 12, faster-aspart protocol page 108, LYC-30937 protocol page 71, caplacizumab protocol page 112, PALISADE protocol page 94, COVID-19 combination-treatment protocol page 13 and thoracoscopic-analgesia analysis page 2. No exclusion depends on truncated OCR or an inferred hidden passage.

## Review gate

None of the eight families enters the registered benchmark. Their slots remain outside the completed-question count and are replenished so that the working collection continues to contain exactly 120 public families across registered drafts and metadata candidates.
