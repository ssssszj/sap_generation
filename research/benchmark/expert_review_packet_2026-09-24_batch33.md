# Expert Review Packet — Batch 33

## Scope

Batch 33 reviewed eight ClinicalTrials.gov protocol/SAP pairs. One pair was promoted to a version-verified first-pass annotation draft, two were placed on hold, and five were excluded. The reference SAP remains an annotation aid and must never be supplied to the generation model.

## Promoted study

### PUBLIC-TIGER-HSTNI-EMS-001 / NCT07008391

- Protocol: 10 physical PDF pages, most recent amendment dated 2025-05-15, SHA-256 `9c3135e367a95f19122314c963441e34bf7fea127795c12a02ec1f0d212cecae`.
- Reference SAP: 9 physical PDF pages, dated 2025-05-15, SHA-256 `7114b52be3d03192000fd13432675cd8dce5941eb85fda37381acce080f60f11`.
- Version evidence: exact title and date match; both documents predate actual start on 2025-06-25. The protocol records original version date 2024-03-21 and latest amendment 2025-05-15, and explicitly delegates statistical analysis to the separate SAP.
- Visual QA: all pages were rendered and checked, with focused review of both covers, protocol physical pages 4-10 and SAP physical pages 2-9. No material redaction was found.
- Annotation: 24 atomic evidence-backed requirements, status `draft_needs_expert_review`.

## Critical adjudication questions

1. Resolve the primary event definition across protocol FMC-to-PCI, SAP/registry FMC-to-vascular-access and SAP inferential text FMC-to-balloon.
2. Resolve whether the primary population is all randomized suspected-MI patients under the protocol ITT statement or only discharge-confirmed MI patients under the SAP. The latter is post-randomization selection.
3. Replace or justify the SAP's modified-Poisson risk ratio for an unthresholded time outcome and fully specify no-PCI, death and censoring rules.
4. Reconcile MACE: protocol/SAP outcome list includes angina, while the SAP derivation substitutes PCI/CABG revascularization.
5. Define a primary success rule, multiplicity strategy and outcome-specific MAR/MNAR sensitivity analyses.
6. Formalize the 150-participant interim review, including data cut, access, quantitative safety or length-of-stay triggers and lack of efficacy claims unless type-I error is controlled.

## Holds

- `NCT05822648` — `hold_version_reconciliation`: protocol and SAP covers match, but the SAP analyzes future T2D onset and body-fat mediation, whereas the current pilot's Aim 1 is three-month BMI/HbA1c change and Aim 2 is caloric intake/physical activity. The protocol says T2D-onset testing belongs to a future fully powered trial.
- `NCT03174132` — `hold_public_redaction`: exact study identity and pre-start dates match, but opaque black redactions remove substantial endpoint, analysis-population, missing-data, sample-size and statistical-method content from the public protocol/SAP.

## Exclusions

- `NCT04091087` — protocol embeds sample size, analysis sets, longitudinal/ANOVA methods, missing-response handling and interim design.
- `NCT02840721` — protocol embeds the two-stage interim design, analysis populations, UMVUE estimation, sample-size rationale and futility framework.
- `NCT02615691` — SAP is post-primary-completion and protocol embeds cohorts, missingness, primary exact method, ABR model and interim analysis.
- `NCT02752776` — protocol embeds analysis sets, primary descriptive method, missing-data rules, safety summaries and sample size.
- `NCT02612428` — SAP Version 4 is post-primary and execution-informed; protocol independently embeds the survival analysis, alpha, populations and power assumptions.

## Review gate

The promoted study is suitable only as a first-pass benchmark draft. A statistician and a second annotator must resolve the critical items and recheck physical-page evidence before any frozen split assignment.
