# Expert Review Packet — Batch 70

## Scope

Batch 70 reviewed eight ClinicalTrials.gov protocol/SAP families. No family passed the public, prospective, version-matched, independent-hidden-target gate: four protocols expose executable target analyses, three files occupying the SAP slot are retrospective or execution-informed methods records, and the remaining otherwise prospective pair has decision-defining public redactions. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology, formula, redaction and decision-defining pages.

## Exclusions

- NCT02864953 — protocol pages 60-64 expose populations, primary/secondary models, closed testing, adaptive sample-size re-estimation, the CHW formula and power; the selected public protocol also predates the protocol versions cited by SAP v3.
- NCT05794763 — the three-page analysis upload reports models already fit, observed ICC and missingness, and 50 completed imputations; it is a retrospective methods note.
- NCT05696392 — protocol pages 62-65 expose sample size, populations, endpoint derivations, paired tests, LOCF and safety analyses; the SAP was signed on the actual completion date.
- NCT03233217 — protocol pages 67-70 expose populations, estimands, confidence-interval methods, subgroups, missing-data rules and analysis timing; the otherwise prospective SAP is not an independent hidden target.
- NCT03927846 — the two-page post-completion upload contains only a past-tense ANCOVA sentence and lacks governing-SAP provenance.
- NCT01993836 — SAP v5 records unanalyzed patient samples, current results sheets, an observed unstable factor solution, executed code and decisions made after PI correspondence.
- NCT01678664 — protocol pages 30-32 expose the exact-binomial design, analysis sets, success threshold and time-to-event analyses; the SAP is titled Final Analysis and postdates its own final-analysis point date.

## Hold

- NCT04305587 — protocol pages 24-30 obscure objective/endpoint rows, cohort-design, dose-rationale and PK content, while SAP pages 37-45 obscure prior derivations, model inputs and analysis-code context. The public pair cannot support complete evidence adjudication without guessing through material CCI redactions.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02864953 | protocol leakage plus version-chain defect | 78 / 45 | 632dc132608330ca7ca54383f1484785cdb98af6c51d3b618fbd3e6f8d6efad9 | 4e9fb70880558f9e82e16ab71ef298d114e84b3e85ed14ed628eabf44ddf0f12 |
| NCT04305587 | material public-redaction hold | 112 / 51 | 7c600edad0fb85938361fe9ca38129a8dc40f753d016609546863cb826978dc4 | 223e06bf2eb6a49119cebfe5da108cb189844503fc144c991815fdf14cf6df81 |
| NCT05794763 | retrospective methods/results note | 11 / 3 | a8c4bcecc0cd49a11086cb634c846df7e6a6fc7c54727b24ea1246d2bd06f73b | 328d271effe463114bb551534be4e578e7c9d894ae4d61dc94ccd646014069ba |
| NCT05696392 | protocol leakage plus completion-day SAP | 80 / 38 | 20f89ad623decb9e0318eaef70de7f62a40ad405c10c84befe9bf1eef6e55504 | b09151c317f52d4ba7a8807537eb7cfae2e524bf59fd3783f70c41671bf61cac |
| NCT03233217 | protocol analysis leakage | 80 / 50 | 0f1a8aac95cc2ae7e4fdb9724f20f8e3659c5a677e8a3ac7ec940fc36b83418a | a46f210d8ea7f5425e6f6529f1bc33b451e369b5d0d59cbb16241052af37d00b |
| NCT03927846 | post-completion methods note | 9 / 2 | bd6db8630094110f946fd6cf43b6488bf53562ca76a2c4c9011e9e13cbe8f987 | 366062893a497f01f3d46f01f680c0892b5f37c21da551add24a035b525c1807 |
| NCT01993836 | execution-informed working analysis record | 4 / 7 | 58490743a2e7a02f99f9b1e361a80616dd3d8c97a155d14b81ffca9bbf025581 | c2d48c63ce138cde0236198cb57c142a6bb475c961dc05c9cba7b197cbfd6c6c |
| NCT01678664 | protocol leakage plus execution-stage final SAP | 36 / 20 | b5216f33bfb7f14f29a4d1465c72a084bff30eb02d360d79f1c9e18e5b34b921 | df8a241bb1fabe439845579ab253a5263bdfa056bad1cbd72f79ad92353f84d3 |

## Review gate

None of these eight families may enter train/dev/test. Four fail prompt/reference independence, three do not provide a clean prospective governing SAP, and one remains on hold because material public content is redacted. Batch 70 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
