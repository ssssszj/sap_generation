# Expert Review Packet — Batch 53

## Scope

Batch 53 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed all prospective-version, identity and independent-target gates: seven model-visible protocols expose executable target analysis content, five selected document chains are additionally post-completion or execution-informed, and one two-page file labelled as an SAP is a retrospective description of analyses already performed. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages.

## Decisions

- NCT02442206 — excluded: protocol pages 53-57 expose FAS/PP/safety sets, PP-primary use, the primary ANOVA model, two-sided alpha, missingness, supportive analyses, safety summaries, interim intent and power.
- NCT03197324 — excluded: protocol pages 43-45 expose safety/PK sets, noncompartmental derivations, BLQ rules, crossover ANOVA effects, geometric-mean ratios, 90% confidence intervals and 80%-125% bounds; SAP is post-completion.
- NCT06750276 — excluded: protocol pages 65-70 expose FAS/safety/PK sets, safety/ECG summaries, PK displays, geometric summaries and BLQ handling; SAP Edition 2.0 is post-completion.
- NCT04207736 — excluded: protocol pages 57-60 expose populations, hypotheses, crossover MMRM, secondary/safety summaries, missingness and multiplicity; both exact-matched documents are post-completion.
- NCT02824640 — excluded: protocol pages 64-73 expose analysis principles, missingness, logistic and mixed models, exact intervals, mediation, subgroup and power analyses.
- NCT02961062 — excluded: protocol pages 64-69 expose analysis sets, full mixed-model specifications, sensitivities, secondary tests, safety/PK summaries and power; SAP is post-completion.
- NCT02129348 — excluded as the wrong target document type: both files are post-completion, and the two-page "SAP" uses past tense to report published methods, actual enrollment and observed dropout.
- NCT02301611 — excluded: protocol pages 39-43 expose ITT/PP, primary and secondary tests, interim timing, missingness and power; protocol/SAP revisions incorporate an observed recurrence rate from the first 75 participants.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02442206 | protocol leakage | 81 / 28 | 036e27dba800b9dfdc00e6eeb9d34ed51aaa98c0fa46d4a94e732bdd1d7b5715 | a96d9d944fa15975d83c093849889db77a75e5c3258634fc0c22fad0fb2212a5 |
| NCT03197324 | protocol leakage plus post-completion SAP | 58 / 31 | 28e1daa923a47d6113aac93572986add547a32bf00d95fe4c2e8d25226369d4d | 4328e3ae525eaeea1683d8fb2595b861924ddc7c263a601ec08d107d2ee212e5 |
| NCT06750276 | protocol leakage plus post-completion SAP | 106 / 44 | 285365823eff91c33deca9ebb1842dc9d032e53a445faf1b02fd81e12526cb1c | 40dbeb285cd997b15d9d0393c9f5f88eee1d48bb362cfaff4f374637655ef6d6 |
| NCT04207736 | protocol leakage plus post-completion exact pair | 68 / 24 | 5a0b9514622a3d7a8344d239b0fd3ff93e91f4c2e05bffe7f71042fca60b1d00 | caf6b4e068c540e578639760114522cd0f5ca20e3d0e0357057d276261ecd9c8 |
| NCT02824640 | protocol leakage | 107 / 19 | 8bc6ae93ce104d936f51f4ba536250e5bef864b3f322c7d609c6eee1f9c44ebc | 3681524b0f37260a2b1972745d402cb9eb8f3676a38fb675f4f11237c7d09984 |
| NCT02961062 | protocol leakage plus post-completion SAP | 72 / 14 | 8f316b44a509dc950f4d3a182a7f38ffbe8b95baf985a83ce008a2928cfd4f4c | 48a6fedcdc51a018883d1861b265a1d17b586bc3131e9529a49ad4ef7ebe5684 |
| NCT02129348 | post-completion retrospective methods summary | 27 / 2 | 8567d98dc776709b7c5167540622796549622a37d6b56c1daf3a7864ccfd96f6 | aac397e23102c63946547340425b6f168aff939d4448559317a135c3d85cc678 |
| NCT02301611 | protocol leakage plus execution-informed revisions | 74 / 15 | cee19e4f3d7c46b57e6269994c727239b62c22d9c7d17b3e9e97874dd6bd49aa | 12e2e693d6e7403e0d3ab476b0043cc869c1eae43ef116cc8004651623d2b4e1 |

## Review gate

No Batch 53 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
