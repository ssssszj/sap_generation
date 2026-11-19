# Expert Review Packet: Batch 167

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 167 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 892 one-based physical pages; text extraction recovered content from 843 pages. A total of 35 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT04247581 — exclude: the current SAP is dated 2020-04-06, after actual primary/study completion on 2020-03-20. The selected target is post-completion.
- NCT05151731 — exclude: SAP Version 3 dated 2024-05-21 precedes actual primary completion, but physical page 10 explains that under Protocol Version 2 some participants had already entered off-treatment observation before the Week 48 visit and adapts evaluability to that realized conduct. Physical page 3 also records material estimand and sensitivity-analysis revisions. The selected target is execution-informed.
- NCT03619902 — exclude: SAP Version 0.4 dated 2019-09-09 explicitly governs Protocol Amendment 4 dated 2019-08-30, whereas the selected public protocol is the later Amendment 5 dated 2019-10-29. Independently, protocol physical pages 48-54 expose analysis sets, baseline, confidence intervals, the primary and secondary endpoint analyses, missing-data delegation and the interim-analysis trigger and use, substantially reconstructing the target. The selected chain is governing-version-mismatched and protocol-leaking.
- NCT03476135 — exclude: SAP Version 1.0 dated 2018-09-30 follows actual primary/study completion on 2018-09-10. The selected target is post-completion.
- NCT05025787 — exclude: SAP Version 5.2 dated 2024-07-19 follows actual primary/study completion on 2024-06-11. Its history also records multiple protocol-responsive revisions through 2024. The selected target is post-completion.
- NCT03901092 — exclude: SAP Amendment 2 is dated 2019-04-30, after actual primary/study completion on 2019-04-26. The selected target is post-completion.
- NCT02152631 — exclude: SAP Version 3 is dated 2017-10-02, after actual primary completion on 2017-09-15. The registry's current estimated study-completion date does not rescue a post-primary target.
- NCT04111965 — exclude: SAP Version 3.0 created January 2019 explicitly identifies Protocol Version 2.0, while the selected public protocol is Version 1.0 dated 2018-12-11. Independently, protocol physical pages 55-57 expose executable within- and between-group tests, ITT and PP rules, the 70% adherence threshold, the 20% safety stopping rule, the -5-point noninferiority margin, 80% power, alpha 0.05, and the 126-participant sample-size equations, substantially reconstructing the target. The selected chain is governing-version-mismatched and protocol-leaking.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT04247581 | post-completion target | 43 / 32 | `ca8476f9c18c2e16c7b2700ea1b4560704abd6932cd01101027797a0e1085e8b` | `7cdb00c7ea235f7272fb09322791b634001afd548ed6969fd4c0f8ac774115f6` |
| NCT05151731 | execution-informed target | 125 / 49 | `35b3d3e5ada437097e5ead53ecdcc5a02fd1e93d2f016df06eb43fadb2e2e6f9` | `7644a6f9d758225079e793c8cec8f3614a27994d2eb7d6a11524ffcc1e7518fc` |
| NCT03619902 | governing-version mismatch and protocol leakage | 97 / 54 | `e40b0ce61a422dfcdd3c1a030803dc09ad48dcc4daf5d1d4d35168b53e288840` | `9598fc148918bd0c744459b72cfa063a3cecfbc559b11a5cf9449742fb6ab611` |
| NCT03476135 | post-completion target | 71 / 26 | `933847188e48cfb63be75355d9208fac32ca12b3f79713d4946ef187dece0579` | `e6d09ae2044c62324f5fb86f27805daeaf54c8f8614a3090aaf05c255acef114` |
| NCT05025787 | post-completion target | 101 / 19 | `e1f203acb91dfa7e69c46510da50ba46a1adbf263a13192e43e1538baf7cb701` | `5c2cf31e4ecaf1c430e4f1ae9609087d8ece20264521e5748777d6a2d4dbd4ec` |
| NCT03901092 | post-completion target | 16 / 25 | `ad1149849bcc0f8418450057b837cfa300797bef8e1c7b8d62f9157a030a2a1f` | `741922e33778eb9e37ef0d7d30b4e0a683786e02549b092c7bd658fe78ce04ea` |
| NCT02152631 | post-primary target | 114 / 36 | `621ac5e23a5ee6ec679adf1712e7d9df2c3fbacd958ab5ca715faf491875d836` | `dd855cf735e4943e1ef7d8da1c8f941d83485f3638ac658c3f066997f53c14a4` |
| NCT04111965 | governing-version mismatch and protocol leakage | 71 / 13 | `13a21fec33a1c39e64c862187308e9b4e2c6d558ce49ef29b2b1531af64c008f` | `fda6d0148250c0d03128f8e447bf580c6de3fdad11b6f7c902facde9122f5275` |

## Gate interpretation

- Completion chronology is a hard gate: a target finalized after primary or study completion is not a prospective reference SAP.
- A pre-primary SAP is still excluded when its text adapts evaluability or estimands to participants' realized progression through the study.
- A later public protocol cannot silently replace the amendment explicitly governed by an earlier SAP.
- Governing-version mismatch is independently disqualifying here because the selected model-visible protocols also reveal enough executable analysis content to substantially reconstruct the target.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
