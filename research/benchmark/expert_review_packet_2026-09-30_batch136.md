# Expert Review Packet: Batch 136

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 136 review-queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,070 physical pages. Every page was text-extracted; the 53-page NCT02737722 SAP was fully OCRed. A total of 90 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. Seven pairs were excluded, one was placed on version-reconciliation hold and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT02981953 — exclude: although the document dates precede primary completion, the model-visible protocol supplies the sample-size precision rationale, exact confidence interval, analysis scope and adverse-event reporting program needed to reconstruct the short SAP.
- NCT03341312 — exclude: Final SAP Version 3 is post-completion, while the protocol independently exposes the populations, mixed models, effects, confidence intervals and no-interim plan.
- NCT03279081 — exclude: SAP Version 6 is post-primary and its revision history records end-of-study, regulatory-communication, multiplicity and safety changes; the protocol also exposes the executable program.
- NCT03930186 — exclude: the protocol substantially reconstructs the SAP through populations, sample-size calculation, primary and sensitivity analyses, missing-data rules, covariates and safety analyses.
- NCT02737722 — exclude: the month-only primary-completion date cannot establish that the 2017-08-31 SAP preceded primary completion, and the protocol already exposes the populations, tests, multiplicity, missingness, sample-size and interim-safety program.
- NCT02873936 — exclude: the Final Analysis SAP is post-primary and post-completion, while the protocol exposes the analysis sets, CMH/NRI primary analysis, hierarchy, MMRM, sample size and DMC framework.
- NCT02245737 — exclude: SAP Version 7 explicitly records that futility criteria were met and streamlines the plan after the trial stopped; the protocol independently exposes the target models, sets, multiplicity, adaptive design and missing-data method.
- NCT03304587 — hold: two unversioned same-date files were produced late during the trial and contain no revision, signature or approval chain that establishes outcome-uninformed prospective governance.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02981953 | protocol-embedded target leakage | 57 / 15 | `6da7f6df3e631bd0ab8e8c7e0b7dd859e9d74c14b69cb8213622d3a72e2fa9a3` | `66e3fda25adc2737330ce2881c7683105c9f58701f0d6c07dd1706472d8c00f9` |
| NCT03341312 | post-completion target plus protocol leakage | 70 / 17 | `218d7a323ed533db7c6303a7c79d24ede0da2feef2f75af07b53991a04d739e1` | `f12518dc451fecb3856c02646156654e4f863cdcfc75e760569934070d3b40bd` |
| NCT03279081 | post-primary and regulatory/conduct-informed target plus leakage | 139 / 48 | `4b02dc9d31d7162aa1a1d86364fd7d3d2df557ac7fa3b21d71d6706aa68a55fa` | `013ee92fc42a87f9be7cbd4cefb876313e3284278513101b83501ae6449fd0ba` |
| NCT03930186 | protocol-embedded target leakage | 89 / 39 | `621ded0ad36d384386fa8133205e2ffec652a7f3dc99778eb571db8ff55fc120` | `f26586f43864ee30fb4ac8fe45d27718be9a6092cc3b898c281bbfb5781d360a` |
| NCT02737722 | unresolved primary-completion order plus protocol leakage | 163 / 53 | `f6973190887fc5f27783ab5a2f34849590b36c2847f6a9c65ee10c0fd780d682` | `cd9295dcf65574f931da72ad16a65b3c3972fa673a67d0d439c52b60733c5ab6` |
| NCT02873936 | post-primary/post-completion target plus protocol leakage | 108 / 77 | `a8b37508953630617db1313ae9485b7af21738a72348fc1c60200678309873d4` | `58785f99c160af09fc731b77307d98590f64e42fbec6f28bdeb4451c663d1fff` |
| NCT02245737 | futility-stop-informed target plus protocol leakage | 132 / 56 | `ae86a03a5297c42af1d95c422af700658826870e662cb8fb38a5eff51f086f47` | `cdd571e216f98f620a35d992ced7fa550aa6452453ba7033e5f5007011e708b0` |
| NCT03304587 | prospective/version governance unresolved | 5 / 2 | `b6055802ca4d4a3de3dd79cfb39219e63183f24c27e06acb9d62f52657b3b48e` | `5e7aadbf5093d4a2ee1c7edbcdef53b4e751265d91aeca23fd6abd27d016e1a5` |

## Gate interpretation

- A final SAP created after primary completion, study completion or a futility stop is not a defensible prospective target. NCT03341312, NCT03279081, NCT02873936 and NCT02245737 fail this chronology/conduct gate.
- Exact calendar ordering must be supported rather than inferred. NCT02737722 has only a month-level primary-completion value, so the SAP cannot be presumed to precede it.
- Protocol disclosure of design, endpoints or sample size alone is permitted. Here, however, NCT02981953 and NCT03930186 disclose the population, model/test, missingness, uncertainty or reporting details that substantially reconstruct their target SAPs; the other excluded records have independent protocol leakage as an additional defect.
- Unversioned files produced during an ongoing trial are not automatically retrospective, but NCT03304587 lacks the revision/signature evidence needed to establish prospective, outcome-uninformed governance. It is held rather than guessed or mislabeled as definitively retrospective.
- Registry actual enrollment and dates were used only for chronology checks and were not substituted for prospective sample-size targets.

## Replenishment

All eight excluded or held slots are to be replenished from the official API. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates.
