# Expert Review Packet — Batch 08

## PUBLIC-ENGENSIS-DFU-001

- 21 requirements; all remain draft_needs_expert_review.
- Confirm that same-day SAP Version E and Protocol VMNHU-003 Version I dated 2020-02-04 form the correct governing pair, despite participants having enrolled under earlier protocol versions C, E, F, and G.
- Adjudicate the primary closure derivation, the separation of closure from later confirmation, ITT nonresponder handling, and the Fisher exact/binomial-interval analysis.
- Review whether any confirmatory interpretation remains appropriate after enrollment stopped at 44 rather than the planned 300 participants.
- Verify mITT, PP1, PP2, actual-treatment safety attribution, repeated-measures covariance fallback, CWIQ item imputation, and conservative TEAE classification.
- Keep the observed enrollment and nonexecution of the planned interim in confirmed_decisions; they are not hidden protocol-only facts.

## PUBLIC-PEG-RENAL-SAFETY-001

- 16 requirements; all remain draft_needs_expert_review.
- Retain this as an auxiliary prospective observational safety case, not as a randomized comparative trial.
- Verify the stated 1,152-participant sample size, 90% power, and 0.2% AKI incidence calculation; the two-page statistical document does not expose alpha or other assumptions.
- Define the analysis population, endpoint denominators, incidence estimators and confidence intervals, and the operational AKI-reversibility rule.
- Clarify or replace the generic ANOVA/t-test language so Visit 1/2/3 within-participant correlation is handled correctly.
- Prespecify missing-data, multiplicity, and success rules; these remain needs_confirmation, not invented protocol-only facts.

## Version and source decisions

- NCT02563522: promoted. The rendered title pages show SAP Version E explicitly citing Protocol VMNHU-003 Version I; both are dated 2020-02-04 and carry NCT02563522. The protocol and SAP are independent documents. The protocol does not contain the SAP's exact primary test, confidence-interval implementation, missing-value details, or repeated-measures covariance selection.
- NCT02657564: promoted as an auxiliary observational safety case. The five-page protocol and two-page statistical-analysis document have the exact same title, NCT identifier, and 2015-11-18 date. The protocol does not reproduce the separate document's sample-size calculation or generic test choices.
- NCT02866669: excluded_wrong_document_type; the purported analysis plan reports completed analyses, observed odds ratios, confidence intervals, p-values, and complete-case counts.
- NCT05464914: excluded_wrong_document_type; the pair consists of generic immediate-denture guidance and a generic retrospective t-test paragraph rather than a governing prospective protocol and SAP.
- NCT03634488: excluded_wrong_document_type; the uploaded analysis note describes already collected data and already used models and invokes a later 2023 publication.
- NCT05540665: hold_version_reconciliation; the SAP names HZNP-DAX-203 but does not identify its governing protocol version/date, so linkage to public Protocol Version 2.0 dated 2022-05-17 cannot be assumed.
- NCT03435783: excluded_combined_protocol_sap_leakage; the protocol contains the same ITT, Poisson, incidence-rate-ratio, confidence-interval, and GEE plan as the separate two-page upload.
- NCT02015455: excluded_combined_protocol_sap_leakage; the protocol already contains the core analysis plan, while the separate document also adds post-hoc manuscript-stage amendments.

## Source audit

For every candidate below, title/version pages and the pages supporting admission, hold, retrospective-document, or leakage decisions were visually inspected. Page counts and SHA-256 hashes were checked from the frozen public PDFs.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT02563522 | protocol | 123 | 20b3d9600d064fee720d6c4e97a0555258d7855fe28777009ba91b40cea07d01 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/22/NCT02563522/Prot_000.pdf) |
| NCT02563522 | SAP | 32 | 816b62601bcbd14ecc9d236de5193bd851bd14bad6ddf8afb9ae673223b359f2 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/22/NCT02563522/SAP_001.pdf) |
| NCT02657564 | protocol | 5 | c5e4605ecffe2b4a86b85388e74aea6ac15f0374edfcb519fa9eeb0d5833657a | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/64/NCT02657564/Prot_000.pdf) |
| NCT02657564 | statistical analysis | 2 | 53783329fe0c1bf02c6bfaa18ba7698893a3e959fc3bb77cb0bb9077016cb2e7 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/64/NCT02657564/SAP_001.pdf) |
| NCT02866669 | protocol | 82 | fc6eb996bf5975f745dc9da1a7cf0551158d346245eadd6f8b468ba5dd5c84f2 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/69/NCT02866669/Prot_000.pdf) |
| NCT02866669 | uploaded SAP slot | 5 | 97fc6b4040bcc1bdb9cc449e7b2c4e59a25c4adc9abdec38c608191dd18ddb11 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/69/NCT02866669/SAP_001.pdf) |
| NCT05464914 | protocol slot | 2 | 5324634c785b258cb020a106de3791dfaa9f4d98c6c8424d48cd2434049fb3b6 | [Prot_002.pdf](https://cdn.clinicaltrials.gov/large-docs/14/NCT05464914/Prot_002.pdf) |
| NCT05464914 | uploaded SAP slot | 2 | cce8f1f2e24ac1e31989684146eae971a01187d537529a0f66e83cbd7c4a0954 | [SAP_003.pdf](https://cdn.clinicaltrials.gov/large-docs/14/NCT05464914/SAP_003.pdf) |
| NCT03634488 | protocol | 32 | 8eb7f635f0167ad020f68cd2e876c03b4bce148f7000b68989f1ab0dd2c23406 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/88/NCT03634488/Prot_000.pdf) |
| NCT03634488 | uploaded SAP slot | 2 | 6edeb803091640bc3447b607cddcc8a0809e7db4e98a47f760569d3414f4be7d | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/88/NCT03634488/SAP_001.pdf) |
| NCT05540665 | protocol | 120 | a8ad9c87e173cfc6fe07406c63769ebe1889fe0c25de20989b00e9c94d0cbe7c | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/65/NCT05540665/Prot_000.pdf) |
| NCT05540665 | SAP | 48 | 4c93b33e1d4f677b360b03caf5cb78f1af2542fc8255cdaf93ee182d7dd11707 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/65/NCT05540665/SAP_001.pdf) |
| NCT03435783 | protocol | 19 | 90721163ee3b35da12147f96dd936a4d61abb45a72a4bdad66faac70c0e09dae | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/83/NCT03435783/Prot_000.pdf) |
| NCT03435783 | SAP | 2 | 31a0f1260cb39ecc2e4d377268a6604386d9382273322ecc258eb1d5fc5853cb | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/83/NCT03435783/SAP_001.pdf) |
| NCT02015455 | protocol | 52 | 7b6f1652a2fbab7fbe25ead5ac53b2c2e9c8005e47609aea85bbd1a362f4d707 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/55/NCT02015455/Prot_000.pdf) |
| NCT02015455 | SAP | 10 | b34bee3e6d127f56a6df6e11a85d4d9e7ef46f06de232e59e05c42c88413ec74 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/55/NCT02015455/SAP_001.pdf) |

The local PDFs are acquisition artifacts under the gitignored source tree. Their URLs, hashes, and page counts are recorded here or in the manifest; PDFs are not committed.
