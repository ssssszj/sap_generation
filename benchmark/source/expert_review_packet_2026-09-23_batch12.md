# Expert Review Packet — Batch 12

## PUBLIC-BERTILIMUMAB-UC-001

- 19 requirements; all remain draft_needs_expert_review.
- Confirm Immune/BRT/UC-01 Protocol Final Version 8.0 dated 2018-05-23 and final SAP Version 1.0 dated 2019-01-15.
- Adjudicate the later mITT post-baseline requirement, safety exposure to prophylaxis, and replacement of the protocol multiple-imputation branch with a nearest-value window.
- Define the primary response contrast, estimator, test, treatment attribution, out-of-window missing rule, and executable sensitivity analyses.

## PUBLIC-CATPAD-FOLLOWUP-001

- 18 requirements; all remain draft_needs_expert_review.
- Confirm CP007A SAP Version 2.0 dated 2017-02-23 against Protocol Version 5 dated 2014-12-08.
- Verify annual FAS and indoor-cat mITT reclassification, inherited CP007 randomized treatment attribution, and the primary combined symptom/medication score.
- Adjudicate within-year Holm testing, across-year hierarchy, LOCF/WOCF/BOCF, MAR MMRM, and safety treatment attribution.

## PUBLIC-IVERMECTIN-COVID-001

- 15 requirements; all remain draft_needs_expert_review.
- Confirm exact title, NCT identifier, trial code and date 2020-08-05 across the independent protocol and four-page SAP.
- Reconcile the protocol failure rule with the SAP complete-case wording and correct the safety population wording that appears to omit placebo recipients.
- Correct the malformed null hypothesis and define the estimand, effect measure, confidence interval and small-cell test; assess multiplicity and sample-size adequacy.

## PUBLIC-ULTIMATE-II-MS-001

- 19 requirements; all remain draft_needs_expert_review.
- Confirm TG1101-RMS302 Protocol Version 5.0 and ULTIMATE II SAP Version 3.0, both dated 2020-09-04.
- Verify the primary negative-binomial/GEE relapse model, exposure offset, post-discontinuation sensitivity and ten-imputation procedure.
- Audit the fixed sequence across ULTIMATE I and II, pooled 12-week CDP gate, blinded sample-size reassessment, and detailed CDP censoring conventions.

## PUBLIC-LAMPALIZUMAB-GA-001

- 22 requirements; all remain draft_needs_expert_review.
- Confirm GX29185 Protocol Version 6 dated 2015-09-24 and SAP Version 3 dated 2017-08-17; the SAP explicitly states that it supersedes the protocol analysis plan.
- Adjudicate the change from the protocol biomarker-first hierarchy to SAP testing of Q4W overall, Q4W biomarker-positive, Q6W overall, and Q6W biomarker-positive at alpha 0.0496.
- Verify the Week-48 MMRM, data cutoffs, 100-imputation MAR/MNAR sensitivity families, and the GX29176/GX29185 pooled microperimetry gate.

## Version and source decisions

- NCT01671956: promoted. The protocol and SAP share Immune/BRT/UC-01; Protocol Version 8 predates final SAP Version 1.0, with material later decisions separated by track.
- NCT02040844: promoted. SAP Version 2.0 explicitly states that it is based on CP007A Protocol Version 5 dated 2014-12-08.
- NCT04407507: promoted. The protocol and SAP share exact title, NCT identifier, study code and date; internal analysis ambiguities are explicit review requirements rather than version uncertainty.
- NCT03277248: promoted. SAP Version 3.0 explicitly cites TG1101-RMS302 Protocol Version 5.0 and both are dated 2020-09-04.
- NCT02247531: promoted. SAP Version 3 explicitly names Protocol Version 6 and documents that its later primary hierarchy supersedes the protocol plan.
- NCT03181971 and NCT01317875: excluded_wrong_document_type; their analysis uploads are retrospective/CSR analysis materials rather than prospective governing SAPs.
- NCT00589316: excluded_combined_protocol_sap_leakage; the protocol contains the target dose-escalation analysis repeated by the short SAP.
- NCT01983462, NCT02672332, NCT03316118, and NCT00993551: hold_version_reconciliation; unresolved dose or internal version conflicts prevent a defensible governing pair.

## Source audit

