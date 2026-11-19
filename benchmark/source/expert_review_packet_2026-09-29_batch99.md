# Expert Review Packet - Batch 99

## Scope and decision boundary

Batch 99 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally and extracted page by page. The batch produced no promotion: four families fail the protocol-only leakage boundary and four fail prospective governing-version chronology. All eight slots are replenished rather than reducing the 120-family intake.

## Exclusions

- `NCT02975505` — the 2025-02-13 protocol/plan pair postdates terminated-study completion on 2021-07-18 by more than three years.
- `NCT02612857` — protocol pages 21-22 and 74-76 expose populations, repeated mixed modeling, logistic regression, power, one-sided alpha, safety and missing-data rules.
- `NCT03422159` — protocol pages 7 and 9 reproduce essentially the entire two-page SAP, including endpoints, power, target, tests and alpha.
- `NCT01972529` — Final 3.0 SAP dated 2017-02-16 follows primary completion on 2017-01-26 and is embedded in a CSR appendix.
- `NCT02418000` — SAP Version 1.0 dated 2017-10-19 follows terminated-study completion on 2017-06-08.
- `NCT02176486` — Final SAP dated 2018-03-06 follows completion on 2018-01-19 and cites Protocol Amendment 9 rather than selected Amendment 11.
- `NCT01543087` — protocol pages 76-79 expose the estimation framework, repeated mixed model, endpoint intervals, populations, safety, missingness and interim timing.
- `NCT04343235` — the five-page protocol exposes planning rates, power, alpha, sample size and named categorical/continuous tests, leaving little protected target in the SAP.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02975505 | post-completion pair | 11 / 1 | cbe69ecb7b2a00bc30bb05a1832fa21b57f2d82afcb698796c0e1b3fcf39d420 | acfa50d767b858700f427adb7f047ed10a6ab717d0c323f82be4a37157aec289 |
| NCT02612857 | protocol leakage | 110 / 53 | 37048b15bb8f0d2e7cdb60cae3ef609b0792162881e58919554fe408f39123bf | b1db37895acbf5f16d05ba55c9b95fb56dd1b7cad66ef3d78455de7b72823c8e |
| NCT03422159 | protocol leakage | 15 / 2 | d26a62edbc2e7a42afc54b8df3e6a289080b583385e9a10aa41f3d49e1e0cdfb | a2bf34947de140849968a6556a4f18e6ea333009bda7989031ef9cfbb6813a5f |
| NCT01972529 | post-primary CSR SAP | 101 / 30 | d9e5d1d64028b87dbe438aae060bb2c4bbb74410badd1571e43817bf5d567e82 | 461777ddb3dee9456fb5b4654b67c67ea6257d3b8b3711e939cd66aae9ea9dc7 |
| NCT02418000 | post-completion SAP | 72 / 16 | 1aa6d014b8cb876bbb3d63175f43af1b0525b6b9338c699833731ca83010ba54 | d8140c63fba50db4efac95495f1c66b03cce8a06fd2534908a37e24fe2e51ba0 |
| NCT02176486 | post-completion/mismatched SAP | 165 / 27 | 4814b6ace6015c6ac5134f3c58bdcc05af9e0f6126e9444877bcf697773ac9fc | 6a3c7decfe9aa0d24d3d974e251cbfe253423ff8cc7fc292e51ba228d92b6c17 |
| NCT01543087 | protocol leakage | 88 / 25 | 4bfefbff9c39374e8493d9e8abc86de090d2a08a84188c9381c1a1fba325e18c | c34f8fa77fe307bf066cb1eb11b4f9384f37dc2f36a173703f43ad07ec25e5e0 |
| NCT04343235 | protocol leakage | 5 / 2 | c29d094e0c9fdb19024d86347fd1c7d1ada281a55855e530fe49114d903cb010 | 557e5b73c4a41cf3b430bf11fbf92bb70354e08bfdd3b1628634b2f425938ac7 |

## Review gate

No Batch 99 family enters the registered benchmark. The candidate pool must remain metadata-only until the replacement families pass document-level review.
