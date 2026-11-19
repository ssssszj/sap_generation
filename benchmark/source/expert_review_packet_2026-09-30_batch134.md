# Expert Review Packet: Batch 134

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 134 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,089 physical pages. Every page was text-extracted, and 196 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT02027701 — exclude: IgPro20_3004 is an extension of pivotal study IgPro20_3003 and imports its treatment state, relapse history and cross-study baselines; the protocol exposes analysis sets, missingness, snapshot timing and the descriptive program, while the SAP records changed snapshot/submission conduct.
- NCT02403323 — exclude: GA29145 is an open-label extension of parent study GA29144 and imports parent-study baselines and eligibility; the SAP was written after last dosing and fixes a database-snapshot analysis, while the protocol already exposes the descriptive efficacy/safety program.
- NCT02722837 — exclude: the SAP is dated after primary completion, cites the 2015-07-17 original protocol rather than selected Amendment 1, and the selected protocol independently exposes the SVR12 population, imputation, exact-CI analysis and sample-size program.
- NCT02837952 — exclude: both selected Protocol Amendment 1 and SAP Version 1.0 are dated after actual study completion, the PDF approval trail is later still, and protocol pages 53-56 substantially reconstruct the populations, primary/secondary models, sample size and safety analysis.
- NCT02966028 — exclude: SAP Final is post-completion, and Protocol Amendment 5 explicitly adds analyses in response to an equivocal futility result from the interim dataset; the protocol and SAP also expose the executable ANCOVA, interim, imputation and conditional-power program.
- NCT03315780 — exclude: the SAP cites the 2017-07-12 final protocol rather than selected Amendment (a), but the selected protocol itself exposes the sample-size assumptions, populations, mixed-effects model, fixed/random effects and no-interim decision.
- NCT04178967 — exclude: SAP Version 4 was triggered by a critical site-audit finding after primary database lock, and Version 5 was prepared after induction-treatment unblinding; this is accumulated-conduct-informed material rather than a clean prospective target.
- NCT04732494 — exclude: same-date Protocol Amendment 2 and SAP Version 1.0 both follow actual primary completion; the study was sponsor-unblinded, and the protocol reproduces the analysis sets, hierarchy, CMH primary test, missing-as-nonresponse rule, survival models and sample-size assumptions.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02027701 | related-study extension + accumulated conduct + leakage | 83 / 50 | `6f725a5936e2177dd90a5597ab0906e9b8f71d6fc67a807caae3e26775bfb26d` | `64955bc6915ba6b606282f63ecc65d9a8116af356392bca02789e6f2c12642d0` |
| NCT02403323 | related-study extension + post-last-dose target + leakage | 106 / 26 | `5f6d80765f6a73a7f1aad545ce7cecd4525602fb957e3982d20258da7b802522` | `f9fbd118f00372c376c59e19342640dc572328e695ba3358d692dd70ae4ac17e` |
| NCT02722837 | post-primary/version-mismatched target + leakage | 91 / 35 | `3317d181f9519334424ae9c65d70f38a11db33c53788e0fd37d009f91df8688b` | `060d19d33a866285790618129cec29100dc60125756401f431d80236103efacf` |
| NCT02837952 | post-completion protocol/SAP + leakage | 65 / 29 | `f3bb78dabd5541913dd0a5c79920d92be53a019bc536ead4c29b0daf4b40491d` | `8529590d1ebcbaecc3b9a03cd92aa2028ec38719dd930fc647c3db41ee8502f6` |
| NCT02966028 | post-completion and interim-result-informed target + leakage | 103 / 52 | `375cf408797e9a0d069ba680d5fe14eff792a95dc5ecf5ae52c9f44e6a6dd4be` | `5f68e51357dce723b2c01e51e5e26adb327051c800396b68dcb8cb5fa30a8d23` |
| NCT03315780 | protocol-embedded target leakage | 55 / 15 | `16bb8750d5082916064dffdfdfa3a2f7f72d919bc6712b46025886e2ecf09344` | `a4f3bf66ae6969f6c1587ee05c41372dba849a8af375262fd0d6355b229ce7fd` |
| NCT04178967 | post-lock audit and unblinding-informed target | 84 / 118 | `ba5e499aed5b7d5a71c1387d935bf6d0b8ee107a3417363d334c6907a0bdb2aa` | `81c81ebf4622ab4bcec8956fad75374094443e68f9b5401d1833aa7449efc7e7` |
| NCT04732494 | post-primary sponsor-unblinded target + leakage | 142 / 35 | `3ea6cd832b7bedf9643756569220ce3cb386b02ef81d395b7ed3eaea39cd8c47` | `58ddab5c64de8e4d6aa42f2a0b959a683fac265799bcfa23ce3b76a7549a06f5` |

## Gate interpretation

- A same-date protocol/SAP pair is not prospective when both documents follow the registered primary-completion date; this disqualifies NCT04732494.
- A nominal SAP date before full study completion does not rescue a target produced after primary completion, as in NCT02722837, or a revision that incorporates data-lock, audit or unblinding knowledge, as in NCT04178967.
- Parent-study rollover, inherited baseline and prior-treatment state make NCT02027701 and NCT02403323 study-family-dependent questions even before protocol leakage is considered.
- For NCT03315780, the unverified Amendment (a) linkage does not require guessing because the independently sufficient protocol-leakage failure already makes the pair non-promotable.
- Registry actual enrollment and dates were used only for chronology checks and were not substituted for prospective sample-size targets.

## Replenishment

All eight excluded slots are to be replenished from the official API. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates.
