# Expert Review Packet — Batch 72

## Scope

Batch 72 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the public, prospective, version-matched, independent-hidden-target gate. Every model-visible protocol exposes an executable target analysis; six families also fail prospective-governing-plan or family-independence requirements. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining statistical pages. The scan-only NCT04445714 SAP was fully OCRed, and the decisive pages of the character-encoded NCT02224703 pair were independently OCRed before visual review.

## Exclusions

- NCT02944968 — protocol pages 59-61 expose the feasibility sample size, analysis populations, descriptive rule and acute device, safety and procedural summaries.
- NCT04445714 — protocol pages 2 and 5 expose the study size, endpoints, adverse-event stratification, annualized rates and paired t/Wilcoxon analysis; OCR and visual review confirmed that the SAP follows the same plan.
- NCT02117713 — non-independent LUM001-301 rollover/extension family; protocol pages 91-94 expose its population and descriptive plan, while the SAP acknowledges a locked and unblinded parent database.
- NCT06101823 — protocol pages 23-24 and 65-67 expose power, populations, MMRM, CMH, covariance and safety/PK analyses; the final SAP postdates primary completion.
- NCT03283319 — protocol pages 51-55 expose endpoints, populations, confidence intervals, interim/final analyses, sample size, multiplicity and missing-data rules; SAP v2 records final-CSR changes and postdates primary completion.
- NCT03956550 — protocol pages 57-62 expose the hierarchy, sample size, estimand, imputation, ANCOVA/CMH and safety analyses; SAP v2 explicitly changes the plan after negative interim results and termination.
- NCT02224703 — post-completion Protocol v8 pages 88-94 expose populations, hierarchy, negative-binomial and ANCOVA analyses and sensitivity imputations; the final SAP is also post-completion.
- NCT01698918 — late Extension-Phase Protocol v5 pages 97-102 expose the efficacy and safety plan; the SAP states that Core primary and overall-survival CSRs were already reported, making this a non-independent execution-stage target.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02944968 | protocol analysis leakage | 83 / 11 | c2ad14be2e0ef8833ced0e20e963b1f8f8707e1bbf5d2090d001d0101ba31541 | fe7dd20e66c5b84373b41a06b742311cd1307ecc81f2aa64fa4f5b4f402de301 |
| NCT04445714 | protocol analysis leakage | 52 / 71 | eccfc11d983e66d0e800e3c1befb6699cce339d8a36fba883dd397dbbad46cc0 | d168e5c0c508656b0688faf02985bf4255e0e3b819f99de888fb33f26595c962 |
| NCT02117713 | protocol leakage plus non-independent extension | 197 / 83 | 0c2d0a36cb23f8f8dfcf5d15446ada44ad2f9ddaa368260a115f9d9c6d018cca | f87187958939dacf72681262e97cb799bbaf18b922583567cb43f8e7a5238220 |
| NCT06101823 | protocol leakage plus post-primary SAP | 83 / 85 | 04bce0625fc58bc61a97d55fb7cc78a011ce8d1b7ef3382c8894b9dfd3c21c39 | f770e322275f92113ee99ba78698dfdeaa1284dc85831af319018833f22d6688 |
| NCT03283319 | protocol leakage plus post-primary SAP | 73 / 39 | ae65daae81f92bca7b4b93d8ad902b33df7a13acc06d2b09a6d99dedfd91d1cd | 4c257ddfb229ae4359b54ccd0547838b16ea5b1ce52eb90e8c5362deb9ef829f |
| NCT03956550 | protocol leakage plus execution-informed SAP | 73 / 69 | 15710f440f4c932a7826d0aea5c57d81d5b1549b820605f3cc8a0c658ed3a101 | 20b04b41c58b67cb3e1ef88af79a8a8ff002b9d7302e97751aaccbcea37260ec |
| NCT02224703 | protocol leakage plus post-completion pair | 121 / 66 | 04932dbc584f231adc95d0b3ed127af1d46b5f1802dcda3c646fe184c83ac190 | 1ee9a43867946fd97d1ab67d36df43c577b21affd85600c4a946b9a24f05076c |
| NCT01698918 | protocol leakage plus execution-stage extension | 131 / 71 | 235d155ae611c8e27a8077fe63c051500c6ef4c5d51cbc81ef5fcec71dcae060 | 121b6b54d33837cc135b2a66830620a122153b7c4e9ad3287093d3b8d1281a17 |

## Review gate

None of these eight families may enter train/dev/test. Each fails prompt/reference independence, and six also fail prospective chronology or independent-family provenance. Batch 72 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
