# Expert Review Packet — Batch 76

## Scope

Batch 76 reviewed eight ClinicalTrials.gov document families. None passed the public, prospective, version-matched, independent-hidden-target gate. Five model-visible protocols expose executable analyses and also have a post-completion, termination-informed or governing-version defect. Three remaining families use execution-updated summaries, an internal procedure guide, or retrospective analysis notes instead of clean prospective governing protocol/SAP pairs. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. Full-page OCR was performed for the scan-only NCT03052530 SAP and the sparse-text NCT04089735 protocol.

## Decisions

- NCT03052530 — protocol pages 7 and 24 expose the 60-subject, descriptive-only, ITT/per-protocol design; the matching SAP is post-completion.
- NCT04737330 — protocol pages 81-87 expose populations, estimands, regression, multiplicity, missingness, sensitivity, MMRM, safety and power; SAP pages 2 and 22 replace inference with descriptive analysis after premature termination.
- NCT03797157 — protocol pages 7, 19-20 and 36-37 expose the executable primary, secondary, interim and sample-size plan; the SAP cites Protocol 2018/Version 1 rather than selected Protocol 2020/Version 4.
- NCT04400214 — the selected six-page protocol is an execution-stage pandemic-modified summary, and the analysis file retrospectively says planned tests were impossible because recruitment was insufficient.
- NCT03386110 — the selected protocol says it is an internal Study Procedure Guide, not an IRB protocol, and contains post-COVID operational changes; the post-completion two-page analysis plan reports methods used in past tense.
- NCT04089735 — protocol pages 39 and 99-102 expose populations, tests, endpoints, rescue/LOCF, sample size and no-interim rule; the SAP is post-completion.
- NCT02425644 — protocol pages 187-208 expose sets, multiplicity, negative-binomial analysis, missingness, sensitivity, secondary models and power; the post-completion SAP adds updated MI and conduct changes.
- NCT01794520 — protocol pages 152-160 expose populations, PK, response hypotheses, Hochberg, censoring, Kaplan-Meier, safety and sample size; the selected SAP is post-completion and revises censoring/population rules.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03052530 | protocol leakage plus post-completion SAP | 32 / 37 | 895fa172b4fc7ce5f2c8826eda2b5b8c222512741c8921b571004e24252b6356 | 0c88b65ae50583011ae4335279efb4f661a127b4621a3f49f397fc1e3a3f05b7 |
| NCT04737330 | protocol leakage plus termination-informed SAP | 99 / 27 | a9354593f06dc5b37273716c6ebcc86eccef3079226f3ed3b32f1be4e7988d94 | 3eb3a6dd1223a3220dd06b6d84cc1be550d558eb4f25f6202938c1b6705c0969 |
| NCT03797157 | protocol leakage plus governing-version mismatch | 63 / 32 | 5a903aae8ebacceabbacd003529f269c709649da5dfdf428721488b0fc3d59a3 | 86d5c41c0961761e171f4ccb10777de80c27698fbfee1c9ffd9d4a4508bba07c |
| NCT04400214 | execution-informed wrong document types | 6 / 6 | 3a6292e4e1095e24816a8065daf6dcb79bf0e7e6d00ce0253fe8bf62799f5e92 | 28e64117c58c45d454cdfdf9a1e113066b7a7b67c0d4a3e7f958909b4ec33f74 |
| NCT03386110 | internal procedure guide plus post-completion analysis note | 23 / 2 | 4093120890008cfbb22a05a9873eec0111e46527b0d470d198d40565239af60b | 6a8b865c48f58bdf1e24f33083afe74054455f95785c831704f679b61b98dea1 |
| NCT04089735 | protocol leakage plus post-completion SAP | 108 / 40 | 6d24ae10796dd036b7628e7bd0ccb0ba0a5d1597c40ed198b835576376e94781 | ede0d41db0a97a9fcfe3a52a1f890ee04018da4f64d06edf1e25c5a29137da2b |
| NCT02425644 | protocol leakage plus post-completion SAP | 376 / 183 | c8fa3782e073e32a90124d6710640c4ce640c33e9b8058d6a18eee01d2f6d786 | a71bd51bcb93c06f4df1fd12f60874c31aae6b33dd5777e9cdd519fd8f8bca6d |
| NCT01794520 | protocol leakage plus post-completion SAP | 195 / 75 | 4c5ea45311a9e1efe9c6779d55a6f20a679c8951f3e2b35cec58940aae7f31eb | 6011fa384ed59ac5cee1e40017baafa217e63844e1809ac60b6cec894bf12c73 |

## Review gate

None of these eight families may enter train/dev/test. NCT03052530, NCT04737330, NCT03797157, NCT04089735, NCT02425644 and NCT01794520 fail prompt/reference independence through executable protocol leakage and also have chronology, execution-stage or version defects. NCT04400214 and NCT03386110 fail prospective-document provenance. Batch 76 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
