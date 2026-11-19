# Expert Review Packet: Batch 133

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 133 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,495 physical pages. Every page was text-extracted; all 126 pages of the scan-only NCT03985943 SAP were OCRed, and 130 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT01964560 — exclude: this open-label extension imports parent-study baselines and responder definitions from SP0967/SP0969, while its protocol exposes the analysis sets, missingness, sample size and efficacy/safety program; the 2021 SAP amendment also incorporates COVID-era and endpoint changes.
- NCT02365584 — exclude: the SAP was finalized after termination/completion and changes the inferential program around the observed 43/84 recruitment shortfall; the protocol also exposes the executable target.
- NCT02713230 — exclude: the signed SAP is prospective and version-aligned, but the protocol exposes the primary ANCOVA, populations, missingness, hierarchy, sample size, blinded re-estimation, PK interim and safety program.
- NCT02719743 — exclude: SAP Amendment 2 follows study completion, refers to analyses already performed for the iSRC and changes the ATP/program; the protocol also exposes the substantive target.
- NCT02951429 — exclude: the SAP is prospective and explicitly cites the selected protocol, but that protocol already exposes the composite endpoint, populations, primary test, sample size, missingness, secondary models, multiplicity and interim program.
- NCT03267576 — exclude: the protocol contains a near-complete statistical plan, and the separate SAP directs a post-exploratory meeting to select/confirm final multivariable and alternative analyses after missingness, distributions and outliers are inspected.
- NCT03712358 — exclude: the same-date protocol and SAP both contain accumulated conduct, including enrolled cohorts, the unused Cohort 4 and absence of retreatment; the protocol also exposes the analysis program.
- NCT03985943 — exclude: the final SAP was dated and approved after both primary and study completion; the apparent 2020 footer date belongs to the controlled template rather than this SAP version.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01964560 | related-study extension + leakage | 146 / 116 | `336dc6e57d01c92cbd113fe064e423b80087e25f6499b23421d11cf6b5eeb65e` | `d1ff2856c928120cb35dc6f1f248757fbafeb1c0f17e7a243c08845432412251` |
| NCT02365584 | post-completion termination changes + leakage | 54 / 32 | `1a43633a8bc14063b6396c82bbb71c45c0f4bcbb2155130c07cd07ce839346b8` | `1f2168dd6d9f4897015110ef2456a87d1f4592c908953d6de7488bc8872917e7` |
| NCT02713230 | protocol-embedded target leakage | 82 / 167 | `391ccd1662f159e5aabc842c27eac6f14b1243a453cc142b243e59a72be615db` | `8e82adbf63ce55b3fd71b6042f706343dea7c69f5cb208d7c699ef5ec56bcca2` |
| NCT02719743 | post-completion and ongoing-analysis changes + leakage | 117 / 79 | `47ac4b6853a215164af1f11a91994873776d3514e5a1ded86eadb1796ddeabbd` | `1f8429e5d26e7cdb9eb9aa491f6327ba262bdd17a0573cd4ee6dd5924626614f` |
| NCT02951429 | protocol-embedded target leakage | 102 / 78 | `ba581c1451977fae1ac43e272cf53ed7b244a9605d028612c3beffca780cdee4` | `592082c463d22a985a00b32c0d47eb876ff7281e0e2d6d47b0f50669966f88ab` |
| NCT03267576 | exploratory-data-driven target + leakage | 85 / 9 | `642d09286612232176839e6118a769cde11f029056b5f634fde03b39be79ac38` | `8822af54af2ba11af9110d99f54f4fb5dc0dfe279343ca8058146f492aa54ae4` |
| NCT03712358 | accumulated conduct + leakage | 76 / 8 | `2d91ae6aa7a560feacd02457df433f1220544f11093f0a01603eada0afc0f8f7` | `c66c5f3518f6daaac778630ca3b20bd4c8a3813c0576282c29b1fb1ce57e439c` |
| NCT03985943 | post-completion final SAP | 218 / 126 | `36829742c538785cb71b5cdd7a5039e0d302c839a51b537acfcaa5f6778bbcd1` | `91c86391e9e0146e453a804307b54eeff49e5a8ec956d5fe5a34ebe0bc4788a8` |

## Gate interpretation

- A pre-primary SAP date did not rescue NCT02713230 or NCT02951429 because their model-visible protocols substantially reconstruct the reference targets.
- An exact protocol/SAP document-date match did not rescue NCT03712358 because both documents explicitly record accumulated enrollment and cohort conduct.
- NCT03267576 is disqualified on two independent grounds: protocol leakage and a separate SAP that leaves analysis selection dependent on exploratory data review.
- The controlled-document effective date in an SAP footer is not interchangeable with its revision/version date; NCT03985943 is therefore post-completion.
- Registry actual enrollment was used only to reconcile chronology and was never substituted for a prospective sample-size target.

## Replenishment

All eight excluded slots were replenished from the official API. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates.
