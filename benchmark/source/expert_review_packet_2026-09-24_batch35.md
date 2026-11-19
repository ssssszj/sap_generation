# Expert Review Packet — Batch 35

## Scope

Batch 35 reviewed eight ClinicalTrials.gov protocol/SAP pairs. One pair passed the prospective-version, identity, extraction-quality and protocol-leakage gates and received a 22-item first-pass annotation. Seven pairs were excluded: three because the public analysis artifact is retrospective or post-completion, and four because the model-visible protocol exposes the executable target plan (two of those also have post-completion or execution-informed SAPs).

All 16 PDFs were hash-frozen and text-extracted. Covers, version histories and decision-defining statistical pages were rendered and visually checked before promotion or exclusion.

## Promoted study

- `NCT02405091` / `PUBLIC-VALBENAZINE-TD-001` — Protocol Amendment 2 Final dated 2015-12-03 and SAP Version 1.0 dated 2016-04-05 share the exact title and internal identifier `NBI-98854-1402`, both before actual primary/study completion in 2017-03. Protocol physical pages 10-13 define the open-label titration design, schedule and assessments; page 65 confines statistical content to descriptive summaries, one safety set and a practical non-powered sample size while delegating missing-data detail. The reference SAP remains annotation-only and supplies dose-trajectory summaries, early-termination mapping, missing-data rules, scale derivations and safety displays.

### Review focus

- Confirm that the 40 mg, 80 mg and 80/40 mg categories are described as observed dose trajectories rather than randomized causal arms.
- Check the safety-set exclusions, early-termination visit mapping and non-imputation rule.
- Adjudicate the terminology `primary efficacy variable` in a safety-focused descriptive study.
- Verify all critical one-based physical-PDF locators against the frozen documents.

## Wrong-document-type exclusions

- `NCT01824394` — SAP Version 1.0 is post-completion, based on a termination Closeout Plan, supersedes protocol methods and uses execution-era enrollment for a final-CSR descriptive analysis.
- `NCT04651218` — both short public summaries are dated after primary completion and do not establish a prospective governing protocol/SAP pair.
- `NCT03596164` — the available Final Version 2.0 SAP is post-completion and contains execution-era revisions; the earlier 2019 version is not the frozen public artifact.

## Protocol-leakage exclusions

- `NCT05568225` — the protocol exposes analysis sets, exact-binomial test, alpha, power and futility rules; the SAP is additionally post-completion and intended for an abbreviated CSR.
- `NCT03421197` — the protocol exposes co-primary models, FAS/PP/safety sets, MCMC MI, mNRI, LOCF, multiplicity and power.
- `NCT02842853` — the protocol exposes equivalence/noninferiority hypotheses, populations, confidence-interval methods, missingness and sample size; the SAP additionally adds conduct-informed populations after site-quality problems.
- `NCT03906136` — the protocol exposes sets, estimand, logistic model, covariates, alpha, NRI/MI sensitivity and sample size; the SAP is also post-completion.

## Review gate

Only `PUBLIC-VALBENAZINE-TD-001` enters the draft benchmark. It remains `draft_needs_expert_review`; no Batch 35 item is expert-adjudicated or eligible for a frozen split.
