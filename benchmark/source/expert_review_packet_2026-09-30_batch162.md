# Expert Review Packet: Batch 162

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 162 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 1,319 one-based physical pages; text extraction recovered content from 1,318 pages. A total of 51 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03887052 — exclude: although SAP Version 1 is dated 2019-03-19, one day before first enrollment, Protocol 3324582_B physical pages 34-38 already specify the prospective sample size, ITT/PP/SAF populations, endpoint definitions, one-sided hypothesis, random-effects Poisson primary model, site effect, patient covariates, bootstrap sensitivity, secondary summaries, adverse-event summaries and subgroup work. SAP physical pages 4-9 mostly reproduce and elaborate that executable program. The target is substantially reconstructable from the model-visible protocol.
- NCT04964128 — exclude: the selected Clinical Biostatistical Plan Version 1.0 is dated 2022-07-11, after actual primary completion on 2022-06-10. Study completion on 2022-07-26 does not cure the failed primary-completion chronology gate. The selected target is post-primary and lacks an outcome-uninformed prospective finalization chain.
- NCT06444165 — exclude: SAP Version 2.0 is dated 2024-07-16 and was signed on 2024-07-18/19, after actual primary/study completion on 2024-06-10. Physical pages 9-11 state that the final analysis follows database lock and define the selected final program. The target is post-completion.
- NCT03382834 — exclude: Primary SAP Version 2.0 is dated 2019-09-10, after actual primary completion on 2018-12-04. Physical page 12 further says pharmacodynamic analyses will be developed after review of pharmacokinetic data and results of the primary and secondary analyses. The target is post-primary and explicitly outcome-informed for part of its analysis scope.
- NCT04527380 — exclude: SAP Version 4 is dated 2024-03-12, after actual primary completion on 2024-02-19. Physical page 10 records substantive revisions to Bayesian success criteria, primary methodology, sensitivity analyses, interim/futility monitoring, COVID-19 sensitivity language and summaries of missing Week 16 outcomes. The selected target is post-primary and conduct-informed.
- NCT03700320 — exclude: SAP Amendment 1 is dated 2020-06-23, after actual primary/study completion on 2020-05-21. Physical pages 50-51 add analyses of realized COVID-19 visit, assessment, protocol-deviation, drug-disruption and adverse-event impacts; the change appendix also records multiple conduct-responsive revisions. The target is post-completion and COVID/conduct-informed.
- NCT02088541 — exclude: Protocol Version 5 physical pages 76-83 already specify sample size, ITT/PP/safety populations, two efficacy interims and boundaries, conditional sample-size reassessment, OS log-rank/Kaplan-Meier/Cox work, hierarchical secondary tests, CMH comparisons, repeated-measures QoL analysis, safety summaries and missing-data handling. Physical page 83 also says the selected version implements a dose reduction after the 2015-07-29 annual safety review and excludes pre-Version-5 patients from efficacy analyses. The target is protocol-reconstructable and the governing package is accumulated-conduct-informed.
- NCT03861234 — exclude: SAP Version 2.0 is dated 2024-02-02, after actual primary/study completion on 2023-11-01. Physical page 36 shows that Version 1.0, dated 2023-12-07 and described as the final TSAP, was itself post-completion; Version 2 contains publishing corrections only. No prospective public target exists in the selected chain.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03887052 | protocol leakage | 48 / 11 | `aaa6aaf2f358f156255b464db88507b95964ca5784d4ed52bc245d04c60f9eca` | `24562aec76fcf543663bcb910c8b4255dc50277ec4bea63984d6dcad7c38e7ba` |
| NCT04964128 | post-primary target | 94 / 8 | `c1c52e438c69d0528b7b02efda932792acb9334e456f1b06712981c035d1a7c5` | `a6550aa52ef6d3b1a352b4be1cfc511235626b4c73ba3e990c2241b2089c322b` |
| NCT06444165 | post-completion target | 50 / 21 | `0646634f0a05f3b52906d68bf60b24272bd14ddbf380ac1fef984915e2f6f63c` | `7adff80217c8ff349f96802fb4b4b8b38df20b19bf7576cd621e82992a834e5e` |
| NCT03382834 | post-primary/outcome-informed target | 71 / 13 | `049d231a25bceb00fe19bdd013618b1d5e648f94dd3cc4bb2e17423604ef8705` | `fdd1d57d5afffa3c8c3e6edd33a2e41441023cbf2d8345285ff9fa4796775b8f` |
| NCT04527380 | post-primary/conduct-informed target | 196 / 139 | `7748bc3e03fbc004bb54606f4c3e4bb39d03b6d2924ccc4ae157c7311f0f5cf6` | `3b8917a243694667e31553f0bc59c75dd79ce6d0f411f45ca22186b537372c24` |
| NCT03700320 | post-completion/COVID-informed target | 108 / 79 | `28c19e81ef28f89502a263cb22f640b1a5b2aed8077eb0b775d62b15b9976edf` | `d25ca1f1b312bdf72b223084c9a6b77c71385b7d97278b3aa252353738bffe2a` |
| NCT02088541 | protocol leakage and conduct-informed package | 137 / 193 | `2dab3fd4e9a5c6267bd6473b430cfbd3f5efbe43da649fff081eaa7b25229a9b` | `b362381dfce06459b423846f6044915e76e6fc5e7a0b1fa11aa8865dd45f5c7d` |
| NCT03861234 | post-completion target | 115 / 36 | `a116a235d443fcb532c68ae860d88d9aafe7eb4a617abae005208969493e156f` | `42331f2e772cca5774ae880bae213c1cf8c8a937843d549ec8cc3be3c783bec9` |

## Gate interpretation

- A target finalized after actual primary completion is excluded even when overall study completion is later; the primary-completion gate protects against outcome-informed finalization.
- One-day prerecruitment chronology is not enough to rescue a target when the model-visible protocol already exposes the executable analysis program.
- Protocol leakage requires substantive reconstructability. Here the affected protocols jointly expose analysis populations, endpoints, models/tests, sensitivities or interims, not merely study design, endpoint names or a sample-size target.
- A nominally pre-completion package is still invalid when its selected protocol amendment explicitly implements prior safety-review decisions and changes the efficacy population.
- A publishing-only correction after completion does not establish that the prior version was prospective when the prior version was also post-completion.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
