# Expert Review Packet — Batch 46

## Scope

Batch 46 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent prospective-target gate: five protocols disclose executable target analyses, while three selected analysis packages are post-study, retrospective or execution-informed rather than prospective governing SAPs. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining statistical pages.

## Exclusions

- `NCT02257632` — protocol pages 44-49 expose analysis sets, primary ANCOVA, baseline adjustment, missingness, sensitivity, blinded variance interim and sample size; the SAP is post-completion.
- `NCT05266053` — the alleged protocol is a post-study results manuscript whose 2024-11-16 cover conflicts with registry metadata, and the two-page post-completion analysis note is not a prospective governing SAP.
- `NCT02802514` — the post-completion Reporting and Analysis Plan explicitly incorporates early termination, cancellation of Part B, the four completed Part A subjects and an execution-informed analysis change.
- `NCT04701411` — protocol pages 73-75 expose ITT/safety sets, Clopper-Pearson analyses, time-to-event censoring, safety summaries and interim analysis despite a clean pre-completion version chain.
- `NCT04514510` — protocol pages 46-54 expose power, populations, ANCOVA/Wilcoxon, multiple imputation and safety stopping; the public protocol is also later than both SAP issuance and study completion.
- `NCT03832738` — protocol pages 56-58 expose four analysis sets, sample size, no-interim policy and primary/sensitivity population usage; the SAP confirms Protocol Version 3.0 and is post-completion.
- `NCT02753842` — the five-page analysis document is a post-completion JMIR publication artifact rather than a prospective SAP; protocol pages 31-33 additionally expose aims, hypotheses, sample size and outcome mapping.
- `NCT02697773` — protocol pages 104-109 expose power, ITT, ANCOVA, multiplicity, multiple imputation, LOCF/BOCF/MMRM, secondary methods and safety; the SAP is post-completion.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02257632 | leakage + post-completion SAP | 55 / 29 | `93ffe6db1dd7de9e22f048976ac4d9f79cb9cbb497e6ff1fd93753ef0a008064` | `c9b3be0c3effd2b71db51c7a91706faf3cd739a0324d4c25e37fca68c4ee0576` |
| NCT05266053 | post-study manuscript + post-completion note | 14 / 2 | `bf75c5220e6aadac0ce14c5c14f300c9031c22b09935a1b136134e72ed1ff5b8` | `6103fbe0cce4cdf9a99d86b7ea8a2f7494d7b0257e71adf37a671fa8e6ddc924` |
| NCT02802514 | execution-informed RAP | 93 / 33 | `d54593d757839ea9c5b542d8d2b7ed338ad9da80a6f971bd5321dec898a964bc` | `a78acc8fd974e3dd83b9b7b79af5a47116183c90701dc1dea6ad54f3a4bc5fb8` |
| NCT04701411 | protocol leakage | 109 / 31 | `7c40e3eb955ecb246ba5376edacf2c83485dedc569adc05ff6b7ad1b386a7c9d` | `418be09246641f92f419ea50030783e6f9fc1aaed2ff50d61b4bf3586e0ef3ad` |
| NCT04514510 | leakage + non-governing chronology | 68 / 3 | `7dc401b2a6c379b185a295f4529c60a65f5506a69a33086ea367fa345b0e61d9` | `c299164cafd3274f6d85a92aae8fc798aa724d6b08121a0491d5668e0b32d221` |
| NCT03832738 | leakage + post-completion SAP | 71 / 35 | `f652f96ab9f5922967f0919d403d36db52d9b300406597e327b7f52886509c5b` | `6b41f727240a1155738e2f1927146c637a61f43197ad6ea97332826eff8b82c0` |
| NCT02753842 | publication artifact + protocol leakage | 48 / 5 | `3ac797555395e4a7ad8f56b106398b530d8cbeb067cf445151a2309a6ec74a55` | `ef4849ebb2f1a0ae78cf0b8d89753b4d50fff452afa13a729c1a1632b828d5eb` |
| NCT02697773 | leakage + post-completion SAP | 151 / 56 | `b9bf9ec92f428ac40a160c41ecd9aa8a4edaa796f6828c6e2cda61b3ffee25b8` | `33984952bb4ea556963aff80311183a0b003321ab2b98cc09c175551b5d1c320` |

## Review gate

These eight candidates cannot enter train/dev/test. All eight slots must be replenished; no Batch 46 record is counted as a completed benchmark question.
