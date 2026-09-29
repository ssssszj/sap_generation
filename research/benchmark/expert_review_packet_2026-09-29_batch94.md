# Expert Review Packet - Batch 94

## Scope and decision boundary

Batch 94 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally and extracted page by page. The scan-only NCT03365934 and NCT01881425 files were fully OCRed, and decisive identity, chronology, leakage, interim and execution-stage pages were rendered and visually inspected. One family is promoted as a first-pass annotation draft and seven are excluded. The seven open slots are replenished so the intake remains 120 public families.

## Promotion

- `NCT02996864` -> `PUBLIC-HEALTHY-DETOURS-001`. The 13-page operational protocol and independent three-page Statistical Analysis Plan share the exact title, NCT and 2016-08-16 date and prospectively describe the Fall 2016 and Spring 2017 LSU RCT. The model-visible protocol defines the two apps, 300 target and baseline, six-week and 12-week procedures without exposing the reference-only HEI hierarchy, ANCOVA, Hotelling T-squared, generalized least squares, CACE or bootstrap mediation. Twenty-two evidence-backed requirements were added. Because both files were uploaded after study completion, their original unmodified IRB/grant provenance remains an explicit review gate, along with allocation, population, scoring, estimand, missingness and multiplicity details.

## Exclusions

- `NCT02260258` — completed-study combined protocol/SAP. Both ten-page files are post-completion and use executed-study language, including an eligibility change after participant 42.
- `NCT03365934` — post-completion SAP. The scan-only final SAP is dated 14 days after actual primary/study completion.
- `NCT03155945` — post-completion SAP. Amendment 1 is dated more than six months after study completion.
- `NCT03370172` — post-completion SAP. Version 2.0 is dated almost three months after study completion.
- `NCT02776033` — protocol leakage and interim-informed analysis. Protocol pages 59-61 expose populations, unblinded reviews, formal interim analysis, MMRM, GEE and data-dependent probability-of-success work.
- `NCT01009814` — protocol leakage. Protocol pages 6 and 72 expose power, thresholds, confidence intervals, primary analysis and PK/PD models.
- `NCT01881425` — execution-informed within-study plan. SAP v1.11 follows Phase I and the 75-participant interim safety review and adds analyses using available 24-month information.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02260258 | completed-study combined protocol/SAP | 10 / 10 | 5f7714bad20dc36bd1445ff3746f3efdaa1ef8c7fba267104c940992faf786f4 | dc984f2856789193856a1bb508c8febe5e88ca3a6b2bcc959c093a9216fd26d4 |
| NCT03365934 | post-completion SAP | 60 / 11 | 9b51e10e49dbd728b45a4ef2c83b2f70a5d60769dde604cedf561675746ba6a1 | 4b90a7230e165286d3c21a11a12d6da3c26577b63aeeed1120dc4529ca4761b7 |
| NCT02996864 | promoted draft | 13 / 3 | 07ab7fd7ca5246dc0ac0bb70f6961c4b8cc52fd4ab738379f9e01f693dcb9e4f | f2974d6df334f57dfa8a4defa8589165c40c79f7e30d57c557b68fb3f7abba2c |
| NCT03155945 | post-completion SAP | 117 / 30 | 3f0e1c63889964444b925681d57c550664ba989afe65a400d73787c87cedff88 | 395c36ff7edd9c48109da6669d625e3d03acd829862642db617adccedd0be661 |
| NCT03370172 | post-completion SAP | 107 / 65 | 0e794a587bb565a425f844e9a0626efb7b6cdb8a6698e6b1c2df7706e7a9605b | e6152d089f1aa376edf695432b8975bd68ac2ea863d99c29ce97241fb37210bc |
| NCT02776033 | protocol leakage and interim-informed plan | 107 / 104 | 161088cc877f761bf933ef58bcca2132ee7140b7b2070f24f0369af9d567fcd8 | 679fbb0999b8bb1b48a51469a56cba1872429515dde8934f080d0d6249c7e52d |
| NCT01009814 | protocol leakage | 91 / 53 | f3938ea58a216488cf152d07911ac1b4ad064078a086b3a24e93e1f96c7e2e31 | 4f12bd459063152f092f634a8ef1b972dd9f74111819e4a082e747f3800889a3 |
| NCT01881425 | execution-informed within-study plan | 85 / 32 | 1d40de7aa7a732c3b053aa13e74cc6136edeb1e7bb87e90d6ba4725816905b1f | 41bdf22f7d8f04e8ca6b0ff6e4e2a53ffb73b98ec0b70e166a38495c58483875 |

## Review gate

The promoted family remains `draft_needs_expert_review`; it is not expert-approved or split-frozen. Its reference SAP remains annotation-only and must never be model-visible. The seven excluded families do not enter the completed-question count.
