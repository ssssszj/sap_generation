# Expert Review Packet - Batch 105

## Scope and decision boundary

Batch 105 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were downloaded sequentially, byte sizes checked against registry metadata, SHA-256 frozen and extracted page by page. Protocol and SAP covers and the decisive chronology, version, execution-stage, statistical-leakage, amendment and interim-governance pages were rendered from the original PDFs and visually inspected. One family is promoted to a first-pass draft and seven are excluded. Promotion is not expert approval or split freezing; every reference SAP remains annotation-only and must never be model-visible.

## Promotion

### PUBLIC-REWARD-RETRAINING-BINGE-001 / NCT04661410

- Exact identity: both covers print the same title, NCT04661410 and 2021-05-19 date.
- Chronology: the pair was fixed during 2020-12-01 to 2021-09-15 conduct, before primary/final completion.
- Independence and leakage: the ten-page protocol describes the prospective RRT-versus-supportive-therapy pilot and explicitly delegates full statistical analyses and power to the separate supplement. It does not expose the reference-only multilevel models, covariance structure, mediation bootstrap, missing-data procedures or power calculations.
- Annotation: 22 atomic requirements cover design, assessment timing, clinical and target endpoints, feasibility thresholds, longitudinal models, mediation, missingness, power and explicit open decisions.
- Expert gates: allocation and analysis-set rules, group clustering, percent-change denominators, binary-outcome model mapping, multiplicity and the n=60 versus n=154 limitation.

## Exclusions

- NCT04723355 — both documents follow 2021-11-16 completion, and 2022 history records changes to primary and secondary analyses.
- NCT03813238 — protocol pages 104-111 disclose the executable populations, MMRM, MAR/MNAR imputation, sensitivity analyses, multiplicity, interim and safety plan; the target SAP is substantially leaked despite its sound independent-iDMC safeguards.
- NCT05501392 — purported protocol says the study stopped early and only observed periods will be presented; the analysis note uses observed skew and overdispersion to choose models.
- NCT02914522 — SAP dated 2020-04-28 follows actual 2020-03-31 primary/final completion, without a proven pre-outcome freeze.
- NCT03559699 — protocol pages 73-80 already expose power, FAS/PPS, endpoint derivations, exact-binomial inference, nonresponder rules and detailed safety analyses.
- NCT02394561 — SAP dated 2017-09-20 follows actual 2017-06-08 primary/final completion, without a proven pre-outcome freeze.
- NCT02430818 — protocol and SAP slots are the same 11-page, 7,316,117-byte PDF with identical SHA-256.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT04723355 | post-completion conduct-informed | 22 / 13 | 0dfb12702447f09e94d340ccfbe9043bd52885d1a969e6544e123492a8da156b | 82bbb9d65825b54edcb977ad1e88f68a0a6c432205a2addcd6c8ba6bf0f3b635 |
| NCT03813238 | protocol leakage | 256 / 75 | 62bab474aaf70767d81e551d7c834f633e73de9d279c79335776f447fe84c259 | 897880803971d3e0256d57ac11a7137de8fed3b87df77b29dc1821f52103d96f |
| NCT05501392 | retrospective executed methods | 3 / 2 | 2c79d15dc10f0c2206b1f7867a4f8979c97d2f92f8a4a9d6e73181d0662e6344 | a986ee70e04f9c0cae307066bea127d5cd5226c458453d4b8b35de18e01dbda6 |
| NCT02914522 | post-completion SAP | 122 / 96 | 4aef88d3866c1e789b3ae2394973678bf3ab6c3514dce370176b0ec20fee2d0a | 370f8eab500b3014331a288f3a9a33ad9150f7f578ba9cb58e16fe23a42fde8d |
| NCT03559699 | protocol leakage | 85 / 38 | 1aa08930cfbe30bfbc3d4ffe25d6c588fad5963e7857e242ecd0de0a0b0e783d | b1d7c046c71c11a37364db087f1e79096365731358618d38de2ed8282c9bc92d |
| NCT02394561 | post-completion SAP | 70 / 55 | b4ae6e1010f57b93bc944857bdefca3ac2b740b360ccc9395823a8a298b9dd51 | 0ea615f6b48102bdffebfe57a09006693f5b2b89dc984eaff2396a33b633f10c |
| NCT04661410 | promoted first-pass draft | 10 / 3 | 98342c60c706274dfcd2818896266fbfdc1b30d19779a26c0b16676ae9be0eab | 3b4eb67789653df842d273f57e5867fd90de7aaea4f418d5f51586d2cff936c9 |
| NCT02430818 | identical protocol/SAP leakage | 11 / 11 | 35022e8dadff6b0b099148167bdd4878560e2a996c3c27610e939925748b8640 | 35022e8dadff6b0b099148167bdd4878560e2a996c3c27610e939925748b8640 |

## Review gate

Only NCT04661410 enters the registered benchmark, and only as `draft_needs_expert_review`. The seven exclusions remain outside all splits. Their rejected slots must be replenished so registered public drafts plus actionable metadata candidates remain exactly 120.
