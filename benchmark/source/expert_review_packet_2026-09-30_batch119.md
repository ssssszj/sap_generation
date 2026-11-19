# Expert Review Packet - Batch 119

## Scope and decision boundary

Batch 119 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen official PDFs and eight official registry records were downloaded sequentially, size-checked and SHA-256 frozen. Native text was extracted page by page from all 1,609 physical PDF pages; 51 scan-only or otherwise empty-text pages were separately OCRed. Decisive identity, chronology, version, family, conduct and leakage pages were rendered into 17 contact sheets and visually compared with the originals. Seven candidates are excluded and one is placed on governing-version/prospective-governance hold. No Batch 119 candidate enters the registered benchmark.

## Decisions

- NCT02072226 — exclude: the 2017-05-17 SAP was finalized after 2016 early termination for slow recruitment and uses the realized N=313, observed nonadherence, missingness and resulting power. It is conduct-informed.
- NCT02836873 — exclude: protocol physical pages 57-60 disclose the ITT/safety/PP sets, Week 24 MMRM, covariance fallback, observed-data/LOCF/MI sensitivities, rescue handling, hierarchical testing, safety and no-interim choices.
- NCT04075825 — exclude: the long-term extension depends on ADMIRE-CD II participants, and Protocol Amendment 2/SAP Version 2 introduce an interim analysis after parent-study unblinding.
- NCT02222545 — exclude: Protocol Amendment 11 records completed Stage 1 and enrollment, approximately 28 observed HSCT-TMA patients, an actual-response CI example, emerging-data sample-size changes and interim CSR/database-lock activity; the protocol also exposes the analysis.
- NCT03073200 — exclude: SAP Version 3 says it was approved after primary database lock and adds regulatory interim analyses; protocol pages 65-76 already expose the executable program.
- NCT02120352 — exclude: RAP Amendment 5 follows primary completion, adds Week 160 analyses and was written after interim evidence and realized enrollment were known; the amended protocol exposes the Bayesian/interim/population/missingness program.
- NCT04259788 — hold: Protocol Version 6.0 and the two-page SAP have exact title/date matching on 2024-07-30 and precede primary completion, but they were created more than three years into conduct. Protocol page 5 says statisticians, the study manager and dietitian are fully unblinded; neither file supplies revision history, author blinding or SAP sign-off evidence. The VAS eligibility threshold also conflicts between protocol (at least 6) and registry (at least 7). Outcome-uninformed governance cannot be assumed.
- NCT03461861 — exclude: the three-page SAP substantially copies protocol pages 13-14; normalized word-set Jaccard overlap is 0.970 overall and the two substantive page pairs overlap 0.982 and 0.962.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02072226 | post-termination and conduct-informed | 314 / 56 | 471bde3e27c0e9ec8e9e1fcea0b3ce900dba1b14f7c8328fe770db77623090dd | 732238d12db5516e235fc4653dcae791a480dbd39798fd6939cca6c9b2646818 |
| NCT02836873 | protocol leakage | 72 / 66 | f5864827473ea80ac18ce707716a43b499a3d872628b734004a296a8af81b3fc | 81327b83a2b05cf16cfa1dc109f7690b66fb396a96c70b9c43cf2e2bc08e9536 |
| NCT04075825 | parent-family dependent and after-unblinding interim | 55 / 28 | 7472ab07bee38b8a7aaa733e206a264125ae5da935dd54821df7fa6ccc691cde | fd66f25d2a2019c255a908b3dbd29dba90ead262d61e8c83fc50ecc58861711f |
| NCT02222545 | execution-informed and protocol leakage | 103 / 23 | e41dfbf95680c34e0a7d65608cbff584568446f045159aec4eab5129c3dc7840 | b5e01f0a32b3cd0f2e3617eb933576c9c4997522f199ee3ab999b641f1ea5c8d |
| NCT03073200 | post-primary-lock and protocol leakage | 109 / 130 | bd695d81d7e10c3070d6481147721fbf9207946c5c73300b6b556a568cfeedad | 87d46279ab6c69a1d679d36e6e5a2ee369f310a0bdddb03004b30490d9e44754 |
| NCT02120352 | post-primary and interim-informed | 425 / 182 | 954cd95ac5e3294d8e4cf2c685003b3e8e7ad67b068840ba0f506bf3d52b4d34 | a4939b806ef00a793a4a56bc2d30e14e65dfdc5d67ae876956db109954981986 |
| NCT04259788 | governing/prospective-state hold | 15 / 2 | 6f962c66fdeed0c141afbecac2b73d8ef98faca3be4e54084c0710bb9aaefb81 | 20709d08b1fe675337201baf726a8f04105e4ffb4bb16874fa928429f311dead |
| NCT03461861 | complete target leakage in protocol | 26 / 3 | ea2356c490d115efc2d8e49486e5ff431465cbcd5918a6dc7a00eb81804262a0 | 14c68a79736fc044f43a19b4efb031f234a25d028534de6346e87e413a77660e |

## Review gate

No Batch 119 candidate is promoted. NCT04259788 may only be reconsidered if an authoritative amendment history, dated SAP approval/signature or documented blinded-analysis provenance establishes that Version 6 and its SAP were fixed without access to outcome information. All eight slots must be replenished from the official registry pool, preserving 101 public first-pass drafts plus 19 actionable metadata candidates.
