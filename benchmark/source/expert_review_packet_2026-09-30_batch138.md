# Expert Review Packet: Batch 138

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 138 review-queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,326 physical pages. Every native-text page was extracted; the scan-heavy NCT04566666 files were OCRed sufficiently to verify all decision-defining pages. A total of 159 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. Seven pairs were excluded, one was placed on version-reconciliation hold and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT03016975 — exclude: protocol pages 68-79 expose the co-primary hypotheses, Finkelstein-Schoenfeld hierarchy, populations, survival, missingness, multiplicity, interim and sample-size program; the short SAP repeats it and adds conditional-power re-estimation.
- NCT03548987 — exclude: both selected files postdate primary and study completion, and the bundled protocol exposes analysis sets, power, hierarchy, ANCOVA and imputation/sensitivity methods.
- NCT05816473 — hold: the files share the exact NCT and Yale IRB protocol number and the SAP precedes primary completion, but it was approved during recruitment without a revision chain. The protocol's population, N=102 and 3x2x2 mixed-model plan conflict materially with the SAP's medical-student inclusion, N=104 and two-arm Mann-Whitney analysis.
- NCT04566666 — exclude: the during-conduct protocol records completed unblinded PK analyses and exposes the target program; the final SAP postdates primary completion.
- NCT02833844 — exclude: the prospective SAP is substantially reconstructable from protocol pages 52-57, which disclose populations, sample size, hierarchy, Hochberg adjustment, repeated-measures and CMH analyses, missingness and safety.
- NCT02969525 — exclude: the protocol and SAP are post-primary/post-completion; the SAP records changes made after the Week 48 interim, and the protocol exposes the executable target.
- NCT02378844 — exclude: the SAP identifies governing Protocol Version 2 while the selected prompt is Version 3, whose pages 56 and 58-61 already expose the analyses, missingness, sample size and interim program.
- NCT02489448 — exclude: the protocol/SAP package incorporates years of conduct, including realized accrual, and the seven-page SAP effectively duplicates the protocol's complete statistical section.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03016975 | protocol-embedded target leakage | 113 / 18 | `6b9fad4dde3093ff6bf099c1ff4694c168dfd3b24d4273556d3bb2d9af5dd9a0` | `28b2d6224187736362e934e6288a7e30dbfc94d5125426b90ac63681b3e6ea20` |
| NCT03548987 | post-completion target plus protocol leakage | 115 / 33 | `a4c3af49d70637b07bf31a9bc6ce51a9825a04611e59857c5ae7a7172f754f12` | `27756275d7b23f0dc11e9eb7a9adc94e440dadced3ee5a215c1c0c24f1789473` |
| NCT05816473 | prospective/version governance unresolved | 4 / 3 | `abc7e02416cba11498a14475f999dbf7df52c7dab37fe2664c60233c92fc74d9` | `12dd581ba82bd6d6a9da9aa818a3c8afd5eaf8de9e59c1f77bcc994599a26fac` |
| NCT04566666 | conduct-informed/post-primary target plus leakage | 152 / 66 | `bce68ddab6cd6528523ccb64c12de5e99421ee4baae9d0dc7d4704f2507e4431` | `61efa6baa0dfca1912160dc0a8b356aafe986eb9cea80caded66298c99329916` |
| NCT02833844 | protocol-embedded target leakage | 93 / 35 | `55dfecde7df9d471b693a59a8fc6b0d4225d770c5d7a0e558a566fdd6b7160e6` | `0e00329ab67dd751888e60efe0f5077d27c5080ccfa27ec784a240b060e62cc5` |
| NCT02969525 | post-primary/interim-informed target plus leakage | 131 / 183 | `04a23d40e8c0235fb79f1c691c9c7671d968027dd43ccc26d42680b866a83837` | `183ed8498625382f4c0b7e7d728a9eab82a4eb2379e171c1012064406174c9a2` |
| NCT02378844 | governing-version mismatch plus protocol leakage | 75 / 27 | `f9926dbccc28cd6239d2dcb34a3eee0b4fd8595604acd8ccb4a4efe285201699` | `aca3f7086dc78b4402c9541547c0b8650c2b3a778899291f7128574838f0b871` |
| NCT02489448 | execution-informed duplicated target | 118 / 7 | `460167fef8688a16d0b5bd4f35dd65144e7486d9b85bc9aa1d63b6d0dba19ca8` | `d9ba678bb65c704e949f945b6fdab878da98b7ed69575ce46324193566ebf809` |

## Gate interpretation

- A pre-primary SAP date is necessary but not sufficient. NCT05816473 lacks a public revision chain capable of reconciling material protocol-to-SAP design, population, sample-size and method differences, so it is held rather than guessed.
- Protocol disclosure of design, endpoints and sample size alone is permitted. The other seven prompts fail because they additionally disclose populations, executable models/tests, missingness, multiplicity, interim decisions or nearly the complete short target.
- Documents produced after primary completion, or changed in response to actual accrual, interim discovery, unblinded analysis or termination, cannot serve as clean prospective hidden targets.
- Registry actual enrollment was used only as conduct context and was never substituted for a prospective target.

## Replenishment

All eight excluded or held slots are replenished from the official API. The release-eligible intake remains 120: 105 public first-pass drafts and 15 actionable metadata candidates.
