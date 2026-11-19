# Expert Review Packet - Batch 91

## Scope and decision boundary

Batch 91 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally and page-extracted; decisive chronology, execution, leakage, adaptation and document-independence pages were rendered for visual inspection. No family is promoted. Two protocols expose their target analyses, three references are post-completion or executed-results packages, one design was revised using outcomes from the same ongoing study, and two nominal pairs are retrospective/registry/grant excerpts rather than independent prospective protocol and SAP documents. All eight slots are replenished.

## Exclusions

- `NCT03683030` — post-completion package. Protocol Version 11.0 and SAP Version 4.0 are both dated 2022-11-15, nine months after actual primary/study completion, and retain an adaptive Bayesian/interim-analysis design.
- `NCT05650567` — outcome-informed termination plan. IAP Version 3.0 follows completion; page 20 says interim results led to premature termination and replacement of planned primary/secondary analyses with a reduced abbreviated-CSR analysis.
- `NCT04259632` — executed-results analysis. Pages 2-4 say analyses were conducted, name an observed participant with extreme 14.1 kg weight loss and use R 4.3.1; protocol pages 48-49 independently expose the planned models, missingness and power.
- `NCT02819635` — protocol leakage. Protocol pages 156-171 expose ITT/safety sets, NRI/MMRM, MCP-Mod, CMH strata, multiplicity, hierarchies and sample-size assumptions reproduced in the SAP.
- `NCT03136185` — within-study outcome-informed adaptation. Protocol page 35 says observed treated-patient data and repeated DSMC/SAB review drove dose/titration changes and removal of a visit; the SAP also incorporates Phase 1/2a data and actual treated counts.
- `NCT02690935` — protocol leakage. Protocol pages 25-27 expose power scenarios, populations, software, missing-data rule, tests, alpha and lack of multiplicity adjustment.
- `NCT03519568` — wrong document type. The short same-date uploads are retrospective/registry-style summaries with past-tense recruitment and randomization language, repeated arms/interventions/outcomes and no defensible independent governing chain.
- `NCT04869085` — non-independent split. Both files share the same ORA header and form contiguous B3 grant/IRB sections; the one-page analysis excerpt is not an independent SAP.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03683030 | post-completion adaptive package | 100 / 46 | 6bc74760aa010e3ff40089953c06da067d38cbe21a9fdf08911c7d2c9b44aedd | edb5b905a5c903718a4d21c67ddd50a15a65b8f1a9efa5212f50a09fb4523359 |
| NCT05650567 | termination-informed post-completion plan | 132 / 86 | c0b5fa8ba0ed5b63306d78852f87c9609e58b5f5e0f02228c0c47236b690ff0a | c4a68dfb81f14e78ec442cc087bec01b0e2d13e837d2ab1ba6582abd2ad33efa |
| NCT04259632 | executed-results methods | 80 / 6 | 1f1059d34f7df192fc57abf68381f800e1a7fe2d6c846470edad62098e3ac846 | 890bc0eac0ca37811cef2cfc15c27b3246c4ee9b5f901685dd1f3048361aeda2 |
| NCT02819635 | protocol leakage | 224 / 146 | 8ac9534502bc60d3bac5a82f05bb052c435b8203b0e39301b33df5caaab69507 | 7942dad13777c322889ff320083ff9f646a6460b8a0c766320391ac7e7d0b521 |
| NCT03136185 | within-study outcome-informed | 98 / 33 | 05fafb73b34a59c77ad3e02f97bbb20eac0d2354fd5ec777770f3b9d667bf8c1 | 324d2168ba39bb1ff8cbf22d88005b7a486641338568756ef348029ef22e5465 |
| NCT02690935 | protocol leakage | 33 / 29 | 4aa1b7c7ea6d287c5e296b307d04c8e9b8aa04eb46a295448c995325c9bb2b1e | 6d6c03bae8889eb61d851dce5cfa4063cb373eea4b00b0f62ec9a59f5ff4ed4e |
| NCT03519568 | retrospective/registry summary | 8 / 5 | 57e36d6f7ae30dbda46c10a31a60f749589b4c38d1a036e9548df297eec5a3dd | e5d03f3232954ca2d401aba374a4e10b56d11137e0b0f2002c7dfad772e7677d |
| NCT04869085 | non-independent grant/IRB split | 5 / 1 | 58d61769ef8087987420749ec3813511e337a3e169814a0eac83abd223c3d7f5 | 9b9ee814cf2e3ad55cb13a642708e290c5443dd07767bdba05c754a96dc9f7ff |

## Visual review

Rendered one-based physical PDF pages confirmed the decisive findings: STELLAR protocol page 1, NEPTUNIA IAP page 20, fasting-study analysis page 2, upadacitinib protocol page 162, bomedemstat protocol page 35, 2LALERG protocol page 27, EV71 methods page 3 and e-PainSupport analysis page 1. The visible redactions in the NEPTUNIA and bomedemstat files do not obscure the termination or within-study adaptation evidence.

## Review gate

None of the eight families enters the registered benchmark. Their slots remain outside the completed-question count and are replenished so that the working collection continues to contain exactly 120 public families across registered drafts and metadata candidates.
