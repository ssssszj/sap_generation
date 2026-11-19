# Expert Review Packet: Batch 137

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 137 review-queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 2,423 physical pages. Every page was text-extracted; all 40 NCT03014180 SAP pages and the 124-page protocol plus 33-page SAP for NCT04313400 were OCRed. A total of 97 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. One pair survived first-pass promotion, and seven were excluded. This remains first-pass work requiring independent expert review.

## Decisions

- NCT03606928 — promote as `PUBLIC-MFLOT-GC-001`: the independent three-page protocol and one-page statistical-analysis document print the exact title, NCT and 2018-05-02 date before actual start; the protocol defines the classical 3+3 design, DLT, MTD/RD, treatment, RECIST and survival outcomes without exposing the reference-only Kaplan-Meier and SPSS choices. The unsigned/unversioned governing chain, post-start registry submission, eligibility conflict and absent Table 1 remain explicit second-review gates.
- NCT02322021 — exclude: the post-completion SAP repeatedly says analyses were cancelled or reduced because the study terminated, and the termination followed unblinded data from other Phase 3 studies.
- NCT02766088 — exclude: the post-completion SAP incorporates termination, realized site/enrollment/case counts and analysis deletions or changes; the protocol also exposes the executable target.
- NCT02880475 — exclude: the SAP follows primary and study completion, while the protocol already discloses populations, pharmacokinetic mixed models and safety reporting.
- NCT03014180 — exclude: the final SAP addendum follows study completion and database lock, while the protocol exposes the exact-binomial, analysis-set, missingness, interval, Bayesian and safety program.
- NCT03495102 — exclude: the SAP was approved after primary completion and its revision history records analysis changes and a results-summary appendix; the protocol also exposes estimands, models, imputation and multiplicity.
- NCT05385952 — exclude: the SAP cites Protocol Version 7 but the selected input is Version 8, whose pages 62-66 already disclose an almost complete noninferiority and group-sequential program.
- NCT04313400 — exclude: the Part 2 protocol pages 99-106 expose endpoint definitions, sample-size rationale, populations, missingness, Type-I-error decision and analysis rules needed to reconstruct the short SAP.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03606928 | promote with prospective-governance and version gates | 3 / 1 | `fc3646a55b8ac3a482c321e32d09939b3f8103dab71438e5b4bacbf4b1f0c8b7` | `5f2f727b8db0e61891cfb90a44ed8dfea53f041397528805382db8fefdc2b074` |
| NCT02322021 | termination/external-outcome-informed target | 1658 / 26 | `d331b9c2694a76e57df894a60202d30df47f1a4abce3048389f36a3347cfdf9d` | `c5bebef197e84970229596d35210b74b2a2bbf069166e02de3777311270cfdf6` |
| NCT02766088 | post-completion/termination-informed target plus leakage | 118 / 22 | `9abd87b6a13cb2838998d25a19e9a7f0f8d8372dd9253f69ad86ae01255bbf97` | `569b83898245d66b516cee13176514db61a4c3c2bd6f73b6620d63e3ca696650` |
| NCT02880475 | post-completion target plus leakage | 51 / 33 | `4ceaa795b1d7fa8f11c6e72d608124981943dfb720452c65402108754a1a1fcf` | `e8aa3f930f2281b785c2891a4c7e5327b5afe3b7bcf369439f2b60cb92a2a9ff` |
| NCT03014180 | post-completion/post-lock target plus leakage | 39 / 40 | `c9c3fe19a63b5efee31dab33f71cd9899eda05928d6c9bbb231f97118432607f` | `0ae7efe3424db9594e736b7ba49ca8d7f80972ee00b7b979e4bcde4188c0ee4d` |
| NCT03495102 | post-primary, revision-informed target plus leakage | 90 / 39 | `79c39d693af92e66d448ea49cd19b25a2b313bf250e56b2ba792fc9dfb6c3e01` | `e6e0458b0761e3276e8be8c88dcb277a8a7ca3972349f6bf8b25509168464b29` |
| NCT05385952 | governing-version mismatch plus protocol leakage | 94 / 52 | `81c89fc241762e630e9a141d241b703152ae7ff0ed52e4edd7843c3cb4ee0526` | `f03dfecc1f838ea6d1288162c8cd47881d6612468f4d0a564c80ad10cbb65f03` |
| NCT04313400 | protocol-embedded Part 2 target leakage | 124 / 33 | `d1da04406c47d11493b326c40485262ccb2bb9f167aa33e59cab90667b3f0f4a` | `ac00620895d7d59cfeb5f86dee2241be5e31ea10f2cea7559aad590d9425bfeb` |

## Gate interpretation

- A pre-start internal date supports NCT03606928 but does not by itself prove prospective governance where both PDFs are unsigned and unversioned and the registry was first submitted after start. The pair is a draft with explicit second-review gates, not expert-approved or frozen.
- Protocol disclosure of design, endpoints and sample size alone is permitted. NCT04313400 and NCT05385952 fail because their protocols additionally disclose the populations, inferential models, missingness or multiplicity machinery needed to reconstruct the target.
- Post-completion plans and changes made in response to termination, actual accrual, database lock or a results summary are execution-informed even when uploaded as an SAP.
- NCT03606928 requirements use only the frozen protocol eligibility and explicitly surface its conflict with later registry metadata; neither the missing dose table nor a total sample-size target was guessed.
- Registry actual enrollment was used only as conduct context and was not substituted for prospective sample size.

## Replenishment

The seven exclusions are replenished from the official API, while the promoted family consumes one candidate slot. The release-eligible intake remains 120: 105 public first-pass drafts and 15 actionable metadata candidates.
