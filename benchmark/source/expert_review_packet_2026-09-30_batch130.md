# Expert Review Packet: Batch 130

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 130 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,076 physical pages. Every page was text-extracted, and 98 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT02914457 — exclude: protocol physical pages 42-44 expose the executable analysis, and SAP physical page 9 records a conduct-driven increase in sample size.
- NCT03166124 — exclude: the amended protocol exposes the PK, gastric-dilatation and safety program, while SAP physical page 16 documents an unblinded interim and an observed-issue-driven change to nonparametric VAS analysis.
- NCT00790933 — exclude: the 2013 SAP is paired to a 2016 protocol amendment incorporating open-label data, DSMB unblinded safety data and realized infections; the protocol also exposes the target methods.
- NCT03075878 — exclude: the adaptive amendment uses ongoing study data and early efficacy to calibrate Cohort 2, the SAP is dated six days before primary completion, and the protocol exposes populations and PK/PD/safety methods.
- NCT02652624 — exclude: the SAP follows primary completion and records a completed IDMC analysis; the protocol exposes the noninferiority, population, missingness, power and analysis-schedule program.
- NCT02689063 — exclude: the SAP follows both primary and study completion, while the protocol exposes ANCOVA, pairwise, population, missingness and sample-size methods.
- NCT01224106 — exclude: the post-completion SAP and protocol incorporate a completed CSR, futility outcome, realized enrollment, treatment discontinuation and later OLE design.
- NCT01616875 — exclude: the seven-page SAP is essentially a duplicate extraction of the protocol statistical section.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02914457 | protocol leakage + conduct-informed sample size | 59 / 33 | `d8fbba2f1b5299e067a03ca0329d28c2b5a99278239011fc810cdee485fcd02f` | `50e5d35f44d8f759c64d474c35b8c296ae2da7ec16552debe463edafed595535` |
| NCT03166124 | execution-informed + protocol leakage | 64 / 18 | `e56091bf4d7059b9c4092618e2b7739159eca70d6801a7c94aed59a051e13948` | `613704727fe00916a9089b0234010cf09d078ecfae396cf45a1ce33a0643be17` |
| NCT00790933 | version mismatch + accumulated-conduct leakage | 123 / 62 | `b8313f2388534245e339cc0cc6b355f653cfd4309f7b5f258b88fe41b046a2e6` | `23b66ca203429c3ff0cc5b56a7230e5c13aa9963217764b2f4a8a577d7b9f0d0` |
| NCT03075878 | adaptive conduct-informed + leakage | 103 / 32 | `2fa056342981dd5c29f13c5f77768a3a16f146524ec1c63e06d348f2547e80ea` | `941ce940b3df7c9f9fa1302cfa19133b2b77b8e13ca7a636dd7cf476fed074c9` |
| NCT02652624 | post-primary + leakage | 122 / 93 | `dceb8b7aad601a0d89cff111e8ae054c230019037e336b8935f06fa44d010084` | `682a905776d3885bcb5d39269c5315c49aef1695be0799e15249785dca035e81` |
| NCT02689063 | post-completion + leakage | 50 / 16 | `64852204396d1f910669f2b7a3526e366254209b2c8a6d39b9678478ef121ecb` | `abf0c92238c1cd5f0ae522a565639ec5ed4206c8c4b13cd16bc0f91a0135740e` |
| NCT01224106 | post-completion and outcome-informed | 160 / 71 | `5a439ac3fe6bc83717d2b25391327a818504ecb642dd42a755fa5defbea9b5ad` | `5b8fa44a33190eb7db36336b53306cc8409720c2f2cfc0588cbee453b326886a` |
| NCT01616875 | duplicate protocol/SAP content | 63 / 7 | `033c381c8006dad6e2441c9eee58508d8e67be12bbebf0ee1b568fbeb459aa05` | `090e6dd3b61c85e8c7d1f55f85a3386ef0d5c95956675403daa549ea00ceeb57` |

## Gate interpretation

- Near-primary timing did not establish prospective governance for NCT03075878 or NCT02652624 where the documents themselves reveal accumulated-conduct or completed-interim information.
- Matching protocol/SAP dates did not rescue NCT01616875 because the alleged hidden reference is only a duplicate extraction of model-visible content.
- Registry actual enrollment was used only to assess conduct chronology and was never substituted for a prospective sample-size target.

## Replenishment

All eight excluded slots were replenished from the official API. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates.
