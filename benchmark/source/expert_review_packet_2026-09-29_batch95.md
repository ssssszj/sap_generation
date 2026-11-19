# Expert Review Packet - Batch 95

## Scope and decision boundary

Batch 95 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally and extracted page by page; the two promoted pairs and every decisive identity, chronology, leakage and execution-stage page were rendered and visually inspected. Two families are promoted as first-pass annotation drafts and six are excluded. The six open slots are replenished so the intake remains 120 public families.

## Promotions

- `NCT03486223` -> `PUBLIC-SEH-INSULIN-001`. The 23-page protocol extract and independent two-page Statistical Analysis Plan share the exact title, NCT and 2021-08-11 IRB-version date and predate actual 2021-11-18 completion. The model-visible protocol defines the randomized double-blind two-period crossover, prospective 34-person target, seven-day treatments, seven-week washout, clamp and mechanistic measurements without exposing the reference-only paired-test choice, Jones-Kenward carryover branch, Hills-Armitage period test or power assumptions. Twenty-two evidence-backed requirements were added. Because the pair was adapted late during conduct and uploaded after completion, original unmodified IRB provenance remains an explicit review gate.
- `NCT03293329` -> `PUBLIC-DIAPHRAGM-RCI-001`. The three-page protocol and independent two-page Statistical Analysis Plan share exact title, investigator, sponsor, unique protocol ID, EudraCT ID and internal 2017-09-24 date and were uploaded before registry posting and recorded completion. The protocol defines three interventions and immediate pre/post movement, pain and pressure-threshold measures without the reference-only test list. Twenty evidence-backed requirements were added. ClinicalTrials.gov labels both documents 2017-11-24 despite their internal date and 2017-09-24 upload timestamps; this metadata discrepancy and the terse plan's unresolved hierarchy, target, population, model, multiplicity, missingness and safety decisions remain review gates.

## Exclusions

- `NCT06403098` — retrospectively reconstructed plan. The nominally 2024-06-10 SAP cites the jamovi project, 2025 and software versions unavailable on its stated date; both files were uploaded in 2026 after completion.
- `NCT03892564` — post-completion SAP. The plan is dated 2019-03-11, two days after actual primary and study completion.
- `NCT03196427` — post-primary and completion-date SAP. The plan follows primary completion by more than three months and is dated on final completion.
- `NCT02740335` — protocol leakage. Protocol pages 61-63 expose the exact non-inferiority hypotheses and margin, alpha, Farrington-Manning test, alpha and beta spending, boundaries, sample size, populations and sensitivity rules.
- `NCT02804763` — post-primary SAP amendment. Amendment 1 follows primary completion and contains interim/final branching plus implementation and result-display revisions.
- `NCT02058108` — termination- and execution-informed plan. The trial stopped after a futility interim; the plan says analyses were abridged after termination and revised after review of dry-run TLFs.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT06403098 | retrospective reconstruction | 17 / 3 | ab40e487a272c5e301ff2e218cdc391558854cb1a448959b40a9a276480fe172 | d83c101bbb6b7e6225542155c3b72923454ca0f4421ac64360e8a1283460da3e |
| NCT03892564 | post-completion SAP | 43 / 32 | 45328ff8e896dbc91dd0ec5155a0d76d97c2522aa0713026e3c3a4cbc587630e | 7696ef8c9cbe5ba23afe84c1181fd204c1874b7324d0e9171cc97196a5f0ee5e |
| NCT03486223 | promoted draft | 23 / 2 | d1a3999c39f2d30992111b536d7e826ca99cb41f75d0ba9e72c588d7b3e4414e | 4cf57ffead77c76086d44d284287dd947c488318ebbcf684a00a6566fd63198a |
| NCT03196427 | post-primary/completion SAP | 119 / 68 | e0bcaf768a816d3cda5c6ead448304944b343363d99d42e768a55a4658c92fd0 | fa14ef93f3a3c59673bbc60be6e7db03219df30adbce5ab56a7c698cecf0db72 |
| NCT02740335 | protocol leakage | 74 / 31 | 946cf1e84564a2552f45724d667485000b2ddaf244e96e729b00ebb816184638 | dd4c9f14adc1dfc7ca0a4fcc470f0c8f4cd49de6c9dd7371f7808c878c41550c |
| NCT02804763 | post-primary SAP amendment | 145 / 100 | 7edbd24c62f03bb1602132840f9e15e8f775bf38f39bc44c7216dcb29e53cde0 | 621f49cfb655998028417b994f0d7f068a25a03ac91e258e9c11872aa94a98ff |
| NCT02058108 | termination/execution-informed SAP | 87 / 55 | 71edbd267bd94ded3c48bebaabfb3aca804c4578c22d10865ccd19cea92cb13c | 15ff7d763eb9b81b060314e146461d99986a8bdbb85f09962a10c126579db669 |
| NCT03293329 | promoted draft | 3 / 2 | 0bc7ca35a8a8564ab759d5be8bd58866b7d7a0f6392e84ecc2810809c1ad6033 | df0c1d79f007a0f48240caee99362c0b3f69ef03f3c1bebf1fbc3ebdbb6fdaf0 |

## Review gate

Both promoted families remain `draft_needs_expert_review`; neither is expert-approved or split-frozen. Their reference SAPs remain annotation-only and must never be model-visible. The six excluded families do not enter the completed-question count.
