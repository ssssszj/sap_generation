# Expert Review Packet — Batch 85

## Scope

Batch 85 reviewed eight ClinicalTrials.gov document families. Three families passed the prospective version-chain, study-family independence and protocol-only leakage gates and were promoted: NCT02805257 as `PUBLIC-AMC-GLAUCOMA-001`, NCT07484620 as `PUBLIC-PAFIT-IBD-001`, and NCT04549454 as `PUBLIC-FITSTART-PLUS-001`. Each received 22 evidence-backed requirements. Five families were excluded: four because the model-visible protocol already exposed an executable target analysis and one because both selected documents were retrospective and post-completion.

All 16 PDFs and eight registry records were downloaded and hash-frozen before decision making. Text was extracted by one-based physical page and the identity, date and decisive statistical pages were rendered and visually inspected. The three promoted source packages were fetched again after candidate-pool refresh and their frozen hashes reverified. Reference SAPs are isolated under annotation-only `reference/` paths and are never model-visible.

## Promotions

### `PUBLIC-AMC-GLAUCOMA-001` / NCT02805257

- The ten-page Manual of Operation and four-page SAP share the AMC identity, NCT02805257 and 2017-12-12 date, before actual primary/study completion in 2020.
- Protocol pages 3-8 define the randomized study, one-eye rule, block randomization, visits, endpoint measurements and safety monitoring but do not expose the reference's endpoint-specific regression plan.
- Two source conflicts remain explicit. Protocol page 7 calls postoperative six-month IOP primary, while SAP pages 2-3 call twelve-month IOP primary. Protocol pages 3 and 5 call the trial single-masked and leave surgeons unmasked, while SAP page 2 calls it double-masked and says participating surgeons and participants are masked.
- The 22 requirements cover design, randomization, prospective sample size, study-eye unit, ITT, endpoint hierarchy, IOP derivation, regression, estimand, alpha, failure/success derivations, time to failure, hypertensive phase, complications, missing data, multiplicity, interim review, center handling, corneal outcomes and visits.

### `PUBLIC-PAFIT-IBD-001` / NCT07484620

- The protocol and SAP share the exact PAFIT-IBD title, NCT07484620, sponsor and 2026-03-10 date. Both call the study prospective and predate estimated primary completion on 2026-11-01.
- Protocol pages 2-8 provide the single-arm phases, 12-week intervention, outcomes and sample-size target without exposing paired tests, mixed models, mediation, missing-data or multiplicity decisions.
- SAP page 4 identifies the single primary endpoint as T0-to-T1 20mSRT change, but pages 6-9 expand “primary” analyses to accelerometry and several fitness variables. The 20mSRT metric also remains stages versus optional estimated VO2max. These hierarchy and derivation conflicts are retained as needs-confirmation gates.
- The 22 requirements cover design, sample size, populations, endpoint hierarchy, 20mSRT definition and method, ALPHA outcomes, accelerometry validity, visits, mixed models, alpha, transformations, multiplicity, secondary domains, associations, mediation, subgroups, missing data, sensitivity, estimand and safety.

### `PUBLIC-FITSTART-PLUS-001` / NCT04549454

- The protocol and SAP covers share the exact FITSTART+ title, NCT04549454 and 2021-04-26 date, before actual study start on 2021-07-22.
- Protocol pages 2-3 and 6-8 plus the measures appendix define parent-level randomized app delivery, student linkage, assessment schedule, alcohol outcomes and safety processes without an executable HGLM.
- Prospective sample-size quantities conflict: the protocol says 400-600 trial students, recruitment continues to 700 completed baselines, and the SAP power section says 300 per arm. The SAP names three model DVs but omits registry-primary peak drinks and leaves Gaussian versus Poisson errors unresolved.
- SAP page 2 contains the isolated past-tense phrase “Pairwise comparisons ... were conducted.” Its pre-start cover date and otherwise prospective language support retention at draft stage, but the wording is an explicit provenance-review gate rather than ignored evidence.
- The 22 requirements cover design, parent-level randomization, sample-size reconciliation, population, endpoint families and derivations, model family, estimands, HGLM, contrasts, covariates, Tukey comparisons, missingness, pattern-mixture/MI sensitivity, attrition, multiplicity, power, safety, provenance and masking.

