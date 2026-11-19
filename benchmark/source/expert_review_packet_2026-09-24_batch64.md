# Expert Review Packet — Batch 64

## Scope

Batch 64 reviewed eight ClinicalTrials.gov protocol/SAP families. No family passed the prospective, version-matched, independent-hidden-target gate. Five model-visible protocols expose executable target analyses and have post-primary or post-completion analysis files; one selected file is only a one-page post-completion methods note. Two otherwise potentially useful families remain on hold because the public files cannot establish the governing prospective version. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. The scan-only NCT06584435 protocol and SAP were fully OCRed before review.

## Exclusions

- NCT02656329 — protocol pages 54-61 expose populations, event-driven noninferiority Cox analysis, margin, alpha, missingness, sensitivity, hierarchy, interim rules and sample size; SAP is post-completion.
- NCT04039503 — protocol pages 70-75 expose estimands, analysis sets, MMRM and covariance, survival/binary/count models, imputation, safety and PK/PD methods; SAP is post-completion.
- NCT05073458 — protocol pages 77-80 expose enrollment-closure context, populations, CMH and sensitivity analyses, gatekeeping, safety and no-interim rule; SAP is post-primary-completion.
- NCT03086655 — the one-page 2023-12-22 analysis note follows 2023-01-11 completion, describes illustrative underpowered analyses and supplies no prospective SAP version chain.
- NCT03454555 — protocol pages 48-53 expose the primary mixed model, correlation, populations, missing-data sensitivity, multiplicity and other analyses; SAP was finalized two days after completion and records late analysis changes.
- NCT02605174 — protocol pages 43-51 expose populations, alpha, logistic primary method, imputation, gatekeeping and safety; the selected late file is internally an Output Templates package rather than a governing SAP.

## Holds

- NCT03201445 — SAP Version 1.0 is based on Protocol Amendment 4 dated 2020-03-18, but the public prompt is Amendment 6 dated 2022-09-09 after IA2 and disclosure of completed-participant treatment assignments. Hold until the actual governing Amendment 4 prompt is available.
- NCT06584435 — the files claim 2022-10-01 but were uploaded in December 2025 after primary completion; the registry record first appeared in 2024, the covers already carry NCT06584435, and the compact SAP cannot be reconciled with the protocol's descriptive-only statement. Hold until immutable pre-analysis provenance or a contemporaneous source is available.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02656329 | protocol leakage plus post-completion SAP | 108 / 28 | 4f960da819f10bdb0c4534833e35bac256d66c1f93488eb84544881194b9ce25 | 4950cb615fe9a99bad46b3ba256711972ad9a758b1dc3fa8fe4bfd74eaa21947 |
| NCT04039503 | protocol leakage plus post-completion SAP | 100 / 50 | 497063aab2c36081111eebf93bbc4ab220c4bdb325144d916f0b493bde2e1973 | fc5f0a99b81c9cdea9791e160651bc80ff9228c016b5c548c8c8b73d9aad5253 |
| NCT03201445 | governing-version hold | 123 / 75 | 4bc298c900f951e326415244ab3d27f6dd7e3d2fdba809db52e613a972cceca7 | 3ada25bfac202901e1c83cf430d0126e9a9b5a27c78afe4a24f3052a291842e4 |
| NCT05073458 | protocol leakage plus post-primary SAP | 119 / 25 | e664b1c33967ba7e2b6393387283dd0604443910cfcac3921e006574f74aeae4 | 0e10e635d3f5eb007ee8d60c6080d78ca0905c85ba1ec49d7affff80871f0844 |
| NCT03086655 | post-completion methods note | 45 / 1 | 0522e0b290197c73919ccd905caeb4ecb56da694883d22e8de02671cbf38ff01 | 086f4b49de1476637301bdbc2bed51ca3a519c09c5033501b688a4812974c89b |
| NCT03454555 | protocol leakage plus post-completion SAP | 81 / 39 | 99fb6fb94214d1487af7a1eff0a24a4860528e0f2856e8fb1f5ea82cb20da06c | a2245833069723c2b7a053fb31481f83cc63f0fc6ca7a330e16ea3a0a7e716fb |
| NCT02605174 | protocol leakage plus wrong late document | 76 / 51 | 1f98d3b86d98e190088bf80cccb9746d81616ea985482f73e820f51746235781 | c4da659a3e6a4346de5e002a235e8ec86c49389ccdef6e7ef1d60aa2572da471 |
| NCT06584435 | prospective-provenance hold | 9 / 5 | 45109f3d153654037239b122ac6650c64e98b2e82659736a8098a12f511b5bef | 3c34eb731213dcab622d1962629f68988d27fcc82489620375b1f5625039d7d7 |

## Review gate

None of these eight families may enter train/dev/test. The two held families require external contemporaneous version evidence before reconsideration; the six excluded families remain outside the actionable pool. Batch 64 preserves 72 registered public drafts and replenishes the actionable metadata pool to 48.
