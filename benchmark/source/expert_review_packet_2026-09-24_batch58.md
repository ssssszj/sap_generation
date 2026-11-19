# Expert Review Packet — Batch 58

## Scope

Batch 58 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent-target gate. Seven model-visible protocols expose executable target-analysis content, five of those families also have post-primary or post-completion SAP chronology, and two selected plans jointly cover multiple studies. The remaining pair, NCT02759588, uses observed Phase 1b outcomes in both the protocol and SAP to design Phase 2 and is therefore execution-informed. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages; visual review also confirmed the sparse embedded text layer in the NCT02358538 SAP.

## Decisions

- NCT02415400 — excluded: protocol pages 44-48 expose sample-size adaptation, analysis sets, Cox noninferiority, censoring and hierarchical testing; SAP is post-completion.
- NCT03426345 — excluded: protocol pages 66-70 expose simulation power, populations, change-from-baseline/responder models, Holm multiplicity, multiple imputation and safety; the post-completion master plan jointly covers RLM-MD-01/02.
- NCT02240121 — excluded: protocol pages 69-71 expose missing-data, multiplicity and pooled-study analyses; the post-completion plan jointly covers RECD3125/3126.
- NCT04603027 — excluded: protocol pages 131-146 expose Bayesian MMRM, estimands, populations, sample size, dose response and unblinded interim futility; SAP is post-primary.
- NCT02994056 — excluded: protocol pages 54-58 expose HCV missing-data rules, FAS primary exact analysis, safety and sample size; SAP is post-primary.
- NCT03122860 — excluded: protocol pages 56-60 expose FAS/mFAS/PPAS/SAS, ANCOVA, MCP-Mod, secondary/safety methods and sample size; SAP is post-completion.
- NCT02358538 — excluded: protocol pages 37-39 expose ITT/PP, available-case/no-imputation handling, seizure-frequency derivation, descriptive efficacy/safety and sample size; SAP is post-primary.
- NCT02759588 — excluded: protocol page 3 states that Version 1.6 adds existing Phase 1b safety/efficacy data; protocol page 92 and SAP page 3 use the observed 55% disease-control rate among 6 of 11 evaluable participants to design Phase 2.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02415400 | protocol leakage plus post-completion SAP | 58 / 30 | 9f64a24f6f0da6b0cb7d268dfe1a9f02c90b6534a4438d27b9b01e0b0b622acc | cf3cff2cf87f05ff9a72a2b4fffc7fbd5f99f65801f82406192bceefb372f338 |
| NCT03426345 | protocol leakage plus cross-study post-completion plan | 79 / 51 | 6fa186ab2ef80ca1b8011a4dfee393d588fc905caef2264597aaa7fd95330871 | c4af5d9155e1ecf8ebc0ade406c113cc94f62a278516be4d0558cae91fba479e |
| NCT02240121 | protocol leakage plus cross-study post-completion plan | 116 / 28 | 965d6bfc810ee951ba2dbbf9fbcc2223c32e6950c21e76c59db96f16f63c4310 | 327da2024dbcad07213e74cc28ee13c23a12861368c5626cc33c0b71f03dc86c |
| NCT04603027 | protocol leakage plus post-primary SAP | 166 / 82 | 9942a5ab10a0be8ed6fd576ea5d39d426e2f6008ead93f4d08fca2c2b9f1aae2 | 2218fc7c7e407f17848060d0e98a548adfe5ee2a7718ceda78255a9a7a4dc9ac |
| NCT02994056 | protocol leakage plus post-primary SAP | 94 / 51 | 8033ef033f74974a3952d566afdd33905521ea30147d7e6c3d669f74f3ef3aab | 7639e0aec02406005c003cdb4ea011d6ddd2f67d2eb1741bd12c9fda8c669b47 |
| NCT03122860 | protocol leakage plus post-completion SAP | 82 / 18 | ed65862e166e0b9dc10b457011e7ed28350e42186cdac649e85f77054c5e7966 | b09c1c5a79c7d08ac63d02fccbac3d63a9a0d9df5c3ce6384adecc0935d4806b |
| NCT02358538 | protocol leakage plus post-primary SAP | 70 / 29 | be38353688e74fbe19d3394ab1ec8ab084ef2ab628cdac0a30a2fb4198923365 | 4fc5fb53b9942c05753641644b9afdd4c84dccbfa326d04a10c4a5fc1df138f1 |
| NCT02759588 | execution-informed phase expansion plus protocol leakage | 118 / 12 | a42b1100918af1fe86a5ef2a26499e6c8ab0d165bb320f7a89f37382358f5208 | 1efb5c3306395568b410e3054c8a94b873e2409799159ffb3bf0a6dc5dc6d2b0 |

## Review gate

No Batch 58 family may enter train/dev/test. All eight slots must be replenished before the next document-review batch; the registered public draft count remains 71.
