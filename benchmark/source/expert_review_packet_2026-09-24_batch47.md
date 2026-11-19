# Expert Review Packet — Batch 47

## Scope

Batch 47 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent prospective-target gate: six protocols disclose executable target analyses, while two selected packages contain a post-completion analysis document or the wrong protocol document type. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining statistical pages.

## Exclusions

- `NCT01629862` — both Protocol Version 27 and the two-page analysis note postdate actual study completion, so the package is not a prospective governing pair.
- `NCT02818998` — protocol pages 7 and 48-54 expose analysis sets, noninferiority margin, Hochberg, ANCOVA, missing-data sensitivity analyses, sample size and the no-interim rule; SAP Version 4.0 cites that protocol.
- `NCT04618315` — the protocol slot contains a Manual of Operations, while the post-completion analysis plan reports actual group counts, attrition and analyses performed.
- `NCT04784455` — the public protocol covers Parts A and B but the SAP covers Part A under an earlier protocol version; protocol pages 52-55 also expose power, analysis sets, exact-binomial/Kaplan-Meier methods and the interim boundary.
- `NCT03845517` — post-completion SAP Version 5 incorporates blinded-data-review changes; protocol pages 156-161 independently expose estimands, gatekeeping, populations, sample size and primary/secondary methods.
- `NCT02778204` — protocol pages 49, 52, 55 and 59 expose accrual/sample size, dosing and safety algorithms, confidence intervals, primary/secondary analyses and PK methods.
- `NCT02706951` — protocol pages 15, 114, 117-119 and 124 expose analysis populations, CMH/ANCOVA, missing-data rules, graphical multiplicity and power/sample size.
- `NCT05529706` — protocol pages 19-20 reproduce the sample-size rationale, NPS formula and success/attendance/continuation thresholds, and page 29 adds safety-interim wording.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01629862 | post-completion protocol and analysis note | 19 / 2 | `d4cd058ff1936a27a704b66e00e05f85021c90a167d185060957374c493ec449` | `e635d3923b459952230b713eb83b871e6b51126a77b8d4d0970a83f92398afc1` |
| NCT02818998 | protocol leakage | 75 / 43 | `347e8c958d7b54e40e4e94f196ec36073b38d3a3d49f34fb62dfd98eafeb4dee` | `ee2222dd37a4c105c3fadc394738f707f3510155270b6cc05356a3f6be75e086` |
| NCT04618315 | MOP plus execution-informed analysis plan | 124 / 6 | `f761b762c70c8456963b09967c5de4f52904ce8e5789911c0447ca4056b292f6` | `72903df10dbdf19415adc35d0bb70dbe2519bcd98caf57562ff4ac9d22f53961` |
| NCT04784455 | scope/version mismatch plus protocol leakage | 85 / 19 | `ee85988ed0ead73542146d721e5c6c6e3fd53a31a264cf72ceb707d2ecedfc69` | `02d7bd29f689420d27d52bbaf6392c7d7ba95c724497071c5b892493c2de3965` |
| NCT03845517 | execution-informed SAP plus protocol leakage | 228 / 86 | `0278b3c10bcdf059c3999cff1bf5b04cb087cb12830126c89d43284e0ced0606` | `432fdb5dd6930b58377f83dcdbc8f1802377e56c6018fd7292605769ac7013a0` |
| NCT02778204 | protocol leakage | 94 / 22 | `c0b888a2fc8575d68011ee0516d942020797ed809195e0dd1200f5b2c4d165a8` | `6960480863aee3ce7b790ecf6424b1489f008bd597fba1861332a29cf3f06f99` |
| NCT02706951 | protocol leakage | 177 / 88 | `df1df836ad2ec87831c9964327860d7a0bd677b0ef43ffa755266c8e9bde6325` | `57f27b4a44deb44f31041ca83355c3e5899d0647a2df56e14ebdafa612633b1e` |
| NCT05529706 | protocol leakage | 38 / 3 | `81dc12576da0062610c97b6d64ff98f9d7a31ec443dfcd55e98ef01dd7a39ff3` | `18b407cdff8da2533d78fdcb65a3e99cc42c3b62d430844fae0f8d006400c` |

## Review gate

These eight candidates cannot enter train/dev/test. All eight slots must be replenished; no Batch 47 record is counted as a completed benchmark question.
