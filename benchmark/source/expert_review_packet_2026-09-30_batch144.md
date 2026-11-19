# Expert Review Packet: Batch 144

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 144 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 833 physical pages in the 16 PDFs; pages with image-only signatures or sparse text were reviewed in the rendered originals. A total of 319 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. Seven pairs were excluded and one was placed on governing-version hold; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03131167 — exclude: the post-completion SAP records unmasking and completed-cohort interim analyses used to inform later cohorts, while the protocol exposes analysis populations, PK/PD models, safety and adaptive/interim rules.
- NCT03802825 — hold: the short SAP predates completion and contains no results, but "Published version" is its only provenance; it has no version, revision, sign-off, approval or governing-protocol citation linking it to the unversioned conduct-era protocol.
- NCT04921969 — exclude: the post-primary SAP follows an enrollment-informed amendment that increased N from 250 to 315 after an eligible subgroup was found under-enrolled, and protocol pages 73-78 nearly reconstruct the SAP.
- NCT02989194 — exclude: the post-completion SAP made final pre-database-lock changes, internally cites two different governing protocol versions, matches neither the selected Version 2.2 protocol, and is substantially exposed by that protocol.
- NCT03417778 — exclude: the post-completion Final Analysis SAP is explicitly run after completion and data finalization, cites an earlier protocol than the selected public document and inherits its adaptive PK program.
- NCT02551809 — exclude: the post-completion SAP history documents July-October conduct-era model and sensitivity-analysis revisions; it is not outcome-uninformed despite matching Protocol Version 5.0.
- NCT01339910 — exclude: protocol pages 49-55 disclose the ITT group-sequential Kaplan-Meier primary analysis, power, interim boundaries, competing-risk and covariate methods needed to reconstruct the prospective SAP.
- NCT07239128 — exclude: both post-completion files are completed-study manuscript methods written in the past tense, and the alleged SAP states that analyses were conducted and normality confirmed.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03131167 | post-completion unmasked/conduct target plus leakage | 111 / 77 | `30d7974f4f20f66f9091f61733db38a50f93ee47bdf816093f06bd8735362a11` | `78f2882c0966e8a31867a69c52beb5b11aad33223f0243dd8e10df069490dc21` |
| NCT03802825 | governing-version/prospective-approval hold | 15 / 4 | `15ea1437110868f5da9e5dd13a0feb3d2eadd7217e35b10bf03194e19eeceb75` | `81f159d0cf7a9fe3cc453f3708ffde6fd22e16b1ae4932b21c58e875844f031e` |
| NCT04921969 | post-primary enrollment-informed target plus leakage | 113 / 62 | `436e8d769a2abd3d308e50f711c99eb12aca754c22428339a553332d9e8a91b0` | `d2c468412c07e951ce263b0b73beb7c5c536cf63d89d36c4c05a2af0312718d5` |
| NCT02989194 | post-completion version-conflicted target plus leakage | 75 / 41 | `141ac40792a1b32ec404c3aba8ad28f86c1f1095085c4ca00afffa841c431258` | `e88e4602fc9d43450e67426a8f3508507445c12036b8a0ba3825ee5ddd7e6177` |
| NCT03417778 | post-completion final-analysis target plus version conflict | 68 / 35 | `6bb455c749f90a8c58928ac6f1c2cdc648a7f79b4d03f0a5335d40fc7ede75bb` | `eedda401ea12121a09d50aa2516d27c86c94bb0efce987e1639b6fe264505843` |
| NCT02551809 | post-completion conduct-era SAP revisions | 76 / 20 | `21155d825e116cf92e750684fae7d8123abf5d9dc158046bcabd10d53f69e238` | `51089deb0e9d4114285759f1e59550c6e81261e7fc004cf67af61067526d32db` |
| NCT01339910 | protocol-embedded target leakage | 102 / 29 | `ff5ab86f222780ae069f993386dad44f1f5121568080262b40d9ebda52212c45` | `4fce02129d30c12940d5940c173fe0bb5ec39baffe0f4859c6c2ff37222b5f3f` |
| NCT07239128 | post-completion executed manuscript methods | 3 / 2 | `812c3abb89fe80ce0726a7170d92f43ca80cb79e54629f2172eff04a7d547675` | `b4b0257600137254250f84293568dd26ec150acc9402785329e9bf7fd09050f5` |

## Gate interpretation

- A date before completion is not enough to establish prospective governance. An unversioned "Published version" without approval/sign-off or a governing-protocol citation remains on hold rather than being guessed valid.
- A post-completion revision described as final or pre-database-lock is not rescued by formal formatting or signatures; recorded model changes, unmasking, completed-cohort review and data-finalization language are execution evidence.
- Design, endpoints and sample size alone do not trigger protocol leakage. NCT03131167, NCT04921969, NCT02989194, NCT03417778 and NCT01339910 fail because their protocols additionally provide analysis populations, executable models/tests, missingness, multiplicity, interim boundaries, sensitivities or safety implementation.
- A PDF uploaded in a protocol or SAP slot is judged by its contents. Past-tense completed-study methods that state analyses were conducted are execution summaries, not prospective source documents.
- Registry actual enrollment and dates were used only as chronology/conduct evidence, never as prospective sample-size substitutes.

## Replenishment

All eight non-promotable slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
