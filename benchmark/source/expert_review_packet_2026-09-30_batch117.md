# Expert Review Packet - Batch 117

## Scope and decision boundary

Batch 117 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen official PDFs and eight registry records were downloaded sequentially, byte-checked and SHA-256 frozen. All 274 pages lacking usable native text were OCRed, including all 222 pages for NCT06393452 and 52 scanned pages for NCT03758443. Two hundred forty decisive identity, chronology, version, family, leakage and document-type pages were rendered into 18 contact sheets and visually inspected against the original PDFs. NCT04111276 is promoted after exact identity and prerecruitment chronology review; six families are excluded for post-completion, conduct-informed, family-dependent or protocol-leaking material, and one remains on a governing-version hold.

## Decisions

- NCT04111276 — promote as `PUBLIC-OA-BRACE-GAIT-001`: Protocol Version 1.1 dated 2019-06-07, WIRB protocol approval dated 2019-07-11 and the independently authored analysis plan dated 2019-07-11 all precede actual study start on 2019-07-12. Exact title, investigator, institution and protocol identifiers match. The protocol gives the 20-evaluable/up-to-24 prospective target, within-participant brace/no-brace gait design, five stance instants and medial-condylar-separation endpoint but does not expose the reference-only test list. The reference's independent-cohort framing is statistically inconsistent with the paired design and is retained as a decision requiring correction, not an unquestioned gold method.
- NCT02019264 — exclude: Final SAP Version 3 follows actual primary/final completion, records a censoring change discovered during validation and is additionally reconstructable from detailed protocol statistical content.
- NCT06393452 — hold: the public prompt is Protocol Version 5.0 / Amendment 4, but the SAP explicitly governs Version 4.0 / Amendment 3. The missing Version 4 prompt prevents a defensible frozen pair.
- NCT02769481 — exclude: the final SAP follows actual primary/final completion, and protocol pages 65-70 already expose the populations, MMRM, missing-data sensitivities, hierarchy, sample size and interim decision.
- NCT03758443 — exclude: interim lack of efficacy terminated the study, and the selected plan replaces planned analyses with small-sample methods after termination; the protocol also exposes an extensive executable program.
- NCT06454630 — exclude: protocol pages 61-65 expose the Bayesian primary, populations, posterior rules, multiplicity, safety, PK and interim framework. The SAP date inconsistency is noted but is not needed to resolve the exclusion.
- NCT02749370 — exclude: protocol pages 44-47 expose the population, LOCF and observed-case rules, multiplicity/interim decisions, inferential outputs and safety program.
- NCT01934140 — exclude: the long-term persistence/booster extension depends on the MenACWY-TT-015 parent cohort, records an approval-delayed missed visit and result-timed analyses, and has protocol leakage.

## Promoted-family annotation gates

`PUBLIC-OA-BRACE-GAIT-001` has 23 first-pass evidence-backed requirements. Expert review must preserve the single-group within-participant brace/no-brace structure and fixed condition order; reject the reference plan's two-independent-cohort interpretation; adjudicate a paired condition-by-stance-phase analysis; and complete the population, estimand, missing-frame, multiplicity, effect-interval, precision and safety specifications. The prospective targets are 20 evaluable and up to 24 enrolled; registry actual enrollment 23 is conduct context only.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT04111276 | promote with paired-analysis correction gate | 18 / 2 | 5899fbab17d6a32c25662eb7a9b0a0068892b6dfd5cdad05dc639393e0fe4424 | 6d7192ab99d310782176b0bf7be1a4ea8ecd97f68fdded1d1ce8581a9fb6d5f1 |
| NCT02019264 | post-completion, validation-informed and leakage | 142 / 67 | 2c537d4a561c8ddafd3272eb0de198db939fa944eb907d8f7196078997e16869 | 0802d79437953d53ef2f4a3f5ceaddc861f6cc8b511fba60d6cf0e0d57a93618 |
| NCT06393452 | governing-version hold | 87 / 135 | 390bd0ac4150c7b7362347f68d55f3967558c4a176912530db00fc23d2e2b892 | c2b0f282670183ef7f2f5a62251b5165b86d83926c7d5df27a0579a3b8ee0ff4 |
| NCT02769481 | post-completion and leakage | 80 / 66 | 2711049340f3edceb95df6d39b75a1afe3aeef02e939d38b019ca2f83bb19bef | 6ee0163ec53cb4e4e6645ecac38bffe9a38ea068eaf97fb430d5dab28643438d |
| NCT03758443 | termination-informed wrong document and leakage | 145 / 111 | 29cec8c792900579f7e6d19375cb9052b1aa10a456360a1c1b0189d843574edd | 3bffb57f3a2848811be0d7eaccaa94f796e90ce4a666593f61970ed637c6f10f |
| NCT06454630 | protocol leakage | 79 / 42 | bb2055373916d8d0b2c5be95b1994ed2b22f5bd00b170f25122062f0538c27be | 87596887d86eafcb8c65dd610ec11a8cbd3d4123c4fc205297b102771050727e |
| NCT02749370 | protocol leakage | 61 / 26 | f3c830dd7d18284a5dd09cd2a544b5ac0b1b8ae3313c33aa7db1d5d222a58f1d | 8a356695765abb248ece97d9b68ee170065ebadc7cccdf0b3416a01e8d975d61 |
| NCT01934140 | related extension, conduct-informed and leakage | 94 / 21 | 8e2bc3a5f13931c81df012a9d97052f563e921839d22af730fa7029f664ba56c | 8b1199db4c7ce86e1f50f732f4db0ab9ff47392feb567f8979aed27ef97d07d7 |

## Review gate

Only NCT04111276 enters the registered benchmark, as a draft requiring independent expert review. The other seven slots must be replenished so the release intake remains 101 version-verified public drafts plus 19 actionable metadata candidates.
