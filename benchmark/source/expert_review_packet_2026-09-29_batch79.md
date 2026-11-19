# Expert Review Packet — Batch 79

## Scope

Batch 79 reviewed eight ClinicalTrials.gov document families. Three independent, prospective and identity-matched protocol/SAP pairs were promoted to first-pass annotation drafts. Four families were excluded because the selected analysis material was retrospective or not an independent SAP, or because the model-visible protocol already exposed an executable target. One family remains on governing-version hold. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology, version and decision-defining pages.

## Promotions

- `NCT01757067` → `PUBLIC-EVAC-HF-001`. The protocol and independent Data Analysis document share the exact EVAC-HF title, NCT and 2011-09-17 date, before the 2013 study start. The protocol supplies the randomized treatment contrast and follow-up but not the separate document's power assumptions, permuted-block implementation, crossover-aware ITT rule, missing-LVEF rule or change-score analyses. The 23 requirements isolate reference-only facts to `confirmed_decisions`.
- `NCT03689452` → `PUBLIC-PRP-ALOPECIA-001`. Protocol Version 2 and the independent statistical analysis document share the exact title, investigator and 2018-09-21 date, before study start. The protocol supplies the PRP-versus-saline design and repeated photographic outcomes but not the reference's change-score tests. The 20 requirements expose unresolved hierarchy, derivation, population, missing-data, sample-size and multiplicity choices.
- `NCT02967172` → `PUBLIC-ANKLE-PAI-001`. The protocol and independent statistical plan share the exact title, NCT and 2016-08-08 date, before study start. The protocol supplies the randomized blinded design and prospective approximately-200 target, while the reference supplies exact VAS power assumptions and only a generic test list. The 21 requirements keep prospective targets separate from registry actual enrollment and require an endpoint-specific repeated-pain analysis.

## Exclusions and hold

- `NCT02409329` — excluded as the 2020-03-31 analysis document postdates 2019-06-04 completion and reports analyses performed, inspected data visualizations and an observed subgroup of 219.
- `NCT02510560` — excluded because FIT-04 Protocol Version 7 pages 46-54 already expose populations, randomization, multiplicity, sample-size re-estimation, primary analyses, multiple-imputation sensitivity and futility rules.
- `NCT03388970` — held because the three-page statistical plan has no title, NCT, protocol identifier, version, date or signature evidence with which to establish its governing protocol.
- `NCT02651714` — excluded because the selected seven-page file is the protocol's statistics section and explicitly delegates complete methodology to a separate SAP.
- `NCT02673489` — excluded because AI444379 Protocol Version 2.0 pages 75-80 expose the population, SVR12 analysis, threshold, sensitivity analyses, safety and interim methods sufficiently to reconstruct the target.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01757067 | promoted | 9 / 5 | 35f090c31d162dbd270479770b0eed636e72c201aaabf11374fa12b41f01b6b9 | b0508513044631859794e2e9ef67e226e451cf0abd64e57ac393ddcf1ea5138d |
| NCT03689452 | promoted | 7 / 2 | 1e9111b09479697530ffb9446bd77a8937985600c4717dc84732d56508475ab1 | 6b2349697fa81d63b5462e35096bba94d2ed679b26e6bc7a7c381fb85a4f5183 |
| NCT02409329 | retrospective methods exclusion | 29 / 3 | 94d76d4f6d6a94d2c669aeaa96e67431f2b35e7935340aa9721249cbe5e5f672 | 27b2351b0d608f0f3d605a525b1240376a2584e65f7225d13f6079fc6c68f76f |
| NCT02510560 | protocol leakage | 69 / 40 | 3fc57fadc91b748c9dc287013c21dd25bcff480664d1c7fb700964da5c659ff1 | 7796da32ef06b4446c815ff9aa3373af3b49ae819ed017c5391eaed972011f87 |
| NCT03388970 | version hold | 19 / 3 | 65384ebe3c1356ba8cbade7d246fcb1d0ea5ea36dba7eb68ed1ae55837a13da4 | 14f896cfea4cf3afff9f3b1816f8752fa3eae6a69985a8545aa9d078d59b3628 |
| NCT02651714 | wrong document type | 8 / 7 | 0e3608fb8106b18c9f8e682a313bdd1760cc391a23b46984c338d592896c4c96 | ca24c5651cf4192779909a2885558ab6123c9dd3425ebcfdf4423651eea6c63d |
| NCT02673489 | protocol leakage | 115 / 17 | 7193a340721a189b5ff09150f9f7eaeb7b144f03a3e38b289b68d9b88828acce | 2789f6bee7cf0dbf687ad83c8f37c07396774d321bd7672af309b7f2305df20f |
| NCT02967172 | promoted | 4 / 2 | 32f52cc1e16ab67de9f80cff6c24679645bac2e4ced7592b0da96a6f116f7963 | b5688674ff48eb3415f37e1dd539bc0bd919259ce8cdafecb828efeb872a8476 |

## Review gate

The three promotions remain `draft_needs_expert_review`; none is approved for a frozen train/dev/test split. Reviewers must verify every critical locator on the rendered one-based physical PDF pages and adjudicate the unresolved primary-model, estimand, analysis-population, missing-data, multiplicity and safety decisions. Reference SAPs remain annotation aids only and must never be included in `protocol_only` model inputs. The four exclusions and one hold remain outside the actionable candidate pool.
