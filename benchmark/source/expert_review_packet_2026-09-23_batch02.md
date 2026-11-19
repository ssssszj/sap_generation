# Expert Review Packet: Dasiglucagon CHI and BP Control in Hypertensive Smokers

## Scope

This packet covers the second annotation batch added on 2026-09-23:

- `PUBLIC-DASI-CHI-001`: 22 requirements;
- `PUBLIC-BP-SMOKERS-001`: 23 requirements.

Both document pairs were downloaded from ClinicalTrials.gov, hash-frozen, text-extracted, and visually checked. The governing protocols are the evidence source for `protocol_only`; reference SAPs were used only to identify operational additions, discrepancies, and hidden decisions.

## Requested review decision for every requirement

For every JSONL record, record **accept / edit / reject**, verify track applicability, epistemic status, severity, source locator, acceptable values, and whether the requirement is independently scorable. Preserve the raw first-pass record before adjudication.

## Dasiglucagon CHI: priority adjudication

- `R006-R009`: confirm the estimand, placebo-minus-dasiglucagon contrast, two-sided alpha, and exact superiority decision rule.
- `R014-R015`: verify the asymmetric protocol imputation and the three protocol sensitivity analyses; do not import later SAP-only tipping-point or multiple-imputation details.
- `R016`: adjudicate the protocol inconsistency between total carbohydrates by any route and one synopsis reference to gastric carbohydrates.
- `R017`: decide whether the key secondary endpoint requires explicit gatekeeping or should remain an unresolved multiplicity question.
- `R022`: confirm that sequence-generation and concealment details are genuinely absent from the allowed input.

## BP Control in Hypertensive Smokers: priority adjudication

- `R006`: decide whether SBP and DBP are separate primary variables in addition to body weight.
- `R008-R010`: assess the primary analysis restricted to abstinent participants with observed follow-up, including the resulting post-randomization selection and estimand interpretation.
- `R012`: evaluate whether data-dependent selection of baseline covariates is sufficiently operationalized.
- `R014-R016`: reconcile protected Fisher LSD, the alpha 0.025 power calculations, and the missing overall success rule across outcomes and contrasts.
- `R017`: distinguish relapse assignment from missing continuous-outcome handling and specify what an executable SAP must ask the statistician to decide.
- `R022-R023`: review the boundary between safety monitoring, safety analysis, and DSMB governance.

## Adjudication output

After review, update each requirement in place, increment `annotation_version`, change `status` to `expert_adjudicated` only after all critical issues are resolved, and add an adjudication note. Neither study should enter a frozen split before leakage review and source-rights review are complete.
