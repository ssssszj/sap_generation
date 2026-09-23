# Expert Review Packet — Batch 11

## PUBLIC-SELECT-CV-001

- 16 requirements; all remain `draft_needs_expert_review`.
- Confirm EX9536-4388 Protocol Version 7 dated 2022-02-09 and SAP Version 3.0 dated 2022-04-22 inside the public 2023 CSR wrappers.
- Verify the 1,225-event design, ITT treatment-policy estimand, Cox model, one superiority interim, Lan-DeMets/O'Brien-Fleming alpha spending, and hierarchical confirmatory endpoints.
- Adjudicate censoring, competing-risk, on-treatment, and subgroup operational choices.

## PUBLIC-SARECYCLINE-ACNE-001

- 15 requirements; all remain `draft_needs_expert_review`.
- Confirm SC1401 Protocol Amendment 3 dated 2015-12-16 and SAP Amendment 1 revised 2017-03-03.
- Verify the Week-12 lesion-count and IGA co-primary endpoints, ANCOVA and center-stratified CMH analyses, and conjunctive success rule.
- Adjudicate LOCF/failure rules, center pooling, PP exclusions, and sensitivity analyses.

## PUBLIC-NI071-RA-001

- 17 requirements; all remain `draft_needs_expert_review`.
- Confirm NI071F2 Protocol Version 4.0 dated 2017-08-09 and SAP Version 5.0 dated 2019-06-27 inside the CSR wrappers.
- Verify the -12%/+15% Stage-1 efficacy margins, nonresponse conventions, and gate from biosimilarity to Stage-2 PK interchangeability.
- Adjudicate Stage-2 PK parameters and limits, PP definitions, tipping-point implementation, and conservative safety imputations.

## PUBLIC-MS-TELEREHAB-001

- 13 requirements; all remain `draft_needs_expert_review`.
- Confirm the exact title, NCT identifier, and approval date 2015-07-27 across the independent three-page protocol and SAP.
- Verify EDSS-stratified permuted-block randomization, the two six-month mobility outcomes, change-score ANOVA, and longitudinal mixed model.
- Specify co-primary multiplicity and success, covariance and degrees of freedom, MAR/MNAR sensitivity, and operational safety conventions.

## PUBLIC-CORIN-ICOTINIB-001

- 14 requirements; all remain `draft_needs_expert_review`.
- Confirm GASTO 1003 Protocol Version 1.1 and SAP Version 1.1, both dated May 2020.
- Verify the three-year DFS proportion, two-sided alpha 0.10, 128-participant calculation, and supportive Kaplan-Meier/log-rank/Cox analyses.
- Adjudicate the proportion-difference variance and confidence interval, censoring and competing events, and stratified survival sensitivity analyses.

## PUBLIC-NIVOLUMAB-SEPSIS-001

- 16 requirements; all remain `draft_needs_expert_review`.
- Confirm CA209923 Revised Protocol 01 dated 2017-03-03 and SAP Version 2.0 dated 2017-05-17.
- Verify domain-specific analysis sets and as-randomized versus as-treated attribution, descriptive safety, and noncompartmental PK summaries using actual sample times.
- Preserve the non-powered, descriptive Phase 1b framing; do not invent confirmatory efficacy, multiplicity, estimand, or interim boundaries.

## Version and source decisions

- NCT03574597: promoted. The public wrappers contain a complete Protocol Version 7 and later SAP Version 3.0 for the same trial identifier.
- NCT02320149: promoted. Protocol Amendment 3 and SAP Amendment 1 identify the same SC1401 trial and form a prospective governing pair.
- NCT02990806: promoted. The public CSR wrappers identify complete NI071F2 Protocol Version 4.0 and SAP Version 5.0.
- NCT02346734: promoted. The protocol and SAP share exact title, NCT identifier, and approval date.
- NCT02264210: promoted. Protocol and SAP Version 1.1 share GASTO 1003, NCT02264210, and May 2020.
- NCT02960854: promoted. SAP Version 2.0 explicitly lists Revised Protocol 01 in its amendment table.
- NCT02024750, NCT07673497, and NCT06616376: `excluded_wrong_document_type`; their statistical uploads describe completed-study conduct or analysis rather than prospective governing SAPs.
- NCT07352566: `excluded_combined_protocol_sap_leakage`; the protocol already contains the target feasibility analysis.
- NCT03771638: `hold_version_reconciliation`; the protocol is Version 4.0 while the analysis plan identifies Protocol Version 2.0 despite the same document date.
- NCT05646719: `hold_version_reconciliation`; the matched Amendment 3/SAP Version 1.0 pair contains conflicting Stage-1 versus Stage-2 primary endpoint, hierarchy, and success-population statements.

## Source audit

