# Expert Review Packet — Batch 10

## PUBLIC-DYSVASCULAR-AMP-001

- 15 requirements; all remain `draft_needs_expert_review`.
- Confirm that the protocol dated 2014-01-05 and independent same-date SAP form the governing pair.
- Adjudicate the change from analysis restricted to at least six weeks of exposure with early-termination carry-forward to maximum-likelihood repeated measures using all available data under MAR.
- Specify analysis population, covariance structure, degrees of freedom, death or inability-to-perform handling, and sensitivity analyses.
- Preserve TUG at Week 12 as the sole powered primary endpoint and the other outcomes as unadjusted exploratory analyses.

## PUBLIC-DIABETES-TEC-001

- 15 requirements; all remain `draft_needs_expert_review`.
- Preserve the study architecture: TEC versus peer support alone is randomized, while the usual-care group is observational.
- Verify the 348-patient/87-peer-mentor clustered sample size, initial-pairing ITT rule, 6-month HbA1c primary endpoint, and 12-month sustainability analysis.
- Adjudicate propensity-stratified missing-outcome imputation, covariance and degrees-of-freedom details, and multiplicity across secondary, mediation, and moderation analyses.
- Do not replace the protocol target with the registry's eventual observed enrollment.

## PUBLIC-GFLIP-VITC-001

- 15 requirements; all remain `draft_needs_expert_review`.
- Preserve the single-arm efficacy design. Randomization applies only to immediate versus two-cycle-delayed ascorbic-acid timing for acute safety.
- Confirm the denominator and time origin for 12-month survival and define censoring for OS and PFS.
- Treat historical FOLFIRINOX comparisons and G-FLIP versus post-progression G-FLIP-DM response analyses as contextual or exploratory, not causal concurrent-control analyses.
- Define the analysis population, missing-data rules, multiplicity, and study-level success criterion.

## PUBLIC-PRENATAL-ESBI-001

- 15 requirements; all remain `draft_needs_expert_review`.
- Confirm the protocol and independent SAP by exact title, NCT identifier, 2015-05-01 document date, and 2015-06-15 approval date.
- Reconcile the randomized enrollment wording with the SAP's conservative 65-per-group and 60-per-group follow-up scenarios.
- Define the primary risky-drinking outcome hierarchy, drink-size derivations, depression interaction, formal analysis population, and pregnancy-after-randomization handling.
- Adjudicate continuous-outcome modeling, GEE link and robust variance, multiple-imputation implementation, and multiplicity; preserve the SAP's explicit post-hoc labels.

## PUBLIC-VM202-PDN-001

- 20 requirements; all remain `draft_needs_expert_review`.
- Confirm Protocol VMDN-003 Version H and SAP Version E, both dated 2019-09-05, as the governing pair.
- Verify the two sequential Day 90 primary endpoints, gated Day 180 endpoints, diary derivations, 477-participant sample size, ITT and safety attribution, and fixed-sequence success rule.
- Adjudicate continuous and categorical repeated-measures models, Kenward-Roger degrees of freedom, covariance fallback, MCMC and mean-other-group imputation, fully conditional responder imputation, and PP sensitivity populations.
- Review protocol-revision cohorts, prohibited-medication handling, subgroup interactions, and conservative missing AE conventions.

## PUBLIC-TWICE-WEEKLY-HD-001

- 16 requirements; all remain `draft_needs_expert_review`.
- Confirm the exact-title/NCT/date match between the four-page protocol and one-page Data Analysis Plans dated 2025-04-30.
- Adjudicate the KDQOL-36 equivalence estimand, -5 to +5 margin, 90% confidence interval, treatment-by-period branch, and 30-completer power basis.
- Specify sequence generation, allocation, washout or carryover handling, covariance and degrees of freedom, and randomized and per-protocol analysis populations.
- Add an equivalence-appropriate PP and MNAR sensitivity analysis and operational period-specific safety summaries.

## Version and source decisions

