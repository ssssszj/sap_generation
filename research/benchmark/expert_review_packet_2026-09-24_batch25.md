# Expert Review Packet — Batch 25

Batch 25 promoted one study and rejected seven. NCT05187013 passed the identity, timing, prospective-document and protocol-leakage gates; five pairs exposed the target analysis in the model-visible protocol and two lacked a trustworthy prospective protocol/reference-SAP pair.

## Promoted annotation draft

### PUBLIC-MHEALTH-HOMELESS-HTN-001 / NCT05187013

- Identity and timing: the protocol and separate Statistical Design and Power document share NCT05187013, NCR203140, the exact title and 2021-01-26 date, before study start.
- Protocol-leakage gate: the protocol describes the two-site randomized design, outcomes, sample target and an unspecified interim analysis, but does not expose the reference document's t-test, mixed-effects, conditional ANCOVA, adherence-regression, GEE/MANOVA, MAR or grounded-theory choices.
- Annotation: 24 atomic evidence-backed requirements spanning design, randomization, outcomes, sample size, ITT, analysis models, estimands, missing data, multiplicity, interim analysis, qualitative analysis and safety.
- Expert adjudication: resolve endpoint hierarchy; the reference document's AIM 2 label beside a mean-blood-pressure power calculation; visit windows; estimands and intercurrent events; definitive primary models; prespecified covariates; missing-data sensitivity; multiplicity; interim rules; safety analysis; and qualitative sampling/saturation.
- Input isolation: only `input/protocol.pdf` is model-visible; `reference/sap.pdf` remains annotation-only.

## Screening decisions

- NCT03271021: `excluded_combined_protocol_sap_leakage`. Scanned protocol physical page 3 gives ITT/PP, MI, LOCF/BOCF, co-primary endpoints, ANCOVA, CMH and two-sided alpha 0.05.
- NCT03036592: `excluded_wrong_document_type`. Both files are titled INTERVENTION STUDY PROTOCOL and dated 2016-09-01; the purported SAP contains executed-analysis wording and no defensible independent SAP identity.
- NCT03077412: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 75-78 disclose populations, missingness, primary CI, NRI, KM/Cox, safety and sample size; SAP Version 2.0 also postdates completion.
- NCT03401112: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 65-67 disclose populations, safety/PK/PD methods, interim analysis and sample size; the SAP also postdates completion.
- NCT03131648: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 94, 97, 100 and 110 disclose estimands, CMH, MI, sensitivity and multiplicity; the SAP also postdates primary completion.
- NCT02175758: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 70-76 disclose populations, missingness, SVR12 analysis, exact binomial inference, DMC and sample size.
- NCT04731233: `excluded_wrong_document_type`. Both uploads are dated after primary/study completion for a terminated study with actual enrollment five.

## Source audit

All 16 PDFs were obtained from ClinicalTrials.gov, hashed and page-counted. Identity pages and all decision-defining statistical or timing pages were rendered and visually inspected; the scanned NCT03271021 protocol was additionally OCR-checked. Reference SAPs remain annotation-only acquisition artifacts under the gitignored source tree.

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT05187013 | promoted | 10 / 9 | `b1232103f7f1121c6234f5e37c03d77727bc88b8d38f910ab375bb33b43ca5fa` | `af0e4da0feebf4167db4661767aa42a1e5019c0b2de3a072734af22ff6e48f79` |
| NCT03271021 | protocol leakage | 3 / 36 | `322200e8e015f4a36bbe507c1b8c0a812565e9ddc002353233b6e5278ee773f4` | `b12915a4d6256e57eeaca478a57662bece91d9bb4e59bdc2174597a1339c6d58` |
| NCT03036592 | wrong / non-independent document type | 4 / 3 | `84012d629f397d7e00586a1c1fb4ccf0fb3fe0e72388124a00314cdb1ad98822` | `88ee683f6c03e45f318cffe068876b49c34489faf1ef55e979d8d260903685d8` |
| NCT03077412 | protocol leakage / post-completion SAP | 104 / 83 | `676bd187c1e63dc3b73e640fd627a42d3404e648a006a134795497a007081d34` | `72785a90eaa43b5b7c9f172696a9ced3cf2c85e3154d8db68fe31fca80b3bccd` |
| NCT03401112 | protocol leakage / post-completion SAP | 79 / 75 | `25684358eb5d89eedbe7b60dc61f432bdfbaef9749fd99d8c690b22d5cee1592` | `d5b944cca8406cdc9f8b18257db6b05c9a26c83195e248886ee99bc114e58d96` |
| NCT03131648 | protocol leakage / post-completion SAP | 171 / 33 | `c1d59696ff5366f88eb69e9b128e7d8e5e7c49de4c4ada3b6e9ab5ab769d59c5` | `66e90403d2182b926c1cf3f4fd971a06b66375feca61faa691956170ed4d8238` |
| NCT02175758 | protocol leakage | 119 / 52 | `215fa324785cbae1bfbe95c85705daf84067d1b074242ef4f3e0598a822c0782` | `8663c55e536603cf85a23759b718d4d46b6162cbce9057f49fc446d5b7a955b4` |
| NCT04731233 | post-completion documents | 2 / 2 | `14142a8ddc9fdf142f41301cde2dd5045d0f91dd4d8057e72b8b63d051510fb5` | `4e88e951e37e8c4c2fbc9a84387ada9e5fba177c63f8473454b6a68d5666d077` |
