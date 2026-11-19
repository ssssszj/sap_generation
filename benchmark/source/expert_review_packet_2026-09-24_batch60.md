# Expert Review Packet — Batch 60

## Scope

Batch 60 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent-target gate: seven model-visible protocols expose executable target analyses, and NCT03847389 supplies a post-completion, termination-informed abbreviated safety-CSR plan rather than a prospective hidden target. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. Temporary Ghostscript-repaired copies were used only to parse the malformed NCT04891406 page trees; the frozen originals and hashes were not changed. The scan-only NCT03847389 pair was fully OCRed and then checked against the rendered originals.

## Decisions

- NCT02558231 — excluded: protocol pages 78-82 expose analysis sets, PVR analysis, futility and hierarchy, missingness, primary/secondary models and subgroups; selected SAP is post-primary.
- NCT03512262 — excluded: protocol pages 70-74 expose populations, PMM multiple imputation, ANCOVA, MMRM, LOCF, fixed-sequence testing and safety; SAP is post-primary.
- NCT04891406 — excluded: protocol pages 55-59 expose populations, PK derivations, mixed model, Bonferroni-Holm testing, secondary analyses and safety; SAP is post-completion.
- NCT03847389 — excluded: scan-only protocol pages 8, 42 and 44 expose cohort progression, populations, derivations, descriptive analysis, missingness, sample size, safety and interim summaries; post-completion plan incorporates termination after eight participants and is limited to an abbreviated safety CSR.
- NCT03053050 — excluded: protocol pages 91-96 expose populations, missingness, multiplicity, stratified primary analysis, treatment-failure handling and secondary analyses.
- NCT03319719 — excluded: protocol pages 56-61 expose sample size, populations, paired one-sided testing, descriptive analysis and observed-case/LOCF handling; SAP is post-completion.
- NCT02373098 — excluded: protocol pages 31-32 expose populations, descriptive analyses, paired-difference power and the no-interim rule; SAP is post-completion.
- NCT02285855 — excluded: protocol pages 8-9 expose allocation, Mann-Whitney testing, genotype power, correlation, AUROC and regression analyses; the one-page same-day SAP duplicates that protocol text.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02558231 | protocol leakage plus post-primary SAP | 97 / 138 | 74224ded18d074ca6b0534c238825120dbb61b56d91e9ac0812517ab750ef85a | 72343ea3330ca95f8cd767b118a8c425dc7e673dfc7b1f97380317a6c364b32e |
| NCT03512262 | protocol leakage plus post-primary SAP | 82 / 52 | 3a8b37bd840ee83978816f256ee89959fc2fe2a6f143dfa2506bc790afe4fa38 | 1a4bbb43f252deee249abe2dc8055a6e6c841f578bc116c725be883306d5bfa1 |
| NCT04891406 | protocol leakage plus post-completion SAP | 63 / 34 | 9bb16ac5ffa6a2c3d33a98ad371f4481978482b66b9478af6db81eebd7a08ebb | 5d29b96b091062621a9743cf22690f5aa00034069e116bffdeeeffbbbf109550 |
| NCT03847389 | execution-informed abbreviated CSR plan | 60 / 12 | 35c6f9f7b1d523ed4d7e60f23563c5a268081f7fc19da97da81daf0d288a1b7e | 19734e60018944f7d4d38869b7570ee9a68f9a8279ee80979f37c15aac404243 |
| NCT03053050 | protocol leakage | 124 / 81 | b7dd65234b385d3fb879fa10efa6983f7164a2d5a5a8d36566eef68cf166ab87 | e3cc21ac53938607d310e163764f1b024a2024e723201aaf2eed50513dec5be1 |
| NCT03319719 | protocol leakage plus post-completion SAP | 68 / 19 | 837a26822e85753023bebab34c50cbcf4597846d2fea74115c281f0764392272 | 5f5cbf6088b98acf2983dc3cf2d6a33249a9f683a9ca8df71a6c6218c6a804ee |
| NCT02373098 | protocol leakage plus post-completion SAP | 38 / 9 | 3a6b5e8a589614a86c9d5ee851daab337b6d7530b30c1251fcf3dee95dba64be | 4afc0b625bd116f9a90fee2b705d004819498746982dbb2da4546f18fcaf360b |
| NCT02285855 | protocol leakage plus duplicated extract | 15 / 1 | 3b81e2d852635b335be2b28c22bec6df896864c7ef2e4fa0c760b060dc172401 | 8cdf7548fff0c0b5d5835b63cb950befe9f4b7d9e09257bf186ab1bc6d83115a |

## Review gate

No Batch 60 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
