# Expert Review Packet: Batch 160

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 160 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 1,238 one-based physical pages; text extraction recovered content from 1,182 pages, including partial image-based documents. A total of 57 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03795298 — exclude: Protocol Rev E physical pages 59-66 already specify primary and secondary hypotheses, fixed-margin sample-size calculations, exact primary and secondary statistical methods, analysis sets, site pooling, subgroup/multivariable work, missing-data sensitivity analyses and interim rules. SAP Version B dated 2024-01-12 substantially elaborates an analysis program that is already executable from the model-visible protocol. The target is substantially reconstructable.
- NCT04839393 — exclude: Protocol Amendment 2 physical pages 77-84 specifies sample sizes, analysis sets, PK and endogenous-biomarker derivations, log-transformed mixed-effects models, 90% confidence intervals, safety analysis and unblinded sponsor reviews. SAP Version 2 physical page 6 also says preliminary draft data from related study C3421007 motivated adding endogenous endpoints. The target is reconstructable from the protocol and partly related-study-data-informed.
- NCT05917288 — exclude: SAP Amendment 2 is dated 2024-11-19, after actual primary/study completion on 2024-10-30. Physical pages 4-5 record post-original changes to laboratory shift analyses, allowable SLE medication summaries and WHO Drug coding rules, including an update stated to be based on the study. The selected target is post-completion and conduct-informed.
- NCT03368053 — exclude: SAP Final is dated 2018-09-03, after actual primary/study completion on 2018-01-30. The model-visible protocol physical pages 38-42 also lays out sample-size logic, analysis cohorts, derived data, immunogenicity summaries, confidence intervals, safety summaries and the absence of an interim analysis. The selected target is post-completion, with substantial protocol disclosure as an additional defect.
- NCT04506463 — exclude: SAP dated 2022-09-30 follows actual primary completion on 2022-05-04 and study completion on 2022-08-10. Its deviations section on physical pages 28-29 changes the primary comparison from Fisher LSD to step-down Dunnett testing, removes a treatment-compliance summary, changes the FAS definition and materially changes the PPAS definition. The selected target is post-completion and conduct-informed.
- NCT03548584 — exclude: The 139-page ClinicalTrials.gov SAP upload is a retrospective compound bundle rather than a clean prospective target: it contains the original SAP, a 2021-09-08 addendum, a 2022-05-31 addendum, an interim-analysis plan and further CSR/DMC material. Physical pages 52 and 54 show that the first addendum modified multiplicity after the DMC reviewed unblinded interim results and recommended continuation; physical page 56 begins a final addendum dated after actual primary completion on 2022-05-23. The bundle is post-primary and unblinded-interim-informed.
- NCT01796171 — exclude: SAP Final 5.0 dated 2022-04-05 precedes primary completion but its modification history records changes following a 2019 DSUR extract and draft TFL production, a Part A interim dry run and Part A interim delivery. Physical page 13 states that an interim safety and efficacy analysis had already been performed and used to continue dose escalation and expand enrollment. The selected target is outcome- and execution-informed.
- NCT03846193 — exclude: SAP dated 2024-06-17 is only eight days before actual completion on 2024-06-25; the registry later records termination because an interim analysis demonstrated lack of efficacy. Independently of the unknown within-window ordering of that futility decision, Protocol Amendment 9 physical pages 3, 6 and 9 explicitly incorporates emerging safety information, the completed Part 1 dose-escalation safety profile, investigator feedback and conduct-driven changes to hospitalization and study-eye randomization. The selected study package is accumulated-conduct-informed; no claim is made that the SAP necessarily saw the final futility result.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03795298 | protocol leakage | 102 / 34 | `4c96649eb03359666291265dea48df9c40710fd0ed4a8451a66ef5b28e3cb44a` | `ea4c393975a0b73b465bcd671d14657b66bd8cbfff80f2a70f5f6ed9415d02bf` |
| NCT04839393 | protocol leakage and related-study evidence | 118 / 35 | `8a6f0734ba54941d79fcac5e2b3f0e9f122a5f5957a4b72563c49174128e536d` | `f457702dff7ad29be9bb8badbdea141f52653c9773d7531c1dd33595760faa53` |
| NCT05917288 | post-completion conduct-informed target | 105 / 26 | `6a283ca0aba23b584262f1587879e52bb30acd135b0d5726f32302b944c694ac` | `f2e8dd283a4035b2d222bac3e8760d0d7d29e8c279827cd7f020f1ea0e3f3e20` |
| NCT03368053 | post-completion target | 49 / 29 | `32ae4d60b0c9c7b1cec2a89c9a78932e2548115b23aa6155e91f0de1ccda4e24` | `736ac4a775a0cdae16c372acf0dd871e3b5cd8c7d034438a1c25896bb9bc0aa0` |
| NCT04506463 | post-completion conduct-informed target | 82 / 29 | `02f40f41ab76aadfaf0065c97b50701794fbad9e81f941ed276773d84668db33` | `ee2a38c9e855d4438d140b2b0ffe233d30334bcbcf847e67758ad85fa373e3ed` |
| NCT03548584 | post-primary unblinded-interim bundle | 111 / 139 | `e6da769b793d17bef126de78f0434f1164332124e4250f95832feb7426aa0a7f` | `d53668ae87561f68e0ab8bc0e31286f8c7aa246cfef895f642eb2cb5a0a669a2` |
| NCT01796171 | outcome/execution-informed target | 165 / 40 | `ebcf815a48fa6937f02bbd43539f019ed4721d930af1ea125f768758f5be40bc` | `dcaed244683b3506f67d621e19719117cb2ebf7676352e316d467d4697b615e5` |
| NCT03846193 | accumulated-conduct-informed package | 144 / 30 | `59f4edd64075c99adec1d04a916435ec5f3a9a3c20bc119991e2042fff461418` | `a872ad0a81abb2dcab23bb2b2785bf74d72e8fc84e60272c5728273e01db07f0` |

## Gate interpretation

- A model-visible protocol crosses the leakage gate when it makes the target analysis substantially reconstructable across populations, hypotheses, models, missingness, sensitivity work and sample-size logic; endpoint names and sample size alone remain insufficient.
- A date before primary completion does not rescue a target whose own revision history says existing study data, draft TFLs, dry runs or delivered interim analyses drove changes.
- A ClinicalTrials.gov file labelled SAP is not a valid clean target when it is a compound CSR-era bundle containing post-interim addenda, an interim-analysis plan and later operational artifacts.
- When a near-completion chronology does not prove that an SAP saw a later interim result, the decision must rest on independently documented accumulated-conduct evidence rather than inferring an unobserved within-window order.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
