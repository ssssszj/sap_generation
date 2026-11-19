# Expert Review Packet — Batch 38

## Scope

Batch 38 reviewed eight ClinicalTrials.gov protocol/SAP pairs. None passed the benchmark's independence and prospective-governance gates: seven model-visible protocols already expose the executable target analysis plan, and one SAP addendum is a post-database-lock document created after study completion. Several packages also contain execution-informed amendments or post-primary analysis revisions.

All 16 PDFs were downloaded, SHA-256 frozen and text-extracted. Protocol/SAP covers, version pages and decision-defining statistical or revision-history pages were rendered and visually inspected. No OCR was required for this batch.

## Protocol-leakage exclusions

- `NCT01252953` — protocol pages 11–16 expose ITT, log-rank, rate-ratio/95% CI, Kaplan-Meier, alpha, multiplicity and complete sample-size/power logic.
- `NCT02991144` — protocol pages 23, 32, 36 and 83 expose the Bayesian CRM, OBD and stopping rules; page 123 changes sample size using the observed enrollment status of nine participants, and SAP v4.0 incorporates that execution-era amendment.
- `NCT02451137` — protocol pages 8, 63 and 65 expose logistic regression, MMRM, strata, Gamma(-3) alpha spending, interim boundaries and sample-size assumptions.
- `NCT03893565` — protocol pages 39, 42, 80 and 83 expose Bayesian dose response, population, sample-size and interim rules; the RAP is post-completion and records changes following sponsor termination.
- `NCT03517566` — protocol pages 66–72 expose sets, MCP-Mod, logistic/MMRM, MI, nonresponder and sensitivity rules; the post-primary SAP responds to interim results and early stopping.
- `NCT02568215` — protocol pages 44–54 expose prevention-efficacy hypotheses, alpha, sequential monitoring, MITT, sample size and power; the SAP additionally covers two AMP trials.
- `NCT02174861` — protocol pages 63–66 expose populations, descriptive methods, no-testing/no-imputation rules, timing and sample-size precision.

## Wrong-document-type exclusion

- `NCT02201290` — SAP Addendum Final v1.0 is dated after study completion and explicitly records a post-database-lock update. The protocol independently exposes the all-treated descriptive plan.

## Review gate

No Batch 38 candidate enters the draft benchmark. All eight slots must be replenished before the next review batch; no exclusion is eligible for train/dev/test assignment.
