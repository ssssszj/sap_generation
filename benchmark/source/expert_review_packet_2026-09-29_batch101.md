# Expert Review Packet - Batch 101

## Scope and decision boundary

Batch 101 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally and extracted page by page. Decisive identity, chronology, executed-analysis and target-leakage pages were rendered and visually inspected. One family is promoted as a first-pass annotation draft and seven are excluded. Seven open slots are replenished so the intake remains 120 public families.

## Promotion

- `NCT04469218` -> `PUBLIC-DIPPER-SAFEBREAK-001`. The four-page protocol synopsis and independent three-page statistical-plan synopsis share HHC-2020-0086, title and 2020-10-13 IRB approval date during recruitment and before completion. The protocol defines the prospective randomized SafeBreak-versus-standard-care comparison, conditional noninferiority/superiority objective, target and endpoints without leaking the reference-only Wilcoxon, Kaplan-Meier, Poisson, per-protocol or censoring choices. Twenty requirements were added. The absent noninferiority margin, delay derivation, randomized and PP populations, success gate, missingness, recurrent events, safety, multiplicity and sample-size assumptions require expert adjudication.

## Exclusions

- `NCT03727646` — the analysis upload reports a calculated p-value and a test already performed rather than a prospective plan.
- `NCT03103906` — SAP Amendment 1 postdates actual primary and final completion, with unresolved unblinding timing.
- `NCT03980808` — both selected documents postdate completion by nearly eleven months.
- `NCT02394028` — SAP Version 3 postdates completion and acknowledges earlier unblinded analyses that informed design.
- `NCT02502149` — protocol pages 69-72 expose populations, primary PK mixed model, intervals, back-transformation, safety, interim access and sample size.
- `NCT02223182` — protocol and SAP both postdate primary completion and cannot govern the primary analysis prospectively.
- `NCT06127147` — protocol page 13 exposes transformations, tests, ANCOVA, Bonferroni, alpha and conflicting power calculations.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03727646 | executed-results template | 12 / 3 | 396475e995b98c108d4e56dcc9c2204d791741fee925e61475c5f2aee88d168b | b4491063e098bf33a9e0b4428708c2d8638f62270ec884595597c20d53b16fa4 |
| NCT03103906 | post-completion amendment | 91 / 36 | 899a41f33413820d4b5d8d29ca97e42644685e63e01667b9f29123ed07ecce06 | 30d7c8a2a78e3d0e1c9e4e6d24a71a5ae76ccb45a2c2c22cca29c9341140deed |
| NCT03980808 | post-completion pair | 9 / 3 | 36ac10476f30286e3264b289e53b464538d1cc479a126661c3d4b23d77defd6a | 3dc407e2208c0efdf8dfe359cd0feb1676042d4f06df68caaef8005c88bc6709 |
| NCT02394028 | outcome-informed post-completion plan | 186 / 62 | f989f1752a45e2c9cfe53d65d45ff1c3f6033133ce4fbd046a1d85a1909bcfba | 18a5159697aae6300f07da8fa8c183247b9d8d66456ac7c4c9fd93765fa67510 |
| NCT02502149 | protocol leakage | 80 / 54 | b109509e2cb382c00aaaf4d3415dc7f9a3afc8ae8e764cc799876e8877b41ed1 | 8097921758f755509f9f4b48a0f184d8bc837ebd11435790bf3ee77e7e60694b |
| NCT02223182 | post-primary pair | 170 / 75 | 1ef2809fc9648f5e69ff33e5f473f25a369877388bc4f54e1c6992f19630df18 | 7f6bd720a3e3a3a1c541ee21925a731c9c502a05d2db79ae088dcfba9e73130e |
| NCT04469218 | promoted during-recruitment draft | 4 / 3 | f52b745ab1fad2166440934fe5f8fd89b69c3ea4eba0f8657998b0d08d9bce18 | fb434ae7d685ec4bd68d577ff9d7c7358daf71f8e98b79309eb9257715ac8fe0 |
| NCT06127147 | protocol leakage and conflicting methods | 27 / 2 | 99b67f73f6a2d6a4a3bb1a2a8a4d7861acc75791b969ff7364fd03e81e8ba341 | 1f76b1a36fc4b1c781991d626af51463b65b8e8ea1e89fc14e084a81ca4cd6b8 |

## Review gate

The promoted family remains `draft_needs_expert_review`; it is not expert-approved or split-frozen. Its reference plan remains annotation-only and must never be model-visible. The seven exclusions do not enter the completed-question count.
