# Expert Review Packet: Batch 150

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 150 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, public-redaction and document-type gates. Native text was extracted from all 1,057 physical pages in the 16 selected PDFs, and 121 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. Seven candidates were excluded and one was placed on public-redaction hold; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03409731 — hold: the public SAP follows study start and materially redacts the population definitions, full sample-size justification, missing-data rules, covariate rules and multiplicity decisions, while the protocol permits sequential feedback and changes to training or registration criteria during Phase 1. The public record cannot establish a complete, outcome-uninformed target.
- NCT04102189 — exclude: the protocol already exposes the estimands, hierarchy, populations, ANCOVA, RD-MI/J2R/TP-MI, MMRM and sample-size program; the later SAP also adds a six-subject site sensitivity after an observed stadiometer calibration failure and changes prompted by authority and related-trial feedback.
- NCT05186805 — exclude: the SAP follows completion, adds COVID-conduct summaries and governs an analysis after 25% of subjects completed that could change the PK sampling scheme; the protocol already exposes the populations, descriptive efficacy/PK program, observed-data missingness and the same adaptive PK review.
- NCT03149848 — exclude: the RAP became effective one day after study completion and specifies final analyses only after completion, database freeze and release of randomization codes; the protocol already exposes the PK populations, log-scale comparisons, 90% confidence intervals, sample-size precision and no-interim rule.
- NCT03789292 — exclude: SAP Version 2 follows both the Week-24 primary analysis and final study completion, while the protocol prospectively schedules Week-24 database lock and unblinding and already exposes the ACR20 equivalence margin, ITT/PP analyses, confidence-interval decision rule, sample size and sensitivity analysis.
- NCT02687542 — exclude: the selected Version 3 carries a post-completion approval footer and explicitly aligns changes with Interim Analysis 1; the protocol and SAP describe unblinded interim efficacy analyses, possible dose-arm changes, Bayesian Emax/MMRM analyses and the executable primary program.
- NCT01790126 — exclude: the SAP was approved after study completion, and the protocol already exposes the ITT/safety populations, FACT-P MMRM, interim safety boundary, PSA analyses, Kaplan-Meier/log-rank time-to-event program and ANCOVA analyses.
- NCT03478865 — exclude: SAP Version 2 and its governing Protocol Version 9 both follow completion, and the plan explicitly uses preliminary Cohort 1 tolerability and lack-of-improvement results to justify a higher-dose second cohort and revise the analysis program.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03409731 | public-redaction/prospective-governance hold | 41 / 15 | `5e479b4239c694e45e866985027bf54b36353095b59bd56a54c63b785c5a899f` | `749b5a4803667a0e81b7db8e60c2154bd479c2ff541a9592c0da140dcc011e51` |
| NCT04102189 | conduct-informed target plus protocol leakage | 128 / 26 | `5614254b8a199b0de01adc423563567925d88965264976092ba433b324a6abf8` | `99e04239027c7d431414a7e56ffc1f9f8015d7841ca5b6fc7d9266712d8155c0` |
| NCT05186805 | post-completion/adaptive-PK target plus leakage | 75 / 36 | `c18d09929f956711c012b28a30ba7cc230108b5223d26799b8eae0414fa4c349` | `88c88fd6e185af1a85a9fd9d5bacb3e559e9dce22715e0845f76067a6af3946c` |
| NCT03149848 | post-completion/unblinding target plus leakage | 98 / 50 | `573b5a543a46b41798c33faf810d6f621e03ef880f660fdfb13709a756a5bbb2` | `b15f0ac86e7e41e426d02578e6216c84577ce1631d8324c3e59c3fa1822fc11d` |
| NCT03789292 | post-unblinding/post-completion target plus leakage | 113 / 57 | `436bd48ee437450a0e5367ac8b6138dcf28214a070626d48e00c82e36562efe6` | `70c223780526f1ee1953288a05ca64ab7b5070fe257a5c6ecd2033a6fd205588` |
| NCT02687542 | post-completion-approved/interim-informed target plus leakage | 135 / 59 | `3e50819e3bbf4ad956134a666eb90d7e72ce45963ef60cbd7e3b5a191ca45be1` | `9ba88e73464e2caef437c0f59ea4d264c28a46bc29c4fe1caf0e02c4a9ab21d0` |
| NCT01790126 | post-completion target plus leakage | 108 / 25 | `6bc2e8644f7ae16f1c53d3789988da2e7335f781fdb3b57079a1e7b48b0dfadf` | `badfe107258000a35e92cbc76781af56073192d6051707d66cec2b928a6d5cf8` |
| NCT03478865 | post-completion/outcome-informed target plus leakage | 36 / 55 | `c6e9d89fa7ac3cfd728f9f26a40d7e00c61e8a2738d7f397ab5596f548cb7e02` | `688ea2bf14b4a48ed333e274d0ab3fd61fee04c564b72f733700882adae0f2f7` |

## Gate interpretation

- A materially redacted public SAP cannot be promoted when the obscured blocks cover analysis populations, sample-size rationale or missingness/multiplicity decisions; visible surrounding text is not enough to reconstruct a judgeable reference target.
- A pre-completion SAP still fails when it records realized site problems or conduct-specific sensitivity analyses and the model-visible protocol already supplies the executable program.
- A nominal document date does not override a later approval footer, especially where the revision explicitly aligns with an already performed interim analysis.
- A plan issued after an announced database lock/unblinding or final study completion is not rescued by calling its analyses prospectively planned.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight non-promotable slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
