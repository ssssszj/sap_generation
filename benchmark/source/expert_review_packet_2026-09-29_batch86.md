# Expert Review Packet - Batch 86

## Scope and decision boundary

Batch 86 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally, every physical PDF page was text-extracted, and the identity, chronology and decisive statistical pages were rendered for visual inspection. One family is promoted to a first-pass draft and seven are excluded. Promotion is not expert approval or a frozen release. The reference SAP remains annotation-only and must never be included in model-visible input.

## Promotion

### `PUBLIC-PNS-PT-HSP-001` / NCT02893267

- The 79-page IRB protocol export and independent two-page Expectations and Analysis attachment share the exact Multimodal Treatment for Hemiplegic Shoulder Pain title, NCT02893267 and 2021-11-05 cover date. The public registry records a 2017-01 start and actual primary/study completion on 2024-09-30.
- The reference uses anticipated and future-tense language and contains no results. Because its date falls during enrollment rather than before first participant, release requires source-history confirmation that the pair is unmodified and outcome uninformed; this remains an explicit provenance gate in requirement R021 and `annotation_status.json`.
- Protocol physical PDF pages 13-20 define the three groups, adaptive randomization factors, BPI-SF3, response threshold, repeated visits and study procedures. Full-text comparison found no protocol copy of the reference's 2.0-point/SD 2.4 power calculation, one-sided pairwise test, linear mixed-effects model, site-poolability checks or logistic responder regression.
- The 22 requirements cover design, adaptive allocation, masking, prospective sample size, analysis population, primary timepoint, BPI and responder derivations, Aims 1 and 2 contrasts, mixed modeling, site handling, estimand, multiplicity, missingness, logistic response analysis, secondary and mechanistic outcomes, power, safety, provenance and reference isolation.
- Open decisions include role-specific masking, confirmatory BPI-SF3 timepoint, analysis populations, covariance and site rules, intercurrent events, missingness sensitivity, the meaning of combined one-sided alpha and the during-enrollment provenance.

The annotation remains `draft_needs_expert_review`.

## Exclusions

- `NCT02871778` — protocol leakage. Protocol Version 6.0 pages 9 and 63-66 already specify the hypotheses, crossover power assumptions and executable mixed model including compound symmetry and Kenward-Roger degrees of freedom.
- `NCT02773368` — wrong document type. The analysis upload says no separate SAP was prepared and embeds a Final Clinical Trial Report dated after study completion.
- `NCT02365649` — non-independent, post-completion extension plan. The selected SAP explicitly covers the extension phase and is dated after both primary and study completion.
- `NCT02140554` — post-completion SAP. The 2024-03-04 analysis plan follows 2023-07-31 primary completion and 2024-01-30 study completion.
- `NCT03386032` — execution-informed revision. The protocol says enrollment had already run for about four months and changes eligibility and planned randomization after observing excess early withdrawals and recruitment data.
- `NCT04955717` — protocol leakage. Protocol Version 7 already supplies clinic-level ITT, adjusted analyses, cytokine and economic models, sample-size assumptions and the one-sided Fisher exact test.
- `NCT04763876` — protocol leakage and post-completion execution. The protocol contains the noninferiority margin, test, sample size and adverse-effect analysis; the SAP postdates completion and explicitly says a subgroup decision was made during analysis.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02893267 | promoted with provenance gate | 79 / 2 | 18da32121c25b1d73e12df6be333cac52cd83b0e2924f29a5e41720e49227b18 | 65b0b91a9d7f5a027dd7dd0631dcd4f50db12e4f6c88350503907756eb8da6d6 |
| NCT02871778 | protocol leakage | 88 / 76 | 6aef90b0c029b01c1204861ada6044ced86f3fdcf05797efc4f07699df91424e | 303e81ced22cc18556b7c85231a997b2d0298a973618879e015d55c4f67d58c3 |
| NCT02773368 | CSR / no independent SAP | 156 / 566 | 9aa0f8b017f66a9cc182fc733893589a2552db39f5377f4e286b4ec8f9661f9d | 8fc4fbe2d3b092a2ae4623ddeb19dcb14f70eeb0721b37fe08d94dfce23a270d |
| NCT02365649 | extension / post-completion | 156 / 98 | 7448d25b48ed85a79e5a62380438340db4dd05560637b7530a8514d44e1728e2 | b491b7833287e2ba6b0a113fea9d6166eb03b68673fdea092b76480af6f228f7 |
| NCT02140554 | post-completion SAP | 158 / 66 | dda2c1f916f9279a6f1bb243f3ae98023690644879184e808c07ddaf501a1164 | ed207fbfddda5e9bc4dc5a7a8785c548a0b9544cc56cbf38cef0db387ab3a961 |
| NCT03386032 | execution-informed revision | 14 / 4 | 615e4421f75782366da375db94c3333a775c2309063259df777e644ac65a7d7f | ba845f9c2d002a7da0ef0f43e30bf2d772c32f491356ddc4f2d9d1c4387b1097 |
| NCT04955717 | protocol leakage | 25 / 4 | bdf4a1e8e81dcce065dd1a7a03db649443428a2b92f942f8c44d9dc990ba15f2 | f2d7968cdc3e3fb7cd3a87a7590a45d126686ca6333928a7f591bb68e9bee00c |
| NCT04763876 | leakage / post-completion | 38 / 2 | cb5dee9292c03b443a05eeec1fb62927179e9e23b9905313aae8650c48ad4aa6 | b10e0ed55e6f5ae71e25227cb97969ceee089418ebba2486dddfa5892df9e235 |

## Review gate

Only NCT02893267 enters the registered benchmark as a draft. The seven exclusions remain outside the actionable pool. After candidate refresh, rejected slots must be replenished so the working collection remains exactly 120 public families across registered drafts and metadata candidates.
