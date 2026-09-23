# Expert Review Packet — Batch 14

## PUBLIC-PREPOPIK-PED-001

- 15 requirements; all remain `draft_needs_expert_review`.
- Confirm Trial 000103 Protocol Version 5 dated 2014-07-28 against SAP Final Version 2.0 dated 2017-02-16; SAP page 6 lists Protocol Versions 3, 4 and 5.
- Audit the Aronchick responder, age-by-regimen allocation, exact confidence intervals, ITT nonresponse handling and supportive PP analysis.
- Keep nominal comparisons descriptive because no multiplicity-controlled confirmatory hierarchy is defined.

## PUBLIC-DS107G-AD-001

- 16 requirements; all remain `draft_needs_expert_review`.
- Confirm DS107G-02 Protocol Version 2.2 dated 2015-07-22 against SAP Final Version 1.0 dated 2015-10-19; SAP page 7 cites the governing protocol explicitly.
- Audit the Week-8 composite IGA responder, pooled-site CMH model, ITT/PP hierarchy, nonresponder rule and supportive LOCF analysis.
- Treat unadjusted secondary and subgroup analyses as supportive or exploratory.

## PUBLIC-AFLIBERCEPT-DME-QOL-001

- 16 requirements; all remain `draft_needs_expert_review`.
- Confirm BAY86-5321/17850 Integrated Protocol Version 2.0 dated 2015-09-07 against SAP Supplement Version 7 dated 2017-05-04; SAP page 7 lists Protocol Versions 1.0 and 2.0.
- Audit FAS inclusion, Week-52 NEI VFQ-25 scoring, LOCF primary analysis and OC, MCID, MI and repeated-measures sensitivity analyses.
- Keep conclusions descriptive because this is a single-arm study with no formal hypothesis test.

## PUBLIC-ENLIGHTEN2-001

- 19 requirements; all remain `draft_needs_expert_review`.
- Confirm ALK3831-A303 Protocol Amendment 5.0 and SAP Final Version 3.0, both dated 2018-09-18; SAP page 29 cites the governing amendment.
- Reproduce both co-primary analyses, MAR multiple imputation, ANCOVA/logistic models, stage separation and fixed-weight CHW statistics.
- Audit the conjunctive success rule, gated 7% key secondary, conditional-power zones, sample-size expansion and no-early-stop rule.

## Version and source decisions

- NCT01928862: promoted. SAP Final Version 2.0 explicitly lists Protocol Versions 3, 4 and the available governing Version 5 dated 2014-07-28.
- NCT02211417: promoted. SAP Final Version 1.0 explicitly states that analyses follow DS107G-02 Protocol Version 2.2 dated 2015-07-22.
- NCT02581995: promoted. SAP Supplement Version 7 explicitly lists Protocol Versions 1.0 and 2.0; registry document metadata dates the SAP to 2017-05-04.
- NCT02694328: promoted. The SAP and Protocol Amendment 5.0 share study identifier ALK3831-A303 and date 2018-09-18, and the SAP reference list explicitly cites the amendment.
- NCT02068885, NCT03393494, NCT02475070 and NCT01596127: `excluded_combined_protocol_sap_leakage`; their protocols expose the core target analysis or the alleged SAP is merely an extract of the same material.
- NCT00745420 and NCT02351544: `excluded_wrong_document_type`; the uploaded analysis files are retrospective post-study methods/report plans.
- NCT05634863: `excluded_wrong_document_type`; the alleged SAP is a Data Management Plan.
- NCT02267226: `hold_version_reconciliation`; the available Protocol Version 6.0 dated 2014-10-31 does not match the SAP's stated governing protocol date of 2016-07-08.

## Source audit

