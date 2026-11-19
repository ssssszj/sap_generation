# Expert Review Packet — Batch 77

## Scope

Batch 77 reviewed eight ClinicalTrials.gov document families. None passed the public, prospective, version-matched, independent-hidden-target gate. Seven model-visible protocols expose executable target analyses and also have post-primary/post-completion, execution-informed or governing-version defects. The remaining family pairs an IRB modification/consent package with a retrospective two-page account of analyses already carried out. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology, version and decision-defining pages. Full-page OCR was performed for the scan-only NCT02910089 and NCT04753034 protocols.

## Decisions

- NCT03078907 — protocol pages 74-79 expose analysis sets, ANCOVA/repeated-measures methods, missingness, multiplicity, interim and sample-size rules; post-completion SAP page 74 records revisions from actual enrollment and blinded data.
- NCT02910089 — protocol pages 14, 24, 30 and 32-36 expose regression/prediction methods, ITT and power; the post-completion SAP reports the actual 1,400 randomized subjects.
- NCT04665271 — the selected protocol is an IRB modification/consent package; the post-completion two-page analysis narrative reports already executed tests, observed MNAR dropout and unequal groups.
- NCT04753034 — protocol pages 39-43 expose sets, MMRM, ANCOVA, imputation, GLMM, Kaplan-Meier and multiplicity/interim rules; the post-completion SAP drops Kaplan-Meier because of the observed small sample.
- NCT03400163 — protocol pages 64-67 expose populations, hepatic-fat analysis, power, confidence intervals, multiplicity and interim analysis; the SAP is post-completion.
- NCT04108468 — protocol pages 69-71 expose the executable primary and secondary models, imputation and sample size; post-completion SAP pages 3-5 explicitly record final-data review and post-unblinding additions.
- NCT03179891 — protocol pages 43 and 64-68 expose the PK analysis and period comparison; the post-primary SAP cites unavailable Protocol v2.7 rather than selected v3.3.
- NCT01915498 — protocol pages 18-19 expose FAS, exact-binomial analysis and the 42-of-125 success threshold; the post-primary SAP cites a different v8.0 date and reports already-undertaken interim analyses.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03078907 | protocol leakage plus post-completion execution-informed SAP | 105 / 74 | 59b85196df5a5eb33be87fbc351623919f41504bc43d55e77cc2f00d93c5f4f6 | 645931893266e00d8ec0754e60f46ce3c14e3083aea858122d1bca4619ab5cfa |
| NCT02910089 | protocol leakage plus actual-enrollment post-completion SAP | 47 / 16 | 73a3e5922baad3d488484546aba46f149783f8d727776eddb8fc654d790065ad | 310e427c4b7a4d102ba17e0d770077746c44ba28a440cdfb0a2e46c610255fe9 |
| NCT04665271 | IRB modification package plus retrospective analysis narrative | 16 / 2 | 382b0f804cdb3dfcbebc4b4eee772ea1fc5a545531ce03ed5d6f1d6a7c2aa9f4 | 7db5468f1b24f907aca93853ef89b618a43ec11928c0cca8bfb15b55b97e1cb4 |
| NCT04753034 | protocol leakage plus post-completion execution-informed SAP | 69 / 28 | 67a1ab10c9b5812ef638c0fec6bcce720dbce648d31baf7104e53ee97eb564d0 | 2ace3508a2fe65cc297f6f22062d01fd17d0e4fce41d11aa81bb4372ee88a45a |
| NCT03400163 | protocol leakage plus post-completion SAP | 85 / 27 | bfe6545986cc0b4939bdf1e11f35f7ae00a4db3cf38da31a5d6fc02f347ba29a | d6d704e2b8ed135cce8cadb670b447c84e6954ce93059bbf612805a89d93029c |
| NCT04108468 | protocol leakage plus post-unblinding SAP | 98 / 55 | cbbdbd2f9b431a2ee41858432c87a8ddcbf6b7a2cdcd00795e03abbff0f164f6 | aa51b4c11402c210fe400116456c4132ef132c01f51d2840081cb2d613183f6b |
| NCT03179891 | protocol leakage plus post-primary governing-version mismatch | 73 / 29 | e70f2449b3d495455fb07b9f34bf0f1b7b891f04feaf34d30d6f7c02284f9aa7 | 9c80cfd6b8e149d9efeda62d12143af6a816d76bac21fbd547b505db54ff04f1 |
| NCT01915498 | protocol leakage plus post-primary execution/version defects | 156 / 72 | 3c75811e46f36012eec18985c5b606dd4ef3dcc707c0ac39e0140d7a45581043 | b8942802b872083abe1d9fd8871de8e47f5f24fb5b7ee0b20a34417eed7cec26 |

## Review gate

None of these eight families may enter train/dev/test. NCT03078907, NCT02910089, NCT04753034, NCT03400163, NCT04108468, NCT03179891 and NCT01915498 fail prompt/reference independence through executable protocol leakage and also have chronology, execution-stage or version defects. NCT04665271 fails prospective-document provenance. Batch 77 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
