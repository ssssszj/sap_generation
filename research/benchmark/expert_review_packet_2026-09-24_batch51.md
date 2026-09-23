# Expert Review Packet — Batch 51

## Scope

Batch 51 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent prospective-target gate: all eight model-visible protocols expose executable target analysis content, and five selected document chains also have post-primary/completion or execution-informed defects. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages.

## Exclusions

- NCT02419508 — protocol pages 10-12 and 48-54 expose analysis sets, eye selection, repeated-measures model, closed testing, missingness and power; SAP is post-completion.
- NCT03066830 — protocol pages 9-10 and 79-88 expose ITT, ANCOVA, multiple imputation, hierarchy, sample size and interim rules; SAP v3 is post-completion.
- NCT05882032 — protocol pages 45-48 expose all analysis sets, noncompartmental PK, log-ANCOVA, 90% confidence intervals, Wilcoxon analysis and sample-size rationale.
- NCT03407651 — protocol pages 72-75 expose hypotheses, modified populations, primary test, historical comparison, missingness and sample size.
- NCT04145219 — protocol pages 81-86 expose transformed LME/MMRM, inference, hierarchy, control-based imputation and power; SAP is post-completion.
- NCT02858401 — protocol pages 79-83 expose all analysis sets, BLQ, efficacy/safety/PK summaries, interim access and sample-size basis; SAP is post-completion.
- NCT02946073 — protocol pages 79-82 expose populations, primary and secondary models, missingness/censoring, PK/safety and power; SAP is post-primary-completion.
- NCT00351611 — protocol pages 2 and 46-48 expose exact noninferiority, ANCOVA, missingness and observed-data-based power; both protocol Amendment 5 and SAP v5 are post-completion and execution-informed.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02419508 | protocol leakage + post-completion SAP | 67 / 26 | f0e24fcea5c0f7718d178ab67027c43b1a92c8ea898ce0d9d19dce708b66ed42 | 48007ca23e922a6c537c8c64321e978f1e322673baf969c5db64b17b205326ba |
| NCT03066830 | protocol leakage + post-completion SAP | 114 / 82 | a28fc2831a6841a1fc2b882f1499ba9abe3978d76c786f47b9c94435aae1b1fb | 13483f73e0f9fcf07ff47c4852e2511d299d669f4c49404a2c2a3f54f0a678bd |
| NCT05882032 | protocol leakage | 83 / 23 | 5d4b27da59d6549f8a60fddccae43e4c96d290ebac3e948247d29c67f1ff9b1b | d4c6a6d43a95cbf28059562ba874c31ff83945da00041620f374aee3254c3698 |
| NCT03407651 | protocol leakage | 116 / 79 | da1ae2b54efb349975fa31552f24d9eeeab69245317d1e0aec5b03da1e280194 | 3c7207ef1b2c7c2726f86dc8c1869e1631de0a742504ed620864bfbad2052557 |
| NCT04145219 | protocol leakage + post-completion SAP | 99 / 50 | e8f23fcf4e3546396a81487f62fcf5218b3a204b245c52746036b7c8d336a5d7 | f94ec3f78b4da5e996779248fcd0fbb1ff12b9a3a6b19ccf636eacfd2976b0a1 |
| NCT02858401 | protocol leakage + post-completion SAP | 132 / 52 | e732b514c3e17f7293ed198f4b7fdd6f0bf2bfc05b25d694b3b49da4c8e36902 | 1c5290f9dd270ae6426836d237b3349f2e7859cc3b59ee04d38279b7ce30aa07 |
| NCT02946073 | protocol leakage + post-primary SAP | 99 / 23 | 712893106a33464411ee5311170e62140b5a713ed194b646a73cf47c0c07ce06 | 4a871fd7f9066c38500e6f87be9581bdb857e72d0d309e087c9331bfeeadc568 |
| NCT00351611 | protocol leakage + post-completion execution-informed chain | 88 / 37 | 60e1399b482b07a9ad18228e1dd8410d741be6cf2330c343b4aa6ed0b001f5dc | c594ad194cdc8574405bf02e3512e71c337dc392f803212c1147ecc6265f95e8 |

## Review gate

No Batch 51 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
