# Expert Review Packet - Batch 107

## Scope and decision boundary

Batch 107 reviewed three exact-document-date metadata candidates from the public ClinicalTrials.gov queue. All six official PDFs and three registry records were downloaded, byte-checked, SHA-256 frozen and extracted page by page. All 60 physical PDF pages were rendered; the covers and decisive identity, chronology, document-independence, leakage, formula, sample-size and execution-stage pages were visually inspected. One family is promoted to a first-pass draft and two are excluded. Promotion is not expert approval or split freezing; the reference SAP remains annotation-only and must never be model-visible.

## Promotion

### PUBLIC-COVID-AG-OTC-001 / NCT05584176

- Exact identity: the 23-page Revision C protocol and five-page Statistical Analysis Plan both print protocol `EDP-SOP-TNC-014` and date 2021-12-01.
- Chronology: both documents predate the registry's 2021-12-09 actual study start and 2022-01-21 primary/final completion.
- Independence and leakage: the protocol gives the prospective paired antigen/PCR design, valid-run and discrepant-testing rules, accrual composition and PPA/NPA thresholds. It delegates the calculations to standard methods and does not disclose the reference-only interval equations, symptom-day, demographic, Ct or low-viral-load analysis program.
- Annotation: 21 atomic requirements cover design, paired evaluation unit, specimen order, valid-result population, invalid-result repetition, discordance testing, PPA/NPA, performance criteria, intervals, prospective accrual, subgroup summaries, missingness, multiplicity, safety and explicit unresolved decisions. Exact PPA/NPA formulas and symptomatic/asymptomatic agreement analyses are restricted to `confirmed_decisions` because their executable forms occur only in the reference SAP.
- Expert gates: reconcile the prospective accrual rule with the SAP's unexplained total N=188; verify the score interval and replace or justify CLSI EP05-A3; operationalize the Ct-at-least-32 fractions; define missing-data denominators, performance success on point estimates versus confidence limits, multiplicity and participant-level dependence. Registry actual enrollment 332 is conduct context only and is not treated as the prospective target.

## Exclusions

- NCT05488652 — the three-page SAP reproduces the protocol's complete statistical-methods section, including GLM and repeated measures, Bonferroni, fNIRS preprocessing, the mixed-effects formula, TCD/DVA analyses, EEG distribution-dependent tests and FDR, and cognitive composites. The model-visible protocol therefore exposes the target plan's executable core.
- NCT02729831 — the five-page analysis upload explicitly says its analysis section was taken from the published 2019 BMJ Open protocol. It is a later excerpt of public protocol text rather than an independently governed prospective SAP; the 2017 cover date does not establish that the excerpt itself was frozen prospectively.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT05488652 | protocol leakage | 11 / 3 | a1dfa4a47c83d04c0f09b8eb92f8e6de4d96160c77380f2a5e4ec86b700bdcac | f76a6be7fa4338a6d0477639fe17e7b5324244181dddc60c36f6d3d76156a030 |
| NCT05584176 | promoted first-pass draft | 23 / 5 | 2643aa181d14846535ce475806fb9d816c4406ec6b2010cc031d1252102de656 | b38ae114cb4fedf2f7f3f0f710867946af1cddd908b24db6d414344fbc555453 |
| NCT02729831 | wrong document type | 22 / 5 | 55abee3b39455076cc3581a8f6843c4edd18535fccfee89b64b278d276142186 | 9693b6f6ce29c22c966ee012b98011dd045be729a3227dfdf327d36a57e07ad0 |

## Review gate

Only NCT05584176 enters the registered benchmark, and only as `draft_needs_expert_review`. The two exclusions remain outside all splits. Their rejected slots must be replenished so registered public drafts plus actionable metadata candidates remain exactly 120.