For every candidate below, title/version pages and pages supporting admission, hold, leakage, or retrospective-document decisions were visually inspected. Page counts and SHA-256 hashes were checked from the frozen public PDFs.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT03574597 | protocol | 103 | f0ff59b32f20b166c877b46875c8d95f905d302dbebb4fe2e06be63b89f8803f | [Prot_002.pdf](https://cdn.clinicaltrials.gov/large-docs/97/NCT03574597/Prot_002.pdf) |
| NCT03574597 | SAP | 42 | 3133a6100a31d793657b24eb501719a9004fc654cf5370e9df1ceacded0cc6cb | [SAP_003.pdf](https://cdn.clinicaltrials.gov/large-docs/97/NCT03574597/SAP_003.pdf) |
| NCT02320149 | protocol | 67 | 3553c25d61d57aa2e4fb6ab4cdb10c991ca7da162aad028b1f3ac67a145a5049 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/49/NCT02320149/Prot_000.pdf) |
| NCT02320149 | SAP | 64 | fa3a62f15e374effef3cf51dc8bef4c25552f661a53413722222f9dcea0e3651 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/49/NCT02320149/SAP_001.pdf) |
| NCT02990806 | protocol | 96 | fb26ea8894933904f2e80659aacdc49d640a0e633aae64807810d0b0573a042c | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/06/NCT02990806/Prot_000.pdf) |
| NCT02990806 | SAP | 47 | 6206d53636a429d8fd6d360118ac487957da826582c1d67a34113aac21e1ce6a | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/06/NCT02990806/SAP_001.pdf) |
| NCT02346734 | protocol | 3 | 38e829470ae69c9bc7c8c4ca9cec68097ca91a33f2a105390226a8b0c6857e80 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/34/NCT02346734/Prot_000.pdf) |
| NCT02346734 | SAP | 3 | 629642ef86577da1a833f71bcbd618c95b37196c1d53d962b329ab02440d1f62 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/34/NCT02346734/SAP_001.pdf) |
| NCT02264210 | protocol | 42 | 3870f053a6de549d4bdb939d7ae9f36426eea4faace39b22c31f52eacd016362 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/10/NCT02264210/Prot_000.pdf) |
| NCT02264210 | SAP | 17 | f0278216ba21368792af223b3c294202aa01af04b8c977d62947106c0da1ded5 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/10/NCT02264210/SAP_001.pdf) |
| NCT02960854 | protocol | 77 | ad0e6c3482c88338438081031840719fb9032e925b54415fa8bed0e9961b4a4f | [Prot_001.pdf](https://cdn.clinicaltrials.gov/large-docs/54/NCT02960854/Prot_001.pdf) |
| NCT02960854 | SAP | 30 | ddc735ce6dcc0c45172ade0fb9e7ddd3f1e8b6cdb5ecb6f6863245777f6d2a32 | [SAP_000.pdf](https://cdn.clinicaltrials.gov/large-docs/54/NCT02960854/SAP_000.pdf) |
| NCT02024750 | protocol | 13 | c796689ff5013500b85a6ac437f3adeb7bd34bfa86fff797458da925a79598c6 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/50/NCT02024750/Prot_000.pdf) |
| NCT02024750 | analysis upload | 3 | b32abf57389c8ffe92b1539b23fa131d2dfb5317d7c5c276b7b3529471a68eb3 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/50/NCT02024750/SAP_001.pdf) |
| NCT07673497 | protocol | 4 | 78abcd7957198fefc5e2f6d0cf98f9123d9f8ce375b8ffb5014833ca4fea346a | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/97/NCT07673497/Prot_000.pdf) |
| NCT07673497 | analysis upload | 3 | 7bc9eefb61dd5abdd18926c4c1cee3dc02ae81519e9d091fa09019e6d172e234 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/97/NCT07673497/SAP_001.pdf) |
| NCT06616376 | protocol upload | 2 | 041386c89ad5d01123b7200fa62ab49fa61b6368da8b823654c4e6ff8dadb344 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/76/NCT06616376/Prot_000.pdf) |
| NCT06616376 | analysis upload | 1 | fa09a90dbe3c7192764d9a25365e1f0eb1fc4d47f275503a347426ce51efbb04 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/76/NCT06616376/SAP_001.pdf) |
| NCT07352566 | protocol | 32 | 397efeab65b42bb7207eb9c48af7dd8035eba587be6df65be793da08067bb267 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/66/NCT07352566/Prot_000.pdf) |
| NCT07352566 | SAP | 2 | b45e857baa1e96af1ab8ee9269341a00631f76b13cca49aaf2aa951aeb56680c | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/66/NCT07352566/SAP_001.pdf) |
| NCT03771638 | protocol | 27 | 181ac9846099dd4e7230937c636bc8fa2bef2275ee748ddaae21d57b449cf074 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/38/NCT03771638/Prot_000.pdf) |
| NCT03771638 | analysis plan | 4 | 4206e479d6669bd4dc3867854d44d845d8340cda991d975e47fb267c13679849 | [SAP_002.pdf](https://cdn.clinicaltrials.gov/large-docs/38/NCT03771638/SAP_002.pdf) |
| NCT05646719 | protocol | 76 | e51849f3520ee781dfcf227f392b6faf5b98de35788f6e73ca9860366229f612 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/19/NCT05646719/Prot_000.pdf) |
| NCT05646719 | SAP | 51 | f23272446f9aaac49aebed42dc67a3728b1ab65f568307a94bd963c6cd2d7987 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/19/NCT05646719/SAP_001.pdf) |

The local PDFs are acquisition artifacts under the gitignored source tree. Their URLs, hashes, and page counts are recorded here or in the manifest; PDFs are not committed.
