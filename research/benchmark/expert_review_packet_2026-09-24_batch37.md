# Expert Review Packet — Batch 37

## Scope

Batch 37 reviewed eight ClinicalTrials.gov protocol/SAP pairs. One pair passed prospective chronology, identity, extraction-quality, independence and protocol-leakage gates and received a 20-item first-pass annotation. Six pairs were excluded because the model-visible protocol exposes the executable target plan, often together with a post-primary or post-completion SAP; one SAP-slot file was a post-completion final-CSR notice explicitly stating that no SAP was created.

All 16 PDFs were hash-frozen and text-extracted. NCT02235909's encoded statistical pages and the first 20 pages of NCT04881890's protocol were OCRed. Covers, version/date pages and decisive statistical pages were rendered and visually checked before promotion or exclusion.

## Promoted study

- `NCT04881890` / `PUBLIC-VA-LCDPP-001` — the independent protocol package and SAP share the exact VA LC-DPP title and 2021-04-20 ClinicalTrials resubmission date, before actual primary completion on 2021-09-30. The protocol defines a single-arm mixed-methods feasibility pilot with up to 30 participants, 24 group sessions, baseline/6-/12-month assessments and optional interviews without disclosing the reference SAP's quantitative tests or qualitative coding workflow.

### Review focus

- Operationalize recruitment, retention, attendance, self-weighing, food tracking and physical-activity adherence denominators.
- Preserve the prospective target of up to 30; do not substitute the registry's execution-era actual enrollment of 18.
- Confirm analysis populations, withdrawal handling, item-level scoring and missing-data rules.
- Adjudicate paired-t assumptions and use paired categorical methods instead of unqualified chi-square/Fisher tests for within-participant change.
- Keep inference exploratory and estimation-focused for the small uncontrolled pilot.
- Verify all critical one-based physical-PDF locators.

## Protocol-leakage exclusions

- `NCT02235909` — the protocol exposes analysis sets, ANCOVA, MMRM, MI, LOCF, significance and sample size; the SAP is also post-completion.
- `NCT02899000` — the protocol exposes ITT/safety populations, observed/no-imputation and LOCF rules, confidence intervals and analysis structure.
- `NCT03752970` — the protocol exposes sets, analysis timing, confidence intervals and sample size; the SAP is also post-primary.
- `NCT01945593` — the protocol exposes safety/FAS/PP sets, missingness, Wilcoxon analyses and sample size; the SAP is also post-completion.
- `NCT03504852` — the protocol exposes FAS, logistic modeling, MI/mNRI, multiplicity and sample size; the SAP is also post-completion.
- `NCT02564523` — the protocol exposes power, analysis sets, analysis timing and confidence-interval logic.

## Wrong-document-type exclusion

- `NCT01856309` — the one-page `Statistical Analysis Plan (Final CSR)` notice is post-completion and explicitly says no SAP was created for the abbreviated final CSR.

## Review gate

Only `PUBLIC-VA-LCDPP-001` enters the draft benchmark. It remains `draft_needs_expert_review`; no Batch 37 item is expert-adjudicated or eligible for a frozen split.
