# Expert Review Packet: Batch 148

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 148 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 1,231 physical pages in the 16 selected PDFs. OCR was added for 152 pages, including the entire 81-page NCT03317002 SAP, and 176 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. The separate 20-page NCT01652469 statistical plan was also downloaded and reviewed because the candidate harvester had selected the same-date mock-table attachment instead. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03317002 — exclude: final SAP v7.0 follows study completion, incorporates changes after interim analyses and adds COVID, PK and actual-treatment handling; the protocol also exposes the principal analysis and interim program.
- NCT03989232 — exclude: the internally dated SAP is pre-primary-completion and explicitly matches Protocol v4.0, but that protocol already gives the estimands, analysis sets, MI/ANCOVA models, 500 imputations, tipping-point analyses, multiplicity and sample-size program.
- NCT05073315 — exclude: SAP v2.0 follows study completion and changes primary PK analysis-set eligibility while adding COVID analyses; the model-visible protocol independently gives the core interchangeability analysis, populations, missing-data rules and success margins.
- NCT03077438 — exclude: both Protocol v3.0 and SAP v2.0 are post-completion amendments, and the protocol already specifies the four-serogroup noninferiority hypotheses, Wilson intervals, analysis sets, missing-data handling, delayed rSBA analysis and safety program.
- NCT03613662 — exclude: SAP v1.0 is pre-completion and exactly matches Protocol v1.0, but the protocol already discloses the PD populations, AUEC/Emax derivations, PROC MIXED model, 90% confidence intervals, 80%-125% criterion, sample-size rationale and no-interim rule.
- NCT02637856 — exclude: SAP v2.0 was finalized after two interim analyses used for conference/publication purposes and only three days before completion; it adds primary-endpoint sensitivity rules and an optional substudy, while Protocol v5 also exposes the principal populations, endpoint analysis, missing-data rules, sample size and interim program.
- NCT01652469 — exclude: the selected SAP_006 attachment is only mock tables, while the same-date SAP_007 is the actual 20-page statistical plan. Review of that plan does not rescue the candidate because Protocol v1.0 already specifies the Cox treatment-by-VeriStrat interaction, KM/log-rank analyses, efficacy population, power assumptions, adaptive sample-size review and safety summaries.
- NCT03442751 — exclude: SAP v2.0 follows study completion and adds COVID-affected populations, listings and sensitivity analysis; the protocol already exposes the ITT/safety/PP populations, primary and secondary hypotheses, sample size and safety program.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03317002 | post-completion interim/COVID-informed target plus leakage | 88 / 81 | `1c570aba2f028cc88b714f4b226a5eb4da6aba9950084fe2eef33b60c8177aba` | `632ad08d926f76cdc0cac607bf5923dd21caf52bae64ec2a633e0dcd32c2ea21` |
| NCT03989232 | protocol-embedded target leakage | 128 / 262 | `1363d353ffe7612936bfe639b06f00a88fbf9b8115c30887e7b3c8f5808cfa93` | `582f7c82b4bee90b32b1bb136193bc075a9be3170e9168b958746d1d262cb0cf` |
| NCT05073315 | post-completion changed target plus leakage | 87 / 36 | `df8888a2be5ec984cefe3c6d4757aa3f6ae54214f0196b18f9c2e952ed4e1023` | `43f26083a0af312a525bfb0ec92b0c6f068b33411399ed61b71215bdde57bb39` |
| NCT03077438 | post-completion amendment pair plus leakage | 81 / 42 | `428091417719c8cfcfb2a989223a9d0a24da2c44ef42c69e19ee77100f172067` | `9892641ac1601d0e21df0251b122db21903c15ba53f5a203c5ed9d007b9cb3ec` |
| NCT03613662 | protocol-embedded target leakage | 85 / 30 | `e5858ce8e95c8160a4e53c34f891b5c788e36ee226120501853f596a26a50b23` | `7d2d1b7b046b17f72074c4e82fc78e073821b7543b4543ba58b2ab052d525175` |
| NCT02637856 | performed-interim/publication-informed target plus leakage | 95 / 53 | `53f625fb08f388656539fd5c5467276b4e5d8ccbfb6793f776ca3eb2efd74639` | `5ba415be0078b5bd9bccbceec2ed8940ba1f8011ccad2259ac3fd7533aea3211` |
| NCT01652469 | selected mock-table attachment and protocol leakage | 38 / 20 | `9f89ef82063f7a54c21ce1342821d5c47b59553b63231dcc3e36ef5f53cce6dd` | `a39c91aa399ae4d7749bf0af1c9877f09b6cbc165b41a57368369191c7c9a8b1` |
| NCT03442751 | post-completion COVID-informed target plus leakage | 69 / 36 | `0c3f8bab2d7947c2ab75eb39edb9b7d871033d3d20734035e8989e5beb829b26` | `cc5cb376a777cf28534cae2fa00c0d394e34b3a222f3285d911a61e0c9653242` |

For NCT01652469, the independently reviewed same-date SAP_007 has 20 pages and SHA-256 `a4660b0da52abc15b7fb5646b8cb989103bfc0f4e556985d12e10ec6330d0ba2`. It confirms that the target's executable core is already present in the protocol; the selected SAP_006 hash above is retained to preserve the exact queue decision chain.

## Gate interpretation

- A SAP dated before primary completion can still fail when already-performed interim analyses, publication use or observed conduct informed the selected final version.
- A post-completion SAP does not become prospective merely by saying it was finalized before database lock; the public chronology and revision history must support that claim.
- Protocol leakage here is not based on endpoints or a sample-size target alone. It requires executable populations, models/tests, covariates, missing-data or sensitivity rules, multiplicity/success criteria, interim procedures or endpoint-specific safety analyses sufficient to reconstruct the target.
- Selecting a mock-table attachment instead of the same-date narrative SAP is a document-selection defect. The candidate can only be rescued by reviewing the actual plan, and NCT01652469 still fails the independent protocol-leakage gate after that review.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight non-promotable slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
