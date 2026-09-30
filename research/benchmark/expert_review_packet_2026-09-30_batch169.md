# Expert Review Packet: Batch 169

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 169 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 856 one-based physical pages; native text extraction recovered content from 828 pages, and all 130 pages of the font-corrupt NCT02210559 protocol/SAP pair were additionally OCRed. A total of 61 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT02210559 — exclude: SAP Version 1.0 dated 2018-03-20 exactly identifies Protocol Amendment 6 dated 2016-09-29, but model-visible protocol physical pages 36-38 already specify N=42, 2:1 allocation, ITT/safety/PP populations, no imputation, two-sided alpha 0.05, Kaplan-Meier OS/PFS, RECIST and CA19-9 summaries, exploratory Cox/logistic models and continuous efficacy monitoring. The protocol substantially reconstructs the target plan.
- NCT03555981 — exclude: SAP Version 1.1 dated 2020-06-24 follows actual primary/study completion on 2020-04-20. Physical page 4 states that the trial was conducted from May 2018 to April 2020; the selected target is post-completion and conduct-informed.
- NCT03984305 — exclude: SAP Version 1.0 dated 2020-09-09 precedes actual completion, but physical pages 4-5 state that enrollment had already stopped at 41 rather than the planned 350 and add a COVID-19 primary-endpoint analysis; physical pages 10-11 repeat the realized enrollment and classify COVID-affected data collection. The target is realized-enrollment- and COVID/conduct-informed.
- NCT04285580 — exclude: SAP v1.0 dated 2021-03-30 matches the protocol dated 2019-12-20, but model-visible protocol physical pages 44-47 already give the two database locks, sample size and attrition, SAF/FAS rules, rescue-data exclusion, descriptive primary/secondary analyses, paired-t confidence intervals, Kaplan-Meier rescue analysis and periodic safety analyses. The protocol substantially reconstructs the target plan.
- NCT04567329 — exclude: SAP Version 1.0 dated 2020-12-17 matches Protocol 904 Amendment 1 dated 2020-11-09, but model-visible protocol physical pages 48-51 and 55 expose the FAS/PPS/SAF, primary ANCOVA, discontinuation-triggered LOCF/MCMC strategies, sensitivity analyses, hierarchical multiplicity, hypotheses, effect-size assumptions, alpha, power and N=560. The protocol substantially reconstructs the target plan.
- NCT04931563 — exclude: SAP Edition 2.0 dated 2025-05-16 follows actual primary completion on 2025-04-07. Physical pages 12-13 show analysis changes made in 2024 against Protocol Version 3.0, and physical page 33 plans COVID-impact summaries. The selected target is post-primary and conduct-informed.
- NCT05244187 — exclude: SAP Version 3.0 dated 2023-11-27 follows actual primary completion on 2023-10-30 and study completion on 2023-11-23. Physical page 4 says Version 3 corrected an error in the per-protocol treatment duration, and physical pages 7-8 define analysis after all participants completed treatment. The target is post-completion and execution-stage.
- NCT05264376 — exclude: the two-page SAP dated 2024-01-31 follows actual primary/study completion on 2023-04-15. Physical page 2 reports realized group counts and observed missingness ranges and describes fitted/transformed models in past tense. It is a retrospective executed-analysis note, not a prospective governing SAP.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT02210559 | executable protocol leakage | 56 / 74 | `6f97ef6ebf494b3731b0f0bf07f348fb9a94a7ce367ade78219ca2518a7644a7` | `1dbd1c8d82a1efe9613fb46bf688af47c970eea9cc1be2738e4e77a1019fb851` |
| NCT03555981 | post-completion/conduct-informed target | 60 / 12 | `3e7fa77e4b48798136b10662e9f8f52e0f8af375d5b567d07d4e33e6d7333afd` | `65b48c293ede72036ccb0dca9f4b862257d87b9bd05914b377d7f0ac54dd72f8` |
| NCT03984305 | realized-enrollment/COVID-informed target | 31 / 16 | `29abb93f0d9c9266985fc26b1002090f143b15545c22b9715d5a84dead2fbded` | `ec7e2bfe30a95b313366933d216a828d0fed5a0e4f557b5a3a873c2637ab6b2d` |
| NCT04285580 | executable protocol leakage | 78 / 31 | `1dfb8bfd7cb309c883aaa7c06ae7774f4eb3c1575a85689ff25031ba59e0efa9` | `8a425cd9f26ca4660568a738d2d4e79e1df0f48c6681adcacc30db6d2d203566` |
| NCT04567329 | executable protocol leakage | 75 / 45 | `35045f7c2193d8635a90df0e81b780399167ed9f362bbb4e3564232c2e00ff6b` | `b8d5ecc84f83b724761a328bcebf0ce508684a4c824d2cc3c84c84eb025882ef` |
| NCT04931563 | post-primary/conduct-informed target | 193 / 124 | `716b7ea0e0a83d7e07e28c87545be056376194bb3fd4af26d84c318bbe238dd2` | `898f30982f38150f574ee45fadf4d7fdbd5d8a5ff3f484f94cf0b1c26a2c43b6` |
| NCT05244187 | post-completion/execution-stage target | 36 / 9 | `14a11d1448f0f0a9333362f21cdb756be23ac612d1ca4ab00477c3fc0b687c00` | `c17547430d2e323b6bef32f33052b86a3d589eaae1f3e8e653b534d780cbda4f` |
| NCT05264376 | retrospective executed-analysis note | 14 / 2 | `0b1ba5ce6c71b17f1ff22e8972509057699dd38bc42dacb3a5b813173b456d04` | `25362816a8e2f472a8759ae90dd70d0fbe463126b572fc3899de3a7cf60a51ff` |

## Gate interpretation

- A target finalized after actual primary completion is not prospective even when the public protocol predates enrollment or the target calls itself an SAP.
- Realized enrollment, observed missingness, COVID-affected collection and completed-treatment corrections are execution information and cannot govern a prospective hidden target.
- Protocols may state design, endpoints and sample-size targets, but a protocol that also exposes populations, estimators/models, missing-data rules, sensitivity analyses, multiplicity and success criteria substantially reconstructs the reference and fails the protocol-only independence gate.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
