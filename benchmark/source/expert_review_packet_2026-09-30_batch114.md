# Expert Review Packet - Batch 114

## Scope and decision boundary

Batch 114 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen official PDFs and eight registry records were downloaded sequentially, byte-checked, SHA-256 frozen and extracted page by page. The 94-page NCT06831448 protocol and 43-page NCT02576678 SAP required full-page OCR because native extraction was absent or font-corrupt. One hundred fifteen decisive identity, chronology, family-dependency and statistical pages were rendered from the original PDFs and visually inspected; OCR was used only to locate evidence. No family is promoted: four model-visible protocols substantially reconstruct the selected analysis target, three selected plans are post-primary, interim/conduct-informed or observed-data-informed, and one is an executed-data rollover dependent on three parent trials.

## Decisions

- NCT01560624 — exclude: the timing and blinding governance are plausible, but Protocol Amendment 8 physical pages 65-69 already expose the event-driven power, ITT attribution, stratified log-rank analysis, alpha spending, secondary methods, safety summaries and interim governance; the SAP mainly adds implementation details.
- NCT06831448 — exclude: prerecruitment CIP Version 4 physical pages 18-22 expose the Newcombe non-inferiority tests, 15% margin, alpha allocation, complete sample-size assumptions and two fixed endpoint hierarchies. Version 4 also contains substantive analysis changes and is not merely an administrative successor to SAP-cited CIP Version 2.
- NCT02683746 — exclude: the RAP follows both primary and final completion, while protocol physical pages 60-66 already expose the non-inferiority MMRM, populations, covariates, missingness, safety and power program.
- NCT03482635 — exclude: TSAP Version 3 was revised due to early termination and describes first and second interim snapshots, use of results for authority interactions, and comparison of final results with prior interim results.
- NCT04603495 — exclude: SAP Version 2 follows primary completion and incorporates post-primary FDA feedback; post-primary Protocol Version 6 physical pages 74-78 also expose the analysis sets, hierarchy, CMH/ANCOVA methods, missingness, safety and power program.
- NCT02576678 — exclude: the prospectively dated SAP is independent, but Protocol Amendment 2 physical pages 55-57 already provides the safety/PK sets, feasibility target, descriptive safety, noncompartmental and population-PK methods, parameter list and dose-selection interim program.
- NCT01266902 — exclude: this is a continued-access rollover dependent on C204/C209/C215 baselines and prior treatment; the selected SAP analyzes an already observed 2018-02-08 data cut through Week 360.
- NCT03950791 — exclude: the plan explicitly says the Mann-Whitney U method was selected because observed MED and difference-score distributions were non-normal.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01560624 | protocol leakage | 87 / 52 | c8df60616c84ef56b0c4f80fea52ae7956708ae33adfa6494a58f4f6ee92dc4b | 1f102cb6da151d985b1490d1f72728e6dd0752673fb53dc1bc26a748d225ea49 |
| NCT06831448 | protocol leakage and governing-version mismatch | 94 / 65 | bb5ac2116f87c97b10eda7bf382c77369d6c546edb98bf28966cdd23f07c5d52 | adfcbdf5f755af0fb6a8496d7f66a670004a3474d4e8707fbb0612a5af1f7eb8 |
| NCT02683746 | post-completion RAP and leakage | 146 / 96 | 6c75b5772853d064bd65177418b6e2b0c23a0bc550bad7efdfab7c21f0c1bc86 | 4fb4a9c0dbed7b79adde12bb5c56f13efdc3de6a27e24595ff4026c7b2ecb3ea |
| NCT03482635 | interim/conduct-informed revision | 154 / 80 | 2899bee6fc969ad03b87ee21cc9ef4e6e9ac5e5bb81ff6c04a446d48c9a8c31f | 419db0f5d682faf819ab5efe37f508cc6b80eeb0690a703cf5296d3e9903e056 |
| NCT04603495 | post-primary/regulator-informed SAP and leakage | 102 / 74 | bffe1605bea59251d153912d5a3d93412d68dc4f5db7df4b381d0691ddd1e398 | a3c08334042752184d4ce732b3f9324983ca4ce716bbd76bdbb2ff0d4136c7f0 |
| NCT02576678 | protocol leakage | 98 / 43 | d43506b8ffea617b950eb8897e02967bb018c18444c47f9138d4498015400fb1 | d66e062495a7ffac86e2de524dc78dc7518ce4586e6f852b79c50d88d61c2276 |
| NCT01266902 | executed-data parent-trial rollover | 84 / 21 | f89ae3882dd30ea8b4e280e145114d2504f8d71acc9c2221ca046f307e67c46c | 1a7b87d6be9eff8a07981346b35155751cccf5d44bc05744d99c1eb26a2e3717 |
| NCT03950791 | observed-data-informed plan | 12 / 2 | 00fe32eb8a3739c40e43f17346b85493f331b1bc3bb72184c3a45e08f510b1e1 | 4bb3f19d846b9b08122709109fe8a069290251b98e041cdd177ef9d631b8b2c3 |

## Review gate

No Batch 114 family enters the registered benchmark. All eight slots must be replenished so the release intake remains 100 version-verified public drafts plus 20 actionable metadata candidates.
