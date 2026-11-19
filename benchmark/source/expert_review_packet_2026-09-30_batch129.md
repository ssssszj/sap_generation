# Expert Review Packet: Batch 129

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 129 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,647 physical pages. Every page was text-extracted; the scan-only 106-page protocol and 32-page SAP for NCT02687451 were fully OCRed; and 66 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT02906579 — exclude: the SAP follows completion and protocol physical pages 57-59 already expose the descriptive PD, endothelial, platelet, safety and PK program.
- NCT03164928 — exclude: the selected protocol and SAP are post-primary; Amendment 3 records realized recruitment of only 24 patients versus 150 planned and the SAP adds later endpoint and sensitivity changes.
- NCT06106022 — exclude: the SAP follows completion and protocol physical pages 59-60 expose sample size, populations, PK/PD/safety methods and interim popPK logic.
- NCT03607422 — exclude: both selected Measure Up 2 documents are post-primary, with the SAP finalized more than four years after primary completion.
- NCT02628444 — exclude: protocol physical pages 110-120 expose the staged noninferiority/superiority hierarchy, tests, margins, multiplicity, populations, missingness, safety and power program; physical page 81 records planned unblinded analyses.
- NCT02687451 — exclude: the post-completion SAP states that the study terminated early and defines an abbreviated CSR with safety only and no efficacy or PK analyses.
- NCT00938912 — exclude: the selected late protocol and SAP amendments follow more than a decade of conduct, revise cohorts, exposure intervals, termination mapping and analysis rules, and expose the executable program.
- NCT01593254 — exclude: both selected documents are dated after primary completion and cannot establish outcome-uninformed prospective governance.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02906579 | post-completion + leakage | 74 / 33 | `d5bf565fc43c8275c6d49572a0854b5f724d8cf671e1a32d17f1d12736bff62f` | `2dcfa9311246e395f0d129c71f61635d276619b9ac439ed301dedbb3c92ccf4c` |
| NCT03164928 | post-primary package | 100 / 64 | `9df07d711b314da1a60f2a158e2a6bd7bd368bdfbeee82af945ecaff64eb040f` | `fc00500add9e9b454bcd5b43ab229cec50a72e0b96e945a3b5bcefdff66e076f` |
| NCT06106022 | post-completion + leakage | 129 / 29 | `4c83590a0aecc361e33ecf5bffe19a7573a2d828c110e012e6f1ddc17694ec79` | `5f38a7bdda04b7934d38c805999bcd0c4e91c6686d08a6d6042f222ebc04409a` |
| NCT03607422 | post-primary package | 145 / 114 | `ee32aa64877daffeec2d7c8ac42953c53b1f380ea2c14004d22c80eba69dcd95` | `206fcb4574833a3e0e12bd915e9289edef20b6a37a4c44fa80fcf3b7a17a3016` |
| NCT02628444 | protocol leakage | 127 / 53 | `f2bdb9b4079d880c55832fbcc5537e57d36d9b79403527efc1831e29c83e68a2` | `54dd6f061d52f6f19f118373bff78b994d870bbcd68292ac5fc6c5e3d7feeabd` |
| NCT02687451 | termination-informed abbreviated CSR | 106 / 32 | `cd124379a721a9330cd0d4e1a6e1513ab18ac4ded29aafd485e7eca4098d6b66` | `51413d54c5d65693fd1363d4638b4583696759f929cae39193d59b72bf757de5` |
| NCT00938912 | accumulated-conduct-informed + leakage | 325 / 148 | `15d52025e4ef6855c53f15eae1cc40dfc7cc0232d464739e05caef4a76c9b76c` | `e0a5209e507d36f61d303268373c8531960eab151ebe07aa88ef12a91c45a122` |
| NCT01593254 | post-primary package | 134 / 34 | `d38b72455b8d521d869655b6d575724eee15a8846ff9b50882bca0fa8c302421` | `bc99594d0028cbfa2fee44e90f9c2e20510cd5e66bcec38ea9319322695e8d06` |

## Gate interpretation

- A pre-completion SAP date did not rescue NCT02628444 because the model-visible protocol already contains the executable target program.
- A matching protocol/SAP date did not rescue NCT01593254 where both selected documents follow primary completion.
- NCT02687451 was evaluated against the intended protocol target, not accepted merely because the uploaded file is labeled SAP; its own text limits the work to a termination-informed abbreviated safety CSR.
- Registry actual enrollment was used only as evidence that an amendment incorporated realized conduct and was never substituted for a prospective sample-size target.

## Replenishment

All eight excluded slots are to be replenished from the official API. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates.
