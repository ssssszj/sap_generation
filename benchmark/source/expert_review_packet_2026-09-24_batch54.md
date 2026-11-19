# Expert Review Packet — Batch 54

## Scope

Batch 54 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed all prospective-version, identity and independent-target gates: every model-visible protocol exposes executable target analysis content, six document chains have additional post-primary, post-completion or governing-version defects, and one SAP explicitly changes the design using already-observed DLTs. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. Visual review was used as the authoritative check for the malformed NCT02915302 SAP text layer and the sparse early NCT04211363 extraction.

## Decisions

- NCT02462486 — excluded: protocol pages 39-43 expose ITT/PP/safety sets, LOCF and multiple imputation, CMH noninferiority analysis and margin, MMRM/ANCOVA, sequential testing, sample size and interim intent; SAP is post-primary-completion.
- NCT03238963 — excluded: protocol pages 58-62 expose analysis sets, logistic and safety analyses, interim/missing-data rules and sample-size operating probabilities; SAP is post-completion.
- NCT00320606 — excluded: protocol pages 46-48 expose populations, exact intervals, Kaplan-Meier, repeated-measures, safety and sample-size rules; the public protocol is post-primary-completion and postdates the final SAP.
- NCT04211363 — excluded: protocol pages 53-56 expose populations, multiple imputation, primary CMH analysis, alpha partition and sample size; SAP is post-completion.
- NCT02915302 — excluded: protocol pages 64-68 expose noninferiority hypotheses and methods, analysis sets, missingness, interim intent and power; SAP is post-completion.
- NCT03002974 — excluded: protocol pages 60-70 contain extensive executable population, mixed-model, endpoint, sensitivity, subgroup, missingness, safety, multiplicity and sample-size rules; SAP is post-primary-completion.
- NCT00150800 — excluded: protocol pages 58-60 expose analysis populations, time windows, summary conventions, seizure and safety outputs, missing-day handling, exposure categories and interim snapshot intent.
- NCT02472977 — excluded: protocol pages 91-92 expose interim decision rules and response thresholds; SAP page 9 explicitly uses already-observed DLTs to remove randomization and one regimen.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02462486 | protocol leakage plus post-primary SAP | 84 / 41 | ef1393e340188841be16c274d3410960ce545ed0ca33e9de96de62a9a6ca657e | 824b3a7ed90d6b27fc502ef71f742252bd46e5cb4b19a78237e6996f9f339bf3 |
| NCT03238963 | protocol leakage plus post-completion SAP | 95 / 54 | 1a8c76dec1fac39d4e3ad21f50f00e35c999db1b5f0c34033b39364d5b74d1c3 | beb945878e36f002f01a840b8b05f352feb3678494c9193d4a743888890cc75d |
| NCT00320606 | protocol leakage plus non-governing chronology | 60 / 30 | 84bdb4f81466e6a3aad108f6b0ed86b90382106b2057d77443977aa91a43869f | 1206a55da66a2ef2a656d293dc9bcb1e8f663f68a0619cf9d71d4987c0e6ee96 |
| NCT04211363 | protocol leakage plus post-completion SAP | 87 / 42 | 8a6083122324344ec0fc73798fe01200ffbe89585fd78cdd7f0adcb908116623 | b17d7fd3ebe3cced8033fb75ec87ccca8e845eb6b543fb83160839b15fa0c6d6 |
| NCT02915302 | protocol leakage plus post-completion SAP | 73 / 36 | 461ae5c11e33b73265100c2d1f09b086540da77bdd720352736f4dfdafda45c4 | 67fcdabaac07307f24e8bd61882ec9e30c836ef26e8a6049eeeb328e104ca4b0 |
| NCT03002974 | protocol leakage plus post-primary SAP | 85 / 52 | 3a3d878334cf1babaf35493e65b4567b454196bfab6692f04205044d6ad76d0f | 4c24accf019c21c99209fdd33657a57a65addee3f9fea7644f2960f00585dba0 |
| NCT00150800 | protocol leakage | 72 / 46 | f4c39a6e54014c65465f8e1a996615ae4abfd801c09666d0cfa474b23f248f37 | a6a0b5cd0e50a28ef8d5acb271811226d93d813ae4821d0bcca7f4f10ebcfc64 |
| NCT02472977 | protocol leakage plus execution-informed SAP | 124 / 43 | 1871c34310b450228c2f628daa22145c3dcbd6a1fcf406b7763155f3b91617f1 | 770f8d0c2df07d681ec2dcff784ab179d506100d1e9c6e06c0eb0d03f141a23e |

## Review gate

No Batch 54 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
