# Expert Review Packet - Batch 113

## Scope and decision boundary

Batch 113 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen official PDFs and eight registry records were downloaded sequentially, byte-checked, SHA-256 frozen and extracted page by page. Seventy-six decisive identity, chronology, family-dependency, statistical and document-type pages were rendered from the original PDFs and visually inspected. No family is promoted: four selected SAPs are post-primary, post-completion or explicitly outcome-informed, two are parent-study-dependent extensions whose protocols expose the analysis program, one is both post-primary and decision-complete in the protocol, and one has byte-identical protocol/SAP uploads.

## Decisions

- NCT01342952 — exclude: AMB114588 inherits treatment history and baselines from parent AMB112529; protocol pages 42 and 44-45 also expose populations, feasible sample size, descriptive analyses and Kaplan-Meier reporting.
- NCT05856526 — exclude: SAP Version 1.0 follows primary completion by ten days; protocol pages 74-80 expose the hierarchy, estimands, exact test, MMRM, missingness, safety, randomization and power program.
- NCT02666430 — exclude: this extension inherits baseline, eligibility and randomized treatment sequences from MYL-GAI-3001; protocol pages 64-70 expose the executable equivalence program.
- NCT03329209 — exclude: the final SAP was approved after both primary and final completion; protocol pages 54-55 already expose its descriptive PK/safety plan and n=16.
- NCT02372877 — exclude: SAP Version 21 follows final completion; protocol pages 57-62 expose equivalence margins, power, populations, imputation, sensitivity, safety and interim analysis.
- NCT02927457 — exclude: the RAP follows primary/final completion; protocol pages 58-62 expose Bayesian sample-size scenarios, populations, mixed models and interval reporting.
- NCT00865566 — exclude: the 2014 plan followed the April 2013 DSMB stop/unblinding and a second result-informed protocol change, so it is an outcome-informed extended-follow-up analysis.
- NCT03642938 — exclude: the protocol and purported SAP are byte-identical files, leaving no independent hidden target.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01342952 | related extension family and leakage | 73 / 165 | 690c8ecee62270ac92a6cb277116a3f2e2780cbce630ac144cea50885261939d | f0fada8c2e5f0574b11a78021c888ffaf96d81358646940764e0676d91cf62c8 |
| NCT05856526 | post-primary SAP and leakage | 133 / 44 | 96d0b3a7abddb0e5f15dfcd7da6759167c8252f23ab2f83aceea3a0ef325d6d4 | af3cf7d5a36ee7ac6f0236858d3b043e3c9a86b64a44a8645f1d9a0bf55a32fa |
| NCT02666430 | related extension family and leakage | 90 / 39 | b654732bbf2ad1db337d91f2814c8e6a1b3065293d4ed2bff1cf774ea78d280e | b3914bb5510b0eeb417f5d49a6a4d0c0df981f2fefaf77c4e9dc6eb17971b239 |
| NCT03329209 | post-completion SAP and leakage | 83 / 22 | 3f8110723360c07ee67b060b588b3fc543eab8e109f76351864a210849aee206 | a891adb9afd1df13add1acd24c1b989975084970b593fd0f7844a316192807cc |
| NCT02372877 | post-completion SAP and leakage | 134 / 83 | ba754cd5306d622d7e17e3bbc82a52bfaea056fd5d9329fc996c1217eaba6e4d | 043743ea8ef30b50fa3bf27fb6e2c88b4e3ed293d018d8a088cd98fe724016fc |
| NCT02927457 | post-completion RAP and leakage | 119 / 93 | 21dbe36f9459a8ef53a67d0f9e9e42f9f2c2508b15576b28aefba428d23fd540 | 6ab9c844979807b90282d79fda412cae815454d680e7bcf8cfe115a01411a8c1 |
| NCT00865566 | DSMB/outcome-informed follow-up plan | 112 / 29 | 39358572a9684644dd5e9e6245683a1018dc0ee85d1c7ec8b96e7b2e9cad5c31 | 3050756dd5f6b25cd05277217e481fc6e5e1ee434eeefcd46b447fb120a0f626 |
| NCT03642938 | byte-identical protocol/SAP | 12 / 12 | 0f8f0ebe211215c720cb130b484adb1e080ca9c50c4ba9de14f64533f1b08274 | 0f8f0ebe211215c720cb130b484adb1e080ca9c50c4ba9de14f64533f1b08274 |

## Review gate

No Batch 113 family enters the registered benchmark. All eight slots must be replenished so the release intake remains 100 version-verified public drafts plus 20 actionable metadata candidates.
