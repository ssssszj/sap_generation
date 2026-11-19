# Expert Review Packet: Batch 143

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 143 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 PDFs contain 1,121 physical pages. Native text was extracted from every file except the scan-only 64-page NCT03410056 SAP, which was fully OCRed. A total of 383 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded; this remains first-pass screening requiring independent expert review.

## Decisions

- NCT03118518 — exclude: protocol pages 83-95 provide the populations, hypotheses, time-to-event implementation, censoring, sample size, multiplicity and secondary models needed to reconstruct the SAP; the SAP also has internally inconsistent Version 2.0/3.0 labels.
- NCT03738865 — exclude: the SAP postdates both primary and study completion, while protocol pages 59-62 already expose the exact noninferiority risk-difference framework, margin, populations, sample size and secondary/PK/safety methods.
- NCT04881461 — exclude: the post-completion SAP records during-trial decisions driven by missing collection, realized stratification, random-effect revision and a later-study MCID change, while the protocol exposes the analysis core.
- NCT02979535 — exclude: the post-completion SAP and selected protocol amendment incorporate exploratory findings, an IDMC review, a seronegative risk, halted vaccination, a study hold and resulting design changes.
- NCT03410056 — exclude: the post-primary scanned SAP and conduct-era protocol incorporate Phase 1b/2a interim conduct, Bayesian dose escalation and realized amendment/enrollment changes, and the protocol exposes the model and stopping program.
- NCT02549196 — exclude: the SAP explicitly reports realized findings after eight and six participants, and later cohorts plus the selected protocol were changed in response to earlier-cohort results.
- NCT01274351 — exclude: protocol pages 13 and 44-47 disclose populations, nonresponder handling, confidence intervals, Kaplan-Meier analysis, sample size and interim framework, substantially reconstructing the SAP.
- NCT05985304 — exclude: the selected Revision 7.0 protocol does not match the SAP's stated governing Protocol Version 5.0, and Revision 7.0 pages 36-48 independently disclose nearly the complete executable plan.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03118518 | protocol-embedded target leakage | 131 / 38 | `08147c68b117c4212b52be1013cb7662f856ff35eeca3175ef97e9b0be1606bb` | `e71b6f74958c9ee177700cff5a614ed11fac4b2b40cd89ee57f45f27024add14` |
| NCT03738865 | post-completion target plus protocol leakage | 78 / 35 | `d536c32d18e4039152472ff6967349cefbc3e955a8a30676aaefeeee0c335993` | `b58fb145beb8fb6f7b56861d0f9f483c731e4767b80de3a20da1fda89f29b6d5` |
| NCT04881461 | post-completion conduct-informed target plus leakage | 78 / 49 | `b7bcf1ffe24c8886083e82867a0a893ca156fa155fe28dcfb043d8b293c0344c` | `c4ed17ae647faddae95a7d4af4f7568c782d1407f92b52cb0ca25d30e2c65736` |
| NCT02979535 | outcome/IDMC-informed post-completion package | 100 / 38 | `b7e166a70025686900002fe54167a9f9775b9ad8c129f463e8bac34b8e00ade4` | `f976d63999f95dc891803b788bdf6caea619c3898aeaee163ec4759508a756ab` |
| NCT03410056 | post-primary conduct-informed target plus leakage | 131 / 64 | `ffbcfce1c4ce288daec2c5e6cafb2c238ef738bc9baab0c99eaf7ca2caa581ae` | `2cb9eb47af74b03df4d218d08ea3511efb11aea75477cbe96233b7751807a2e4` |
| NCT02549196 | observed-cohort-informed adaptive package | 161 / 26 | `e84159e6df678235c5e335daa2d942230f8f63815759972bd53157c23d122c29` | `127f5f42d2b65b0fc95dd790ad01fcdf805b2878cb71506ec6b504c609a9c4d7` |
| NCT01274351 | protocol-embedded target leakage | 51 / 22 | `e88a576c8d1db9b2c10c8eb085ba71444da6181d677c3f3e94eaf015da816069` | `f165d9d4ec42698ab4945d54c06e24c6922c7d66921d04379c0a62bff30bcb0e` |
| NCT05985304 | governing-version mismatch plus protocol leakage | 58 / 39 | `981cdb171c72c33e199ead83e2328a5ff165d266f1dd716b26f177e68b5ef703` | `8794cf7db5cbef49f7329897a7d1f31767176748d8ee29b13a9e4c70f95b133b` |

## Gate interpretation

- A SAP finalized after primary or study completion cannot be treated as outcome-uninformed without an authoritative pre-outcome approval chain. Statements about pre-unblinding approval do not cure recorded during-trial decision changes.
- A conduct-era protocol amendment is not a clean model-visible input when it incorporates IDMC findings, observed cohort outcomes, stopped treatment or other realized execution and the target analysis inherits those changes.
- Design, endpoints and sample size alone do not trigger leakage exclusion. NCT03118518, NCT03738865, NCT04881461, NCT03410056, NCT01274351 and NCT05985304 fail because their protocols additionally disclose analysis populations, executable models/tests, censoring or missingness, multiplicity, sensitivities, safety methods or stopping logic.
- Registry file dates do not override internal version provenance. NCT05985304's same-day registry dates cannot reconcile SAP Version 4.0's explicit dependence on Protocol Version 5.0 with the selected Revision 7.0 input.
- Registry actual enrollment and dates were used only as chronology/conduct evidence, never as prospective sample-size substitutes.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
