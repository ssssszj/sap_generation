# Expert Review Packet — Batch 67

## Scope

Batch 67 reviewed eight ClinicalTrials.gov protocol/SAP families. No family passed the public, prospective, version-matched, independent-hidden-target gate: every model-visible protocol contains enough executable statistical content to make the reference SAP non-independent, and five selected SAPs also fail prospective chronology or incorporate execution-informed changes. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining pages.

## Exclusions

- NCT02617446 — protocol pages 50-53 expose populations, sample size, primary/secondary models, interim analysis and PK methods; SAP is post-primary and records a 2018 memo-driven analysis change.
- NCT04276207 — protocol pages 62-67 expose crossover populations, models, Fieller intervals, PK/GD methods and the no-interim decision.
- NCT04026113 — protocol pages 84-92 expose IBS-C estimand handling, Bayesian borrowing, populations, endpoint derivations and the FC interim-futility framework.
- NCT05375955 — protocol pages 83-88 expose estimands, missingness, multiplicity, exact inference, ANCOVA/MMRM, interim analysis and sample size; SAP v3 is post-completion and responds to observed enrolment and rater events.
- NCT03146403 — protocol pages 43-45 expose populations, Wilcoxon, chi-square, Kaplan-Meier/log-rank, safety and interim analyses; SAP is post-primary.
- NCT03793010 — protocol pages 61-65 expose populations, endpoints, sample size, MMRM, ANCOVA and sequential testing; SAP is post-completion.
- NCT02760602 — protocol pages 51-57 expose sample size, populations, missingness, the primary and secondary repeated-measures models, subgroup analyses and gatekeeping.
- NCT01492088 — protocol pages 73-77 expose the 3+3/sample-size design, populations, exact-binomial and Kaplan-Meier analyses, safety and the no-interim decision; SAP is post-primary.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02617446 | protocol leakage plus post-primary SAP | 62 / 28 | 564ad7e15a294b6fab96bc2a5c76500efe5d132466406744eda3a5d0561d45a2 | 6b845938cb13c98048580bbad54dd230cc82fc3986feb9d133a694e49e8dd7b5 |
| NCT04276207 | protocol analysis leakage | 76 / 48 | ed37ee898a55200a6cdf8055be121569bcf0639e1e85a8a0be7aabeb806b3173 | c4179b5e9d8f1bf251b5ec95170c077abdce5471138ede69749916b0d56d9e1c |
| NCT04026113 | protocol analysis leakage | 136 / 125 | fb2acc76193c3d00e70ee754f6c4026fc1173f67513bfcf4aac0e0167b223c23 | 162e653eeb4eb85d663fe02f043b06c1e6381992b98d35265bed0b5daef576ab |
| NCT05375955 | protocol leakage plus execution-informed post-completion SAP | 137 / 44 | f1d1864b334f0fd1db349e5495dcb626a7be3a50a4de4c836306d8b55cfa03e3 | 9ccfc825e5b7a5a50978115dd9b52021d9cc7a363a51609299a8422f1ee569d1 |
| NCT03146403 | protocol leakage plus post-primary SAP | 75 / 69 | 95880db1e0883e32d4483d8d15fd2689af850f14e70fb52e8308ea6bafa9c733 | a71851cf3b131cea89c15a751587c61251b2d875e1299f59c4ef86046f152abe |
| NCT03793010 | protocol leakage plus post-completion SAP | 72 / 49 | 0cf2dea87379264908d59f6a6ee90d28d2d83d9386c3964b8e3950925015a9af | e3eca2bf316083fd0d8eb13fed9c2c03fc0219d2d57f2e8e087488b30d567c2e |
| NCT02760602 | protocol analysis leakage | 73 / 16 | a7faac09553fa4cea856e7840732024f654b07071f0e6400bc40da67edb921d5 | 54a51942bd155c41c6ba25a2b74e4549378943583ded65b84ebbcec217894561 |
| NCT01492088 | protocol leakage plus post-primary SAP | 127 / 25 | facd5deede2919174c96855e066afc588b569463cb111f15ef527411c744a554 | 260451709c0b46e82f32471a96327868054f6488551eac369fd96fcabc25c324 |

## Review gate

None of these eight families may enter train/dev/test. All eight remain outside the actionable pool because their model-visible prompts disclose executable target-analysis content; the chronology and execution-informed defects provide additional independent grounds where noted. Batch 67 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
