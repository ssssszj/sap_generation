# Expert Review Packet — Batch 16

## PUBLIC-RIXFP-HEMOPHILIA-B-001

- 22 requirements; all remain `draft_needs_expert_review`.
- Confirm SAP Version 4 Final dated 2020-12-11 against CSL654_3003 Protocol Amendment 6 Final dated 2020-02-03; SAP physical page 11 explicitly names that governing amendment.
- Reproduce the exposure-qualified FIX-inhibitor incidence denominators for PTPs and PUPs and the PUP 50-IU/kg incremental-recovery endpoint.
- Adjudicate the protocol-to-SAP changes from Poisson to negative-binomial principal ABR modeling, inclusion of the first three post-surgery months, and descriptive-only PUP regimen summaries.
- Reconcile the protocol's `rank sum` wording for a matched-pair comparison with the SAP's Wilcoxon signed-rank method, then verify the three-step noninferiority sequence.
- Keep the surgery and subcutaneous substudy populations, periods and outputs distinct from the main efficacy analysis.

## PUBLIC-US-EPIDURAL-OBESITY-001

- 15 requirements; all remain `draft_needs_expert_review`.
- Confirm the independent protocol and SAP by their exact title, NCT02984267 identifier and common date of 2016-10-01, before enrollment began.
- Recompute and record the numeric sample size implied by the unavailable pilot means and variances; the public SAP gives only 80% power, a six-minute effect and two-sided alpha 0.05.
- Resolve the SAP's unexplained use of both Kruskal-Wallis and Mann-Whitney tests for the same two-group nonnormal setting.
- Define the randomized analysis set and rules for unavailable marking investigators, failed or redirected procedures, incomplete WOMBLSQ data and missing 24-hour follow-up.
- Decide whether to adjust for site, marking investigator or epidural-provider experience, and label secondary comparisons exploratory unless multiplicity is controlled.

## Version and source decisions

- NCT02053792: promoted. SAP Version 4 Final explicitly states that it is based on Protocol Amendment 6 dated 2020-02-03; both documents share CSL654_3003 and the SAP predates primary completion.
- NCT02984267: promoted. The independent protocol and SAP share the exact title, NCT and 2016-10-01 date before enrollment; the two-page SAP remains intentionally under-specified rather than duplicating protocol text.
- NCT02344576, NCT02536248, NCT04761822 and NCT01802216: `excluded_combined_protocol_sap_leakage`; their protocols expose essentially all target analysis content or the alleged SAP is a protocol-section extract.
- NCT02575950, NCT02225353, NCT02119156, NCT02029443, NCT01898299 and NCT06684951: `excluded_wrong_document_type`; the public analysis documents postdate primary completion without a defensible pre-unblinding chain, describe executed analyses, or are completed-study thesis/manuscript material.

## Source audit

