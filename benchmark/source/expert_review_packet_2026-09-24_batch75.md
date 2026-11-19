# Expert Review Packet — Batch 75

## Scope

Batch 75 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the public, prospective, version-matched, independent-hidden-target gate. Seven model-visible protocols expose an executable target analysis; the remaining selected analysis file is a one-page post-completion retrospective methods note whose protocol already discloses the principal pilot thresholds. Five references additionally have post-primary, post-completion, execution-informed, version-chain or non-independent extension defects. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology, redaction and decision-defining statistical pages.

## Decisions

- NCT03036150 — protocol pages 9 and 71-73 expose the event/sample-size design, populations, ITT, stratified Cox model, hierarchy, Kaplan-Meier, subgroup and safety analyses.
- NCT04692688 — protocol pages 51-54 expose power, populations, logistic/ANCOVA models, covariates and imputation; the otherwise prospective SAP has material public redactions.
- NCT04248933 — the selected one-page post-completion Data Analysis Plan retrospectively says descriptive statistics were used and is not a prospective governing SAP; protocol pages 3 and 12 already give the pilot thresholds and follow-up principle.
- NCT04212169 — protocol pages 7-9 and 75-78 expose populations, power, MCP-Mod, MMRM, estimand/rescue handling, sensitivity models and multiplicity; the SAP predates the selected protocol and records extensive revisions.
- NCT03376321 — protocol pages 17-21 expose power, population, proportional-odds analysis, multiplicity, imputation and interim re-estimation; the post-completion SAP records COVID-19, interim and endpoint-driven changes.
- NCT04065074 — protocol pages 40-42 expose the population, adaptive sample-size rule, confidence interval and summaries; the SAP is post-primary and cites Protocol Version 1 rather than the selected Version 2.
- NCT03047629 — protocol pages 57-60 expose the stage design, sample, success criterion and exact-binomial analysis; the post-completion SAP cites an unavailable amendment and deletes analyses after randomization removal and insufficient enrollment.
- NCT01724346 — protocol pages 62-65 expose pooled parent/extension time-to-event, response and safety analyses; the non-independent extension SAP deletes an endpoint using nine years of observed follow-up and only two MRD-negative participants.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03036150 | protocol analysis leakage | 99 / 30 | 742916a101d7a279639772d34d5e307a268c9f9fa8fcfc31760f56fc446b24d8 | 83dfd86cf3346991b973ece0afe4fb97ea1eb45ce51d1f43839091792bc17b7b |
| NCT04692688 | protocol leakage plus material SAP redaction | 70 / 43 | 5eb2aa698920c951eb4a5706ea768fba0098bfa17fe65b3a7d1e15fef43d3282 | 321fca1e4c3263f5f3a98e3620f9d19c8b55043909c245ba1f81d09d950aadeb |
| NCT04248933 | post-completion retrospective methods note | 21 / 1 | 3a4ccc137e2af74175f121a73f1eb4038f7d378def749926cc87d927bc9dff35 | d9b8f648eee65a36a43a7c4bfb7567504155c685eeab514873d10aea780ed230 |
| NCT04212169 | protocol leakage plus version-chain defect | 133 / 49 | 0e24ada9597f45edd9c0d2a2b2314122df4ed5f36e25b3e3066a22cb0324cba9 | 6036ac5fbd9091d60d985f03a3bddeff7c5e6688ccb962efa9ce23ae8a217f85 |
| NCT03376321 | protocol leakage plus post-completion execution-informed SAP | 129 / 116 | 7e44355b8e6960aada456783431113ef1607be86cf75533789c800ca06de4b97 | ae27a416524f5dd90b744e92df4f0a0e85f33fc08c2bfb83121633038db280a8 |
| NCT04065074 | protocol leakage plus post-primary version mismatch | 51 / 40 | a6a9a7584195cd7866313a25fc7f0bf5155514c7de0e6cf4cfc156daf5d0997e | b4dda26c0dc48c2f763b12f56be3a8f4833d1b5d4a3debb2ddd65ef932e4ee62 |
| NCT03047629 | protocol leakage plus post-completion execution-informed SAP | 135 / 47 | 5f40b1d256399f8aa21e765f0477869b6e0fa30a4e4fe6c725e1ba3daa9c8408 | 5c3a21517a566e4956ae56203855bc9bfb489c31ae115af71084b288d9ef4e26 |
| NCT01724346 | non-independent execution-informed extension | 102 / 30 | 1de2735086affa9009929781f2bfb2b9f08c19dafdfe0ff6d8942d66cbf229d3 | 0badac4b7ed51d7152663e737e0a8b3317fbebe0085bb12dee392f52f259aa50 |

## Review gate

None of these eight families may enter train/dev/test. All fail the prospective independent-target gate through executable protocol leakage, wrong document type, or both. NCT03376321, NCT04065074 and NCT03047629 additionally use post-primary or post-completion references; NCT03047629 and NCT01724346 contain direct executed-study adaptations; NCT04212169 and NCT04065074 lack a clean governing-version chain. Batch 75 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
