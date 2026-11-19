# Expert Review Packet — Batch 15

## PUBLIC-EMRICASAN-LIVER-FIBROSIS-001

- 17 requirements; all remain `draft_needs_expert_review`.
- Confirm IDN-6556-07 Protocol Version 3.1 dated 2015-08-03 against SAP Version 2.0 Final dated 2018-01-18.
- Adjudicate the SAP's explicit change from the protocol's ordinal Ishak-change primary analysis to a stage-dependent binary Month-24 response rate.
- Reproduce the primary multiple imputation and observed-biopsy, visit-window, missing-as-nonresponse and PPS sensitivity analyses.
- Confirm the primary estimand and handling of death or retransplantation, and interpret the three treatment-effect categories as Phase-II screening guidance rather than formal success boundaries.

## PUBLIC-GLIOMA-SEDATION-001

- 14 requirements; all remain `draft_needs_expert_review`.
- Confirm the independent protocol and SAP using their exact title and common date of 2016-04-01; protocol page 2 identifies NCT02439164.
- Select an executable primary contrast for peg-test time across glioma/control groups, hands, midazolam sedation and flumazenil reversal.
- Resolve the repeated-measures covariance or sphericity approach, analysis population, informative missingness, multiplicity and sample-size inconsistencies.
- Preserve the protocol's limited timing blind and do not describe the nonrandomized group comparison as randomized or allocation-blinded.

## PUBLIC-NB-SCHIZOPHRENIA-001

- 17 requirements; all remain `draft_needs_expert_review`.
- Confirm the exact-title, exact-NCT and exact-date protocol/SAP pair dated 2015-12-30, before enrollment began.
- Audit 1:1 permuted-block randomization stratified by imaging participation, the Week-24 weight estimand, and the 60-subject power calculation based on 4.5 kg difference and 6 kg standard deviation.
- Complete the repeated-measures implementation: operational ITT, residual covariance, estimation and degrees of freedom, convergence fallback, and prespecified confounders.
- Resolve post-discontinuation data, missingness sensitivity, multiplicity across secondary endpoints and the safety population and outputs.

## PUBLIC-ROXADUSTAT-NDD-CKD-001

- 24 requirements; all remain `draft_needs_expert_review`.
- Confirm that Final SAP Version 1.0, released 2018-09-13, governs FGCL-4592-060 Protocol Amendment 3 dated 2017-09-20 and was finalized before unblinding. The SAP running header reads 11/23/2020 and requires provenance confirmation.
- Reconcile two content differences: the protocol uses a 1 g/dL US power effect and at least 12 treatment weeks for PPS, while the SAP uses 0.75 g/dL and at least eight weeks.
- Reproduce the US Weeks-28-to-52 Hb MI ANCOVA, 200-dataset imputation algorithm, MMRM and MNAR sensitivity suite, and rescue-censoring analyses.
- Reproduce the ex-US 24-week Hb responder definition, rescue/discontinuation nonresponse rule, adjusted CMH analysis and logistic-regression sensitivity.
- Audit amendment-era treatment pooling, FAS/ITT regional roles, fixed-sequence multiplicity and the boundary between study-specific safety output and pooled MACE inference.

## Version and source decisions

- NCT02138253: promoted. Separate protocol and SAP share IDN-6556-07; SAP Version 2.0 Final predates primary completion and explicitly records the primary-analysis change.
- NCT02439164: promoted. Separate documents have the exact title and 2016-04-01 date, and the protocol identifies the NCT.
- NCT02736474: promoted. Separate documents have the exact title, NCT and 2015-12-30 date, before the May-2016 study start.
- NCT01750190: promoted. SAP Final Version 1.0 explicitly names Protocol Amendment 3 and its registry release date precedes primary completion by eleven days; the later running header remains an expert provenance question.
- NCT02154750, NCT06831760, NCT02481596, NCT02349061 and NCT02978833: `excluded_wrong_document_type`; the files are retrospective or executed methods notes, do not govern the primary analysis, or cannot be established as prospective plans.
- NCT01787552, NCT04333225 and NCT01924169: `excluded_combined_protocol_sap_leakage`; the protocol contains the target statistical analysis or the alleged SAP repeats it.

## Source audit

