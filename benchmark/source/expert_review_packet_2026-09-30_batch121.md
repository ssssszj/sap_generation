# Expert Review Packet - Batch 121

## Scope and decision boundary

Batch 121 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen selected official PDFs and eight official registry records were downloaded sequentially and SHA-256 frozen. The pairs contain 1,000 one-based physical PDF pages. Native text was extracted page by page, all 26 empty-text pages were separately rendered and OCRed, and 109 decisive identity, chronology, version, analysis and leakage pages were rendered into 17 contact sheets and visually compared with the originals. One candidate is promoted to a public first-pass annotation draft, six are excluded and one is placed on governing-study-family/prospective-governance hold.

## Decisions

- NCT02182830 — exclude: protocol physical pages 73-79 already expose the hierarchical testing, analysis populations, HbA1c MMRM, ABPM ANCOVA/LOCF, missingness, safety, no-interim and sample-size/power program.
- NCT02910466 — exclude: selected SAP Final 3.0 is post-completion. Its history identifies a pre-completion Final 1.0, but that version is not independently public; protocol pages 51-52 additionally expose the descriptive population and endpoint program.
- NCT04130919 — exclude: the post-primary SAP records realized N=19, termination and cancellation/change of interim and formal analyses; protocol pages 66-71 also disclose the executable CMH/NRI, multiplicity, population, sample-size and interim plan.
- NCT02938585 — exclude: the SAP is post-primary and explicitly says its statistical analysis was already prespecified in the protocol with no changes; protocol pages 92-96 and SAP pages 8-12 materially repeat the target program.
- NCT03135548 — exclude: protocol pages 56-64 expose the ppPASI50 primary analysis, risk difference, Wilson/bootstrap intervals, hierarchical comparisons, FAS/safety sets, NRI, MMRM, interim analyses, sample size and decision thresholds.
- NCT02388165 — exclude: SAP Amendment 5 is post-completion and its history documents changes following a December 2018 interim analysis; protocol pages 92-100 independently expose the event-driven efficacy, futility, population, sample-size, immunogenicity and safety program.
- NCT05425563 — hold: the exact-title same-day pair was produced 14 months after recruitment began. The 23-page umbrella IRB protocol covers 150 participants and four fMRI sessions, while the two-page SAP governs a narrower cue-by-intensity task analysis; revision/sign-off history and governing-substudy linkage are absent.
- NCT04906057 — promote as `PUBLIC-FORCED-AEROBIC-MS-001`: exact title, NCT and 2021-07-15 match across the seven-page protocol and independent two-page analysis document, with IRB 19-1003 also printed in the reference. The protocol supplies the randomized FE-versus-VE pilot, EDSS strata, intervention, feasibility threshold and outcomes without disclosing the reference-only paired tests, mixed models or baseline-adjusted regressions.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02182830 | protocol leakage | 146 / 64 | 75c947af9180aa2aa8ae33ad6ac815b71afff92bd1fb1fada9298251b1b7c212 | b4a74527b284c01792750a4b655b7eb11bd8a96e0d1541c6a6e316d4651950b6 |
| NCT02910466 | post-completion selected SAP; prospective version unavailable | 86 / 38 | 767bc8eca62848b993080655d4733a8e3cacd9076c35dfe2433a57173f15e36d | ddca7ad3401dc55a3751ac94807fc25c47c0045cd113ae1412f819ede1fb67bf |
| NCT04130919 | post-primary and execution-informed | 94 / 51 | 03513c9330696bc9c3563ca62f674b94929dc8a460cfa45a052b757d91168179 | a215e65e5a35de9de9cdd80df9fef47c1b3fcc5573fcef78e3c3102e63440c62 |
| NCT02938585 | post-primary and protocol leakage | 110 / 13 | fa0acd43eebc231da7debad0a9b871cf3cdde3235e524a31403fe57e3c480a19 | 091a180dbe05e669c4111d868d80f3254d03c32b5baa98989a7928ac258a79f2 |
| NCT03135548 | protocol leakage | 78 / 71 | 6fcb7a5f3c682755bd68b6b628f6b9946bf79e2a09928061081ae4ecc533cfe5 | 9d16704245d7cbacd396b4d91652a37a8d8d3d9738b02d52c13d046a3e35bf93 |
| NCT02388165 | post-primary and interim-informed | 129 / 86 | 2e29ca4752b2310f23a974bb80f4653f81b85d874d6820578e7a735d5fafc247 | e89f23cdc0133128890fdb5042f984631bafd9986eb86b6856965dbb53694bcf |
| NCT05425563 | governing-family/prospective-governance hold | 23 / 2 | 69ca991e968a1da4197e5af8341b74feb29d9be19c78982cc242bdbfaf247d3e | fa2cd2fea71acff845e00153e170a828da5d4b81608712f3013dc9e5d0884d04 |
| NCT04906057 | promoted | 7 / 2 | e5639287526f89cc6ec105528775160e66b3b38d4435a0cd350dc4fa82c258c8 | 7de6fae0be6f83089ea7f443d98b0af4e11108ac0636dc673c0ec9ed09f4d052 |

## Promotion annotation and review gate

`PUBLIC-FORCED-AEROBIC-MS-001` has 24 atomic first-pass requirements. They preserve the prospective 20-randomized, 10-per-group target and separately note recruitment up to 24; registry actual N=22 is never substituted. The annotation requires a direct baseline-adjusted randomized FE-versus-VE contrast, treats within-group paired tests as supportive, and exposes unresolved endpoint hierarchy, analysis populations, estimands, missingness, multiplicity, sidedness, confidence intervals, small-sample inference, software and safety decisions.

The draft remains `draft_needs_expert_review`. The same-day pair was finalized nine days after actual study start; expert review must confirm outcome-uninformed governance rather than inferring it solely from the pre-primary date. NCT05425563 may only be reconsidered if a defensible revision/sign-off chain and exact governing-substudy link become available. Seven non-promotable slots were replenished from the official API, preserving 102 public first-pass drafts plus 18 actionable metadata candidates.
