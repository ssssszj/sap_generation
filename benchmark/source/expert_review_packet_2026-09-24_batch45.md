# Expert Review Packet — Batch 45

## Scope

Batch 45 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the independent-target gate because all eight public protocols disclose executable target analyses. All 16 PDFs and eight registry records were downloaded and hash-frozen, extracted by one-based physical page, and visually checked at the identity, chronology and decision-defining statistical pages.

## Exclusions

- `NCT02064868` — protocol pages 62-70 expose FAS/PP sets, adjudicated time-to-event analysis, Kaplan-Meier/Cox and repeated models, safety, interim policy and sample size; the SAP history confirms Amendment 4 overlap.
- `NCT03698331` — protocol pages 44-46 expose three analysis sets, Fisher exact testing, endpoint summaries, missing-data delegation, sample-size rationale and no-interim rule; the SAP explicitly lists Amendment 3.
- `NCT02739984` — protocol pages 47-54 expose analysis sets, repeated-measures primary models, sensitivity analyses, graphical/Hochberg multiplicity and power.
- `NCT04681066` — protocol pages 66-68 expose sample size, four analysis sets, stratified log-rank, Cox/CMH, censoring and no multiplicity; the SAP is post-completion.
- `NCT02578901` — protocol pages 36-40 expose populations, logistic/linear/negative-binomial/proportional-hazards models, MAR/MNAR sensitivity analyses, DSMB boundaries and power.
- `NCT03721172` — protocol pages 49-53 expose analysis sets, CMH, MI/NRI/tipping point, MMRM/ANCOVA, hierarchy, interim policy and power; the SAP is post-primary.
- `NCT02712424` — protocol page 55 exposes populations, time-to-conversion definitions, censoring, log-rank/Kaplan-Meier/discrete-time analyses, missingness and power; the selected SAP is a late updated plan.
- `NCT02655224` — protocol pages 63-65 expose three analysis sets, efficacy/safety methods, alpha/CI, no-interim rule and sample size; the SAP confirms the same original protocol.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02064868 | protocol leakage | 92 / 66 | `af4c217b3ce9b55114f8b0c4501d4d47dd97041a657e8b72a71d0d797c371474` | `d46f9ad6c68d0abd88e62e4fa97198b8469c50bed318410eb697489c372ad1d0` |
| NCT03698331 | protocol leakage | 51 / 33 | `0c201d37c36a8650f29d02f1a9ab2f3e8337722483900ca06f63a7f9e2d89d02` | `9a21db2e5a9e07b879634d8ce045838b87e2f0544c3ef25552887ca2f8762b52` |
| NCT02739984 | protocol leakage | 106 / 31 | `582157c2334f3511186a2ead7c1bb48b532a01b7f35447074725d5dc2ee1971a` | `423410dae8f82e883954b9326fd8abad19c12444ff9785b610a9c62156b9700b` |
| NCT04681066 | leakage + post-completion SAP | 88 / 32 | `392b8e48f17c84e791904132fbc023c3f6cf084c010d263f259761bd84dcc5fb` | `b26c8058943006e8c76ee5d69d6437f990bf932de621f6f104d33c73d6bf8385` |
| NCT02578901 | protocol leakage | 63 / 26 | `07c0fb144222d462d449a138eee5900c3955b37f1f8751be683cb9ff5160ea39` | `9caa207296296a98916e8fea71072967224e929eb5d93bd9e9e1268f958aba23` |
| NCT03721172 | leakage + post-primary SAP | 94 / 50 | `ef42fb5034cd1f7e6f8e9c24c35f93209792d20ab20651dfd3e22806373ca595` | `f5e29e9d8f1fd6a4ec6527552ecce05ec432d7d2facce246581a9489986dc431` |
| NCT02712424 | leakage + late updated SAP | 68 / 8 | `da57fa0affd61e16f2fba6c7a2154192a1731ed680ea30136262f27762ee9b8d` | `770c5045b63b9958d3f709e8b1f8c0545f3858ca68d7822ef7a8118aee0540fe` |
| NCT02655224 | protocol leakage | 72 / 41 | `f4174679ef3be3a0a7fcacb9e49cd4d8464b67e4a91585599c33b3d4e29151d0` | `da90400147fabefe9c0108c4e49ef0d98b23ae0f39ff0fb4d6e37c8e20d9d741` |

## Review gate

These eight candidates cannot enter train/dev/test. All eight slots must be replenished; no Batch 45 record is counted as a completed benchmark question.