All title/version pages and every page supporting admission, leakage or wrong-document-type decisions were visually inspected. Key design, endpoint, population, sample-size, model, multiplicity, missing-data, interim and safety pages were inspected when applicable. Page counts and SHA-256 hashes were checked from the frozen local public PDFs.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT02154750 | protocol / SAP | 6 / 1 | ac714dc4d2f861ae486646d000be883477083c4d634c3bf9e2ea4301e53a9d0d / a8dd292cd231861d443181ce14eea08c2ab57f827e0035624074bbc08f24cf44 | [record](https://clinicaltrials.gov/study/NCT02154750) |
| NCT06831760 | protocol / SAP | 7 / 3 | 2cdfee64cd6bc1b35befcfd1ac8bf89d2439f4970d161467d0015885a6653b45 / e4b66bacc1c9ca13002d55772267cbd81c9d5a33749e6ce3ada8fa1f3959257f | [record](https://clinicaltrials.gov/study/NCT06831760) |
| NCT02481596 | protocol / SAP | 29 / 2 | 914fed4dea803f9dda86f7ac07c1e06912f8fc45ae09aa2893492073730ce1e0 / d57a84b1d0193270f7c20470a2ce5f5c21193e26219817652c5391373a8f3b57 | [record](https://clinicaltrials.gov/study/NCT02481596) |
| NCT02138253 | protocol | 77 | 25d15462f1240858db215016701be247ca9f75e2269a3000f30eda84b9476b61 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/53/NCT02138253/Prot_000.pdf) |
| NCT02138253 | SAP | 32 | b745d0fce8647baba06b6bf07579184be79f5f80f949f5653a65ab08ca1e1626 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/53/NCT02138253/SAP_001.pdf) |
| NCT01787552 | protocol / SAP | 146 / 46 | 0228950e42cb948fa47a039b27f27f053c4eaa31bfb3a8ece73d73245986b05f / 60c967cfe6f7851139b46c6c35b5606dacee7cc4012315374ab60c87c105aabc | [record](https://clinicaltrials.gov/study/NCT01787552) |
| NCT02349061 | protocol / SAP | 148 / 29 | 188a52a558aaaf8176136162314f6e9d6a9c9bc154222ee62370dddb22423698 / 888a9d8db65e3eac44a1283fdcf53daf96f77ad1a651ef5e42b7d4a2eef56be1 | [record](https://clinicaltrials.gov/study/NCT02349061) |
| NCT04333225 | protocol / SAP | 62 / 7 | 1311ff4fedc50a158901d72e80dd7e64f82afc2370c3b06a515926ac20b856d8 / 6a6688b597fcd94f2388f8d3740ba05c9ca1a9de03348d499780d2d002282298 | [record](https://clinicaltrials.gov/study/NCT04333225) |
| NCT02978833 | protocol / SAP | 9 / 2 | bf38dd947a8ea0e82691ccd14ac891e26e321a24aed3d6cacfb123c117563b63 / 1d8f1c0f6887091a6b542e8cb2423b8300fcfcb1c57934287f546afa33b328fb | [record](https://clinicaltrials.gov/study/NCT02978833) |
| NCT02439164 | protocol | 5 | 862b3510d7155ef5cb49d063084659cfdcdd3eb6be161cfe4d2f87964504fae7 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/64/NCT02439164/Prot_000.pdf) |
| NCT02439164 | SAP | 1 | e72d7b7bfe960a36950c04b15b7710e26c8a284cbccf356d5af24baeb3095005 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/64/NCT02439164/SAP_001.pdf) |
| NCT01924169 | protocol / SAP | 27 / 3 | f9844e566e2688f898f8429975aa267a03e0bbfb9d01d6e953b0b80e47900705 / c25b506c62e52a70ce213a88bf0fd1f4501deb392f4be8c5458505d0fdc02758 | [record](https://clinicaltrials.gov/study/NCT01924169) |
| NCT02736474 | protocol | 5 | 622e857e5a125ca334742d40c9a3a0257a1eb92627891a1508d2d3f1dfa00f51 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/74/NCT02736474/Prot_000.pdf) |
| NCT02736474 | SAP | 3 | 43c9fb731b3e3e1cf669737b84aec330169558aca3c6e0f3d5bf27f32a275d28 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/74/NCT02736474/SAP_001.pdf) |
| NCT01750190 | protocol | 94 | e2dc3d77283b62c235c4b6943f4eaee1535246438a3c259de6b85a60fac85d14 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/90/NCT01750190/Prot_000.pdf) |
| NCT01750190 | SAP | 71 | 35730ca5a89c7e704b63b32a4fdd21a7042b77165ca2bd2387f35702898e597e | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/90/NCT01750190/SAP_001.pdf) |

The local PDFs are acquisition artifacts under the gitignored source tree. They are not committed, and reference SAPs remain annotation-only.