All protocol and SAP title/version pages were visually inspected. For the promoted studies, all critical design, population, endpoint, derivation, sample-size, model, multiplicity, missing-data, interim, PK, safety and substudy pages were inspected. For exclusions, the pages establishing duplication, retrospective timing or wrong document type were inspected. Page counts and SHA-256 hashes were checked from the frozen local public PDFs.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT02344576 | protocol / SAP | 13 / 4 | bb04515d0191fbde10ea534c73f785579d9a13cf3646ad5fe5e726c1302f5111 / 730e7002abb34820f0ecb5f53acfd8d50775123850337f5aad40301539ece91e | [record](https://clinicaltrials.gov/study/NCT02344576) |
| NCT02575950 | protocol / SAP | 88 / 10 | 495f2e5cfa63bd01eed7ff58ea483cfb91ac803daf157c7950904807a8b1dcc1 / 6c109ad774f075cd72fb90981f77c94e707d58520b624e7f3196cceea127126f | [record](https://clinicaltrials.gov/study/NCT02575950) |
| NCT02536248 | protocol / SAP | 4 / 2 | 274be34d32fdee45e118f2442dcc6666269fe4866e363efba35631a15b1df797 / 91ba5e7f3a2e8ef3dac6843cbb54637bc689edf4b4325e7f45bc70dc0e1c4203 | [record](https://clinicaltrials.gov/study/NCT02536248) |
| NCT02225353 | protocol / SAP | 23 / 17 | a6953d8ee6800df02f14ea61cc68b4712458a0300a86505ff7dad027ad9f08f2 / c2dac9e55cea666c7ea8a481166bf2abd7dae507d4fdce5db1c7c0766d46eb17 | [record](https://clinicaltrials.gov/study/NCT02225353) |
| NCT02053792 | protocol | 188 | e43a540dde12d10940849a5fb288d7de18f4196b60664810e3c315dea671b514 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/92/NCT02053792/Prot_000.pdf) |
| NCT02053792 | SAP | 74 | 4337888c53a3a918682d097ed6df051f6a498f4fa8e85a00aedfa2dda1170cdc | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/92/NCT02053792/SAP_001.pdf) |
| NCT02119156 | protocol / SAP | 161 / 121 | 211de39b69c2e693372e5c855e85727c6095f42bdbdd37c6c6980c3ba26974e7 / ff9c4279458768b2dabfb0bbe72dc4373af20cd02f1fbc96c1c977c17a080ed8 | [record](https://clinicaltrials.gov/study/NCT02119156) |
| NCT04761822 | protocol / SAP | 83 / 26 | 36f22c4d23697ad81379415e9d338aecb37547ab4f247fe3f1f30a4f2b7a1637 / 17d849c6fa58aca839a70d3f5490bd10f5c05fa48dec4f1fa220913e76bea517 | [record](https://clinicaltrials.gov/study/NCT04761822) |
| NCT02984267 | protocol | 6 | 61118220ab7d4312a3eb760d6226ea908a40c056e78133634f4f41e5c89a18b0 | [Prot_001.pdf](https://cdn.clinicaltrials.gov/large-docs/67/NCT02984267/Prot_001.pdf) |
| NCT02984267 | SAP | 2 | dc79cdfb9d72da14b87aaa92d61ab8ddcdd66b8c9a141017fa24040acaacbb77 | [SAP_000.pdf](https://cdn.clinicaltrials.gov/large-docs/67/NCT02984267/SAP_000.pdf) |
| NCT02029443 | protocol / SAP | 102 / 33 | 6586a77c2f05fcdc01a02b4d26820b618ca86d6c53771554b1feb202fe2e9df2 / a35b3d14be7380642f491cf54db056dea2f49642f0c9fe5bc78049442073848d | [record](https://clinicaltrials.gov/study/NCT02029443) |
| NCT01898299 | protocol / SAP | 32 / 1 | ae2c68aead1f9b1b418bb88b41a8cc20967bf5f88f776cfe1bdb6791899d161e / 7c959de1ba3a764d74ac3e7cc2ebecc27d34197d366b637c1b2d948d89c8c3f5 | [record](https://clinicaltrials.gov/study/NCT01898299) |
| NCT01802216 | protocol / SAP | 28 / 2 | 103176b8e21c471ea8ba9fdc4433188a8288d5d8130e21764e450fd6f9e48a8c / 9a08b1f787bb10766dd82e0303c71800cb319f858ffe095c360e49ea1624a595 | [record](https://clinicaltrials.gov/study/NCT01802216) |
| NCT06684951 | protocol / SAP | 28 / 2 | 47eb10220aae0fdaf8cb595ce449f9e7eedaaeb2d182869f2ca7e7a0c719af6c / 125123e64974105183574cf455b6bafc205322a978ab71c15349761f96a6ac87 | [record](https://clinicaltrials.gov/study/NCT06684951) |

The local PDFs are acquisition artifacts under the gitignored source tree. They are not committed, and reference SAPs remain annotation-only.
