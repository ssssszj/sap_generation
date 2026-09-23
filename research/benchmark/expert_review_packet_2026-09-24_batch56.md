# Expert Review Packet — Batch 56

## Scope

Batch 56 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent-target gate: seven model-visible protocols expose executable statistical methods, while NCT02202551 additionally pairs the target protocol with an integrated multi-study safety plan rather than a study-level SAP. Five families have further retrospective, post-completion or governing-version defects. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. Visual review confirmed the content of the character-encoded NCT03335371 protocol.

## Decisions

- NCT02508116 — excluded: protocol pages 11-13 expose models, subgroup/economic analyses and sample-size calculations; SAP pages 1 and 3 explicitly say it was drafted after completion and describe already-performed analyses.
- NCT03335371 — excluded: protocol pages 116-121 expose analysis sets, alpha allocation, ANCOVA, missing-data sensitivity analyses, safety and interim methods.
- NCT01680640 — excluded: protocol pages 34-38 expose power, randomization, regression, populations, missingness and sensitivity analyses; the SAP predates the public protocol without identifying its governing version.
- NCT04399837 — excluded: protocol pages 103-105 and 126-129 expose MCPMod, Cox/log-rank/CMH models, closed multiplicity, hypotheses and simulation-based power; final TSAP is post-completion.
- NCT02955797 — excluded: protocol pages 68-73 expose noninferiority hypotheses, interval methods, populations and data handling; SAP is post-completion.
- NCT03056690 — excluded: protocol pages 67-75 expose power, populations, MMRM, multiple-imputation and other sensitivity methods, interim analyses and missingness; SAP is post-completion.
- NCT02202551 — excluded: protocol pages 5 and 56-57 expose analysis populations and methods, and the selected analysis plan integrates three studies for a regulatory safety summary rather than governing only the target study.
- NCT02526017 — excluded: protocol pages 129-135 expose populations, efficacy, survival, safety, PK, immunogenicity and interim-summary methods; SAP is post-completion.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02508116 | protocol leakage plus retrospective SAP | 29 / 7 | f57e6abeacac27a1be38baa1276e551439b4564970c0986b6c0a7405ad87424f | 1be4cb2e8695f31a6f804c0576c769e4540a934da67a06d6eca168bf682f417f |
| NCT03335371 | protocol leakage | 129 / 58 | 73186f013b10d51246fc6d8228e499d1f4ec59f96ce89942cd7ad31b1fa0fbaf | 9a9de900265886b9408f23e4caf06fbae59b930b07668f1323e8099f02c1db41 |
| NCT01680640 | protocol leakage plus version defect | 46 / 18 | 290bd2f46945a7126ec18ae429477246c7ad2964721fb72f83de29918a18bb1c | 045925cbee456077773023b4ba63197d3a1b5c920a1c068322bf2459bd0eb960 |
| NCT04399837 | protocol leakage plus post-completion SAP | 196 / 84 | f074c44965bccab0b43ad78bdd2f0c542e7924b39852db300ac5f00692c6d86c | 33d75a6990d4eeb190f07b50fb3e220e6a5c16fdb3af9d02c0be57648aa64d8d |
| NCT02955797 | protocol leakage plus post-completion SAP | 81 / 29 | ed8e85435c6987826f7f7c09fbe58f5fcdb5e2777cecb88516d929cd0d170e65 | 9fa52baa7d7f6d4370397e1529a2739cd5d296b983eb2d7827a655e2c0a2a9fd |
| NCT03056690 | protocol leakage plus post-completion SAP | 103 / 95 | 948774f69c18dd900c8869364218e1a09b3c83dc153e03bda9a26a8e1f25dba0 | d41821ea548396155b84d082e437edbe2030e4116507304dd36eb774dbe60b63 |
| NCT02202551 | protocol leakage plus wrong-scope multi-study SAP | 67 / 141 | b2a6a687b78f32e548a932e15a070196e7a86d43dce769ede46f41ae5044cd99 | cc2708d6b047f7f2378a4947cba6bc5f6039d0ea60c40bd23da95d531b6aa0bc |
| NCT02526017 | protocol leakage plus post-completion SAP | 176 / 49 | 447b52f9caca5155450f027e46bf2ce63e288f3e1ac404e116fa8a373dba0e69 | 173a4d4b1574c74f22d41acbd119362258037196dd912bd667ecca51d4b377cb |

## Review gate

No Batch 56 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
