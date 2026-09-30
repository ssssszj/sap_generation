# Expert Review Packet: Batch 146

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 146 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 1,307 physical pages in the 16 PDFs. A total of 184 decisive one-based physical pages were rendered and visually inspected in eight contact sheets, including the image-only signature pages in NCT03529942 and the sparse table/signature pages in NCT03819153. All eight pairs were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03226457 — exclude: the late-conduct SAP describes the final analysis, imputation, subgroup analyses, adherence sensitivities and realised absence of pregnancy testing as already performed, while the protocol exposes the repeated-measures ANOVA, ITT, multiple-imputation, complete-case and subgroup-interaction program.
- NCT03819153 — exclude: the pre-completion SAP has a coherent Protocol v5.0 lineage, but that model-visible protocol already discloses the group-sequential Cox program, event targets, alpha spending, multiplicity, analysis sets and missing-data framework.
- NCT05001737 — exclude: SAP v4.0 was finalized after study completion and its history attributes the revision to an errata document and dry-run discussions with the study team.
- NCT03005327 — exclude: the repeatedly revised SAP incorporates observed dosing, COVID-related local-laboratory use, DRC timelines and an already generated interim CSR after review of accumulated safety and efficacy data.
- NCT03529942 — exclude: the SAP is chronologically prospective and matches Protocol v6.0, but that protocol already gives the four analysis populations, primary standardized-change analysis and confidence interval, interim analysis, safety summaries and sample-size rule.
- NCT02614287 — exclude: both documents are pre-start and version coherent, but the protocol nearly reconstructs the SAP through its ITT population, MMRM/ANCOVA/LOCF/GLIMMIX/CMH models, covariates, multiplicity, safety summaries and interim policy.
- NCT01343043 — exclude: the RAP was approved after study completion, records that futility evaluation was conducted and contains realised cohort/treatment language; its protocol also exposes the ORR, Wilson-CI, Kaplan-Meier and cohort-stopping program.
- NCT03019627 — exclude: the final SAP follows study completion and a post-completion endpoint note, documents conduct/analysis changes, and is substantially exposed by the protocol's populations, SANDE/LOCF, sample-size, descriptive efficacy and safety program.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03226457 | late-conduct executed target plus leakage | 55 / 20 | `c7d59fee6c2d7581357ab9d2f6885d4213247e1d7801aa23d0a20c5f73fd85b8` | `759ae1b47b4be6957e34f3affc425344e20c71a0afec7aac406e3d9d60885412` |
| NCT03819153 | protocol-embedded target leakage | 89 / 35 | `bae8726d97f1b17477fd3be553ab59b16be3668b9ce358e6e7dba16ca63ad9af` | `01c40326165039baba0f48c3ca9761240d59e4656a724533c4746dd00d35731e` |
| NCT05001737 | post-completion dry-run-informed target | 110 / 120 | `b1dc7642c0570abbe8d9f60bcc54cd8b4e236f1ae76d6bfcf07e4cfbe0197505` | `f3299495259f0e1c29a7d98cd352f14ec0b381172a73e0e619a1806d087c0abe` |
| NCT03005327 | accumulated-conduct/DRC-informed target | 115 / 172 | `b7d0bfa4d1ba3d6260d680babc0d5ce566a0bd8b0661cfc45aade62b7f096336` | `8800dfb76498c13286c4fce19ca28181b057f621f7afeaf660de4037697cab4a` |
| NCT03529942 | protocol-embedded target leakage | 54 / 37 | `8327ee0d741403c258c24bf3374573236563114b6ce8bfeb7759ed2467245d40` | `ddb2cd32ac7fe7627623d143d51ce5c3209cc7b7897929b4096737afa1df557a` |
| NCT02614287 | protocol-embedded target leakage | 58 / 39 | `f209037985806444fc3cc68f3d02c95978681e0bda741de6052fad8481eccbe2` | `77339761228cc18a608a81bfcdea0e65f376faf90cca00d03a108ffb849c4ab4` |
| NCT01343043 | post-completion executed target plus leakage | 100 / 196 | `68a0a736f391261783aa538671b3f1a9759245e3c56e9e79ac60ea931e0971f7` | `8c31c5d786fe966bbdbf414647ace414414d74f2937865f7270330e534c98ae3` |
| NCT03019627 | post-completion changed target plus leakage | 66 / 41 | `dd47aafe4143528a0cad2e5495c0e3beb7f16a7aad2779f4ae81445a73487323` | `e52535c8f007da598ff6ac002d38c60f0be634d8d1682f8d0008728428de3b2b` |

## Gate interpretation

- A document date before primary completion is not sufficient when the SAP itself states that analyses were performed or encodes realised adherence, eligibility, pregnancy-testing, dose, laboratory, DRC or interim-CSR facts.
- COVID language is not automatically execution-informed. NCT03819153 fails on protocol leakage, whereas NCT03005327 fails because its revision history and operative text incorporate realised COVID laboratory practice and accumulated review decisions.
- A detailed protocol does not fail merely for naming endpoints or giving a sample-size target. The leakage decisions here additionally rely on disclosed populations, executable models/tests, covariates, missing-data rules, multiplicity/interim procedures and endpoint-specific summaries.
- A near-completion SAP can remain prospective in principle. NCT03529942 is excluded for the separately sufficient protocol-leakage gate, not because its 2019-11-05 SAP predates 2019-11-08 primary completion by only three days.
- Registry actual dates were used as chronology evidence only, never as a prospective sample-size substitute.

## Replenishment

All eight non-promotable slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
