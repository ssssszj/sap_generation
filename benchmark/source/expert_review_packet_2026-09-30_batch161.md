# Expert Review Packet: Batch 161

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 161 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 1,166 one-based physical pages; text extraction recovered content from 1,132 pages, including partial image-based documents. A total of 52 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03844945 — exclude: SAP Version 2.0 is dated 2020-06-16, after actual primary/study completion on 2019-09-19. Physical page 32 changes the protocol's rejection inequality and adds subgroup analyses said to have been conducted a priori but omitted from SAP Version 1.0 through oversight; it also marks post-hoc tables. The selected target is post-completion and not a clean prospective plan.
- NCT04889157 — exclude: Protocol C3421028 physical pages 61-65 already specify the absence of formal hypotheses, sample size and randomization ratio, PK concentration/parameter and safety analysis sets, descriptive PK statistics and plots, parameter derivations, ECG analyses and unblinded sponsor safety review. The SAP largely elaborates this executable program. The target is substantially reconstructable from the model-visible protocol.
- NCT06011733 — exclude: Protocol Amendment 2 physical pages 56-62 specifies all analysis sets, fixed-sequence multiplicity, exact responder definitions, CMH tests, NRI, FAS/PPS and observed-case sensitivity analyses, secondary methods, Kaplan-Meier/log-rank work, safety summaries and MI-to-LOCF fallback. SAP Amendment 2 also has a conduct-reactive revision history: physical pages 5-11 cite unavailable abnormal ranges, collected body temperature, participants entering maintenance treatment and scenarios where PEOT visits were not conducted. The target is protocol-reconstructable and accumulated-conduct-informed.
- NCT03381196 — exclude: SAP Amendment 3 dated 2020-07-01 follows actual primary completion on 2020-05-28; the registry says the study was terminated after an interim analysis was futile. Physical pages 5-7 add COVID-impact summaries/listings, revise per-protocol criteria and define pre-interim/post-interim subgroups, while physical page 28 retains the sample-size re-estimation and futility interim. The target is post-primary, interim- and conduct-informed.
- NCT04508621 — exclude: SAP Final Version 2.0 is dated 2022-01-28, after actual primary/study completion on 2021-11-01. Physical pages 28-29 govern an adaptive unblinded interim, stage-combination test, possible sample-size adjustment and analysis under early efficacy/futility stopping. Regardless of whether adaptation occurred, the selected final target was created after completion and cannot serve as an outcome-uninformed reference.
- NCT03559257 — exclude: SAP Version 2 is dated 2019-07-08, after actual primary completion on 2019-06-19. Physical page 7 says the version was finalized before the first database lock/unblinding but removes the elderly subgroup because the observed minimum proportion was not met and revises open-label analyses; physical pages 50-51 define the interim as the final double-blind efficacy analysis. The target is post-primary and realized-sample/conduct-informed.
- NCT02049957 — exclude: SAP Final is dated 2018-07-23, after actual primary/study completion on 2018-06-29. Physical pages 32-33 specify multiple cohort-specific futility analyses and final changes to PK reporting, but the governing public target was finalized only after completion. It is a retrospective reference rather than a prospective target.
- NCT03846453 — exclude: SAP Version 2.0 is dated 2019-12-17, after actual primary/study completion on 2019-11-22. Physical pages 37-38 state there were no protocol-analysis changes yet record Version 2 revisions to CAE exposure, interaction testing and output figures. The selected target is post-completion and cannot establish an outcome-uninformed finalization chain.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03844945 | post-completion target | 85 / 40 | `261733ae99ccdd1ed146146f1ca309cd3eacb9fa74893c63b9da4423dcd1aa6a` | `02230bbdc2bbd3ca796e836c3b0083d854050f8d3284f6273f00879cf5c1bbd9` |
| NCT04889157 | protocol leakage | 97 / 26 | `9476d1a1d51cdc5be26a8a76fe0b5ab27433a8aa1ad8bdfd72da4874c70688cc` | `6c601a8749091f7d1ec56596efc5bdcb93b4f037d8538c161b43e0457cc9ba08` |
| NCT06011733 | protocol leakage and conduct-informed target | 100 / 74 | `934e1ac86483811b5609d1d15ccf4896e08a15ee744ce66b8ccea4e6a926a3de` | `1442469b4c6688b02996214e0493181aa97042af83ba3983cee571622740bc0d` |
| NCT03381196 | post-primary interim/conduct-informed target | 106 / 99 | `e0dee4713b21035698827d2c26dd52b5d8397ebbc324e05678cf325a7a05550b` | `a220ca88221e4ad0d8f7e1197ce3bb159e9f02795803804e6324ced981b0b2be` |
| NCT04508621 | post-completion target | 92 / 57 | `1fb006ef41260033eb1260654f4cd0a2701b3c1935d9f97121ed4ef9dff7d0bc` | `ce6409d20cd473611216b8cfd786dbb8c1a3ca9876c50676cc4168a059705379` |
| NCT03559257 | post-primary realized-sample target | 72 / 59 | `d8af052bc57841aa9c9289c21eff82cee32a083a1bfaf1cfe10b9a23a6109ffa` | `b7cd8c9e3d50f16202938288ccddd4539392b22a632fd8a2ac66b0c0ebbce971` |
| NCT02049957 | post-completion target | 105 / 36 | `c1c21599fc47d65f678701306d64b9722dd8059a23c154f57bf5b027113c5ceb` | `f880bcd613b98751f8b89bf1f9782b85c44f3123eba869502724db6987fc75d7` |
| NCT03846453 | post-completion target | 73 / 45 | `d566bac8e64e83f370dbfa7bace90288190881dd31f499b5690c37a94cbbaa2e` | `495a200ad85a075efed4519935ee8c6a28495644baa4f3b5662b8ffa0b418a9e` |

## Gate interpretation

- A post-completion SAP is excluded even if its revision table characterizes changes as clarifications or says there are no deviations from protocol-stated analyses; outcome-uninformed finalization still lacks evidence.
- Stating that a late version preceded database lock or first unblinding does not make it prospective when primary completion has occurred and realized sample composition already changed the analysis scope.
- Protocol leakage requires substantive reconstructability. Here, analysis sets, endpoint derivations, models/tests, multiplicity, missingness, sensitivities and safety methods were jointly available, not merely endpoint names or sample size.
- A protocol-complete target can have an independent second defect when the selected SAP's revision history explicitly responds to unavailable or collected study data and realized visit/treatment-period scenarios.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
