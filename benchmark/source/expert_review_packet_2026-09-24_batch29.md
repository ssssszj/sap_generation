# Expert Review Packet — Batch 29

Batch 29 produced no promotion. Three protocols expose the core target analysis, four purported SAPs are execution-informed methods reports, and one SAP was approved after actual primary completion. All 16 source PDFs were obtained from ClinicalTrials.gov, hashed, page-counted, text-extracted and visually checked at the cover and decision-defining pages. The scan-only NCT02394730 SAP was additionally rendered and OCR-checked page by page.

## Screening decisions

- NCT01683825: excluded_wrong_document_type. SAP physical page 2 describes imaging and software already used, images already acquired and reconstructed, and assessments already performed.
- NCT03255382: excluded_combined_protocol_sap_leakage. Protocol physical pages 74-78 disclose populations, CMH, NRI, LOCF, ANOVA, multiplicity, safety, interim and sample-size decisions.
- NCT03265223: excluded_wrong_document_type. SAP physical page 2 says envelopes were opened at study end, calculations were made and analysis was done in SPSS.
- NCT03203694: excluded_wrong_document_type. Its one-page analysis note says all analyses were completed and describes comparisons selected after significant interactions were found.
- NCT03518086: excluded_combined_protocol_sap_leakage. Protocol physical pages 79-81 disclose power, populations, multiplicity, CMH, logistic regression, MMRM and ANCOVA details.
- NCT03497650: excluded_wrong_document_type. SAP physical page 2 reports that data was analysed, distributions and group differences were tested, and effect sizes were calculated.
- NCT02394730: excluded_combined_protocol_sap_leakage. Protocol physical pages 17-18 disclose sample size, repeated-measures regression, robust standard errors, sensitivity tests, longitudinal and safety analyses, populations and multiplicity.
- NCT03464136: excluded_wrong_document_type. The SAP was approved 2020-12-16, after actual primary completion on 2020-12-15; protocol physical pages 51-53 also disclose power, Mantel-Haenszel testing and hierarchical multiplicity.

## Source audit

Identity covers and all cited decision pages were visually rendered in addition to text extraction. The NCT02394730 SAP has no usable text layer, so all eight pages were rendered at 200 dpi and OCR-checked. The files remain local, gitignored screening artifacts and are not model inputs.

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT01683825 | execution-informed document | 17 / 2 | 9253e53c7c31f334f9cf774a81b4272437de6fb7251ece53b95d488964cbf9dd | 22694bf039eba37551fcf5bfd011ef1ca599a69558b54ee241e16c87300b4145 |
| NCT03255382 | protocol leakage | 118 / 44 | d7acb4afce97e3a6e2dff9ad50088ac8844ad91dc9ddea84bbf3a261a9ed42ee | bd44761aaeef1650b24dcb252548520ef3f51b999fecf8b8aceab36569579bdb |
| NCT03265223 | retrospective document | 9 / 2 | 513bf652f4bcdb6c47552c573ee446f71c883e9335c3e22209a11d3c64514970 | d16959f059f3f04873a86af995ec096770768511964e6821c88b6052aeba975b |
| NCT03203694 | completed-analysis note | 10 / 1 | c4e661d18457def35adc80cce862291c70389075ba6e60cac05cc28b68a41552 | 60fd0632796a40389eee9d1981ea7befc18d9c294d00c8909809c707830d1a91 |
| NCT03518086 | protocol leakage | 150 / 71 | dc979f3cd99fadea6d01468b354d1a4c46d0ca1682b6f21f1a4dfa1c9dc5b679 | b2b62f00e9185e01ecd3b07c80ced6ac830309ecd8785537ac0b64d5d7d876c5 |
| NCT03497650 | execution-informed document | 2 / 2 | 5ab510d50c4b64345c49a2fcc9d21aa9cf99339f7421f563ecc067e8cf13f6a9 | 9ced096b3356b7a7f9b1f98dcf993bd6806e547d048f80ebe6f6c68ae75ea936 |
| NCT02394730 | protocol leakage | 99 / 8 | 0576f9ade729de707b9e8137e98304ea7dd3a8eb1a78b5eb15502d0d4a711dc9 | c73753e10c311340d6c46ee18af10d298155fc51c27c6ee23ae991a9298d1f39 |
| NCT03464136 | post-primary SAP | 105 / 63 | 3722af4214d8a5834feeb84f9abddf8e309d08a8c5ad8ef76644cedcbb58cd41 | 8b09d2921e93f27d66e6e8ca8170ed5564988c126123dd2178fdea3a9fc45840 |
