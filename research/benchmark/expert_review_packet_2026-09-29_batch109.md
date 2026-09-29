# Expert Review Packet - Batch 109

## Scope and decision boundary

Batch 109 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Seventeen official PDFs and eight registry records were downloaded sequentially, byte-checked, SHA-256 frozen and extracted page by page; the extra PDF is the second governing protocol for NCT03503812's shared asthma/atrial-fibrillation SAP. Protocol/SAP covers and 94 decisive identity, chronology, redaction, statistical, interim, sample-size and multiplicity pages were rendered from the original PDFs and visually inspected. No family is promoted: four have protocol-side executable-plan leakage, three use post-completion or executed-analysis material, and one is held because decision-defining public content is redacted.

## Decisions

- NCT03503812 — the two Action C7/C8 protocols form one model-visible family; the AF protocol alone exposes the power, Mann-Whitney-Wilcoxon, case-crossover, conditional-logistic and Poisson hierarchical analyses repeated in the shared SAP.
- NCT04476043 — hold: black CCI redactions obscure sample size, alpha, primary, sensitivity and secondary methods in both the otherwise identity- and chronology-matched protocol and SAP.
- NCT02211261 — protocol pages 113-119 expose cohort sizes, PK populations and derivations, mixed modeling, safety, ECG and interim rules.
- NCT03107793 — the final SAP follows actual primary completion and includes the Week-16 interim attachment; protocol pages 80-83 also expose populations, power, Fisher exact testing, nonresponder handling and analysis sequence.
- NCT03814746 — protocol pages 108-112 and 119 expose the estimand, negative-binomial model, missing-data/supportive analyses, closed testing and power.
- NCT02636699 — SAP Version 4 follows actual completion; protocol pages 92-104 also expose populations, imputation, models, hierarchy, safety and power.
- NCT03123289 — protocol pages 10-11 reproduce the complete two-page SAP analysis.
- NCT03045081 — both files are post-completion Journal of Pain submission materials reporting observed enrollment, evaluability, balance and fitted-analysis results.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03503812 | protocol leakage | 26 + 26 / 5 | 5d17271914e21ea6403fe7ded25f79f7e28fff826de5ef0e0fad7954e6098d85; AF: 53b46f8a55fce76bd115a2bc8f8cc80c7d52fcb30b36656962c222709dd8da2a | 8ae0ce4672c3c1d2f3287980360044f5168122b34345af02a19990295604fa2a |
| NCT04476043 | public-redaction hold | 95 / 66 | 7ec0de3fa137b6ace9b9a8eae6455dfd0f5cd13f26c65647bf62e15689265125 | 33237dba960d8eeafcfcc57c16a3eb42665e00b9294f1853d0a21204dc0dad64 |
| NCT02211261 | protocol leakage | 125 / 28 | e84ef14bab801951429e4c143bbe8b034d626ae4d08b351ce854fbc20d39ea15 | c20af5a547ecad1b433a0d30553a2dd1cabde1da956874d255e08021f83e1dc1 |
| NCT03107793 | post-primary SAP and leakage | 137 / 49 | 124ff2a6d8354e72f3180a37c988537dbe3f8274939ebd4626348cb734e6ace3 | cf05ee327f005d5b5375427902683d59dd93320e0b20b7daefe5cf9c2de93e77 |
| NCT03814746 | protocol leakage | 125 / 57 | 7801a7b55103835792ba7f319ff42990d92154cb07286847908a47ca4dab794f | 6874c47dc0b099132ecdc61647c9acfd496c03874baff5d236a3ffbf720943a4 |
| NCT02636699 | post-completion SAP and leakage | 142 / 80 | d538082a86fd4006f8b40c9236e4beac2ceee5048183cbacaf30c82320dd1d90 | 4ee6d3a2a38007bf14b5fe468905116f49576930d7fa75dc5516d03027782bd9 |
| NCT03123289 | protocol leakage | 13 / 2 | e1a949787ba7348e57d6cae92f28ee29019d194e7eb459dc290cb09c57d63d5f | 4e67d5bd767437070c876f973d5af7cdf505a99cdafd9aa469b4535884d83ba5 |
| NCT03045081 | retrospective executed methods/results | 5 / 2 | 050ae994858d345d0f3e0babbec04feff15884bf1604707229a518c705eb0d6a | 89d50d2f4159742442f3735d2768e8e65211ad7450d7f23b8dc55eee0d980665 |

## Review gate

No Batch 109 family enters the registered benchmark. All eight non-actionable slots must be replenished so the release intake remains 98 version-verified public drafts plus 22 actionable metadata candidates.
