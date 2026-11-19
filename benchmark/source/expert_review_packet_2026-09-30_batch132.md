# Expert Review Packet: Batch 132

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 132 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,264 physical pages. Every page was text-extracted; all 96 pages of the scan-only NCT03214380 protocol were OCRed, and 158 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT02930018 — exclude: although SAP Version 3.0 precedes primary completion, protocol physical pages 14-16 and 61-66 expose the sample size, populations, logistic model, covariates, missingness, interim boundaries and fixed-sequence hierarchy.
- NCT03214380 — exclude: the scanned Protocol Amendment (a) exposes both estimands, copy-reference MI, MMRM/ANCOVA, graphical multiplicity, hypoglycemia models, populations and sensitivity analyses; OCR was checked against the rendered pages.
- NCT02289417 — exclude: both selected documents follow primary completion; the later protocol records completed-phase conduct and exposes the executable target.
- NCT03556202 — exclude: the SAP revision followed external safety-DMC unblinding, the long-term extension depends on four originator studies, and the protocol exposes the cohort, missingness, MMRM, ANCOVA and interim program.
- NCT02712359 — exclude: the governing amendment widened eligibility because observed recruitment was low, and the protocol exposes the sample size, ATP cohort, noninferiority, CI, ANOVA, missingness and sequence.
- NCT02696031 — exclude: the selected reference is a mixed bundle containing a post-completion extension SAP, and the protocol exposes the core and extension analysis program.
- NCT01866111 — exclude: the open-label-extension SAP follows primary completion and the protocol already exposes populations, ranked ANCOVA, step-down testing, missingness and efficacy/safety analyses.
- NCT02360579 — exclude: the SAP is embedded in a primary-analysis CSR package and incorporates realized cohort counts, completed treatment, COVID-impact and regulatory-communication changes; the protocol also exposes the executable target.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02930018 | protocol-embedded target leakage | 88 / 47 | `e448d522029774bda0a1a7a7e9013ec0f89a7b6d7c831797323b46af8ee5d95e` | `7654286cc76e0ece2a3d6204105bfd067f72f987190a6ee253f1788502e38fd2` |
| NCT03214380 | protocol-embedded target leakage | 96 / 54 | `eaa543984656630fb6f4a1b8c8f97e83f8c9e068a90f1920169f5a3be40ad9bf` | `4b66f83338c484ee6b7899ecc11604fb4fa43a8de88fd48b7c80390535d8fae4` |
| NCT02289417 | post-primary accumulated conduct + leakage | 99 / 51 | `90ba622751224875ee47a1dfa72c027fa42e2a7070b95c076d80d778e8bb5523` | `3b139fccdb4f7e451d73363771fa9b7881e1e3d591230eb1496d1e97e76dbe20` |
| NCT03556202 | DMC-informed extension + leakage | 103 / 44 | `0910f84a2d5acf6a8dbde6976c2e2324063baa98f6a79f28717b26eba9591ed6` | `1ecf02f5205e720d7bde48e453a5c5d4dfb61904e597c4b9eb16ef1a7c19e8a5` |
| NCT02712359 | conduct-informed amendment + leakage | 64 / 11 | `a9114d14e91ba9da5bf9478cc42fd2f1a91966f2f6364b38674df4e16091bfa9` | `6855481420157114623f9a5e3cd9ce8a51161b70c00d3a22f683772e448adf07` |
| NCT02696031 | mixed post-completion bundle + leakage | 120 / 117 | `5a9e93c5f99840d0ade58e90b835d1dd0aaa8fecce13af003ff5141666f0c977` | `8ada132667999f823e1cb3d5a26ffa9e81b21f6fa651df97c57123b6c8d96bb0` |
| NCT01866111 | post-primary OLE SAP + leakage | 163 / 43 | `87985c20b9ae190b70ab9a04a69cfd7073a3e31fbec883cf6b173ca5cb29bb12` | `4fd09a4b26364aea8873d661fed843d7e28c16cb4cb9adf095d4d10bed1304c3` |
| NCT02360579 | primary-analysis CSR material + leakage | 129 / 35 | `935cf9b5f5e7d56020e0d7427252b4d25d22a52bea3d2bda7550bb6c1f852970` | `bc703ea644e6e1d8390d89e78d7047d9a5dc331b6787680dff1aa1fe8f51e6ad` |

## Gate interpretation

- A pre-primary SAP date did not rescue NCT02930018 or NCT03214380 because the model-visible protocols substantially reconstruct their targets.
- A pre-completion date did not rescue NCT03556202 or NCT02712359 because the chosen governing documents incorporate actual DMC or recruitment conduct.
- A prospective section inside a mixed bundle was not separated from the post-completion extension artifact for NCT02696031; the selected public reference as distributed is not clean.
- CSR packaging, realized cohort counts and retrospective regulatory/COVID changes disqualify NCT02360579 even though the displayed SAP effective date precedes registry completion.
- Registry actual enrollment was used only for chronology and was never substituted for a prospective sample-size target.

## Replenishment

All eight excluded slots were replenished from the official API. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates.