All three annotations remain `draft_needs_expert_review`; promotion is not expert approval or a frozen release.

## Exclusions

- `NCT02781311` — protocol leakage. Protocol pages 38 and 42-45 disclose mITT and safety populations, two-sided alpha 0.05, no multiplicity adjustment, co-primary hypotheses, ANCOVA, sample size and no interim analysis.
- `NCT03235440` — wrong document type and chronology. Both documents are dated 2020-09-01 after actual completion on 2018-06-15, and the two-page analysis file describes paired t tests, repeated-measures MANOVA and subgroup analyses as already performed.
- `NCT02041299` — protocol leakage. Protocol pages 6 and 8-9 expose the noninferiority margin, power assumptions, ANCOVA, mixed models, subgroup analyses and safety methods.
- `NCT04306965` — protocol leakage. Protocol pages 4-5 already give sample size, primary response, descriptive analysis, the completion-only efficacy population and safety summaries; the two-page SAP substantially repeats them.
- `NCT04481685` — protocol leakage. Protocol pages 10-11 and 49-51 expose FAS/PP definitions, response handling, confidence interval and logistic regression, MMRM, log-rank, intercurrent events, missingness, multiplicity and stopping rules. The shared 2023 date is also after 2021 completion.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02805257 | promoted | 10 / 4 | 10dda46d371447285eaf29e697f5b51eebf22c0e9042ef869e0234c6eee7c645 | 9bee42970603d00041aa1c284bbcdafbafee100c7310483bec7e7cc6f103570f |
| NCT02781311 | protocol leakage | 102 / 32 | 8be2f3ce7f07505a0918bab2a859205323b44af92221d0ac8d0f02d5bacb3821 | 51c0ed0a51eb73ce5aa3f01748c0b161dccc578b996d1e325e90fa00c70398a1 |
| NCT03235440 | retrospective post-completion | 10 / 2 | 56e8960f6707453dff0cea287d1eb641fe55a9c36f065944569f4c989bbfedb1 | c91fab63144519796c89a96011f6c7301407168930af9f41e981ea6c6a90265d |
| NCT07484620 | promoted | 9 / 12 | 8cdc6e0d597dfc6b814636a4a4e107c730bbdd13d6e03392489d36cd53be133b | 913b78f0ebab0807279fc709c69aa609e04e9db9bea27ef6b2f2cbd0948ca8d4 |
| NCT02041299 | protocol leakage | 99 / 60 | 635809e89f903df151ec2a7ca8857a894ab600a33cf686554c1d468a6871b53a | d2a2274a7d72d745e0e742011b2a067d13bf36020336f6b8f72d528e4b119934 |
| NCT04306965 | protocol leakage | 23 / 2 | 0007841e9f77ad851341b1b5b988239830cc941d0f91d049d07398d820df4915 | c0db86e5b531296aa88e6e8e63f7f680d339bbe9f9fc1e0d021e1d5803ce801e |
| NCT04481685 | protocol leakage / post-completion | 71 / 6 | 68ff44c058691ba3a7455cc45e8f682971657b7e309aebc90bc63e6e30aa0115 | ed811eb80c70dfb209fa9f6aa81c23a5eaacfa8ea4dbde63618f7c14947ad510b4 |
| NCT04549454 | promoted | 19 / 3 | 2db2b7aa93be677164e55af7ab01b9c0dd04dabfd4560e5c71372ca44a983c78 | 6a5db64eea93114a0243aad3b640e2a55ee959277bebcaccab73bc36c9d94f95 |

## Review gate

Only NCT02805257, NCT07484620 and NCT04549454 enter the registered benchmark. Their reference SAPs remain annotation-only. The five exclusions remain outside the actionable pool. After refresh, the working collection contains 80 public first-pass drafts and 40 metadata candidates; all rejected slots were replenished, preserving the 120-family intake.
