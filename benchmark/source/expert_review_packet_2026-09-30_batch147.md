# Expert Review Packet: Batch 147

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 147 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 1,309 physical pages in the 16 PDFs, with full-page OCR for the 44-page NCT03908125 protocol and the 75-page protocol plus 50-page SAP for NCT03552276. A total of 133 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03289481 — exclude: the alleged two-page SAP is dated seven months after study completion and reports an already executed t-test and SAS analysis rather than a prospective governing plan.
- NCT03908125 — exclude: the SAP is pre-completion and explicitly matches Protocol v10, but that model-visible protocol already gives the 4% performance goal, exact binomial test, ITT/PP sets, GEE and first-cycle sensitivity analyses, subgroup rules, 1,400-cycle sample-size calculation and interim schedule.
- NCT02975206 — exclude: SAP v2.0 was approved after primary completion, and Protocol v3.0 independently exposes the FAS/safety populations, stratified ANOVA, imputation, LOCF/BOCF sensitivities, CMH responder analyses, multiplicity, sample size and safety program.
- NCT03020745 — exclude: the Part 2 RAP is downstream of Part 1 safety/PK/PD review and includes planned unblinded efficacy/safety project decisions; its protocol also gives the Bayesian responder success criterion, operating characteristics, populations, analysis timing and unblinded governance.
- NCT03552276 — exclude: Protocol Amendment 1 and the SAP follow the parent Phase 2 database lock, cite observed ACR20/50/70 results and use those results to remove dose arms and select 100 mg Q12W; the protocol also discloses the executable descriptive safety and exposure-adjusted AE program.
- NCT02621931 — exclude: final SAP Amendment 02 follows study completion, and its March-May 2017 amendments change the FAS, hierarchy, missing-data rules and primary fallback test. The protocol already discloses the populations, ANCOVA/MMRM, multiplicity, missing-data, sample-size and no-interim program.
- NCT01403948 — exclude: both the revised protocol and TSAP encode realised dose-escalation findings, including the 100-mg Caucasian MTD, Korean safety signals, an executed database snapshot and a Phase I Safety Analysis Report; the protocol also exposes the descriptive/Kaplan-Meier/safety/missingness program.
- NCT03031327 — exclude: final SAP v1.0 is dated after actual primary/study completion. Its statement that it was finalized before database lock and unblinding does not reconcile that chronology, and Protocol v2.0 already provides the analysis sets, repeated-measures ANOVA, endpoint-specific tests, missing-data rule, sample-size rationale and safety summaries.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03289481 | post-completion executed-analysis note | 6 / 2 | `daaf40ecc48a55e95e142d6211835d8048d1101a1c1e6593770906127757fa9e` | `191e913389e2d558c8e545186c6aa32fae426f56340c9517a74145f8f138fa4c` |
| NCT03908125 | protocol-embedded target leakage | 44 / 11 | `596ede64b0e064b0a4e2df2edd4c225d8ed4f43396ce3fa98dae77b1e1699539` | `f2bb2fecb55afc291885c229781cdc2b5e580df5efb7215afe6ebc8d3b7f6a83` |
| NCT02975206 | post-primary target plus protocol leakage | 57 / 26 | `29608f978c44d72dda119fbef6f88f05458a49dba43a33aba3b2b5e94dbc1dec` | `46a09434b169d114f5dbed9ebe96a1e36950eb9b5138b73ad0e0e81df20dcabc` |
| NCT03020745 | prior-part/unblinded-decision target plus leakage | 377 / 133 | `3f3df83e98af73e8621ae46787e7788a075e74316b5bab8a12f6ff5ccc47b5c6` | `29cdf88982cbbe8f184b84576fd0b5deacb8d377722a126b69abd4fd4c2b347a` |
| NCT03552276 | parent-result-dependent extension plus leakage | 75 / 50 | `f90c95c54d1b14d53656f02fb4548f6e535a527bb342aa4bcb6063a3ac512473` | `ad18bb3ec28eac4a0d9abe09abd692e61000595dc1e4d54e88fbc2608f262c6a` |
| NCT02621931 | post-completion changed target plus leakage | 165 / 76 | `bf4e1b02ad069bd00fdc70d165a43a176af41fd4a35efac59d6ea337efec880d` | `c48c0ebdef4e70a5ae8e748c65b9a29c8790ab41bc01c9950dc2dd447add2a44` |
| NCT01403948 | realised dose-escalation target plus leakage | 114 / 46 | `d8071d561034c40ce7a019fe3ca684b4bebed785cbe4ded751ac2a52cac8b649` | `7642a2384a8c9002af4c6d73505845b17bab6ab95165d074ee4ed7b334cd97c5` |
| NCT03031327 | post-completion target plus protocol leakage | 95 / 32 | `e8a1e1d098d492ee10a19e21a581821ba599429e830c1da1db80be53b8b91785` | `ea4ea51f242c8cbcafda51172366f442d00f8ec58f77de272b17f996a34c54fc` |

## Gate interpretation

- A target's statement that it was finalized before database lock or unblinding cannot by itself override a public document date after registry primary/study completion; the chronology must be independently reconcilable.
- A prospective adaptive design may legitimately use earlier-stage data, but a Part 2 target chosen after Part 1 safety/PK/PD review and intended for repeated unblinded project decisions is not an outcome-uninformed protocol-only generation target.
- An extension study is not excluded merely because it follows a parent study. NCT03552276 fails because the selected amendment and SAP explicitly import already observed parent efficacy/database-lock results into dose-arm removal and treatment selection.
- Naming endpoints or a sample-size target alone is not protocol leakage. The leakage exclusions here rely on executable populations, models/tests, missing-data rules, multiplicity, sensitivity/interim procedures, success thresholds or endpoint-specific safety summaries.
- Registry actual dates were used as chronology evidence only, never as a prospective sample-size substitute.

## Replenishment

All eight non-promotable slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
