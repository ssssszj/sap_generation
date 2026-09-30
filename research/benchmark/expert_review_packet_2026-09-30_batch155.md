# Expert Review Packet: Batch 155

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 155 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 1,094 physical pages in the 16 selected PDFs. A total of 137 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03604263 — exclude: the selected Protocol Version 5.0 and SAP Revision 3 were revised during conduct. The protocol version history reduces the target sample from 30 to 15 and follow-up from 12 to 6 months, while the SAP says the final cohort size of 15 is already known, removes infeasible subgroup analyses, and records regulator/IRB-driven changes. Independently, the protocol exposes the endpoint, analysis population, exact-binomial confidence interval, analysis timing and sample-size rationale.
- NCT04450407 — exclude: Protocol Amendment (d) documents termination of Algorithm 2 after observed data-entry errors, dosing-recommendation problems and investigator overrides. It updates sample size, populations and analyses from that experience; SAP Version 2 then pools prior Algorithm 2 participants with Algorithm 1, excludes them from the efficacy population, and is prepared by an already unblinded team. The protocol also exposes the noninferiority estimand, MMRM, covariates, populations, margin and power assumptions.
- NCT05678959 — exclude: SAP Amendment 1 explicitly says Novartis terminated the extension study early and consequently replaced the planned inferential estimands with purely descriptive CSR analyses, omitting exposure-adjusted rates. The target is termination-informed and also depends on participants, assignments, outcomes and baselines inherited from multiple Phase III core studies.
- NCT03236506 — exclude: although the SAP cover displays Version Date 2019-07-29, the PI and trial-statistician approval signatures are dated 2020-09-29, after actual primary completion on 2020-08-31. Protocol Version 5.0 already exposes the ITT analysis, logistic regression, missing-as-failure rule, interaction testing, sample-size calculation and secondary-analysis program.
- NCT04172831 — exclude: Protocol Final Amendment Version 1.2 was issued during conduct after COVID-19 began disrupting this ongoing trial and incorporates telephone/home visits. It also exposes the causal estimand, MMRM, multiple imputation, model covariates, secondary logistic regression and sequential testing. SAP Final Version 2.0 was approved only 13 days before actual completion and includes optional unblinded interim analysis, adaptive sample-size machinery and sponsor pre-lock review of subject-level opioid records.
- NCT03118947 — exclude: SAP Final Version 1.0 was signed 2019-03-06, after actual primary/study completion on 2019-02-25. The protocol only promises SAP approval before database lock and supplies no evidence that this post-completion plan was frozen prospectively; it is therefore not a defensible prospective governing target.
- NCT01923168 — exclude: Protocol Amendment Version 07 was revised during long-running conduct, including a PK analysis-set revision explicitly attributed to the current course of the study, permanent stopping of the buparlisib arm and promotion of ORR to a co-primary endpoint. SAP Amendment 1 incorporates the stopped arm, known blinded allocation counts, pooled placebo handling and revised sample size. The protocol independently exposes the Bayesian beta-binomial primary analysis, proof-of-concept thresholds, priors, populations, missing-as-failure rules and sample-size operating characteristics.
- NCT03681886 — exclude: SAP Rev.02 is dated 2018-03-01, after actual primary/study completion on 2017-12-14, and states in the past tense that the study was carried out at five centers while defining analyses around the realized optic-exchange cohort. The outer Alcon effective wrapper is later still, dated 2019-06-24. Protocol Rev.03 already exposes the cohorts, populations, descriptive methods, missing-data policy and endpoint analysis structure.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03604263 | conduct-informed design reduction plus leakage | 123 / 27 | `d9e42d22b7c79c1b3b90916965d83ba45726a8803899eadeee9e63de40735132` | `ae29b2030474efe14c01fec1e608584d6670d723a6e988fba3a8dad82391427b` |
| NCT04450407 | observed-conduct arm termination plus leakage | 104 / 34 | `2cad38b0485850b335e9a6e388041ae48588842390c3a53dba2d59194368784a` | `12590882c4fb09baa0ac5149157adf5193dd19a1b399cf1ea62d499d6fece721` |
| NCT05678959 | early-termination-informed extension CSR target | 145 / 28 | `d3046c9f640dac19d0e49a1c8a65c47db68454ac76c4eb470bf777e14abe284b` | `72f4f0b2a0b4634d2d910aa35f113e57b033663c90adb7838a8bb0b43f3161b7` |
| NCT03236506 | post-primary approval plus protocol leakage | 39 / 19 | `4e1ad1538d35868914fae8c368ac0d232ee02e70b98e6a8127c7877489e6b7b9` | `074fe8c2abaae2ecf7009125eb1ef1b4b8f309ceebb5abfb90fe60dc9b68fb46` |
| NCT04172831 | COVID/interim/pre-lock-informed plus leakage | 90 / 48 | `1b6654b854790517a54c9b1c9be7457e313fd43051c8a2e056e1a3ad1d29733b` | `7960a199c8895c1821b97f8398055d178be6d195502c950b5442ca6f44348722` |
| NCT03118947 | post-completion governing target | 77 / 38 | `43a8149557fd7257929b37fded0b6d92329f78c5ee0b585bdc61263272c98d34` | `951416c223b2ee4687c551bcd9bbd88ae18aa897b77e789bd91719975b228c35` |
| NCT01923168 | accumulated-conduct arm/endpoint changes plus leakage | 207 / 72 | `fab6b24966de4f60d652aecc2ff8f4bab2e68139fdaf18e0d328586a03fd6ecd` | `9d3de5c0ad8365277d47fc2ad4120d21293a4a79f2f09f8eeeb1fb6bfeff6980` |
| NCT03681886 | post-completion realized-cohort plan plus leakage | 33 / 10 | `69742ae8afad88b74b80062be09076e5972e1586dd8bfc0b1552a0a0cb1ddfeb` | `1ed9c661bd9a5982688683a60a21226b5a0ff046f8af657f1e55331a1403cda4` |

## Gate interpretation

- A late SAP cover date cannot override later actual approval signatures; the approval chain controls prospective-governance assessment.
- A study amendment based on observed dosing errors, investigator overrides or realized arm feasibility is execution-informed even when investigators remain blinded to comparative outcomes.
- Early termination followed by replacing inferential estimands with descriptive CSR analyses is not a clean prospective target.
- A final cohort size already known during SAP revision can invalidate subgroup, sample-size and follow-up decisions as prospective targets.
- Related extension studies cannot be treated as independent protocol-only questions when assignments, baselines or outcomes are inherited from core studies.
- A post-completion SAP with only an outer document-system effective date does not establish pre-completion governance.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
