# Expert Review Packet — Batch 63

## Scope

Batch 63 reviewed eight ClinicalTrials.gov protocol/SAP families. One family, NCT03309917, passed exact identity, prospective chronology, independent-document and non-complete-leakage checks and received a 20-item first-pass annotation. Six families failed because their model-visible protocols expose executable target analyses; NCT02967991 failed because the selected analysis document describes a materially different study design. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages. The character-spaced NCT02627196 protocol was fully OCRed before review.

## Promotion

### NCT03309917 — `PUBLIC-CEREBRAL-BLOOD-FLOW-MAP-001`

- Identity and chronology: the independent protocol and three-page statistical plan share the exact title, NCT03309917, unique protocol ID H-17021598-61256 and date 2017-12-22. The frozen registry records actual start on 2017-12-27 and completion on 2018-04-19.
- Non-leakage: protocol physical pages 5-10 define the three MAP conditions, randomized envelope order, measurement and restart rules, four outcome contrasts, carotid-flow and blood-gas corrections, and sample-size assumptions. They do not expose the reference plan's REML repeated-measures model, transformation/Friedman/Wilcoxon fallback, or slope-interaction mixed model.
- Annotation: 20 atomic requirements cover design, timing, randomized order, outcome hierarchy, derivations, power, reference methods and explicit confirmation needs for covariance, population, incomplete sequences, missingness and multiplicity.
- Review focus: confirm that the protocol's partial statistical content remains below the complete-target leakage gate; adjudicate the mixed-model covariance and inference details and the incomplete-sequence and type-I-error strategies.

## Exclusions

- NCT02627196 — excluded: protocol pages 49-52 expose randomized and safety populations, negative-binomial primary analysis and adjustment, directional hypothesis/success, event-driven power, interim analyses, site pooling and interaction assessments.
- NCT04167553 — excluded: protocol pages 113-116 expose safety/PK/PD populations, missing-data delegation, placebo pooling, descriptive AE/PD/PK and dose-proportionality analyses, interim review and sample-size allocation; SAP is post-completion.
- NCT02967991 — excluded: protocol page 13 describes the 20-subject 19G/22G needle study and its Mann-Whitney-Wilcoxon analysis, whereas SAP page 2 describes 40 subjects in wet-heparin, dry-heparin and control comparisons using McNemar and Wilcoxon tests.
- NCT04999839 — excluded: protocol pages 81-83 expose sample size, ITT/mITT/PP/safety/PK populations, hierarchical CMH primary analysis, MMRM secondary analysis, safety and no-interim rules; SAP is post-completion.
- NCT02891408 — excluded: protocol pages 62-65 expose analysis sets, data conventions, PK ANOVA and interval criterion, safety, no-interim and sample-size methods; SAP is post-completion.
- NCT03390036 — excluded: protocol pages 40-47 expose sample size, endpoint hierarchy, Fisher/ANOVA tests, ITT/PP populations, MAR multiple imputation, sensitivity and safety analyses.
- NCT02462603 — excluded: concatenated protocol package pages 39-40 expose EITT/safety populations, descriptive efficacy/safety analyses and adaptive sample size; SAP cites older Amendment 2.0 rather than the package's later Amendment 5.0.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02627196 | protocol leakage | 65 / 34 | fb23bc908df0f19fa9d36d56a8687b3673b913edabd91cc6fc8aff3cc8e9a848 | 6be35a508f59662473258abba508bbf1465f641da4cb7b0e560a6b0dcc026450 |
| NCT04167553 | protocol leakage plus post-completion SAP | 127 / 43 | f2e41a8bdfbc535428098efc6dd415c9e144170d3e53e4eab7a2437420cb07c7 | 07ddca6d537c2700862a3c7827598e835f0a6e4d8ed547ab01a21d0373c30ac4 |
| NCT02967991 | mismatched analysis document | 23 / 2 | 70c9eed23ba975131b4c22a9c79858e610f2fe09e7706db65b4f00e0c7775e37 | a4798c3c28b316366f49a66674d22c0c34b49b32b5d311f7a3f42651ef6a477c |
| NCT04999839 | protocol leakage plus post-completion SAP | 95 / 46 | 1998adbc9ae5c9f6c0d926a99dd40c3c1e617581696fed6ea95228016fb47415 | c47d5e75c31775b7de5daf3e2250d8f775cf3753d523e67147a557aaca079878 |
| NCT02891408 | protocol leakage plus post-completion SAP | 100 / 38 | e8c940beb08a4798cb76b78532619788455b2b1b9cb629620df2904da5c883b2 | 196204dfa7e9b90defe6bd424e313360dc574de14d0b752e3f88f18e8de82140 |
| NCT03390036 | protocol leakage | 84 / 16 | 1c0ed850d6db92e44333121b8b93d9fb7feb4c4ab0e75a9046aa1f8ec54dd81a | 69b260dd4f3c63aff25ab94821d941f7f8f036cfc3dacfe7531a3baf2d0b7745 |
| NCT02462603 | protocol leakage plus governing-version mismatch | 362 / 18 | 8923cd6a22b0d233df4da77394d8b647d1b03eb7f7269e5a794fe87c01f546e6 | 44f8454f93ee269c695a51fc277829b6e904374a363e5f36101286797d1206b8 |
| NCT03309917 | promoted | 13 / 3 | b60f55d02e9bdf3f3fade5512093c7ba4ff68107840e12b638a6de32085ac368 | dd80fa98b456dfa697b57f70b77b3a38a0a2777795e419df8b9fa108ae0f69bf |

## Review gate

NCT03309917 remains `draft_needs_expert_review` and may not enter a frozen split until independent statistical review. The seven excluded families may not enter train/dev/test. Batch 63 increases the registered public draft count from 71 to 72 and replenishes the actionable metadata pool to 48.
