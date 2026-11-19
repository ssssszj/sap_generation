# Expert Review Packet — Batch 24

Batch 24 produced no promotable study. Four pairs failed the protocol-leakage gate and four pairs used post-completion CTR, CSR, result-bearing or otherwise execution-informed documents.

## Screening decisions

- NCT03464110: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 8-10 disclose the hypotheses, mixed-effects models, covariates, missing-data approach and power assumptions; the short SAP substantially reproduces that material.
- NCT03197883: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 82-84 disclose an execution-informed sample-size revision after treatment misallocation, populations, success rule, missing-data handling and primary/secondary methods.
- NCT02918279: `excluded_wrong_document_type`. Both uploads are Clinical Trial Report appendices dated after primary/study completion; the embedded final SAP is also post-completion.
- NCT03017235: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 59-65 disclose the populations, noninferiority margin, hierarchy, confidence-interval method, missing-data sensitivities, safety and interim strategy.
- NCT03370913: `excluded_wrong_document_type`. SAP physical pages 2-3 are a 2023 Note to File aligning the protocol and two-year SAP to a completed CSR after FDA-requested revisions, with hypothesis-test outcomes already known.
- NCT03055494: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 64-67 disclose analysis sets, primary methods, missing-data handling, sensitivities, database locks and sample-size calculations.
- NCT01983683: `excluded_wrong_document_type`. SAP physical page 1 explicitly targets the Clinical Study Report and postdates study completion; physical pages 159-161 add execution-informed site-integrity revisions and actual counts.
- NCT03636386: `excluded_wrong_document_type`. Protocol physical page 3 reports results and p-values, while physical pages 4-7 contain actual enrollment, baseline and randomization details; the SAP contains populated result tables.

## Source audit

All 16 PDFs were downloaded from the ClinicalTrials.gov registry, hashed, page-counted and extracted by one-based physical page. All identity pages and decision-defining statistical, timing, CSR and results pages were rendered at 144 DPI and visually inspected. Reference SAPs remain annotation-only acquisition artifacts under the gitignored source tree.

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT03464110 | protocol leakage | 12 / 4 | `dacb615e1e8617e914c85efbcff9c7e93a880821d1d2c7197f2106d623065cb6` | `3050bbac479db22aadfbea31fb0f29275228e8bd5455aee1771810bca6a830b9` |
| NCT03197883 | protocol leakage / execution-informed amendment | 93 / 46 | `8a4e23958d6bdd38c304f3995d7838f6bc28ecf52a7f80c5783f727f4850a397` | `bfc9be2116dac864dd55e3531915a4bb0b3d0c7afab32d30597895a55f14dd8d` |
| NCT02918279 | post-completion CTR appendices | 150 / 31 | `e4329b592f6516aac84c626dace9fccc727417c2b8e446bea82782a7d580d120` | `219be6d6b0ceb9ebad6959c3adfd6d5738ad7c26a1b8aa4ed79d8e00cf3467f0` |
| NCT03017235 | protocol leakage / post-completion SAP | 84 / 43 | `3218c18d029006da98a2c458b35a3988a152a2e352227d55cb506ce1d60130ff` | `cd254ad29eb6502882bcaacf4baf4dd512f3e86313c44a17c8f3ce9fa4d5d978` |
| NCT03370913 | post-analysis CSR bridge | 992 / 82 | `c2bc962d82036aa4ec6cca921dd577a92bbec2868173ee3e301133c7ede5495d` | `09a47e24c80d1db1a5bf374085b193c227f57d87832feb4b373c57d3150df417` |
| NCT03055494 | protocol leakage / post-completion SAP | 81 / 40 | `d6253eecc80f71db999d167579990aec66e61bf6f32f4e58585e8f172b5f7740` | `68a067f966513c8d4bc06b6b6a9b83f61d12fafa725a6b4a95a45a74130b78b7` |
| NCT01983683 | post-completion CSR bundle | 138 / 164 | `9d1ad2d3f47e989aff1bef5d6378a8664cc1da779e84af00780b2df48edd9bff` | `6492828309a64241b6f70f76bc001a59608c11069ca9ca7bcb6cfe8b95e76e44` |
| NCT03636386 | completed-study results documents | 10 / 46 | `5ef7a073c54cb335591ffd62c3476dde7f891b463c9aec43d2529b05bb45cf2f` | `e080cfc99680869ec9a9ef1d22fdf0a5541261b496da0c7789d963ef4530dcda` |
