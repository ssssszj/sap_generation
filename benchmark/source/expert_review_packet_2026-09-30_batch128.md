# Expert Review Packet: Batch 128

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 128 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,011 physical pages. Every page was text-extracted, and 71 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT02827500 — exclude: the SAP follows completion, incorporates realized early enrollment termination and repeats an executable program already present in protocol physical pages 43-45.
- NCT03163511 — exclude: the during-conduct SAP revision says derivations were clarified from interim safety summaries and the protocol already exposes populations, ANCOVA, time-to-event, categorical and interim programs.
- NCT04604652 — exclude: despite a pre-completion signed SAP, protocol physical pages 13 and 54-55 expose the primary estimand, test, alpha, populations, missingness, multiplicity, safety and data-dependent stopping rules.
- NCT04700345 — exclude: the SAP follows primary completion and protocol physical pages 21-25 expose the executable primary/secondary program, including SAS code.
- NCT03569293 — exclude: both selected documents are post-primary; the 2025 SAP cannot establish an outcome-uninformed target for a primary endpoint completed in 2021.
- NCT02589795 — exclude: the protocol already exposes the ITT/PP populations, confidence intervals, rank and Fisher tests, MedDRA safety summaries and key conventions of the short SAP.
- NCT02640612 — exclude: the protocol and amendment already expose the descriptive extension-trial program, populations, presentation groups, AE/immunogenicity rules, missingness and interim decisions.
- NCT07716553 — exclude: the three-page SAP is the protocol's statistical section reproduced as a separate file, not an independent hidden target.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02827500 | excluded | 60 / 34 | `1fc0b909ea0f8a79f63663eaf7cd48c0b34341bb64ecfb3e77761ab6cafb8211` | `f5e9a5c4adb39034aaa01df0a7141c48c3c5861a789ffaa93317600ab4a1e607` |
| NCT03163511 | excluded | 92 / 58 | `469bbd9639f947b1a3eecb741cb69d194048c5665b7fb6da0d626cde947f9d75` | `e1c7edfa55cdd82d6cf3ca6d93c804e9ef7cb0280521b02d133c766a0d67c711` |
| NCT04604652 | excluded | 64 / 24 | `fe9fe580b1b14adabc98c8e1051e99871ec1e011e6424734fa458600dadb74c8` | `32c2f78473f04328b9d3c7bbd0241132ec841347849e5236bd625aeb83769c19` |
| NCT04700345 | excluded | 39 / 42 | `08c09e4741293dcb4f625ed1aeef0794b956b91d8df8f3eb8d1413924d0fbb9c` | `76c0014c16d370e58a3a7509efe1b478790a8b3c99c879505c7eab4018b3c772` |
| NCT03569293 | excluded | 104 / 138 | `5050eec5ed5781421990678d7372ce0377e5c474396d8b4917ca521a8b469ac7` | `33c5f181374943034e26c0758ee0705f83ff189e8be3e55c146a88970dceaaaf` |
| NCT02589795 | excluded | 73 / 18 | `7f7ca397250242f21a3312e3d8c4247ae02c1b9cdb1518fb9c4695933c804995` | `e34f94858c4c2d95af57a3d4f6a5ab0bc5815b69e7e0e6e49ae49f6da650a138` |
| NCT02640612 | excluded | 81 / 63 | `0d7ee91fb69de876b359b65814a4d7408b183399e1f5347b9722dea0267f48fc` | `0565513cf7b1b67d0ca567088f57065138bbe528a99a456bd48acf7fb73c239f` |
| NCT07716553 | excluded | 18 / 3 | `3b3e57aea6267ecc383533528608fa331f0bae9ee21ad46755ea364015cf657b` | `0f6315ff6550aa11800965f4dcff5f85bb147c4fef408687643f60562f90d26b` |

## Gate interpretation

- A pre-completion document date did not rescue NCT02589795, NCT02640612 or NCT04604652 because the model-visible protocol independently reconstructed the target analysis.
- An official SAP label did not establish independence where NCT07716553's three pages were copied from the protocol.
- During-conduct amendments tied to interim summaries were treated as execution-informed rather than assumed outcome-uninformed.
- Registry actual enrollment was used only to identify realized-conduct statements and was never substituted for a prospective sample-size target.

## Replenishment

All eight excluded slots are to be replenished from the official API. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates.
