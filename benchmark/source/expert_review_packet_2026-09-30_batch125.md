# Expert Review Packet: Batch 125

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 125 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,251 physical pages. Every page was text-extracted, and 72 decisive physical pages were rendered and visually inspected. NCT05421624 survived promotion; seven pairs were excluded. This remains first-pass work requiring independent expert review.

## Decisions

- NCT05421624 — promote as `PUBLIC-AMPED-PD-001`: the 14-page protocol and independent two-page SAP print the exact title, NCT and 2022-07-12 date, before actual study start on 2022-08-01. The protocol defines the prospective 44-participant RCT, interventions and outcomes without disclosing the reference-only Shapiro-Wilk/Levene gating, between-group ANOVA/Kruskal-Wallis, within-group repeated testing and secondary procedure. Added 25 evidence-backed requirements.
- NCT02695420 — exclude: protocol physical pages 52-58 disclose analysis sets, precision-based sample size, DMC review, PK derivations, secondary repeated analysis and missingness decisions.
- NCT03010319 — exclude: its 2021 SAP follows completion in 2020 and records realized participants and interim sample-size re-estimation; protocol physical pages 52-56 also disclose the group-sequential program, populations, models and LOCF.
- NCT04673357 — exclude: the SAP amendment history records during-conduct data-governance, interim/database-lock, new-analysis, estimand/ICE and regulatory changes; Protocol Amendment 7 also exposes extensive programs.
- NCT03103542 — exclude: the 2020-10-22 SAP follows 2019 primary completion and 2020 study completion and records during-conduct alpha/interim changes.
- NCT03482011 — exclude: SAP Version 3 follows primary completion by one week, while protocol physical pages 70-77 disclose sample size, MMRM/ANCOVA, missingness, multiplicity and interim/final logic.
- NCT02167945 — exclude: TOPAZ-II's primary analysis is pooled with companion TOPAZ-I, and protocol physical pages 7-8 disclose the pooled Cox, Wilson-interval, ANCOVA and safety program.
- NCT02151682 — exclude: the SAP follows primary completion and its history records execution-informed deletion/addition of adaptive and Part 2 interim analyses; the protocol also exposes the fixed program.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02695420 | excluded | 73 / 29 | `ff396cfe1d54c737213a5c699f6d91bdb540ad064443bfcba99a68a3dab3431f` | `4a52b9b4d632386428cd952657169c89bc6ac93d7ce6e1383ab18372240ff9dd` |
| NCT03010319 | excluded | 64 / 30 | `a1c1fa2becda85dbc5fcbb7248273fe6cf327289ca402c0071e770f0d4c23103` | `cd55ddafe404655cc57002b3451cce0560ab22ec22abf9d44e3f1cf193e66dc8` |
| NCT04673357 | excluded | 255 / 112 | `6d6502099cc8f45a021d6c1249e86d35f9908b06eb74a460f590331359eb30b3` | `c1befad80a6c5f63dc10d29f7dbfc7bba0984c58972471ae6d1fa11cbec2ea68` |
| NCT03103542 | excluded | 73 / 65 | `9c4f87dd40bba4c33890b2a2f00f8b5de52d685e568d893b5e61796242e2b7be` | `d3b67c2d57bda7de52347f3c2a331061e9075dfaf1e97ee7f1c3b2a5d9a280e1` |
| NCT03482011 | excluded | 120 / 75 | `19e6c7085d0aa424cf49aa0fa9330fc84032707ae53bbc61b47f71addbdb3494` | `3e5bd77f7f33de524941f87e5583bf544a1858228997aef222505fbc6b48b7c1` |
| NCT02167945 | excluded | 117 / 53 | `93e86496c3e5be8c71db19b334a88f35f986a39ed16613cdc4f54b5036bc1a31` | `bdfab879f94833d1b709f9a36c5c35ccde61b3e3fc002963b13f2a92f78b89e3` |
| NCT02151682 | excluded | 137 / 109 | `fd7541ecce5a01e856da687cf76853d67d7022b0c0209438d6fbf041fedd47cb` | `229db14a151b1755f5fcbe7bc9f94743d73be7d68540b4e689f74bdbafe19624` |
| NCT05421624 | promoted | 14 / 2 | `1684b16fb1b227f4b43c67a048a039e35c887d7738a959769c2cbf39512583c1` | `c8efa745eada365d966845f0709e94452612ccb82d6fe455ac77c0415982bf16` |

## Promotion gates and unresolved work

- The protocol's prospective target is 44; later actual enrollment is not its source even though it has the same value.
- Balanced block randomization is explicit, but allocation ratio, sequence generation, block sizes, concealment and role details remain confirmation gates.
- The four outcomes called primary and their two follow-ups lack a confirmed hierarchy and study-wide multiplicity rule. The SAP's Bonferroni statement applies only to within-group post-hoc comparisons.
- The direct randomized contrast is the between-group change-score test. Within-group repeated-measures ANOVA/Friedman analyses are supportive and cannot replace it.
- Populations, estimands, valid-wear/trial derivations, missing data, intercurrent events, effects, intervals, small-sample inference, software and safety remain unresolved.

## Replenishment

The seven excluded slots were replenished from the official API after the promotion and exclusions were registered. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates. The next queue starts with NCT02703454, NCT03014479, NCT05014672, NCT03855280, NCT03533751, NCT02422524, NCT02376790 and NCT05992467.
