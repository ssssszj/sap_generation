# Expert Review Packet — Batch 74

## Scope

Batch 74 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the public, prospective, version-matched, independent-hidden-target gate. Every model-visible protocol exposes an executable target analysis. Four selected references additionally postdate primary or study completion or incorporate executed-study information. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology, redaction and decision-defining statistical pages.

## Decisions

- NCT02998840 — protocol pages 38-41 expose sample size and power, analysis sets, mixed model, ANCOVA, confidence intervals, safety and missing-data handling; the final SAP is post-primary and revises a power assumption.
- NCT04657016 — protocol pages 69-75 expose hypotheses, sample size, sets, estimands, ANCOVA/logistic/MMRM models, multiple imputation, Kenward-Roger inference, multiplicity and no interim.
- NCT04004611 — protocol pages 103-108 expose sample size, populations, imputation, derivations, PK/PD, snapshots/interims and multiplicity despite visible public redactions.
- NCT03738397 — protocol pages 57-58 expose populations, CMH, NRI/MI, power and safety; both selected documents are post-primary.
- NCT03318315 — protocol pages 116-124 expose sample size, power, precision, interim analyses, populations, exact intervals and categorical tests; the SAP states that it does not change the protocol analyses.
- NCT04052620 — protocol pages 51-56 expose sample size, populations, margin, ANCOVA, interactions, MI/MMRM and no interim; the post-completion RAP/SAP records COVID-19 and sensitivity changes.
- NCT03022799 — protocol pages 62-66 expose analysis sets, descriptive conventions, PK power model/ANOVA, PD summaries, no interim and cohort size.
- NCT01702571 — protocol pages 15-18 expose populations, no formal testing or multiplicity, KM, ORR/CBR, precision and interims; the SAP follows seven interims and a mature-data dry run that changed planned output and analyses.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02998840 | protocol leakage plus post-primary SAP | 58 / 80 | ce940e3575b45b2f65a956e814c7ff2aab4051d9237d204f87c470f78ffd1d28 | e6cc686141d642e0614a3d8c370d043f8f385d8f321b7ceaf03ff2a2b1d49415 |
| NCT04657016 | protocol analysis leakage | 115 / 69 | d1337bf02803fc62c84c72216e566275f67f559d37b341e6bdc457d02a51d1b1 | 0d930dd43d8b297debc0d0969a3860773f084a89e9614e57f2c82dc9f340d881 |
| NCT04004611 | protocol analysis leakage with public redactions | 155 / 54 | 48a70793bd41da2e3f02e08ac3fea6d02d76fc5b9d15fc3d8c3612c422a0bdb4 | 24b5a0d80c5dd30e3e6174d7c6429d296d42864d6ac53c5abab75abcaa81d3f6 |
| NCT03738397 | protocol leakage plus post-primary pair | 74 / 65 | e1cbeb7d3d9fcb2c8c698922f12e133a569c8d25623dc1450b5d0c867c694a89 | eed8b4739156fbdbed293d336c4cea5409895f355bfaa0ce5e9a7d64f453cd58 |
| NCT03318315 | protocol analysis leakage | 156 / 190 | 21f3b4acb1766652bfb9e4d4a9437cc890b59472e0994cc7f0bfc374bf70fff7 | 122cca1a1b75f4416b431bee5c4250afd0d33f707d830df0041768232c09b9ee |
| NCT04052620 | protocol leakage plus post-completion SAP | 64 / 36 | 0afd9c308ae97ac1b28586ceb6e01199cc68d6bf66213f58770d31245a60790e | bcfae6cd8a9b3888303ca36ee2947569f28a267b77e9e7d30d6f420577dbc1b6 |
| NCT03022799 | protocol analysis leakage | 72 / 61 | b9f0b570a851c51c4b4eea3de3e9edcd5b4537eb3c53238b95a9306d33e399de | 41fc549e133d2c1876466865764d5426931ae6e09f39206ba342696232b9ceec |
| NCT01702571 | protocol leakage plus execution-informed SAP | 107 / 51 | 6be149d0f289222bdb06b25fafecd986c975ea9b386f062d2612035d75fdcdfd | 26e5fdd6e998b348607fdac90fc2b2c837705430e645855fccb94ea9e4590e74 |

## Review gate

None of these eight families may enter train/dev/test. All fail prompt/reference independence; NCT02998840, NCT03738397 and NCT04052620 additionally use post-primary or post-completion references, and NCT01702571 uses an execution-informed reference. Batch 74 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
