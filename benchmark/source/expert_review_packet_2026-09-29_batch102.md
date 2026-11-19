# Expert Review Packet - Batch 102

## Scope and decision boundary

Batch 102 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were downloaded again sequentially after a truncated parallel transfer was detected, then parsed page by page. The original source-file SHA-256 values below are for the complete official downloads. Decisive identity, chronology, leakage and executed-analysis pages were rendered and visually inspected. One family is promoted as a first-pass annotation draft and seven are excluded. Seven open slots are replenished so the intake remains 120 public families.

## Promotion

- NCT03854253 -> PUBLIC-INTROLENGTH-RAO-001. The four-page protocol and independent two-page Statistical Analysis Plan share the exact title, institution and cover date 02/11/2019; ClinicalTrials.gov records that document date as 2019-02-11, before the 2019-02-26 start. The protocol defines the randomized long-versus-short 6 Fr introducer comparison, Doppler-ultrasound RAO endpoint and complications without exposing the reference-only Mann-Whitney, Fisher, SPSS or alpha choices. Eighteen requirements were added. NCT-free PDF provenance, ambiguous date format, masking role, randomization details, RAO derivation, analysis population, estimand, missing ultrasound, effect reporting, multiplicity, operator/procedure effects, safety and prospective sample size require expert adjudication. The title suffix (146) is treated as institutional identifier TCRC-146, not as a planned sample-size target.

## Exclusions

- NCT03127956 — protocol pages 30-32 already expose the Safety Population, descriptive-only strategy, missing-data rule, compliance threshold, TEAE derivation and summaries, laboratory shifts and sample-size rationale; the separate SAP is substantially reconstructable.
- NCT04143945 — both selected wrappers are post-completion Clinical Trial Report appendices, and the SAP bundle combines a prospective plan with post-lock Statistical Methods and Analysis Output.
- NCT02559206 — final SAP Version 1.0 dated 2016-10-04 follows actual completion on 2016-09-30; no public evidence establishes a pre-outcome freeze.
- NCT02554773 — final SAP dated five days before completion explicitly incorporates the 2017 clinical hold, 2020 voluntary dose pause, observed thrombotic risk and updated efficacy data.
- NCT02446899 — revised protocol and SAP postdate completion, and the SAP records blinded-data-review changes and reassignment of primary/key-secondary endpoints.
- NCT04498273 — the alleged protocol and SAP are the same 14-page Statistical Analysis Plan content, exposing the full adaptive model and stopping rules rather than supplying an independent protocol.
- NCT06523010 — both short documents describe completed enrollment, measurements, comparisons and analyses in executed past tense; they are retrospective method summaries.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03854253 | promoted prerecruitment draft | 4 / 2 | 859daef0039a0253e18f1253fdd4b744ff4e9b8bf8196d09bee8c32b39477892 | 15c62736f773ac1e3691af05fe34246b3ae605f341cb0cf2d9f5db400bbec8fa |
| NCT03127956 | protocol leakage | 41 / 16 | 0fc0afdf041d3f0cad5d7651a108dffe77468fd7842ff5beaedc059716f66f6a | f3cf224ab557deb9e13ce8c8f3069ea9e9a0fe73cd5a786d56a333d9fceaaf47 |
| NCT04143945 | post-completion CSR bundle | 59 / 37 | ce0334461cb40c9fbe61fbb9e49807efe5f6b2d908c809bba2b4d7ec690a3ece | a101e421f1a81d99fe85e7c62c4ce0e8ce5a16aea784161fd16bd4199933c116 |
| NCT02559206 | post-completion SAP | 117 / 86 | fad40258333e718bcd85a15fee5344e1caba89f69d27d9ddca7a0c3467940892 | 9a631678dd419db0c6fcaf582153ef785c3fc3bd734f1cf10c22263e043acb30 |
| NCT02554773 | outcome-informed final SAP | 124 / 42 | f304b3cfdac9e3d468e96ce775091f587baa52c9bfb62a47aab4172f17b1b6dc | b33a522e375eb2f1c46b4f80fb25803fb1515d03e3f0c6af7135eb0cb0b33ab2 |
| NCT02446899 | post-completion conduct-informed pair | 211 / 179 | 5768b15ba35d1d7193027cd7a66f3339a7145a5678abf6646c9e7d906f8e6754 | cc3548fd71306d0652c9c4343854ebccaa22f214a32614cedeaf9e95d552d864 |
| NCT04498273 | identical SAP content and full leakage | 14 / 14 | bf51cbdd885a7da5d7e96a66271ffd17c4cff0ab701460814986047b92ff2c2f | 557e5d8f74c5cfbc4d22d7e7ec6c6b60e51e18ae3e49e68931060f424c1875ca |
| NCT06523010 | retrospective executed methods | 6 / 2 | d38c8dadee66008541de59d55c5a93f7a64ed77f8e3b56fa40c6684d201e1f29 | d9875a3ba0305f0afc3d6e885964a9524d9e9de4f8c407a949beeb7b7ed27277 |

## Review gate

The promoted family remains draft_needs_expert_review; it is not expert-approved or split-frozen. Its two-page reference plan remains annotation-only and must never be model-visible. The seven exclusions do not enter the completed-question count.
