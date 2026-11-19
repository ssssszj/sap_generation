# Expert Review Packet — Batch 44

## Scope

Batch 44 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed both the independent-target and governing-version gates: seven protocols disclose executable target analyses, and one public pair lacks the SAP's governing protocol version. All 16 PDFs and eight registry records were downloaded and hash-frozen, text-extracted or OCRed, and visually checked at the identity, chronology and decision-defining statistical pages.

## Version hold

- `NCT02050841` — the public protocol is Version 9 dated 2016-11-19, but SAP Final Version 7 cites Protocol Version 10 dated 2017-11-29 on physical SAP page 5. The missing governing protocol prevents a defensible prompt/reference pairing.

## Exclusions

- `NCT03224299` — scan-only protocol pages 13 and 30-34 expose ITT/mITT/PP sets, endpoint-specific missing-data rules, linear regression, the 0.5 log10 noninferiority and 1.2 log10 superiority criteria, ANOVA and sample-size rationale.
- `NCT02735044` — protocol pages 78-85 expose sample size, analysis populations, two-part and penalized multiple imputation, ANCOVA, tipping-point sensitivity analysis and multiplicity.
- `NCT02155725` — protocol pages 60-66 expose blinded sample-size re-estimation, analysis sets, exact logistic regression, missing-as-failure and sensitivity analyses; the SAP is also post-completion.
- `NCT03988608` — protocol pages 66-73 expose FAS/safety/PK sets, descriptive and PK methods, the primary responder analysis and feasibility sample size; the selected final-analysis SAP is post-primary-completion.
- `NCT03616912` — protocol pages 71-80 expose sample size, populations, Firth logistic regression, MMRM/ANCOVA, NRI, delta-adjusted MI, graphical multiplicity, Cox and interim methods; the SAP is post-primary-completion.
- `NCT02735863` — scan-only protocol pages 41-45 expose analysis sets, Kaplan-Meier/categorical tests, ANOVA/ANCOVA, PK analyses, no-interim policy and sample size; the SAP confirms exact Protocol Version 4.0 matching.
- `NCT02620020` — protocol pages 60-66 expose Hochberg plus gatekeeping, four analysis sets, MMRM, pattern-mixture MI, categorical analyses, interim rules and sample size.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02050841 | governing-version hold | 55 / 22 | `046de9e41e985d9cbb958e7d5c0fab172deaab61cb3639418a75460d37d0e016` | `80ce66e5aae48e7589445d8d22555cc7774c11eebcd7a99a6dfaef29d5968978` |
| NCT03224299 | protocol leakage | 49 / 20 | `35aa0ab1493200509dc025e57a09d826d2e1ca0488cb1abb618baf76b023233f` | `fe23180405f76960d43565e709716f01af2bd0df3879ba2865060738d6437052` |
| NCT02735044 | protocol leakage | 100 / 58 | `9e2a85a0f484d0d10de20cd269f2c3e22033bf65ec752100330ac78085add142` | `2927da76b0450495923ac8633a4afc98da980e1ee22be5e8e42f22573f110463` |
| NCT02155725 | leakage + post-completion SAP | 77 / 52 | `04e23a1bb9ddeadc6a7be2ae790125b2026724b5b405efe22321f7d02bcefa27` | `f6f0bcfb23bd43455e998a0707383440633b082dcdc187f6cf8307bdeaaf94c8` |
| NCT03988608 | leakage + post-primary SAP | 80 / 36 | `86b1cc4286e7b01f2fed3e40bf7d0efcc88208e175eb5392d03f6b4331a4e210` | `398b9afdab88e8bc296de727c79e27f21376ee53dbfb92a5b2e27c8759d6b5a0` |
| NCT03616912 | leakage + post-primary SAP | 121 / 86 | `f1708ad0d3fdc89b4b88b0793ec277a719a9f55462c683fcce967f5659c02735` | `4e315b878e7cd7604da95954d2c2951ff5163d168e14e3e9386e2c32a7e04e7b` |
| NCT02735863 | protocol leakage | 52 / 83 | `f16b53cfc47e23e266f15abd33bb1fe786e9b2aafcc342356342d9aaed61e35a` | `09b9c8cd2102255ea4f39fe504fe47f0da211f2afb91f179688b69bcab72695d` |
| NCT02620020 | protocol leakage | 77 / 53 | `30e24941d4d57dca9a79dd1149894c26184f39a9e821155370dd79e3ea90564f` | `2c736b8189b3ddf0a23fd175e530ca0a1dbee469b25dbbb5198b9c363f0bf249` |

## Review gate

These eight candidates cannot enter train/dev/test. The version hold remains outside the actionable queue, and all eight slots must be replenished; no Batch 44 record is counted as a completed benchmark question.
