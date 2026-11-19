# Expert Review Packet — Batch 73

## Scope

Batch 73 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the public, prospective, version-matched, independent-hidden-target gate. Seven model-visible protocols expose an executable target analysis; four of those selected SAP packages also postdate primary or study completion or incorporate executed-study information. The remaining family cannot be promoted because the concise SAP predates the selected protocol by three years and supplies no governing protocol citation. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining statistical pages.

## Decisions

- NCT02970669 — protocol pages 62-64 and 67 expose populations, ANCOVA, covariates, alpha, LOCF, sensitivity analysis and power; the final SAP is post-completion.
- NCT04560998 — protocol pages 59-65 expose hierarchy, sample size, populations, extreme-rank handling, MI/Rubin pooling, Wilcoxon/Hodges-Lehmann, MMRM and tipping-point analyses; SAP v3 is post-completion.
- NCT02406859 — governing-version hold because the unversioned two-page SAP predates the selected protocol by three years and cites no governing protocol.
- NCT06238817 — protocol pages 70-75 expose sample size, populations, multiplicity, CMH, NRI, estimand, MI, survival and safety analyses.
- NCT03295318 — protocol pages 59-66 expose power, populations, intervals, comparisons, missingness, multiplicity and interim analysis; the selected CSR appendix bundles two SAP versions, including a post-completion revision.
- NCT03965091 — protocol pages 18-19 and 87-95 expose populations, MMRM, covariance, MI, rescue sensitivity and interim analyses; the post-completion SAP records termination for futility after the second interim analysis.
- NCT03021018 — protocol pages 37-38 expose populations, the primary time-to-event endpoint, survival and Fisher analyses, no interim and sample size.
- NCT01945775 — protocol pages 11-13 and 87-91 expose PFS, ITT, stratified log-rank, KM/Cox, ORR, OS, event counts and power.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02970669 | protocol leakage plus post-completion SAP | 91 / 33 | a741408c19c3da7cc773e2aa7c11f52218b368402856e21249a8bd4a4a386f86 | 15d6270d00729208c101c1a1b259a6bc3d988815441bcf786b82b4e7792d4c28 |
| NCT04560998 | protocol leakage plus post-completion SAP | 111 / 44 | 391690967a3185e79f204180cbd9677fc66760ea9f5f0ec9573272587e105628 | 4c1dee8c7ff84fc70bc813cfe29a2bd7f5f13203f412b6af08feeadae8acac94 |
| NCT02406859 | governing-version hold | 11 / 2 | 4ab964b331a1cf15351461c5bb7d3c1f3e4b7a7a749f9ef5159ccda6ab36cca3 | 412295823c3780dc4edbd137f0c470c504582b3ea5a489533cb8265509a651e9 |
| NCT06238817 | protocol analysis leakage | 93 / 50 | 87794e460c9d3f3abeeef98bd1f7687f6cf501f287ab100da5efac7df7021d67 | d7d4cf88de158cdab8894bc0b8ce01f26bca5baaea1d11797b92edde3d22aada |
| NCT03295318 | protocol leakage plus mixed CSR-stage SAP bundle | 123 / 62 | 88c1e227b5a111413a52a99f2b711be5ab1fb6cff1f54a6bf2ff6517608b403f | 988d8100fd8c8fe646129a3b85ced7afc7eced513e840f633e2b19e8a5e2453a |
| NCT03965091 | protocol leakage plus execution-informed SAP | 192 / 57 | 168469ec1456823e338fd86f437ecae0715ad1ffd795b29fecc13c1e8a5c50d8 | 64870a86b7d48ed7c07d203771ed05556b02e6c8ec6b98b36cb63d62c453dcb2 |
| NCT03021018 | protocol analysis leakage | 48 / 40 | 5829c3181f075e6f2498cae20f38cd7c62df3394ee88b2af06e2d531c31a0586 | 1661eee6d21f5a268b6a4567129a5c91b0754c443362f14e6967c25132453a10 |
| NCT01945775 | protocol analysis leakage | 115 / 48 | 2c09d9942209604dee29c1c9498bf01885a2d51fbe6ca5a5491a55bd0f378cd1 | baccb691f87badf2d313766ed125e38da87132af52b5ac99ffbc9fce7a7db312 |

## Review gate

None of these eight families may enter train/dev/test. Seven fail prompt/reference independence, and NCT02406859 remains outside the actionable pool until a public version chain can be proven. Batch 73 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