All title/version pages and every page supporting admission, leakage, wrong-type or hold decisions were visually inspected. Key design, endpoint, population, sample-size, model, multiplicity, missing-data, interim and safety pages were inspected when applicable. Page counts and SHA-256 hashes were checked from the frozen local public PDFs; NCT02475070 required OCR because both documents were image-only.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT02068885 | protocol / SAP | 20 / 18 | aa59452faafcb4dd2a8f336aad5a2697ced11ae32141c8fd235d44ecfb41913d / d50283860f23f48008e85e4067a1bb6ae019eeb4e35212f08256aa26dd09bdaa | [record](https://clinicaltrials.gov/study/NCT02068885) |
| NCT03393494 | protocol / SAP | 54 / 16 | 58bcc8ba2756f5c9587cc43b3aaaa66ee0bde1c80f129d553cc1cce98fc83d54 / 7c12dd22f1730abeed03568be51bd5f28253c5d2aa6444437e3846d95ddf4fe3 | [record](https://clinicaltrials.gov/study/NCT03393494) |
| NCT02475070 | protocol / SAP | 16 / 1 | 74c5c509214ee0a968669139f3cf62d9b073378bba63fb936e59c0ddeae569db / 8a4ecea99c09c9448ea32be159a4f095425c4e645028f4dc8a3127844024fb7c | [record](https://clinicaltrials.gov/study/NCT02475070) |
| NCT01928862 | protocol | 65 | 430731ef4900f54c501702f009b036e8840f3cf7486c0c7626cb8a413cbc4eb7 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/62/NCT01928862/Prot_000.pdf) |
| NCT01928862 | SAP | 31 | 1ceec789b9e04ab089a6733550ae331ff6cf205240374fb76ac9eb1480b91a5f | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/62/NCT01928862/SAP_001.pdf) |
| NCT00745420 | protocol / SAP | 103 / 20 | e22eb5c3bcd60b29544eca16965de6043ec23db94e50c22511b6b1abcd86588e / 53a0b9c7888fd3ce69337598b570f196142b95ec2c04d0db860d58593b180484 | [record](https://clinicaltrials.gov/study/NCT00745420) |
| NCT02211417 | protocol | 49 | 693e3785ebf2e479d20694ab01020bc66ef22d65cd807fc60cdd0df3e98eed11 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/17/NCT02211417/Prot_000.pdf) |
| NCT02211417 | SAP | 107 | dff7148a814073e69777793aab191ab36791bdce432bd8ba1e48eae9c955c841 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/17/NCT02211417/SAP_001.pdf) |
| NCT02351544 | protocol / SAP | 10 / 2 | 0286ac30def1c51787ed146b7517d334fa3e65eb3590fa783fb8dec34e22d47f / 80794fca5b08d4987f8290e3904ffe8c5ac28e4325e5cc1eebcd09cb7ef2bb49 | [record](https://clinicaltrials.gov/study/NCT02351544) |
| NCT01596127 | protocol / SAP | 14 / 2 | 2e8bb09a01a98eb8333f168d3092bc982b24e37613d97718bd1cafed8018735f / 1e9deca27d7de5bf6e6db80d6cb9ecf3a6cd3070ed935002b4b71887d926a9fa | [record](https://clinicaltrials.gov/study/NCT01596127) |
| NCT02581995 | protocol | 95 | 7fd759faad0da60c9e63831a198c932738736069579eb7f0ae22b8b014a216e6 | [Prot_001.pdf](https://cdn.clinicaltrials.gov/large-docs/95/NCT02581995/Prot_001.pdf) |
| NCT02581995 | SAP | 30 | 7aacf89d9ec159446cb03048080c7a1c2cb49432f62a1557583503930018982b | [SAP_000.pdf](https://cdn.clinicaltrials.gov/large-docs/95/NCT02581995/SAP_000.pdf) |
| NCT02267226 | protocol / SAP | 88 / 31 | 539f99484e50089c51517f69873a805562b3e6ef26252dd5d4b897cfb11eaf4b / c37391478bf0bede665e790ef08609636a4946d834af81226c9669b5c56622c6 | [record](https://clinicaltrials.gov/study/NCT02267226) |
| NCT02694328 | protocol | 112 | 78738f5f7ef26a6e7ee5bb4cc06b35bef05eb9d44f7d5022efeb43a56c1175eb | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/28/NCT02694328/Prot_000.pdf) |
| NCT02694328 | SAP | 29 | 010b96b7ffa1d9b25a5dd526da173c1f93eb280dc39c4c463b24be4883d827cb | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/28/NCT02694328/SAP_001.pdf) |
| NCT05634863 | protocol / SAP | 36 / 3 | 864969340e4b278262ac4e88613b50c6b681479db0c5416d5c76c6670e41cd68 / e36b2fad04ec1908a8dc659882a21b6d0ab066346c496e175464b78f1137fd3e | [record](https://clinicaltrials.gov/study/NCT05634863) |

The local PDFs are acquisition artifacts under the gitignored source tree. They are not committed, and reference SAPs remain annotation-only.
