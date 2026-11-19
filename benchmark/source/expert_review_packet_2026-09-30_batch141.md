# Expert Review Packet: Batch 141

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 141 review-queue head were reviewed against prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,084 physical pages. Native text was extracted from every file except the 17-page scan-only NCT04448847 SAP, which was fully OCRed. A total of 344 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. Seven pairs were excluded and one survived first-pass promotion. This remains draft work requiring independent expert review.

## Decisions

- NCT02542605 — exclude: the conduct-era protocol amendment records observed safety, adverse-event and PACAP-38 pharmacodynamic findings from the first three cohorts and uses them to revise the study; the SAP also removes ECG summaries in response to realized data collection.
- NCT02935686 — exclude: the late protocol and SAP incorporate years of conduct, late boosting and COVID/TTS changes, while the protocol exposes populations, sample size, immunogenicity tests, safety and interim methods.
- NCT03060577 — exclude: the SAP postdates primary/study completion, and the protocol records actual enrollment, COVID changes, interim/parent-study results and the executable population, endpoint and inferential program.
- NCT03237481 — exclude: although both documents precede completion, the model-visible protocol supplies ITT/PP/safety populations, ANOVA, multiple imputation-by-carry-forward choices, hierarchical multiplicity and the no-interim rule.
- NCT03622593 — exclude: the near-primary-completion SAP jointly covers YOSEMITE and RHINE, incorporates COVID intercurrent-event strategies and is paired here with only the RHINE protocol, which itself exposes the MMRM, estimand, missingness, multiplicity and noninferiority program.
- NCT04253236 — exclude: post-termination SAP Version 3 states that treatment stopped for an observed lipid signal after five participants, Version 2 was written during interim CSR preparation and Version 3 was reduced to listings.
- NCT04448847 — exclude: the SAP was signed after study completion, states that biopsies are analyzed after unblinding and cites a completion-day slide deck.
- NCT07452055 — promote as `PUBLIC-EMBRACE-BC-001`: the protocol and SAP share exact title/NCT/date identity, and SAP Version 1.0 explicitly governs Protocol Version 3.0 dated 2026-02-24 before the 2026-03-24 actual start. The protocol supplies design, endpoints, N=440 and an MMRM skeleton without exposing the reference-only MICE/completer, count, competing-risk, subgroup-interaction or engagement program. Unsigned approval, masking and unnamed-covariate gates remain open.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02542605 | conduct/outcome-informed target and protocol | 116 / 28 | `16a770a9d31646e4dc967a7d7edb3ca8f89b26fde62535a844a442db29d91dfa` | `c674a968aec0d48d888a4b0ed625a52628dded40a9a8c341717d892bad8278ad` |
| NCT02935686 | conduct-era target plus protocol leakage | 150 / 23 | `a0e6d8773bbc75fdf0de5aa4d9932432d33ee8fb2fd9b0434eed1247dc074cc1` | `ec713a47aabf8c168e5e21a73ae7de31151b4fdd80a51ed79a15160c2e247548` |
| NCT03060577 | post-completion/parent-result-informed target plus leakage | 70 / 34 | `9d4851d6206b79de05b5818f005166ba6c73754c17c2aadc06ebc26ed21e75e2` | `9bf6d371480002748bbd3232dd932c3f4acf42920d9d7b4dc34a1eb543f9cc6e` |
| NCT03237481 | protocol-embedded target leakage | 80 / 40 | `5f8e7db20cb4e59e7483d2b33ddd62757cfd06b5c47122074eca4bfc2d49c7e9` | `8b163df61dba38fe09e14d8ec14c6c2bdea9165b8400f3341b6e9e1a0051ada4` |
| NCT03622593 | cross-study target plus protocol leakage | 292 / 79 | `a015b16f473da3539c2508be947f78771cf577136cdfbde967962ac4d738c14d` | `06fcac73298fbdd1187a36ae889fec82f47b419f95e029aa4166b556068f2f13` |
| NCT04253236 | termination- and CSR-informed target | 70 / 24 | `a835935570091d5ee4e4663839cf6d8b742c373dc004a475c10742bc7c45cfdc` | `e0b934181f1724a276599fe63307a24dc60765d4855b7fc6289e864287307131` |
| NCT04448847 | post-completion/post-unblinding target | 42 / 17 | `e0f6bb66c044cdc91526aac65830206a491be92366e9e7cd740bba54ba583052` | `71c099aeb59deacb7ad481cdb67725f96a866c360d71b2b6591b5d7ba6a5ac15` |
| NCT07452055 | first-pass promotion with governance gates | 9 / 10 | `1b2fcb92bb0eebcd1f808b27605127477c277c21fc6fd854aa73da698181388a` | `4e5e606b7c9c8a249bd995662b56a9a0dc2a9de4edab06f9cf4f3abb508e6e54` |

## Gate interpretation

- Outcome-uninformed timing is evaluated from document content and chronology, not merely a PDF label. Observed cohort safety/pharmacodynamic findings, termination signals, unblinding, CSR preparation and actual data availability disqualify a target.
- A protocol may state design, endpoints and sample size. NCT03237481 fails because it additionally provides populations, executable tests, imputation, multiplicity and interim rules; the other excluded model-visible protocols similarly expose enough implementation to reconstruct their targets.
- A SAP shared across two trials is not an independent single-study target when only one governing protocol is model-visible.
- NCT07452055 remains first-pass rather than expert-approved. Its exact same-day Protocol V3.0/SAP V1.0 match and prerecruitment chronology support promotion, while missing signatures, masking implementation and unnamed covariates remain second-review gates.
- Registry actual enrollment was used only as conduct context and never substituted for a prospective sample-size target.

## Annotation and replenishment

NCT07452055 adds 25 atomic evidence-backed requirements covering provenance, design, population, intervention, randomization, masking, visits, endpoint derivation, analysis sets, estimands, MMRM, uncertainty, missingness, count and competing-risk models, subgroups, engagement, multiplicity, sample size, safety and reproducibility. Reference-only decisions remain in `confirmed_decisions` or `needs_confirmation`.

The seven excluded slots are replenished from the official API, while the promoted family consumes one candidate slot. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates.
