# Expert Review Packet — Batch 17

## PUBLIC-SPARK-RBBB-HF-001

- 18 requirements; all remain `draft_needs_expert_review`.
- Confirm the exact match between Protocol 201409760 Version 1.0 and the independent SAP by protocol ID, investigator, title and 24 December 2014 date, before the February 2016 study start.
- Reconcile the protocol's binary primary endpoint (greater-than-15% LVEF increase at six months) with the reference SAP's continuous repeated-measures analysis.
- Complete the crossover model with treatment, period and sequence effects, participant-level covariance, an end-of-period contrast and a carryover sensitivity rule.
- Define missing-data and multiplicity policies and reproduce the omitted sample-size assumptions behind the planned 40 adults.
- Preserve the single blind and separate Dunnett-adjusted follow-up-versus-baseline comparisons from the randomized pacing-versus-non-pacing effect.

## PUBLIC-WE-CAP-COLONOSCOPY-001

- 20 requirements; all remain `draft_needs_expert_review`.
- Confirm the exact title, GAST-015-16S protocol ID, NCT03160859 identifier and approved protocol/statistical-analysis date of 2017-08-14, before study start on 2018-06-08.
- Reproduce the male target of 160 and female target of 96 from the sex-specific pilot effects, 90% power, 90% evaluability and final two-sided alpha 0.0492.
- Verify the single O'Brien-Fleming interim analysis at 50% information, interim alpha 0.0054 and final alpha 0.0492.
- Classify the male and female RTMIP hypotheses as co-primary, separate confirmatory claims or primary-plus-subgroup, and define the corresponding family-wise success rule.
- Approve the t-test/Mann-Whitney trigger, hierarchical site/provider model, ITT early-discontinuation rule, missing-data handling and Benjamini-Hochberg exploratory multiplicity plan.

## Version and source decisions

- NCT02441101: promoted. The protocol and SAP share Unique Protocol ID 201409760, investigator, title and 24 December 2014 date; the protocol does not expose a complete crossover analysis.
- NCT03160859: promoted. The protocol and independent statistical-analysis document share GAST-015-16S, NCT03160859, title and approved date 2017-08-14, before enrollment; sample-size, interim and model details remain reference-only.
- NCT02435212: `hold_version_reconciliation`. The registry bundles Protocol Version 06 dated 2021-06-24 with SAP material from 2018, 2021 and 2024, preventing a single frozen governing pair without further decomposition.
- NCT02998671 and NCT04897594: `excluded_combined_protocol_sap_leakage`; their protocols expose the target analysis sets, models, missingness or adaptive/interim decision rules in operational detail.
- NCT01877564: `excluded_combined_protocol_sap_leakage`; the alleged SAP is a direct extraction of the protocol's statistical pages.
- NCT02804932, NCT02596893, NCT02533375, NCT02621424, NCT02176291 and NCT01696279: `excluded_wrong_document_type`; their analysis documents postdate primary completion, incorporate executed or termination-driven analyses, or lack a defensible prospective governing chain.

## Source audit

