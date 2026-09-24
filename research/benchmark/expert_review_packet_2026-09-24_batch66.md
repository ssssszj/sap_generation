# Expert Review Packet — Batch 66

## Scope

Batch 66 reviewed eight ClinicalTrials.gov protocol/SAP families. No family passed the public, prospective, version-matched, independent-hidden-target gate. Seven model-visible protocols expose executable analyses; four are also extension or cross-study families, and two selected SAPs postdate completion. The remaining family stays on hold because its SAP cites an unavailable earlier protocol while the public later protocol incorporates observed interim data and the complete analysis. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. The scan-only NCT03763175 SAP was fully OCRed before review.

## Exclusions

- NCT02791230 — protocol pages 68-71 expose treatment grouping, sample size, survival/MMRM and safety methods; SAP combines parent and extension data and adds a site-quality-event analysis.
- NCT03651765 — protocol pages 57-58 expose the descriptive, available-data and safety plan; SAP cites an earlier amendment and pools index-study data.
- NCT05364554 — protocol pages 60-67 expose populations, estimands, models and interim use; the SAP jointly covers the parent and LTE studies.
- NCT03095638 — protocol pages 35-38 expose the PK populations, noncompartmental derivations, mixed model, geometric-mean ratios and confidence intervals.
- NCT03714672 — protocol pages 49-54 expose four hypotheses, Holm testing, ANCOVA, populations and missing-data penalties; SAP is post-completion.
- NCT02595983 — protocol pages 52-53 expose sample size, populations, primary t test and intervals, sensitivities and safety analyses.
- NCT01222767 — protocol pages 59-60 expose the Simon two-stage rule, success criteria, analysis population, exact interval and Kaplan-Meier methods; SAP is post-completion.

## Hold

- NCT03763175 — SAP Version 2.0 is based on Protocol Version 3.0 dated 2019-01-09, but only Version 8.0 dated 2020-06-30 is public. Version 8 reports observed disposition for 53 randomized participants and adds an interim futility analysis, so it cannot serve as a prospective prompt.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02791230 | extension-family protocol leakage | 91 / 21 | 28be3e5c45bd83faec71c36a8308eaff7ed0cf281cd13f7492e88d5f5123f729 | 684eed1f7bd26efa1114cfeb8cf2acdfe6ea4cc377fa06c538ee743c9fee300e |
| NCT03651765 | extension leakage and version defect | 71 / 30 | 84aa6c505dbacb23533c484259dd73c8ec5461fd6506cd7353cdcda419b743e6 | e9200ed58e7dba764a99534e2857ad92f9b525f5e1272ebb09425e15c6e468f6 |
| NCT03763175 | governing-version hold | 52 / 23 | 9b7b9f716325cef6eea06ab89ce96a1978ce7fd027fb60da5c417a9f272de446 | c9d5b6510f9072b069ca68fe199661ed8428fc8be8efed8bd4b8b9fb23aafd0e |
| NCT05364554 | parent/LTE combined SAP and protocol leakage | 107 / 83 | 1daa6e30646e2204e5701347cd2db341a220012b06b29865fcc9cdb0545b125c | 11fb8133021867164ebf35df504411b6dbf38f83a7d69511f756c2b0dca3bf00 |
| NCT03095638 | protocol analysis leakage | 82 / 44 | 02364ae7b4570e2f873c2a3913f849463ecda441d656bda0ff755269d634df24 | 14c929640b3f86dcca87c7978c958a5234afe9f2de4e7b85e1977930f53d7f66 |
| NCT03714672 | protocol leakage plus post-completion SAP | 72 / 43 | 76880cf42e8029f5ae3418288912d96ebb409faf42b3deba89ae675e5e574abc | b58b330f63b0b641ef12a0fa4a4833fd881fc7d893c1f0e5802a03c3011a808d |
| NCT02595983 | protocol analysis leakage | 67 / 36 | 7172ed867d06a8856d547f1015ac342eb7539a59bb1a596b743a519bca110ff8 | 327ac86127d17e90fde17107c915fd8fd890b1678b948595b266a8734e9fcc06 |
| NCT01222767 | protocol leakage plus post-completion SAP | 95 / 49 | 8d33281a69600295e07c6ca9706f06cc2dfffa652568d122fd13ccff0d47a5e3 | 30db0ee6870e5d1c96e5da7941be7b5475a51784fdbc0aea8daf055638e5eca4 |

## Review gate

None of these eight families may enter train/dev/test. The held family requires the actual prospective Protocol Version 3 prompt before reconsideration; the seven excluded families remain outside the actionable pool. Batch 66 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
