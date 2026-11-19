# Expert Review Packet: Batch 170

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 170 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 950 one-based physical pages; native text extraction recovered content from 948 pages. A total of 53 decisive physical pages were rendered and visually inspected in eight contact sheets. Six candidates were excluded and two were placed on version-reconciliation hold; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT02211131 — exclude: SAP Version 3.0 dated 2019-05-14 follows actual primary completion on 2019-04-30. Although it identifies Protocol Amendment 3 dated 2018-03-23, physical pages 6 and 21 show that the target governs three interim analyses, an optional regulatory ad hoc analysis and locked interim snapshots; it is not a prospective pre-primary target.
- NCT03595553 — exclude: SAP Version 2.0 dated 2021-11-19 follows actual primary/study completion on 2021-11-17. Physical pages 5-6 also show that it combines C004 and C005 after slow pandemic-era enrollment and updates the analysis for Protocol Amendment 8. The selected target is post-completion and conduct-informed.
- NCT04203498 — exclude: SAP Version 1.0 dated 2022-03-22 exactly governs Protocol V5.0 dated 2021-06-01, but model-visible protocol physical pages 82-88 already give N=446 and power assumptions, FAS/SAF/PP definitions, the primary MMRM with covariates and covariance fallback, MAR/MNAR multiple-imputation sensitivity analysis, hierarchical multiplicity, secondary ANCOVA/MMRM analyses and safety/missing-data rules. The protocol substantially reconstructs the target plan.
- NCT04304534 — exclude: SAP Version 1.0 dated 2022-01-26 matches Protocol Version 1.0 dated 2019-10-22 but was finalized late in conduct. Physical page 12 states that the first pooled Phase 2 interim analysis had already been conducted and the second was not performed; physical page 29 adds COVID-affected-participant listings and conditional analyses. The target is interim- and conduct-informed.
- NCT05067504 — exclude: SAP Version 1.0 dated 2022-09-27 follows actual primary completion on 2022-08-17. Physical page 22 records the already conducted Stage 1 database close and safety analysis, the decision to continue to Stage 2 and observed participation through study end. The target is post-primary and interim/conduct-informed.
- NCT05374434 — hold: Protocol Version 1.0 dated 2022-01-27 and SAP Version 1.0 dated 2022-05-02 are separately public, consistently identify NCT05374434 and predate actual start on 2022-05-10. The protocol defers statistical analysis and the SAP supplies a mixed-effects plan, but the SAP never identifies the governing protocol version or date. The study also distinguishes a 10-person pilot from a later full study, so title/NCT/date agreement alone cannot establish which protocol scope the SAP governs.
- NCT05405244 — exclude: both the selected protocol dated 2022-06-06 and the three-page SAP dated 2022-06-09 follow actual primary/study completion on 2019-09-19 by almost three years. The selected package is retrospective rather than a prospective governing pair.
- NCT06176768 — hold: SAP Version 1 dated 2024-05-02 explicitly says it is based on the protocol dated 2023-10-31, whereas the only selected public protocol is later Amendment (b), approved 2024-07-19. The later protocol also contains a broad executable statistical program on physical pages 70-74, but it cannot be substituted for the SAP's named governing version without reconciling whether the 2023-10-31 protocol is independently public and suitable as model input.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT02211131 | post-primary target | 157 / 47 | `8716ed4e5156054c3444ed20212de3fda04daa53162296b906da3779c7f53038` | `c0a5e8d2156cc84f843f7e93a2bc346a60b64cd6aaace1cc49330a7a2e1b35bc` |
| NCT03595553 | post-completion/conduct-informed target | 94 / 30 | `6a7e252c819e8f78f131d752c9d3464a7f7dd5a9e5f7e8a964e4137956aed4d5` | `6bb282484dfab99f5afe9ed8fb1caa338e5c0ec55db49e03221cb84799eed790` |
| NCT04203498 | executable protocol leakage | 106 / 86 | `a4f681973543d0f3a380804b09369b1f409162e51a66aed99179f61a9e2cc002` | `dc07ada5cee3d93d55eb0e14e930f4a3c95235baef62d4ab329b2d77b203d979` |
| NCT04304534 | interim/COVID conduct-informed target | 79 / 30 | `d94d0af8673880b7291ea34aa56deb476862926ec47efc8ca81b522c4b198dcc` | `fb405e803d2dc39adac396627ef22f60ecc3f1a9e94ab960a75f4b7d7a4c9e07` |
| NCT05067504 | post-primary/interim-informed target | 96 / 23 | `0bd0f8f8d902ed96c025ca1a1a52647f042c2fb39da1cbd4ed39984af83c8056` | `6b2fa011e6a155e6c6c9ec5cd4eb5076a0b598d105310e418fb05bf69470d0e4` |
| NCT05374434 | governing-version hold | 17 / 4 | `f1849dba049589a8a392e3588a90ef37efc11b9dc044ecf03fa26656b10999cb` | `030fb959302ea4a0f69a3abaaaa21f2867784f804647a4b32bdcaed70f7a4535` |
| NCT05405244 | retrospective/post-completion package | 10 / 3 | `9d33cdb872e64c5aa6e8316673464e3c36853c79e632a607b65a31397d8067f2` | `a2d89e2626c4ec9fc87e0985c088cb4214f90d8fa23336087403392f69e1e49c` |
| NCT06176768 | governing-version hold | 124 / 44 | `a893f5107b50be05af0183760e0f78fd19cb2eb94fac20b14b07d79ddcbffa1a` | `9daa4924d7ccfda3ac288e4744cf9414dc4fd642a11307d28d8cf80f048d6208` |

## Gate interpretation

- A target dated after actual primary completion is not prospective, even when it bears a formal SAP title and says it was finalized before database close.
- Interim decisions already taken, combined-study decisions, COVID-affected-participant rules and realized stage progression are execution information and cannot govern a prospective hidden target.
- Protocol descriptions become disqualifying leakage when they jointly expose populations, models/covariates, covariance fallbacks, missing-data sensitivity analyses, multiplicity and success criteria sufficiently to reconstruct the target.
- A later public protocol amendment cannot silently replace the earlier protocol date explicitly named by the SAP; unresolved governing-version chains are held rather than guessed.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight decided slots are outside the actionable pool and are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
