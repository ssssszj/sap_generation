# Expert Review Packet: Batch 139

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 139 review-queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,447 physical pages. Native text was extracted from seven pairs; both NCT01817426 files were image-only, so all 76 pages were OCRed. A total of 125 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT01817426 — exclude: the SAP postdates study completion, records realized enrollment of 115 rather than the planned 136 and changes the primary endpoint because accrual fell short; the model-visible protocol already exposes the survival, regression, sample-size and missingness program.
- NCT02408549 — exclude: this open-label extension depends on actual parent-study SP0982 event and rollover states, directs the analyst to SP0982 SAP Amendment 4 and incorporates several years of protocol/SAP changes after conduct began.
- NCT02838407 — exclude: the protocol and SAP both postdate primary and study completion, while protocol pages 41-42 substantially reproduce the analysis cohorts, estimands, exact intervals and descriptive program.
- NCT03000439 — exclude: late Protocol Amendment 8 records actual accrual through November 2022 and redesigns the study around two planned flare analyses; it and the near-completion SAP expose the exact group-sequential efficacy/futility program and models.
- NCT03022708 — exclude: the pivotal design was created after six early-feasibility subjects produced positive 12-month findings, and both documents incorporate those realized results into the target analysis and sample-size program.
- NCT03596450 — exclude: the protocol exposes the executable estimand, hierarchy, models and 500-imputation program; the SAP explicitly logs changes since first-patient-first-visit, including enrollment-facilitating population expansion, N=2250 to 1387 and power changes, and added subgroup/adherence analyses.
- NCT03673943 — exclude: the alleged protocol and SAP are result-bearing clinical study reports, not a clean protocol/SAP pair; they contain actual N=63, estimates, p-values, adverse-event counts, conclusions and post-database-lock review.
- NCT04607980 — exclude: although both documents are prerecruitment, protocol pages 58-62 disclose the equivalence hypotheses, margin, power, analysis sets, LOCF/observed sensitivity, ANCOVA, NRI, generalized linear models, safety periods, no-interim rule and missingness, substantially reconstructing the SAP.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01817426 | post-completion/conduct-informed target plus leakage | 50 / 26 | `7163e3cbf2beb520e080a4f7d7715c28f098d7314784d8dc0d5912196d61e248` | `a29423907d5e861f8987f7f7eaec3164b5a8c8efe6f99cb919de70bb925c1528` |
| NCT02408549 | parent-family and accumulated-conduct dependence | 275 / 175 | `f1d94fb2898ef1d5df9c5f49feae3e7ae54805dd63eb4ea43a5f5d5c236a076c` | `10accc49ba4fac17c798a7d2403a7bcc55609f460dd5ca54771990326c67f7c3` |
| NCT02838407 | post-completion target plus protocol leakage | 58 / 18 | `591c0008bffa20204d1a7b286f62c9b66fdbd1ec7945226fabc22b2c7f526bed` | `0e199685867021d3abfa23b3b6736f8a565f4d39ce0e2568ffed0e504437c73b` |
| NCT03000439 | conduct-informed group-sequential target plus leakage | 175 / 75 | `771d8db9cac07fbf9e4c7f1ca398ce6e213e429e4da7c1d37b3d3953d4e78433` | `1bec3096dd5c15b02dce1a769e9a686f995d0dcb23b62f94cff120a1fc004d0f` |
| NCT03022708 | early-feasibility-informed pivotal target | 76 / 22 | `570abc251d9eb13ab8e85c77edcf95fa627468d70979e136aaafd0f9e4414fa2` | `d17f16074d0bd0aa2333f2f9916d3532826df3faa77a1108c011ac5dc0882901` |
| NCT03596450 | conduct-informed target plus protocol leakage | 226 / 147 | `de19b0d5d05ca3c3f3ff21e82ea0f1fafba78c9841b32783def5044c485d2bd6` | `9a9833200e061e5752eb7f08a0689f68de6c5eead461cc365922f62713519418` |
| NCT03673943 | wrong document type: result-bearing reports | 77 / 4 | `5dacf26f4cd4f3894de6780146dded18278b8616041b4aeb1367fde82f6d8276` | `3b10123c27d14362921c834561af91fda7d470425878635a8ebe0e9f12f92c43` |
| NCT04607980 | protocol-embedded target leakage | 84 / 39 | `725b23df45c6315a8857a07c0b788e15eeae0fe04fa0b056c3c8fd63662df078` | `6afff33d3be0ff68592fdac300d5acac858db481af62109dcfc3dc5f48bcd2ca` |

## Gate interpretation

- A claim that analysis changes were made before inspecting comparative data does not restore prospective eligibility when the final SAP is post-completion and explicitly reacts to realized shortfall, rollover state, database structure or other accumulated conduct.
- Parent-study and early-feasibility outcomes are outcome-informed context even when the target is labeled an extension or pivotal amendment; a prompt/reference pair cannot depend on hidden related-study SAPs or observed family events.
- Protocol disclosure of design, endpoints and sample size alone is permitted. These prompts fail because they additionally expose executable populations, models/tests, missingness, multiplicity, interim boundaries or nearly the complete target.
- Result-bearing reports and CSRs are not repaired by registry labels that call them protocol or SAP uploads. Registry actual enrollment was used only as conduct context and never substituted for a prospective target.

## Replenishment

All eight excluded slots are replenished from the official API. The release-eligible intake remains 120: 105 public first-pass drafts and 15 actionable metadata candidates.
