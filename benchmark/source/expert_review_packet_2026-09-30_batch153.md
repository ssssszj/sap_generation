# Expert Review Packet: Batch 153

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 153 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 1,226 physical pages in the 16 selected PDFs, and 167 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03504020 — exclude: the public SAP has an internally inconsistent version display (cover Version 1.0 dated 2021-12-14 versus Version 2 running headers), and Version 2 adds analysis timing, subject/data-selection, sensitivity, subgroup and manuscript analyses during conduct. Independently, the pre-SAP protocol exposes the mITT cohort, primary endpoint, two-sample t test, missing-data rule, sample-size assumptions and power.
- NCT04288778 — exclude: the protocol package was revised during conduct and includes a COVID-19 appendix governing disrupted visits, deviations, discontinuations and alternative delivery/assessment procedures; the later SAP specifically adds COVID-related deviation and infection listings. The protocol also exposes the sample size, analysis populations, descriptive analysis program and no-interim rule.
- NCT05430919 — exclude: although the SAP precedes primary completion, the protocol already specifies the primary hypothesis, sample size and power, FAS/SAF sets, six comparisons, ANCOVA factors, rescue/BOCF strategy, multiple imputation, multiplicity control and analysis timing, substantially reconstructing the target.
- NCT03197376 — exclude: SAP Version 1.0 dated 2018-06-28 follows actual primary completion on 2018-06-06. The protocol already exposes the analysis populations, primary immunogenicity equivalence and noninferiority procedures, safety testing, missing-data framework, multiplicity policy and sample-size/power calculations.
- NCT03980483 — exclude: the final RAP effective 2022-08-08 follows actual primary completion on 2021-09-15 and explicitly describes the final analyses required for the study. The protocol already exposes the estimand, ITT/PP/Safety sets, GEE/MMRM models, step-down hierarchy, missing-data strategy, sample-size/power and primary-analysis timing.
- NCT02974153 — exclude: the registry gives only month-level primary completion (`2017-11`), so no within-month chronology was inferred for the 2017-11-08 SAP. Independently, the protocol exposes the full and safety populations, endpoint derivations, eDiary missing-data rules, ANCOVA and repeated-measures models, multiplicity sequence, sample size and safety/PK analyses.
- NCT01882803 — exclude: the selected protocol is Amendment 4 while SAP Version 2 explicitly governs Amendment 3, so the selected pair is not a clean governing-version chain. More decisively, the later model-visible protocol exposes the FAS/EAS, exact-binomial primary test, nonresponder imputation, sample size, group-sequential futility boundary, time-to-event analyses and IDMC program that reconstruct the SAP target.
- NCT03633461 — exclude: SAP Version 1.0 dated 2018-10-04 follows actual primary/study completion on 2018-09-20. The public package also materially redacts much of the primary, exploratory, sensitivity and imputation program, so it cannot serve as a prospective complete reference.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03504020 | during-conduct version ambiguity plus leakage | 93 / 28 | `2e3e3afed43535b44d270f6fbd854894cf7eb6a382e75d51fe14d42646ceb1f6` | `eb53830b7a4cff4ecc058ff56b31d59bbe48349c67d376621e0b397b8fd2f685` |
| NCT04288778 | COVID/conduct-informed target plus leakage | 60 / 16 | `a77e49c5f88d9ead071f8774dc6c494a840bc2626d1344ccc399f840b59f95bf` | `9e7cfe9d183939d7cc309b66986b331b5a23bea5b26e86804e4b1a9e7b41d699` |
| NCT05430919 | protocol leakage | 103 / 70 | `c1991c41e5f4c286e45ad8a3adfb60e521d739cf17468313eac5e2b4d8434f8e` | `d697bcf6b230cee74df118f661e8751afe48c1871f98cf6f38556ff0e4e6d00b` |
| NCT03197376 | post-primary target plus leakage | 89 / 36 | `f451f5279079dde346df27c9668294bf308ad11e5fa0effe02e8171b088c61bc` | `b7c10eef9a49b640372dd7a81d5faa458e7cd5818d03badb705ee66782717991` |
| NCT03980483 | post-primary final-analysis target plus leakage | 126 / 226 | `63920884c6f20cbfcaa02683f58709b21367243a4ccf5278479170d6e0ded3f2` | `21fadb56f605c9e76cdb0c72216642bcc9b21c13bb0407bf04b6567219b5767f` |
| NCT02974153 | protocol leakage; month-only chronology unused | 88 / 40 | `d599b98dbf3c019b30ff95de30febc5c5001d776d9f753869fd20314ebb48cef` | `b13e748a350da9d36d1e38aba8e9b9c614418e1597155c7dbfb07609d46a2f4a` |
| NCT01882803 | governing-version mismatch plus leakage | 88 / 34 | `e2ac2dbccc1bd4a9b60f919751a543002a87174f9bd0ea0bc8732c21ba48b439` | `1bff9263f18a4f31dc2480921fc481ac78f0f6b9382ff3f18e5c8fa54b98181f` |
| NCT03633461 | post-completion, materially redacted target | 65 / 30 | `db6883b84c66402241d6023644d7031a33a7987776925389220f742299fb844d` | `14f919ff1c134671de3d87d084beffa8b75a2ebfa6dfaee1800740859523098c` |

## Gate interpretation

- A protocol that exposes the executable population, endpoint, model, missing-data, multiplicity and sample-size program fails the no-leakage gate even when the selected SAP is nominally prospective.
- Month-only registry dates do not establish within-month chronology; NCT02974153 is excluded on independent protocol leakage rather than an inferred primary-completion ordering.
- A later protocol amendment cannot silently substitute for the governing version explicitly named by the SAP, and a later model-visible amendment still fails when it reconstructs the target.
- COVID-era conduct appendices and SAP provisions tied to COVID deviations or infections are execution-informed when added after study start.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
