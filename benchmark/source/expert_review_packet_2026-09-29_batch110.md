# Expert Review Packet - Batch 110

## Scope and decision boundary

Batch 110 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen official PDFs and eight registry records were downloaded sequentially, byte-checked, SHA-256 frozen and extracted page by page. Protocol/SAP covers and 102 decisive identity, chronology, statistical, sample-size, multiplicity and document-type pages were rendered from the original PDFs and visually inspected. NCT05142280 is promoted after exact identity/date matching and a clean protocol-to-reference boundary; four pairs expose the executable target in the protocol, and three use post-completion or otherwise non-prospective target material.

## Decisions

- NCT05142280 — promote: Protocol Version 1 and the independent SAP both print the exact title, NCT05142280 and 2021-11-19, before recruitment began on 2022-01-19. The protocol gives generic regression families but not the SAP-only endpoint mapping, coding, reliability or modifier details.
- NCT04609020 — exclude: SAP Version 3 follows actual completion; protocol pages 48-50 also expose populations, testing, alpha, safety and sample size.
- NCT02414958 — exclude: the SAP follows final completion; protocol pages 75-87 and 117-124 also expose populations, MMRM, gatekeeping, missingness, negative-binomial analysis and power.
- NCT02980666 — exclude: protocol pages 358-361 expose the descriptive populations, interim/DMC and efficacy/safety program; the SAP file also bundles main and PK plans.
- NCT03993288 — exclude: protocol pages 94-99 expose the ANCOVA noninferiority analysis, PP sensitivity, interim recalculation, margin, power and safety.
- NCT02708095 — exclude: protocol pages 50-58 expose logistic regression, MMRM, nonresponder/placebo multiple imputation, populations, multiplicity, safety and interim decisions.
- NCT03474666 — exclude: the two-page SAP reproduces the statistical paragraph on protocol page 10.
- NCT03291613 — exclude: both documents postdate completion and report already conducted usability sessions and observed enrollment.

## Promoted-family annotation gates

`PUBLIC-ACTIVE-CHOICE-CVD-001` has 24 first-pass evidence-backed requirements. Expert review must reconcile the protocol's one/three intention-strength/commitment item counts against the registry's two/five, resolve the objective's age 40 lower bound against eligibility age 45, define the randomized analysis population and multiplicity, replace data-dependent age/modifier rules, and interpret the estimand as the full bundled intervention because the arms differ in risk format as well as choice framing. The prospective sample-size target is 724; registry actual enrollment 743 is conduct context only.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT05142280 | promote | 10 / 3 | 66903da2398df4ba667633f87abcc9244495748dbcb34f94dbd754d77cc12506 | b66538ebe28c0f09a7355681af1d9122db67183fde34f0bf49aa943095873e86 |
| NCT04609020 | post-completion SAP and leakage | 96 / 35 | e601b1da5417f70f673f8f93b702ecf21c8294d81777646dc96f33ca599bbd83 | 9710a6a022ee79161d66c7b125fbd99b9cae49773daa4903bb93b3964adb376e |
| NCT02414958 | post-completion SAP and leakage | 146 / 93 | 97b2a072d3d510156fc25be3e3e162a69a1c8cdd943feb825440b3e1d94d3045 | 023b30812ee56c8cbcf4b7fbcb8d828d18d0de06ce663177427aab1883c04aee |
| NCT02980666 | protocol leakage | 379 / 59 | ec3be7834da36abd655501e43f4e17e111390d35be13535a3db8d199037ae011 | 4fe4d73bca46bf35ce3f3c24e4dbcbb880c606757d54311d53e9c718dcc12a1d |
| NCT03993288 | protocol leakage | 117 / 69 | 9e4295db9132949afeb7de9b7d1064c7231998a05a80d15ce2098da06b86edb4 | ec4e0f699863f25601ae558677b00776474a07ae16a29ae1f829bf0c7b51a2bc |
| NCT02708095 | protocol leakage | 81 / 79 | d5c22add0bcc3c5462a4616ef81582cc737ab1410a87884776dee9c3e4c8e0c3 | a9a946b970a7b0a9764d015e2f3af253619b186029b55f16f142b7ad5eaea8b5 |
| NCT03474666 | protocol/SAP duplication | 13 / 2 | a57f7593f8d3e5fda48a63c789028a747d0aee951ac3260f75fbc1464ac4463b | 5d1f19c42493cc7d8125670229ac13add15c4e0781ed1adb39259869c071ac27 |
| NCT03291613 | retrospective executed package | 2 / 2 | 756f6dc29c0e4f4d146d9b9f79fd83eaa9f1f397e39980b7e5c0870abc64bf69 | d0feedc4f07efc7879c1b4951b0d2ae0366c1b5ba562a9f9abaa6b49b009be36 |

## Review gate

Only NCT05142280 enters the registered benchmark, as a draft requiring independent expert review. The other seven slots must be replenished so the release intake remains 99 version-verified public drafts plus 21 actionable metadata candidates.
