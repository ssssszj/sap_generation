# Expert Review Packet: Batch 151

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 151 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, public-redaction, study-family and document-type gates. Native text was extracted from all 958 physical pages in the 16 selected PDFs, and 123 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03496207 — exclude: the extension SAP follows base-period completion and unblinding, uses realized randomization and extension-entry counts, adds a Month-6 supportive analysis and a cardiac-index subgroup, cites a different protocol revision from the selected public protocol, and targets a study-family program already exposed by that protocol.
- NCT04140032 — exclude: the two-page alleged SAP and its selected protocol both follow study completion, and the SAP describes models in the past tense. The package is an executed post-completion methods note and scale-calibration/COVID conduct dossier rather than a prospective governing SAP.
- NCT05375929 — exclude: SAP Version 3 follows primary completion, changes the primary and safety populations after that milestone, and plans summaries for an authority using initial results; the protocol also exposes the estimands, analysis sets, endpoint methods, confidence intervals, sample size and interim program.
- NCT03170609 — exclude: the SAP amendment responds to CSR-shell comments and changes immunogenicity analyses and timing, while the protocol already exposes the evaluable immunogenicity, mITT and safety populations, GMC/log-transformation/confidence-interval methods, safety program and result-driven cohort-escalation review.
- NCT03853694 — exclude: the SAP follows study completion and records that the 60-subject interim was completed and used to choose the treated-sample target; the protocol prospectively exposes the arm-selection, sample-size-re-estimation and endpoint-selection program.
- NCT02783573 — exclude: SAP Version 3 was approved after the study had stopped for futility and changes objectives, populations, stopping, missing-data, summary and interpretation rules in response; the protocol already exposes the sample size, populations, MMRM, covariates, missingness and conditional-futility interim.
- NCT00357682 — exclude: final SAP Version 2 follows study completion and performed two- and four-year interim analyses reviewed by the DSMC; the protocol already exposes the ITT/safety sets, log-rank, AFT/Cox, covariate, sensitivity and interim program.
- NCT03499873 — exclude: the public SAP materially redacts the sample-size rationale, PP definition and primary-analysis blocks, while the selected protocol independently exposes the 450-subject target, PP/mITT/safety sets, LOCF, confidence-interval margins, Fisher test, alpha, multiplicity policy and primary success rules. The protocol therefore reconstructs the target despite the unusable redacted reference.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03496207 | related-study-family/post-unblinding leakage | 101 / 34 | `934f8c4c408b2332d96ec4581fc6fdcf80205188c3747640082e08267fc38c66` | `824808db006c6352842039343a09b5717604218bd2b5860e11efe089a3686559` |
| NCT04140032 | post-completion executed methods note | 36 / 2 | `00d5cb39b7cd01f51e43941341d8bf75f5b635bf62998084066ab77d870c3907` | `0a9a1a2522a23ff5c8607f35ee98a9f112c502338ca991126c44d6a7ae5bb7e0` |
| NCT05375929 | post-primary/authority-informed target plus leakage | 112 / 29 | `cb681186c5069bf977e4778f90ff43fe2d4578a4a4c907c476b98d2da936636a` | `3a6dcc6d5460a9222ac368af3abac64671c72b212c9d47ef9a4294a9aea0e5aa` |
| NCT03170609 | CSR-shell/cohort-review-informed target plus leakage | 81 / 35 | `aeb6194caa15c744a9534f37ce4041ca1a05dcdab0a4e40ddd83c6ea061179f7` | `330b23b1204337a8d75369400ba22910e856360aa48277b125a8bbf225fb1aa2` |
| NCT03853694 | post-completion/performed-interim target plus leakage | 73 / 139 | `ffb18f3b0f25eb3c52034c7c02a9b5a0a8ad974b881840d1fab71afcb3c515ed` | `bfaa9de396dcdd24cba873d3377669a68236910306ce064c6777640d21159f58` |
| NCT02783573 | futility-termination-informed target plus leakage | 93 / 47 | `a71dfdd9554f2d384a750ce8a766e736caf245453c005506f894a952b3509ba4` | `9bac1eba92f501cc66d7fc2bcd3cd8920afb422085fd2cacf9ee83077592694a` |
| NCT00357682 | post-completion/performed-interim target plus leakage | 45 / 35 | `53c70559fe03ff2aa1d5967520eaba489231632159b86f3dfd179d49616c96cf` | `5a2d8217bb60a646de8269c1a417ae81e29185e08b934455a1d8a716a4c4a33f` |
| NCT03499873 | protocol leakage plus material public redaction | 73 / 23 | `fd4a1d83dd7f4f672d7e1ed08fb00a60e70e75e5334d24ea023585655b975f17` | `53aef5c7c0a87ffce3868d98d09305d0dd665fafc88dba8c7b8029a470724090` |

## Gate interpretation

- A later extension SAP is not outcome-uninformed when its analysis depends on completed and unblinded base-period state, realized disposition counts or added analyses tied to that state.
- A short document describing analyses in the past tense after study completion is an executed methods note, not a prospective SAP, even if ClinicalTrials.gov labels the upload as an SAP.
- Authority-facing summaries, CSR-shell review, performed interim selection, futility termination and DSMC-reviewed interim results are execution-informed inputs; revisions made after those events cannot serve as hidden prospective targets.
- Material SAP redaction independently prevents a complete judgeable reference. If the model-visible protocol nevertheless exposes the executable analysis program, the stronger release decision is combined protocol/SAP leakage with the redaction defect preserved in the evidence.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
