# Expert Review Packet: Batch 154

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 154 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 960 physical pages in the 16 selected PDFs; the 35-page scan-only NCT01889069 SAP was also fully OCRed. A total of 146 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03510663 — exclude: SAP Version 1.0 dated 2018-09-25 follows actual primary/study completion on 2018-07-05. Independently, Protocol Version 1.0 exposes the QTcF endpoint, intersection-union central-tendency test, categorical thresholds, assay-sensitivity model, multiplicity correction, analysis sets and sample-size/power assumptions.
- NCT04450394 — exclude: Protocol Amendment (d) and SAP Version 2 were revised during conduct after observed Algorithm 2 data-entry and dosing-recommendation problems caused that arm to be terminated. The SAP incorporates arm removal, pooled treatment handling, deviation-based sensitivity analyses and an already unblinded study team. The protocol also exposes the estimand, MMRM, intercurrent-event handling, noninferiority margin, populations and power assumptions.
- NCT05439941 — exclude: SAP Version 2.0 dated 2023-06-07 follows actual primary completion on 2023-05-25 and coincides with actual study completion. It plans repeated parent-cohort interim/final deliveries after cohort completion and makes parent-study assignments available after parent database lock. Protocol Version 4.0 already exposes the analysis sets, data-point sets, estimands, intercurrent-event strategies, interim program and sample-size rule.
- NCT03198507 — exclude: SAP Final Version 2.0 dated 2018-11-20 follows actual primary completion on 2018-10-24, and its included 2019-02-06 addendum explicitly specifies additional ad-hoc analyses performed after final statistical analysis. Protocol Amendment 3 already exposes the analysis populations, primary responder test, missing-as-failure rule, subgroup program, sample size and no-interim statement.
- NCT04114656 — exclude: RAP approved 2021-10-12 follows actual primary/study completion on 2021-09-16. Protocol Amendment 4 and the RAP provide two during-conduct interim analyses, futility stopping, unblinded review and observed-data/model-diagnostic choices; the protocol also exposes the primary models, populations, multiplicity policy and sample-size program.
- NCT02988401 — exclude: SAP Version 4.0 dated 2022-12-09 follows actual primary/study completion on 2021-12-17 and explicitly stratifies analyses by the realized pre-shutdown versus shutdown/post-shutdown periods. Protocol Version 2.4 was itself revised during conduct for COVID-19 and already exposes the longitudinal models, covariates, safety program and sample-size/power calculations.
- NCT01889069 — exclude: the selected target is an intermediate-analysis SAP, and Protocol Amendment Version 4 says the intermediate analysis was added because all patients had concluded induction for the relevant safety/PK endpoints. The SAP also has an unresolved internal final-date display (2016 versus 2017). Independently, the protocol exposes the analysis populations, descriptive and time-to-event program, repeated-measures PK models, no multiplicity correction and sample size.
- NCT03636061 — exclude: SAP Version 1.0 dated 2018-10-04 follows actual primary/study completion on 2018-09-26. Material blocks covering the primary method, multiplicity, sample size, missing-data procedures, sensitivity analyses and output details are publicly redacted, so the post-completion reference is also too incomplete to support a judgeable prospective target.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03510663 | post-completion plus protocol leakage | 84 / 20 | `3a49c1f90d557e98733b8f739d134fc5b2e9f48df1f7edd69b868809c1a4386d` | `b8bb24de498bfc8c87ccbd71f36947252eeac23a69f632fb3605d38a00ef510b` |
| NCT04450394 | observed-conduct arm removal plus leakage | 104 / 37 | `2be1c35a3bca510019a2e52b4716a2886a225b0d186dd47b319570c67f596652` | `6870e388e0e00fd1aeeff2d7824a9f4ecc343fbcfe9abefe6a3dacbbe62c5f9c` |
| NCT05439941 | post-primary/parent-lock-informed plus leakage | 91 / 76 | `3ae00405dc4ffcfad792d35384f8631fb56675a23417da940d8d3faf6309374e` | `4dc4de9295b006ae080875b4ed001e95b40bde28313f643c986a387d389084c9` |
| NCT03198507 | post-primary/final-analysis addendum plus leakage | 66 / 46 | `6ec9ddfb3fe922910cffc8bdf654b3640963a1f94defdc71c792c0276f3cb8d4` | `9b16c2151d76e11dd22e854c9a54937696c7124bba12bda344e5a4df851dbd4c` |
| NCT04114656 | post-completion/interim-unblinding plus leakage | 92 / 87 | `66e56e9c8f4411ac8ba373f2369ff114422728eeb744a1026a8bad457b3a0f9c` | `dfac45b7d9c5465140a143149a7354564133c5898f4567e03ab5db7d2585ca77` |
| NCT02988401 | post-completion/COVID-shutdown-informed plus leakage | 19 / 4 | `fb52e7de5ecc47a4d601ec0f696e4eff5a8cf8919292f107dd0198b8af0a0dd2` | `2daf3ade7ba82ca0bf3687c264a73a24c37e13a45211a942a83e989b02371338` |
| NCT01889069 | conduct-informed intermediate target plus leakage | 109 / 35 | `d8286d03a50e52f079df86d557da041b25a4a0df2f2934026726b6cc4bc66b51` | `97967bd6e1412bb601027c11f553f023c272623560e72403d14b926222d3561a` |
| NCT03636061 | post-completion, materially redacted target | 59 / 31 | `a4d511c68888a29ebbe7f1392627a05e63aee9d7fcf031c74f3ae3f3e12dfb3c` | `bffb5687251903d9da2e95615c0f38d8b2a51e0b2f1089a3a333abc32bf57d03` |

## Gate interpretation

- A SAP signed after actual primary completion cannot be treated as the prospective governing target even when the study completed only days or weeks later.
- A during-conduct amendment prompted by observed data-entry, dosing or safety problems is execution-informed; removing an arm and adapting populations or sensitivity analyses from that experience is not a clean prospective target.
- Parent-study database lock, cohort completion and repeated parent-cohort deliveries are execution state, not merely design metadata.
- An intermediate-analysis SAP added after the relevant patients completed induction is conduct-informed even when the overall study continues for later follow-up.
- A post-completion SAP with material public redactions cannot support complete, evidence-backed judge requirements.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