- NCT01929018: promoted. Exact title and date match; the independent SAP contains the final maximum-likelihood repeated-measures plan not present in the protocol.
- NCT01855399: promoted. Exact title/NCT/date match; randomized TEC versus peer support and observational usual care are kept distinct.
- NCT01905150: promoted. Protocol number, NCT identifier, title, and date match; overall efficacy is single-arm and only vitamin-C timing is randomized.
- NCT02337361: promoted. Protocol and SAP share title, NCT, document date, and approval date; explicitly post-hoc analyses are labeled as such.
- NCT02427464: promoted. SAP Version E explicitly names Protocol VMDN-003 Version H and both are dated 2019-09-05.
- NCT03874117: promoted. Exact title/NCT/date match; the protocol does not expose the DAP's equivalence model or margin.
- NCT03658941: `hold_version_reconciliation`; cover dates conflict with the SAP's internal version/date and governing-protocol date.
- NCT02242760, NCT07148791, and NCT03669133: `excluded_combined_protocol_sap_leakage`; the protocol already exposes the target analysis plan.
- NCT04173429, NCT03101020, NCT03374306, NCT07437209, NCT02205177, and NCT02088216: `excluded_wrong_document_type`; the analysis uploads document completed analyses or observed-data decisions in the past tense.

## Source audit

