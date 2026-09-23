# Expert Review Packet — Batch 65

## Scope

Batch 65 reviewed eight ClinicalTrials.gov protocol/SAP families. No family passed the public, prospective, version-matched, independent-hidden-target gate. Six model-visible protocols expose material executable analysis content, and four of those families also have post-primary, execution-informed or non-independent extension defects. One selected technical SAP is a post-completion, multi-trial expanded-access package rather than an independent study-level target. The remaining version-matched pair stays on hold because the public PDFs obscure its prospective sample-size and allocation design. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages.

## Exclusions

- NCT04109547 — protocol pages 87-97 expose estimands, populations, sample size, MMRM, imputation, sensitivities and closed testing; SAP is post-completion.
- NCT03451292 — protocol pages 60-65 expose populations, survival analyses, sample size and fixed-sequence multiplicity; SAP is post-completion.
- NCT05239039 — SAP Version 2 is post-completion, records late analysis changes on page 21 and jointly covers three expanded-access trials.
- NCT03089944 — protocol pages 148-154 expose both primary analyses, confidence-interval rules, success thresholds, hierarchy, sensitivities and multiplicity.
- NCT03486457 — protocol pages 95-96 expose sample size, population, primary inference, missingness and MMRM; Amendment 4 uses observed COVID-related missingness.
- NCT02525874 — protocol pages 59-63 expose the pharmacodynamic population, detailed MMRM, intervals, interim analysis and sample size; SAP is post-primary-completion.
- NCT01090414 — the SAP combines the extension with several parent studies, while protocol pages 20-21 expose population, no-imputation and descriptive analyses; the family is not independent.

## Hold

- NCT02731573 — Protocol Version 05 and SAP Version 3.0 match prospectively, but public black redactions obscure the planned total sample size and Part 1/Part 2 allocation, and SAP page 11 retains an unresolved protocol-table query. Hold until an unredacted contemporaneous pair is available.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02731573 | public-redaction hold | 59 / 24 | b2a5fec00d923fee33e569db9543cbbfe72fafd7ede3d10fe6265714b64137a9 | 4feffe7aaf76028dfcb7d961acb820bedb1123041f94ba32c873143946184711 |
| NCT04109547 | protocol leakage plus post-completion SAP | 149 / 31 | cbee4363656ed5278083944d9ac4ee17c0dcd60461b547f7499f37da7c1845f6 | 378cd96b6bba015319a71cdd4a42c6e8445bde96c1b1ddc23e18436da3524215 |
| NCT03451292 | protocol leakage plus post-completion SAP | 88 / 53 | 4ea5668f39c39b3a5debd43c739e75a2f7c8e018d30e3495f225a7b3211e380e | 2dba83464ffd09b2ec57857260d1a150b6682fc43cf223fe416642670c8409e0 |
| NCT05239039 | post-completion multi-trial TSAP | 53 / 21 | a934860cec40a149a984e45c3e2a6c3b98daead5eaf5173277f8832b6434f5fe | ee25abc68a0c54752e9940ff292072e464ede3ced13836fd70f92a879c2c130c |
| NCT03089944 | protocol analysis leakage | 160 / 54 | 463718b3f0ef19c484422856904f27b0405128d7aa36bd0812cb5b3299b7ef98 | dedff57eaf6bf7f323c2d9f741684d5f4066844f6333d11e1659fbe8e2ab6230 |
| NCT03486457 | protocol leakage plus execution-informed amendment | 117 / 64 | 50d1dd62a1b3a5bb6e6d84815d95405ef366e2def872f57c70322ca7fee1742f | e03e3a846a8a3c4fb065da60746a828c89729cb6b4c653a265f03b2c2c7a650f |
| NCT02525874 | protocol leakage plus post-primary SAP | 142 / 48 | f7093c3e5c71aaa36cd4c8b9d7c3548e6b9c7591c5c73817fe68170908bf82dc | c1e8a780fc1920f44524baa70fd748cdc1206fb7afd9a18d0a167b4d69d67e9a |
| NCT01090414 | non-independent extension plus protocol leakage | 26 / 79 | 7714bc440c48313b8e9a653c40a7f69d53be4412603332bf6d3010c7a95ea493 | 2ce4615ba1ed780893b005584d3e64b54b3449b2f129ebcb5ab41442dfd0f390 |

## Review gate

None of these eight families may enter train/dev/test. The held family requires an unredacted contemporaneous source before reconsideration; the seven excluded families remain outside the actionable pool. Batch 65 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