All listed title/version pages and pages supporting admission, hold, leakage, or wrong-document decisions were visually inspected. Page counts and SHA-256 hashes were checked from the frozen local public PDFs.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT01671956 | protocol | 58 | a77f2ef5614b4bbb388941168bc4e74732b03b8db2b5e5807af03db49d0716d5 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/56/NCT01671956/Prot_000.pdf) |
| NCT01671956 | SAP | 19 | ab66e2d0b1541ef680314679ee05c347798a8905e6b7467ef13e4acfbdbf7284 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/56/NCT01671956/SAP_001.pdf) |
| NCT02040844 | protocol | 50 | d887c7cc480c76a2c8028755231094a61248a1267dc11adcf75de10d435ea5e3 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/44/NCT02040844/Prot_000.pdf) |
| NCT02040844 | SAP | 55 | 07d55112457772939b17ad596d1f8f48cede94669678db48f9c57cc9782c9d91 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/44/NCT02040844/SAP_001.pdf) |
| NCT04407507 | protocol | 43 | 692744c2bf0b8c3e7c6a006d3c19adf791b37600ccb30955920390753e5fdffb | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/07/NCT04407507/Prot_000.pdf) |
| NCT04407507 | SAP | 4 | f35d1ead0149d7b3f444f1f631221f2824b0e93092ae71347a931acdec783d1a | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/07/NCT04407507/SAP_001.pdf) |
| NCT03277248 | protocol | 144 | fd5c181f1dbf43b17700d75dec90aac1e5f6dc236f7d8dff9fa7888decb49b0f | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/48/NCT03277248/Prot_000.pdf) |
| NCT03277248 | SAP | 52 | fb93d98b697fad746a59ece3cde96d8b300000a99d29880ad15b36088eded142 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/48/NCT03277248/SAP_001.pdf) |
| NCT02247531 | protocol | 170 | e64821f77ba340056600dbd76a1af81024297dd632baa281d643c956c66cf253 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/31/NCT02247531/Prot_000.pdf) |
| NCT02247531 | SAP | 33 | 572e146a91906fdc0a569d7e6166ab7c1db81c92182e8bd96a7e6cdbbf503a8c | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/31/NCT02247531/SAP_001.pdf) |
| NCT03181971 | protocol / analysis upload | 13 / 3 | 203b2217432f90b783b11516b2cd5128cfc9e79a0657bae9f361c11af596d63a / fad1cb301fa3302313244dccb195f7d6f2eeccc595643b9bbe0bc77df02c3a54 | [record](https://clinicaltrials.gov/study/NCT03181971) |
| NCT01317875 | protocol / analysis upload | 143 / 24 | f466ddb92bfbcc0b987fcf4500c4c277f0d9ae86058cb0ce163d79aac587b59a / a04657167d653707bd057cbd2263109a85680c20b27d176a1c663ab38806fa8f | [record](https://clinicaltrials.gov/study/NCT01317875) |
| NCT00589316 | protocol / SAP | 51 / 5 | 2dcd2635d8820be83805f71cfe16b00a02a2cae8ff84c1f9fb7a6a6a77cf9571 / e9304dcedb3adf056bd184a00db8757aa0595a93388e8ca58dc075ddc682f8c7 | [record](https://clinicaltrials.gov/study/NCT00589316) |
| NCT01983462 | protocol / SAP | 38 / 2 | ce53d32128ca749a5a6bb6a48dbde589f91b6cc7a26932546a338c9296bb082e / c433d01eee81dbb123a78a790409857937878b508ef989e8b432d36f00ea039b | [record](https://clinicaltrials.gov/study/NCT01983462) |
| NCT02672332 | protocol / SAP | 57 / 90 | de3484c73236bf763114c4b403cd62e0e276472fe74709e303451447f4dce9be / 0efad3428cf2404b2053c7e8db377281869b2af84691fbd8e7aba031f1cc1b26 | [record](https://clinicaltrials.gov/study/NCT02672332) |
| NCT03316118 | protocol / SAP | 13 / 2 | 303fe0aba13afd978860750995162496c77cb5f2602a0e0f3b35b2cd2c322fac / f3b6384619b9cd5318cb92abd58dfed2836cd5486c64deb6abbbb795d437b1cd | [record](https://clinicaltrials.gov/study/NCT03316118) |
| NCT00993551 | protocol / SAP | 94 / 142 | 98cf5e3985d682ddf7103b79b6701b983faa8bf437946d6841caf24b16b7e107 / 608e46c6cb670f62fb9b4fd844dfe957d46968501d7061e9e54c997a013fa78f | [record](https://clinicaltrials.gov/study/NCT00993551) |

The local PDFs are acquisition artifacts under the gitignored source tree. They are not committed and reference SAPs remain annotation-only.