For every candidate below, title/version pages and pages supporting admission, hold, leakage, or retrospective-document decisions were visually inspected. Page counts and SHA-256 hashes were checked from the frozen public PDFs.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT01929018 | protocol | 14 | 5c9fa93ab8feb6197361fd1cca7a2866a12a3b2a208dc4d8c6b4d76b646931e6 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/18/NCT01929018/Prot_000.pdf) |
| NCT01929018 | SAP | 2 | 7b1a9d40034238e70041f81c3c7e73fe41f6b64d65d815bdbf4041aafb0bfa1c | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/18/NCT01929018/SAP_001.pdf) |
| NCT01855399 | protocol | 5 | 736afad7d492e95409e2c41965e63caa6238d5f859ca178e8137580594e4971f | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/99/NCT01855399/Prot_000.pdf) |
| NCT01855399 | DAP | 5 | 342e718ff816d2372d7bc9ff70fae1025958a00bc2d1dcc3e921ff947d3c0bad | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/99/NCT01855399/SAP_001.pdf) |
| NCT01905150 | protocol | 6 | 75d3e57faf2f0a48886c9c2c7d91bbac808a6ec1cb0242ce37b075f5641eb9bd | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/50/NCT01905150/Prot_000.pdf) |
| NCT01905150 | SAOP | 2 | 84dda1637db7c363c94b9c81f7c9d6954192ebfd6df789b8cb45772dc95e52b9 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/50/NCT01905150/SAP_001.pdf) |
| NCT02337361 | protocol | 22 | bc58ca1d13466b874d62440aa4edee9c550d0b7764fea5229320562b9d1f5bfa | [Prot_001.pdf](https://cdn.clinicaltrials.gov/large-docs/61/NCT02337361/Prot_001.pdf) |
| NCT02337361 | SAP | 2 | 5e0b3713fbebdc7b25e0e5a52a9c49b75c31d31cb215d33be99fdc618c459865 | [SAP_000.pdf](https://cdn.clinicaltrials.gov/large-docs/61/NCT02337361/SAP_000.pdf) |
| NCT02427464 | protocol | 138 | 3cfd774c2552ad002de381642424d28d0deb737bb10e481b8183abf581db356b | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/64/NCT02427464/Prot_000.pdf) |
| NCT02427464 | SAP | 39 | 990acf0289a725ae45902e1c6b22b139aab3c1998641d4a29b85a85c551151b7 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/64/NCT02427464/SAP_001.pdf) |
| NCT03874117 | protocol | 4 | 5c9944a25ce8ac7436ee6ff7f090d0354789b806553918fa4286f2e782caa352 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/17/NCT03874117/Prot_000.pdf) |
| NCT03874117 | DAP | 1 | f8bcdad8caa0f3c026681cd9f296b508e1f80611a37f420210a1ef8d1b2d88f1 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/17/NCT03874117/SAP_001.pdf) |
| NCT02242760 | protocol | 70 | ec3c4790961af28349e22c58c9563d3f33abd661ac17b82a6b606da883d2df9a | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/60/NCT02242760/Prot_000.pdf) |
| NCT02242760 | SAP | 187 | 20deda2e6579ff9323078aaffafbdab130ed2667d3cb7b734a9d4e20b57b1f15 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/60/NCT02242760/SAP_001.pdf) |
| NCT03658941 | protocol | 19 | 0d8b9f4d91ff91b622080e3855b25de31093a42638c318603d8fa01331ec48a9 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/41/NCT03658941/Prot_000.pdf) |
| NCT03658941 | SAP | 7 | 3ab137753fe36a811f28bf77a17b2b969be2b09fe3fc01387a4dbfc3ed125c84 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/41/NCT03658941/SAP_001.pdf) |
| NCT04173429 | protocol | 5 | bcbdb776f43e8f91c75c6c4aa7364770a7205496850215e26003b98b840fdd68 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/29/NCT04173429/Prot_000.pdf) |
| NCT04173429 | analysis upload | 2 | 831a82cade245720b3c476ceddd623bdd6f0242a32340c98df970f110f142e36 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/29/NCT04173429/SAP_001.pdf) |
| NCT07148791 | protocol | 10 | d22c01a971479501b44bbb270f41783f1aeb9854a1f12a012595950f8a8271ed | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/91/NCT07148791/Prot_000.pdf) |
| NCT07148791 | SAP | 4 | 1bf6c95b62b11b921ef8ff291bc499afbe026c4a38d77f9de0ce04da5124120e | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/91/NCT07148791/SAP_001.pdf) |
| NCT03669133 | protocol | 12 | f15ad0ffea164e7f10015be42304522c4cf05330f42ca9c34a3a50838996bc25 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/33/NCT03669133/Prot_000.pdf) |
| NCT03669133 | SAP | 2 | 82f55f201fde78b7f6279ea8d93e268890d96da1d994cf595511db4469ee4efa | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/33/NCT03669133/SAP_001.pdf) |
| NCT03101020 | protocol | 6 | 49d33e6c4888022aa7635738e0fe2d50b0fb66226ab82500f9110275409648d8 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/20/NCT03101020/Prot_000.pdf) |
| NCT03101020 | analysis upload | 2 | 10252d79d55234838aa2c81836263e772e5d9866157bd11d8b8a9188e3c9662e | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/20/NCT03101020/SAP_001.pdf) |
| NCT03374306 | protocol | 2 | 99b421f9a0fd368e9b33cf8bb09f6f38d0239fbfcdcbbb5dfc15229c101ef7ee | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/06/NCT03374306/Prot_000.pdf) |
| NCT03374306 | analysis upload | 1 | 51c00bb5ab787ea738f31f304e5d7efde9702c8943b3dc8fd414ccf712aabd7a | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/06/NCT03374306/SAP_001.pdf) |
| NCT07437209 | protocol | 10 | 804b0d9bfcbd14f0ef0b5f3aa69bd4298892b1c06297ff07760d150c08590e7a | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/09/NCT07437209/Prot_000.pdf) |
| NCT07437209 | analysis upload | 1 | b7f1db6792852bcf78d200769c12be620e205fd491ce30264575df6525e3efff | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/09/NCT07437209/SAP_001.pdf) |
| NCT02205177 | protocol | 30 | df2e32011231daf04b314d64f71f503c8a8296ac382262ed6e0849791ba766dc | [Prot_001.pdf](https://cdn.clinicaltrials.gov/large-docs/77/NCT02205177/Prot_001.pdf) |
| NCT02205177 | analysis upload | 2 | 53aa49bfb568b71159e39ad2af61f27c7c63ccccd49e9fde1726bfde2c18c40f | [SAP_002.pdf](https://cdn.clinicaltrials.gov/large-docs/77/NCT02205177/SAP_002.pdf) |
| NCT02088216 | protocol | 4 | d81792827f5c42671da269be8b78ae66950220f067667334aceaee99a6781c7c | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/16/NCT02088216/Prot_000.pdf) |
| NCT02088216 | analysis upload | 2 | bd7600a36ba305cbc732d21b9833c9c04af3e485c8cb89680a16e14981d45986 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/16/NCT02088216/SAP_001.pdf) |

The local PDFs are acquisition artifacts under the gitignored source tree. Their URLs, hashes, and page counts are recorded here or in the manifest; PDFs are not committed.
