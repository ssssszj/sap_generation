# Expert Review Packet — Batch 81

## Scope

Batch 81 reviewed eight ClinicalTrials.gov document families. One independent, prospective and identity-matched protocol/analysis pair was promoted to a first-pass annotation draft. Six families were excluded because the files were identical, the selected materials were the wrong or retrospective document type, or the model-visible protocol already exposed an executable target. One family remains on governing-scope/version hold. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology, model and decision-defining pages.

## Promotion

- `NCT01944423` → `PUBLIC-DCS-PANIC-SMOKING-001`. The protocol and independent three-page Data Analysis document share the exact title, NCT and 2017-06-07 date, before actual primary completion in 2018-10. The protocol supplies randomization, treatments, smoking endpoint definitions, visits, measures, prospective target and safety monitoring without exposing the reference's logistic GLMM, Cox, moderated-mediation, Bayesian-bootstrap or pattern-mixture methods. The 23 requirements isolate reference-only executable decisions to `confirmed_decisions` and keep unresolved populations, estimands, primary missing-data rules, multiplicity and safety conventions visible in `protocol_only`.

## Exclusions and hold

- `NCT02110485` — excluded because the nominal protocol and SAP are byte-identical 17-page protocol files; no independent reference SAP exists.
- `NCT02161757` — excluded because Protocol Edition 3 physical pages 96-119 disclose populations, derivations, sample size, hierarchy, primary and secondary models, missing-data sensitivities and safety analyses; the SAP Edition 4.0 chronology is also redacted.
- `NCT02152540` — excluded because the protocol upload begins as a consent form/IRB package and the nominal SAP is an entire research plan, not a distinct governing SAP.
- `NCT03646669` — held because the protocol is a roughly 400-participant Study 15-0667 supplement while the plan describes an 80-participant Aim 4 pilot, the protocol calls the pilot Aim 3, and the registry's 58 participants and ACQ/AQLQ primary outcomes do not establish that the plan governs this registered analysis.
- `NCT01640951` — excluded because protocol pages 65-71 already disclose the extension-study analysis and the selected Final Analysis RAP was released after study completion for CSR reporting.
- `NCT02332915` — excluded because both files postdate completion and the nominal SAP reports observed n=24, realized effects, test statistics and p-values.
- `NCT04710862` — excluded because both summary documents postdate completion and use completed-conduct/analysis wording.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01944423 | promoted | 29 / 3 | fbcf13cea28d6e6ebfd4165bc21c0fcb6f1c74dbce0c0e18efe9210b84ec1bff | a368b732682ef7f6d915787b3b7060106f25301f663c7806ac3982282cbd208b |
| NCT02110485 | identical-file exclusion | 17 / 17 | 4ce15780ba0d08e90cbe2a535dda9ecfb1fda9d58c7d882b3607c026d2bdf523 | 4ce15780ba0d08e90cbe2a535dda9ecfb1fda9d58c7d882b3607c026d2bdf523 |
| NCT02161757 | protocol leakage | 157 / 85 | 2e921576a3423ecb8e746400dbd4ec9fbc1ac06306363fada041c22d59f5bf49 | f3d0c3a356d0e84d5133d7a3182f1b85f1f9f682c8d5c1794d0caeb3dd13eae2 |
| NCT02152540 | wrong document type | 57 / 10 | c96b4fa6505f3a4c381c556b2d2e6d64ca24544508d19f77a9fd59bcd728a9b5 | ce300865bf048faec6f8d95a5e96b2513c3539410de1cb13e4179c2d447c274a |
| NCT03646669 | version/scope hold | 14 / 2 | 2dc73d105416afae981607cb845fee2e21adfccf663719e78944950f777b27f3 | e10ffe0c6187cd854361e52b6e9fa22bfe4116d9af808e50943b650f524737e9 |
| NCT01640951 | protocol leakage | 81 / 49 | 2129b688f205b057dbb994298cee46f9f00057f3d1594505285e4116aaaeff41 | 35af8d06020547ce05e9f9512a46f30839b7cc883f65fac3a3e538d2f1f829c4 |
| NCT02332915 | retrospective methods exclusion | 9 / 4 | 03436fd315f147b910478d4f7451f19b386873b48b4fc1cc9a8f45e9fce16d75 | c1a2303c756f70426af018d17e05b4eb08f08872356e3890746eee5385d01d98 |
| NCT04710862 | wrong document type | 4 / 2 | 4a34ea66f8c0eb705dcc10b825846e612d92e649943bcd82fbf0266a5e0e0dd7 | 4d25f46f0b349be3a8a6cd3bd9b08c0162961e846ac577561fee6753b87bfe48 |

## Review gate

`PUBLIC-DCS-PANIC-SMOKING-001` remains `draft_needs_expert_review`; it is not approved for a frozen split. Reviewers must verify every critical locator and adjudicate the source-printed cotinine unit, populations, estimands, GLMM/Cox implementation, primary missing-data rules, hierarchy, multiplicity and safety conventions. Reference SAPs remain annotation aids only and must never be included in `protocol_only` model inputs. The six exclusions and one hold remain outside the actionable candidate pool.
