# Expert Review Packet — Batch 50

## Scope

Batch 50 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent prospective-target gate: every model-visible protocol exposes executable target analysis content, and five selected SAPs also have post-primary/completion or execution-informed defects. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. The scan-heavy NCT05731895 pair was additionally rendered at 170 dpi and OCRed with Tesseract before visual adjudication.

## Exclusions

- `NCT01991795` — protocol pages 5 and 63-67 expose FAS/safety sets, Cox/Kaplan-Meier analysis, hierarchical testing, missing-follow-up sensitivity, interim/censoring rules and event-driven power.
- `NCT03056456` — protocol pages 11 and 59-60 expose PK/GD populations, power and alpha, log-scale mixed models, 90% confidence intervals, sensitivity and summary rules.
- `NCT05731895` — OCR-confirmed protocol pages 56-60 expose PK sets and exclusions, log-ANOVA, matched-pair effects, geometric-mean ratios, 90% confidence intervals, missingness and sample size; the SAP is post-completion.
- `NCT03392974` — protocol pages 13-15 and 108-110 expose populations, powered hypotheses, hierarchy and missing-data sensitivity; the later interim SAP is explicitly rewritten around the observed one-subject enrollment.
- `NCT03895372` — protocol pages 13, 15 and 77-79 expose estimands, control-based imputation, populations, exact analysis, multiplicity and interim framework; SAP Version 3.0 is post-completion.
- `NCT02853929` — protocol pages 78-87 expose endpoints, analysis cohorts, derivations, descriptive analysis and timing; the SAP is three days post-completion.
- `NCT02885181` — protocol pages 64-68 expose FAS/safety/PK sets, MMRM/CMH methods, BLQ handling and power; the Final Analysis SAP is post-completion.
- `NCT07542535` — protocol page 5 already specifies ITT mixed-effects analysis and the SAP repeats it while adding achieved power based on the final sample.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01991795 | protocol leakage | 83 / 28 | `aa017c1e164a18916251cc3e1b38f01d392101b8ac40df400bc7b12b424cd775` | `574e4243e4e837b3e8b34622deb58018235f4b53ad1f7539564771c57cead646` |
| NCT03056456 | protocol leakage | 73 / 25 | `d0e6841381efc2ca5701d344b1b6079cba3e11434a461854dec4bddacc927393` | `5d0e1ba514ffaa5203dfd9d7c7f901d9b070cc4d9f033c2d90bd1aa4844624b6` |
| NCT05731895 | protocol leakage + post-completion SAP | 81 / 27 | `1509ffa97671122cf9ecdc15bf2a6e4f595e95c45c310b29ef7a4054abd142fc` | `05797c99229744b92bd7c3dd11bd3ec3a1e7012988903d8051c3e0a4ba89de67` |
| NCT03392974 | protocol leakage + execution-informed SAP | 131 / 32 | `1867dd4a4a6103d5b029659c453df48a23c55dbfda5b5d40c5b04bbc34446a0e` | `88e84dc74032c12fc9161f109e5a7db23cac41a6466d87ef86fa34c5afce1c35` |
| NCT03895372 | protocol leakage + post-completion SAP | 137 / 47 | `5da6d7487184a5a221af9986c320c8a834b160a72e9d7d4af3849a05a5160df4` | `5af1b2d78a3605fd3c504a3dda5abd03bf2ec4e6b7d9624427244473c9c2a939` |
| NCT02853929 | protocol leakage + post-completion SAP | 119 / 60 | `56455d59843f3f9997decee47c3393f2627764ff0b83166f18ca4dd57cf248e9` | `250fa9e7c72e64d7c9c5dc81469629f630f20069cf590fd29c28cc99b0bea194` |
| NCT02885181 | protocol leakage + post-completion SAP | 92 / 49 | `b1a035f871d0ad026fcfa7d83766d879a77aab983896a3c2edbc3527313cf085` | `916c0dfe1db0c9f61cf2ccc4bd404ea7448ccab27d469d974964abf7b0d306ff` |
| NCT07542535 | protocol/SAP target duplication | 5 / 3 | `30049283e8456dad0f039f87f129dea36e88bda44b3339c0987daf91d278c702` | `7ab3d457dc1797a41bc49ce3d7a779f7e72f468b4658fe3669a00b8ea7d200ed` |

## Review gate

No Batch 50 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
