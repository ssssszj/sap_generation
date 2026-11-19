# Expert Review Packet — Batch 78

## Scope

Batch 78 reviewed eight ClinicalTrials.gov document families. None passed the public, prospective, version-matched, independent-hidden-target gate. Seven model-visible protocols expose executable target analyses; five of those references also have post-primary/post-completion, execution-stage or governing-version defects. The remaining otherwise prospective matching pair materially redacts its hypotheses, populations, sample-size and primary-method content. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology, version, redaction and decision-defining pages.

## Decisions

- NCT03098979 — protocol pages 57-68 expose sets, MCP-Mod candidate shapes, target-dose estimation, missing-data strategies, allocation and interim rule; the selected SAP is post-primary.
- NCT04867785 — protocol pages 66-71 expose sample size, populations, estimands, MMRM, multiplicity, safety and interim rules; post-completion SAP v3 is based on Amendment b rather than selected Amendment c and adds a management-requested third interim.
- NCT04845620 — protocol pages 53-56 expose sample size, populations, hybrid estimand, MI/CMH analysis, effect measures and the sequential hierarchy; the prospective initial SAP adds implementation detail to an already executable plan.
- NCT03422172 — protocol pages 54-58 expose the complete simple descriptive Phase 1 design, populations, safety and PK analyses, acceptability/tolerability summaries and no-interim rule.
- NCT04130802 — matching prospective pair is held because protocol pages 38-42 and SAP pages 7 and 28-29 obscure material hypotheses, population, sample-size, model, safety, missing-data and output details.
- NCT02642393 — protocol pages 90-97 expose the primary model, populations, censoring, two efficacy/futility interims and sample-size/alpha rules; the selected SAP is post-completion.
- NCT02023697 — protocol pages 109-116 expose populations, both primary comparisons, survival models, confidence intervals, censoring, sample size and interim rule; the selected SAP is post-completion.
- NCT03982368 — protocol pages 75-81 expose sample size, populations, Williams/ANOVA primary analysis, sensitivity and safety methods; post-completion SAP pages 2, 9 and 39 use actual early termination, completion and database information.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03098979 | protocol leakage plus post-primary SAP | 86 / 39 | 7263a07f1c463b0c45809e86f45a94eea48551f1afeb18a21618808a1c28905e | 8d2ab81a4522ab97ddbf357c77496e7bde92ea85e39201c65ee41bd557dec76f |
| NCT04867785 | leakage plus post-completion execution/version defects | 123 / 54 | c32a675536467353c5ec209a95242a9267bbd8b2f23837bc902251bdb896418e | d2f30c37d3ca201025f5defc6f7bbfdf8830b6950f3455495652e61bf13c9566 |
| NCT04845620 | protocol leakage | 83 / 45 | 236a74d3beb604ca312baecab0f0485d75b1afcfc76a732fe340d0f122d9df99 | f6825aa8c9b36524ed1023579087b27ff7fa03e13253572d43f4f4204880a720 |
| NCT03422172 | protocol leakage | 123 / 173 | e30ec429c78915a7217ad2f96db78c827e8bb1fd81948572b9c63bff52eadbf8 | d35ffce7462ed916812dafae221881520e7ddc1b7d112bd72471b0b7af0be5fe |
| NCT04130802 | public-redaction hold | 65 / 33 | 28d1b8f9d7c7b22cb621562b2de5028f49917f657886a645191aa23d63658562 | e57d10475903a1967c676a14355d080eeaab424f9f83fef859d2bfbe593a23e8 |
| NCT02642393 | protocol leakage plus post-completion SAP | 127 / 34 | 5199476fdf743054d1614fa40d876afd77a8f2093cd025342f52b00310c37051 | f94b8cc4bd05aaa3d41449572d9cc4645e5e0f5e66ba7e90540cec88c4dbb29f |
| NCT02023697 | protocol leakage plus post-completion SAP | 292 / 55 | 94f955e916e850aed124b486be2177b7b400798feb8c42d1e6996d635e65e020 | 3682d34ed8764b0e3e942c1152200dcbce29acf7b9b1051c6463c92672c57d2d |
| NCT03982368 | protocol leakage plus post-completion execution-informed SAP | 91 / 64 | 1c03afa1e1ec303bd79c49f898eeea69eca617be66ffdb740bda60b583089211 | 4b14ed57018e023df3538f010de2a10d59231c38e8d997691686a20989e9ef79 |

## Review gate

None of these eight families may enter train/dev/test. Seven fail prompt/reference independence through executable protocol leakage. NCT04130802 remains outside the actionable queue until an unredacted public pair supports complete evidence-backed annotation. Batch 78 preserves 72 registered public drafts and returns all eight reviewed slots for candidate replenishment.
