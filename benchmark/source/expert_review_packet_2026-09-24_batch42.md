# Expert Review Packet — Batch 42

## Scope

Batch 42 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent-target gate. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining statistical pages.

## Exclusions

- `NCT01975389` — protocol pages 20-21 and 123-133 expose FAS/ITT, stratified log-rank and Cox analyses, Kaplan-Meier summaries, repeated-measures models, multiplicity, interim alpha and complete power assumptions.
- `NCT05192200` — protocol pages 61-65 expose safety, skin, muscle and pooled analysis sets, LANCOVA/ANCOVA, MAR, subgroup analyses, no-interim and sample-size rules.
- `NCT02589639` — protocol pages 57-61 expose ANCOVA, FAS/PPS, LOCF, MMRM sensitivity analysis, randomization and power; the SAP is post-primary-completion.
- `NCT04023396` — protocol pages 45-46 expose SAF/FAS/PP sets, Week 48 interim outputs, descriptive and subgroup analyses and the sample-size rule; the SAP is post-completion.
- `NCT03489291` — the selected protocol is post-primary-completion and pages 17-18 and 85-88 expose descriptive methods, the six-week interim analysis, analysis population and N=3 rationale; the reference is packaged in a CSR addendum.
- `NCT03598790` — protocol pages 109-115 expose analysis sets, non-responder and multiple imputation, efficacy summaries, interim timing and sample-size determination.
- `NCT02699099` — protocol pages 93-100 expose noninferiority margins, power, analysis cohorts, missing-data rules, confidence intervals and safety methods; the SAP is post-primary-completion.
- `NCT02517905` — protocol pages 20 and 57-60 expose primary ANOVA, fixed-sequence multiplicity, analysis sets, WOCF and other imputation, Kaplan-Meier/log-rank, alpha and power; the SAP is post-completion.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01975389 | protocol leakage | 167 / 83 | `e452e8f9c3245425f85be917187aab6edcfc776bd11b9b20f7347d922bab7146` | `d96a5ac82be27c48f2ee64d1827dd5da72f5b58d40d241ca99a610a67938aff8` |
| NCT05192200 | protocol leakage | 109 / 31 | `157a2563ab9122451bb5df1c8f1c590142053c5f34ea8cabc4ce13eefa794f33` | `ce070b4b1cf1fdeeb8644eaedb152bf2871412d3ea0f5d65492080def2ae7fdd` |
| NCT02589639 | leakage + post-primary SAP | 74 / 40 | `2605da3c5959c6aee18dbe7539b97bf6979d0a711b9b490a2aa79d4128ac445f` | `3a57cb166495a36f7e959f1659ed6a2b39dc558e4a4f14da3de8419248a118bc` |
| NCT04023396 | leakage + post-completion SAP | 65 / 49 | `f0672764432b79143033a4b9979c7d2ee1e210c106a5520f3e8af6de92c1d6f1` | `c31c8c87e429aea3d876358f2936084b38be316cf3fa2fe9148dd8c945e253eb` |
| NCT03489291 | post-primary protocol + leakage + CSR package | 113 / 189 | `9e72211c9936857a8ab037a41d60aec521e7cb256abe72b1cc0395ee3a53dc8e` | `4782cee459ae35c6840ca0cc6066224522d5ca1922fdc7add48aebf88411afc2` |
| NCT03598790 | protocol leakage | 217 / 142 | `d96cacd78241f1f5d1d3a368d665da16780a8a9e54e0043f754d27ae4ae2afb2` | `82ea16043a813fb877f20345c681c4243637199d3957abcb31eaf26a2259d019` |
| NCT02699099 | leakage + post-primary SAP | 121 / 75 | `946a75ea80c93b4b4e7889b22a1d52f82c29c612b0f2e734595e5e6f33aeaedc` | `3191d4476b2e34e0a95c9aac4e2fa7796b55427389d99403853c258e710bc470` |
| NCT02517905 | leakage + post-completion SAP | 69 / 141 | `6e078f786590c7ee6c123aca4ac7b15f0bd9e1bec2ebc0aa8b26e2dbfc359160` | `e748d5fce7c2f600f95b755acdc05e7bb7cb41fc5e175603341b1f0dd98136b6` |

## Review gate

These eight candidates cannot enter train/dev/test. All eight slots must be replenished; no Batch 42 record is counted as a completed benchmark question.
