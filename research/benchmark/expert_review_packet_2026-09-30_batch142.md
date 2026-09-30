# Expert Review Packet: Batch 142

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 142 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 PDFs contain 826 physical pages. Native text was extracted from every file except the scan-only 22-page NCT04918823 protocol and two-page SAP, which were fully OCRed. A total of 282 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded; this remains first-pass screening requiring independent expert review.

## Decisions

- NCT03068130 — exclude: the selected protocol does not match the SAP-cited governing version; the SAP encodes the realized 2020-03-30 termination as an imputation date and relies on CATALYST/LARIAT treatment state and unblinding, while the protocol exposes the related-study descriptive program.
- NCT03693430 — exclude: Final SAP Version 1.0 postdates both primary and study completion and specifies retrieved-dropout imputation, tipping-point and observed post-discontinuation handling.
- NCT04836858 — exclude: the amended SAP postdates completion, supports the CSR and incorporates blinded medical review and realized COVID-19 conduct; the conduct-era protocol also exposes the analysis core.
- NCT02954354 — exclude: protocol pages 65-74 supply populations, missingness, hierarchical testing, generalized Wilcoxon and secondary/sample-size methods, while the SAP postdates completion and records blinded review and protocol changes.
- NCT03378076 — exclude: the prospective protocol already supplies the safety/PK populations, NCA, linear model, bioequivalence, summaries, sample size and multiplicity decision needed to reconstruct the short SAP.
- NCT02549092 — exclude: both documents use interim M12-920 data, and protocol pages 10-12 and 110-115 expose MMRM, covariates, Hochberg/gatekeeping, sensitivities, populations, safety and sample-size implementation.
- NCT05987956 — exclude: the same-day post-start protocol literally embeds the statistical analysis plan and the separate SAP substantially duplicates it.
- NCT04918823 — exclude: the two-page post-completion alleged SAP is an executed methods note written in the past tense rather than a prospective governing plan.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03068130 | termination-informed related-study target plus leakage | 65 / 36 | `3112f04e65ba7cb56c6c9e3b888ed026e022220a89eb2f3f45d2d8cb99bb2798` | `d8a164ea9e59afbd094193ed46b7d554261769a779b76a419c4561f40545454f` |
| NCT03693430 | post-completion target | 97 / 27 | `943e538e2505e2a4ffc42122febcffcaa5dca229a7440107977a73a2db0138d1` | `defe8ca426006bce14004f638b8fe353214bd23453a6a94c9aa51a96e2491ce4` |
| NCT04836858 | post-completion CSR/conduct-informed target plus leakage | 97 / 24 | `a4fac5ce48677215e7572d9016b40a36a8ee3c25f44b9ae62efc053d39e486b9` | `dc0b69aa55dd8dbf085a56dbaf5c0a09c00eca2e7439f13a34d46b381d4c68d3` |
| NCT02954354 | post-completion target plus protocol leakage | 95 / 43 | `f1fc1f8e542e3bd644846f0599fd1996de9ed7f16263c5b02fe5ff2a704eb7e4` | `ddd3b0090e637182f2da03e03b17421bcbae16507dffefa9d03636d33eba637c` |
| NCT03378076 | protocol-embedded target leakage | 52 / 35 | `3a3d25616701feece096e8fa41b04eb7033e7b535c2b5dad18fe5673a0261125` | `6b83b850f4a81b4164158449e329373e4c40710f7856cd325a4118c8ac2c629c` |
| NCT02549092 | parent-interim-informed target plus protocol leakage | 149 / 78 | `45b24f523c2d0d2ddc8163b5747a74c0e8c89a6b5d539ede313328533596a552` | `6207491f752d40b9d42a261b098f7b9d1f7202777a6ef5a3f282e05714fbddb1` |
| NCT05987956 | post-start duplicate protocol/SAP leakage | 10 / 12 | `fbaccb19d3ef9b3348196328704159a412c8df6fe49fbc0fbd49f31a438e9665` | `328aa70e063287daf491798ad4630a513c0cfc5fbeb1fd5c4bbaefd007b72e2b` |
| NCT04918823 | post-completion executed-analysis note | 22 / 2 | `d401d4430b37947ed050c4d718cd8ceac89936676734b57419228373b77f5b1c` | `cc3d991b665cf78e8a0daff000657806e395c258749b312dc7cdb82ee5942546` |

## Gate interpretation

- A target written after primary or study completion is excluded unless an authoritative pre-outcome approval chain exists; none exists for NCT03693430, NCT04836858, NCT02954354 or NCT04918823.
- Blinded review does not by itself cure post-completion timing. CSR support, realized COVID handling, termination-date imputation and analysis written in the past tense are execution evidence, not prospective design detail.
- Design, endpoints and sample size may remain visible. NCT03378076, NCT02954354 and NCT02549092 fail because their protocols additionally provide populations, executable models/tests, missingness, multiplicity and sensitivity implementation.
- An extension or rollover target cannot be treated as an independent single-study question when its analysis groups, baselines or sample size depend on participant state, assignment, unblinding or interim results from named parent studies.
- Exact-date matching does not overcome post-start governance or duplication: NCT05987956's protocol itself labels and contains the statistical analysis plan.
- Registry actual enrollment and dates were used only as chronology/conduct evidence, never as prospective sample-size substitutes.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
