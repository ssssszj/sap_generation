# Expert Review Packet - Batch 108

## Scope and decision boundary

Batch 108 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 official PDFs and eight registry records were downloaded sequentially, byte-checked, SHA-256 frozen and extracted page by page. Protocol/SAP covers and 90 decisive identity, chronology, statistical, interim, sample-size and multiplicity pages were rendered from the original PDFs and visually inspected. No family is promoted: four have protocol-side executable-plan leakage, three use a post-completion or observed-outcome-informed SAP, and one is bound to the wrong NCT. None may enter a model-visible benchmark package.

## Exclusions

- NCT02622256 — both files identify NCT02806700, not the candidate registry family; the three-page protocol also reproduces the SAP analysis.
- NCT04092452 — protocol pages 88-93 expose estimands, populations, CMH/minimum-risk inference, NRI, ANCOVA, jump-to-control/MAR handling, multiplicity, power, safety and interim governance.
- NCT01858532 — SAP v3 uses the observed event rate to revise power and removes a now-unreachable interim trigger nine days before completion; the protocol also contains a detailed executable plan.
- NCT02474199 — the final SAP is dated after primary/final completion, without an earlier governing freeze.
- NCT03591406 — SAP v1 is dated almost five months after primary/final completion, without a prospective version history.
- NCT02581345 — protocol pages 54-60 disclose margins, populations, missing-data rules, repeated-measures sensitivity analysis, safety and the administrative interim.
- NCT01962207 — protocol pages 80-91 disclose endpoint cohorts, interval and geometric-mean methods, reverse cumulative distributions, precision calculations, safety and analysis sequence.
- NCT04200352 — protocol pages 94-97 disclose the descriptive sample size, ITT/observed-data rules, no multiplicity, detailed safety and efficacy summaries and no formal inference.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02622256 | wrong NCT binding and leakage | 3 / 2 | 72f590bac410741065bdc5015b6d77dc074f97206a7c70aa0628b8b526f8facd | f0b6f1c5c0748455278a8819a8eed509b830d596dafc19c9329d2ae1eba831b5 |
| NCT04092452 | protocol leakage | 139 / 56 | b74a86e1e9df87b66efe59115e1c98adf7e43060fea9159963ff0d328c9fe8dc | da5ca3fef09b1025a7b25f71fdecc8eac13f639c0284d12938e5ec590c8094a8 |
| NCT01858532 | outcome-informed SAP and leakage | 183 / 54 | 0098f38b6a5831341ce5f5ef1a8a2b27bebed3c5fee846ca099bb6ce690457ce | 6f9d0f965bc28eafc1229d293318c6ab1b57112f55411ad092bbeb147b082a41 |
| NCT02474199 | post-completion SAP | 89 / 24 | 31bf447e94f4c1f27891de2b9387a69c957c585d23e56210d0b1d1b385fef69c | ad5cc811ebf4a9fe2e617b59f03480cc67f97baf3b90d485d432bd58ee553357 |
| NCT03591406 | post-completion SAP | 75 / 35 | 966c18202b6cf4099e30474d4dea3d2bbce6649b8dbc38a78aec7b5beb1a9980 | e979bdf43fe57a25d4fc164295384f8d65a0b9e7adf1c7c9959873290959229c |
| NCT02581345 | protocol leakage | 82 / 33 | 9fac81e1c48d1d245ede2cbf861e2fb9ec16a2b6bab0000a3d8c901c75d3279b | a4018f901ad583c63ecce59688004e0843aaca695366a9363126a7695aa01775 |
| NCT01962207 | protocol leakage | 100 / 33 | 71b82bc78fe261922917ce0d935190176da951795e710c6c8d987a25160ed147 | 83bb8021b54ea2d4bfabf1b794fae229fea825a94116821bb8920b4cc5611015 |
| NCT04200352 | protocol leakage | 236 / 58 | 0269759c5aeae96fdea7837f10eb193f7763618e7f1cc4fba812e9af77b780f7 | 2a3208f50fa3a1b598bfdd581e5f810d841d4de4230c33e8ccf18a33da4d5a1e |

## Review gate

No Batch 108 family enters the registered benchmark. All eight rejected slots must be replenished so the release intake remains 98 version-verified public drafts plus 22 actionable metadata candidates.