All 24 PDFs were downloaded from the registry, hashed, page-counted and extracted by physical page. Title/version pages and the pages establishing promotion, leakage, retrospective timing or version ambiguity were visually checked. For the two promoted studies, the critical design, endpoint, sample-size, analysis-population, model, multiplicity, interim and safety pages were also visually inspected.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT02441101 | protocol | 20 | e5018f2c3d4b9835a2dad5fb09beb9569e97f9ca6a070b1ba5a442db1df9af93 | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/01/NCT02441101/Prot_000.pdf) |
| NCT02441101 | SAP | 2 | 66b328e8e01737fcb4c93f2acd7ad0e92ecfa122fe115e3280e829aad3f2de21 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/01/NCT02441101/SAP_001.pdf) |
| NCT02998671 | protocol / SAP | 94 / 23 | 5ed42a72df03ddd761a745dcec24f0ecf2cec41845aaf57f743b967e72842b67 / ae3490f446e510d4beb39cf771a77df50d89343c992df016683d5e0decdd27a2 | [record](https://clinicaltrials.gov/study/NCT02998671) |
| NCT02804932 | protocol / SAP | 22 / 2 | c91f5c539f28bc6e35b1f3136f4ee1050b398faf15b364f97bd070fb469af705 / a1e02282c6e28cbee824372a3d615b79979fc0806032538bd9f2fac83d3fe6cb | [record](https://clinicaltrials.gov/study/NCT02804932) |
| NCT02596893 | protocol / SAP | 138 / 55 | 63067127e0545e756adbd71b2db06914b58ec0868bef9971c8739087aa16cd6f / e6fc678c0ea0bece89f6893c4a90494955a9257f9f46e578a2dcc3ceabc4c0eb | [record](https://clinicaltrials.gov/study/NCT02596893) |
| NCT02435212 | protocol / SAP | 122 / 131 | 1a0835b3dfefcc05e51e841892d90897c8b6640d1e6d5667ed76cfafcd063497 / f5337a19c774268334853c20a16bab79c9f25a3f9f1be1714344af8afe99839e | [record](https://clinicaltrials.gov/study/NCT02435212) |
| NCT02533375 | protocol / SAP | 123 / 43 | 7e04c52ba05201d1bfcfe7e45aeb076ff8dad4bffa03f66ff8c104f64fd6a7fc / dfc39fc008b977b0c601514e75647aa6753c851b7f78dac3bd4a7927a7a94808 | [record](https://clinicaltrials.gov/study/NCT02533375) |
| NCT04897594 | protocol / SAP | 92 / 50 | d272a0bb5b09806023d8d2af8359a5cb83977521e71185724e9004d029ce0c31 / 016364f70a2832fce9c47d43048548345e5e42d9e0f5d722282c6932b73c50c8 | [record](https://clinicaltrials.gov/study/NCT04897594) |
| NCT03160859 | protocol | 14 | 152dcd12cc8d1a3a5732dc987ab2aa0fb70cff9f9b7d42e15c0433fb99eeac8a | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/59/NCT03160859/Prot_000.pdf) |
| NCT03160859 | SAP | 6 | 13514a9f20111351b0bdaa11a9e3c3af723c4069811e4611b8d5cf435b119bc7 | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/59/NCT03160859/SAP_001.pdf) |
| NCT02621424 | protocol / SAP | 38 / 2 | 7a154dd2084d60330b53404c4879d6733d10164a23efcebb8b0f0f3cda2ab888 / 791d4033e402efd19db6eeb4325eeb7c4cf844145a7bcc4f42dd0008223520d4 | [record](https://clinicaltrials.gov/study/NCT02621424) |
| NCT01877564 | protocol / SAP | 22 / 3 | 89025af449478eab37d2985a2151b011ea1c75e6b9c87c06da69563ba9e985fe / e2a2ed681dbf196e3b105f86eb16bba7473b82cc114e5776a350712f0bc972da | [record](https://clinicaltrials.gov/study/NCT01877564) |
| NCT02176291 | protocol / SAP | 3 / 1 | 6e11523c58eda6a47dfc53789b9103488747270b99a031dbcfb29cff26b8ecf7 / 71d412157e35222d3c23e8a8cc31bd00ec0050b9dc2e9e111ccd91b039a03719 | [record](https://clinicaltrials.gov/study/NCT02176291) |
| NCT01696279 | protocol / SAP | 102 / 70 | 6c5ca1e6179dee80e664024fa7ce24167b21f1160e747a0bdf0873a0f9376815 / 30d319c607b4503f2a45d554a07962e5e3f4e2708daa6dc494da459ed3bffa7d | [record](https://clinicaltrials.gov/study/NCT01696279) |

The local PDFs and registry snapshots are acquisition artifacts under the gitignored source tree. They are not committed, and reference SAPs remain annotation-only.
