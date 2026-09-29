# Expert Review Packet - Batch 111

## Scope and decision boundary

Batch 111 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen official PDFs and eight registry records were downloaded sequentially, byte-checked, SHA-256 frozen and extracted page by page. All five pages for the promoted family and the decisive identity, chronology, statistical, sample-size, multiplicity and document-type pages for the excluded families were rendered from the original PDFs and visually inspected. NCT05293951 is promoted after exact title/institution/date matching through the official registry association and a clean protocol-to-reference boundary; four other protocols expose executable target programs and three selected plans or protocol slots are post-primary, CSR-derived or otherwise non-prospective.

## Decisions

- NCT05293951 — promote: the protocol and separate SAP share the exact title, institution and 2022-02-04 date before the 2022-11-01 start. Both say the NCT was not yet assigned, so the official registry binding remains an explicit provenance gate. The protocol does not expose the SAP-only paired-test choice.
- NCT04856904 — exclude: SAP Final Version 2 follows primary completion; protocol pages 75 and 79 also expose sample size, populations and MAR/MNAR sensitivity methods.
- NCT02609633 — exclude: protocol pages 6-7 expose the cluster design, target, power, primary and secondary ANCOVA program.
- NCT03169894 — exclude: the SAP follows primary completion and lies one week before final completion; protocol pages 70-71 also expose the descriptive analysis program.
- NCT03995784 — exclude: the protocol-slot file is a final Clinical Study Report appendix, and its embedded protocols disclose the executable program.
- NCT02718898 — exclude: SAP Version 2 follows primary completion; protocol pages 68-76 expose populations, missingness, hierarchy, subgroup and interim decisions.
- NCT04641858 — exclude: protocol page 13 exposes the complete Bayesian negative-binomial model, covariates, intervals, Cox analysis and interim superiority rule.
- NCT02390050 — exclude: protocol pages 49-54 expose populations, MMRM/ANCOVA, imputation and sensitivity, multiplicity, interactions, safety and power.

## Promoted-family annotation gates

`PUBLIC-MIRROR-CROSS-ED-STROKE-001` has 23 first-pass evidence-backed requirements. Expert review must confirm the pre-assignment registry association, resolve assessor-only versus participant-plus-assessor masking and protocol-versus-registry outcome hierarchy, define the randomized population, estimand, endpoint derivations, direct between-group repeated-measures contrast, missingness, multiplicity, feasibility, safety and small-sample uncertainty, and supply a prospective sample-size target if one exists. The reference paired t tests are supplementary within-arm summaries, not a valid replacement for the randomized comparison. Registry actual enrollment 24 is conduct context only.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT05293951 | promote with registry-binding gate | 3 / 2 | 837b7ed9ad9731bbd6f35c00a6837fffd91ba8d5aba904c613049c4f365203cd | 9210c1e2bb158c95f0f684cc31459d32a325bf99c3920383cc8a42c8cf9aebec |
| NCT04856904 | post-primary SAP and leakage | 102 / 59 | 75365cf168b5c5790af4961d67ea7bee4164951e10054fdd071edd93cf493469 | 449427b561d895dfd906550c9201fc7fcd1d100c58a80084a7ceba04a6eca59d |
| NCT02609633 | protocol leakage | 58 / 28 | 3e757438d597552db8e3822a7e5326d3a41a4f54a431811590ae0f833ee69b16 | d347d05d7b17a17673cc595e6930e253c50d28902f4764175bd9c0719ac131cc |
| NCT03169894 | post-primary SAP and leakage | 86 / 26 | 3a76b82f7083297816cce2e96ecc30354a3ed1d2c95f5046be6fb4ad7902ffdd | 04a8055716d2b26d7703b4dcb8833148d07fe5242cbea46f521e05c1290f969e |
| NCT03995784 | CSR protocol slot and leakage | 174 / 54 | f28500032afe862d2ece735bde4e96cea00f0a3a6ab9b94eba3df6e700a70d77 | d2091f904698c4ff8d40e12929314ca25b4e04861131c80f4d64ccba46c700e5 |
| NCT02718898 | post-primary SAP and leakage | 117 / 142 | afd12162b7966f73a880c065157d8699d006af874034fff95e9dd90c952f5677 | 1e812e4b448c8c25a635f75a1abf08ad50b5f6677709819479d2a643f11e15a6 |
| NCT04641858 | protocol leakage | 25 / 24 | 5b629d4bf32c08866d8a0015434b926edbd377cb1f2dcb49c334619b0ae0fa84 | a85214820f89eab54bb40dfd0587321a18cb236915e02aa30e8f0c5e0b491782 |
| NCT02390050 | protocol leakage | 65 / 44 | cf45bb399d1d8b7ceed813dac7667dad530daee880ce3f3bf10d531f4ba4fc79 | cbdf22960bd19e9fb6c8204a2ade04ab2afd1165fba3633324a3560ed34f948b |

## Review gate

Only NCT05293951 enters the registered benchmark, as a draft requiring independent expert review. The other seven slots must be replenished so the release intake remains 100 version-verified public drafts plus 20 actionable metadata candidates.
