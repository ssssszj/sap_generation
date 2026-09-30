# Expert Review Packet: Batch 158

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 158 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 995 physical pages in the 16 selected PDFs. Full-page OCR was also performed on 423 pages across the scan-heavy NCT03650556 protocol/SAP, NCT04447040 protocol/SAP and privacy-overlay-obscured NCT02025985 SAP. A total of 113 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03650556 — exclude: Protocol Version D physical pages 44-49 already expose the primary safety/effectiveness hypotheses and thresholds, secondary hypotheses, populations, sample-size basis, analysis timing, subgroups, multiplicity, missing-data procedures, lack of interim analysis and success criteria. SAP dated 2020-05-27 substantially repeats that program and adds COVID-19 sensitivity analyses during ongoing conduct. The target is both reconstructable from the protocol and conduct-informed.
- NCT04797104 — exclude: Protocol Version 1.0 physical pages 60-62 exposes the ITT/mITT/PP/safety populations, coprimary LDL-C endpoints, ANCOVA, multiple imputation, sequential/Hochberg/fallback multiplicity, MMRM/rank-ANCOVA sensitivity analyses, subgroup model, no-interim rule, and sample-size assumptions. SAP Version 2.0 physical pages 3 and 30 additionally incorporates actual conduct, including the Sponsor's decision to end enrollment at 478 rather than the planned 600, all-six-dose PP eligibility, actual-treatment handling, baseline concomitant therapy and IRT rather than EDC stratification. The target is substantially reconstructable and execution-informed despite being labeled pre-lock/pre-unblinding.
- NCT05789576 — exclude: SAP Version 1.0 is dated/signed 2023-07-24, after actual primary completion on 2023-06-30 and actual study completion on 2023-07-19. It calls itself the final-analysis plan and has a conflicting 2023-07-12 date on the signature-page text. The selected artifact is post-completion and cannot serve as an outcome-uninformed prospective target.
- NCT03315104 — exclude: SAP Version 1.0 is dated 2019-11-07, after actual primary/study completion on 2019-06-17. It replaces the prospective target of 75 with the realized 65 randomized/60 dosed, writes the study in retrospective tense, describes post-lock reconciliation/unblinding, and incorporates actual protocol-deviation and treatment-exposure states. The selected plan is post-completion and result/execution-informed.
- NCT04447040 — exclude: SAP Version 2.0 is dated 2021-05-17, after actual primary completion on 2021-04-09 and actual study completion on 2021-05-03. Physical pages 16-17 explicitly change the rescue-analgesic analysis because blinded data showed a high overall rescue proportion and small strata. Protocol Amendment 2 physical pages 51-57 also exposes the analysis sets, sample size, primary model, testing rules, imputation, subgroups and safety analyses. The target is post-completion, blinded-data-informed and substantially reconstructable.
- NCT03467477 — exclude: SAP Final Version 1.0 is dated 2019-02-11, after actual primary/study completion on 2018-11-15, and the public signature page contains no approval dates. The SAP says it was prepared after conduct and uses completed-study framing even while stating that no conduct changes were identified. The selected target is retrospective/post-completion.
- NCT02025985 — exclude: SAP Version 3.0 is dated 2017-07-24, after actual primary completion on 2017-01-24 and actual study completion on 2017-03-29. The governing Protocol Version 3.2 and SAP state that Part 2 schedules were added based on observed tolerability and efficacy in the ongoing ovarian cohort, while the plan includes Simon first-stage efficacy analyses and a long accumulated revision history. The target is post-completion and outcome/conduct-informed.
- NCT03780972 — exclude: SAP Final Version 2.0 is dated 2022-09-14, after actual primary completion on 2021-08-24 and actual study completion on 2022-08-24. Physical page 6 assigns different protocol schedules to named realized patient IDs and explains that Version 1.6 was introduced only for a site lacking B-scan equipment. Its final analysis is explicitly after completion and database lock. The target is post-completion and realized-conduct-informed.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03650556 | protocol leakage plus during-conduct COVID target | 70 / 34 | `e7ad2e160c18a4d728794f37348b38903c4c768143f816257499aa80467bd427` | `353ae371fe5d0ec5a6d7d43a127d528a9668a3dfca483ee2e831a895e314a087` |
| NCT04797104 | protocol leakage plus realized-enrollment/conduct target | 78 / 36 | `8930c1d4276f0ee88f2a76232fe37a448d78e5b840e6430a44417a43db6e733d` | `97a357825ca049c3463156917dc422ed181b5267a320d8f926e58a45903cf61d` |
| NCT05789576 | post-completion final-analysis target | 55 / 21 | `8bfb744368b85ea389555305690123b358218701cbecc6b35cb36726bb935e26` | `1a9204141db221badebb94dcd75f89103b25f1acc1efe49458fc24e6aebee5f9` |
| NCT03315104 | post-completion realized-enrollment/unblinding target | 64 / 36 | `d1fc6bc7e198302e78c4777de4fc33f9b0c2bbf6ff4170b64ff072952356936c` | `8dd59eea8313bd923afb47587788e6d9354853406e1ea834a85f138181a951e7` |
| NCT04447040 | post-completion blinded-data-informed plus leakage | 66 / 23 | `bfcd97e779816f84e84882aaaa4b9382b161e667771e5840968d479eb4285c4a` | `b121190e36f9c5ce7e69746d64ca5e5463763632882c70a5f126b1a42ebd96e3` |
| NCT03467477 | post-completion retrospective target | 40 / 21 | `f3410bfc5e750a8818a81cc727ab34d3e5f5e758ef57dbf94fe0d1c4340127c3` | `89e6d31a5d6f2693f7bdc3184c2844af83eac8830ed74a333729eb8340e6ca06` |
| NCT02025985 | post-completion observed-efficacy/conduct target | 130 / 230 | `0ce1145f124f26cb04b75189991c5ed272f46ba1b1e2892f94d93a2ad8c2c8b7` | `c56fb017a13a804718c6acd6956e519e3ca3a4e09208c73d294cb9667d121b93` |
| NCT03780972 | post-completion realized-patient/site target | 52 / 39 | `dc95515dbfaf8af022f13888b8b5b9e77841b5f012a26d16ce928d3667803549` | `32bf806482df1fbd9801b4e78aa6e218f3810867428dfcc9267779dbeb759958` |

## Gate interpretation

- A target marked "before database lock and unblinding" is still execution-informed when it uses realized enrollment, actual dosing eligibility, operational data sources or blinded aggregate distributions to change the plan.
- Blinded aggregate data can invalidate prospectivity when it changes stratification, rescue handling, analysis populations or other inferential choices.
- A plan finalized after actual completion is retrospective even if it says there were no changes in conduct or analysis.
- Protocol leakage is assessed by substantive reconstructability across populations, endpoint hypotheses, models, missingness, multiplicity, thresholds and sample-size logic, not by verbatim duplication.
- A final SAP that assigns schedules by realized patient IDs or documents a site-specific equipment problem is execution-informed.
- An adaptive oncology package whose later parts were selected from observed tolerability or efficacy is outcome-informed even if the adaptation appears in the protocol.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
