# Expert Review Packet - Batch 115

## Scope and decision boundary

Batch 115 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen official PDFs and eight registry records were downloaded sequentially, byte-checked, SHA-256 frozen and extracted page by page. The 107-page NCT02466243 protocol, its 40-page SAP and the 19-page NCT03639623 SAP required full-page OCR because native extraction was sparse. One hundred thirty-eight decisive identity, chronology, family-dependency and statistical pages were rendered from the original PDFs and visually inspected; OCR was used only to locate evidence. No family is promoted: six selected targets are late, conduct-informed, parent-dependent or already reproduced in the protocol; one lacks a defensible governing-version match and leaks the target; and one same-day prospective pair fails the non-leakage gate.

## Decisions

- NCT01849575 — exclude: the 2024 six-year amendment follows the completed and published primary endpoint and plans analyses of already accumulated baseline through six-year panel data; Protocol Version 6 also supplies the outcomes, sample size and models.
- NCT02466243 — exclude: the Part A SAP cites Protocol Version 2, but the public prompt is Version 5 after Part A completion and exposes sample size, populations, hypotheses, missingness, multiplicity and methods.
- NCT02722408 — exclude: the SAP follows primary completion and explicitly records a completed January 2017 interim data cut; protocol pages 43-45 disclose the principal program.
- NCT03639623 — exclude: the SAP follows actual primary/final completion, while protocol pages 58-61 disclose the populations, LOCF, efficacy/safety summaries, interim stance and sample-size rationale.
- NCT05078138 — exclude: the post-completion two-page upload nearly verbatim reproduces protocol page 17's complete statistical section.
- NCT02969018 — exclude: the SAP follows completion and its amendment history says it aligned with protocol text; protocol pages 75-76 expose MMRM, covariates, MAR, multiplicity and sensitivity analysis.
- NCT01281813 — exclude: the post-completion final CSR SAP is a continued-access analysis dependent on four parent trials.
- NCT03988023 — exclude: despite clean same-day prerecruitment chronology, protocol pages 42-49 already disclose the executable co-primary adaptive program.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01849575 | post-primary observed follow-up and leakage | 46 / 5 | 3e0dc989dc8f45bbdcd72322011712a160849b4f41f84676a8571a734d436819 | f17014847e681dbad0064aa94b379708118b1f724b375bfdedaf363a12d3c03f |
| NCT02466243 | governing-version mismatch and leakage | 107 / 40 | dd6f4bb69da063e400a8f179cf08c032a98855545b14526813f5a589ff06e3a0 | 5b5fd7babe7c882634b2be5ab1f214b835fd96abd303df983b19391e4ed08594 |
| NCT02722408 | post-primary interim-informed SAP and leakage | 62 / 24 | feea4297d5150dacc887198b9e00b34d2bc55274e3faf4b7a319419cf0e0a28a | bd2d9e3b38ff667250bab83999b13e9b7e0202dafa57862f933c9abc59b45d53 |
| NCT03639623 | post-completion SAP and leakage | 80 / 19 | e9f2225d6c109c17941e8169edad6d1d4d6000646639c015fd2bf119da819798 | 62013504247420b0e43eba56e56534e00405ae7b9cc980f4d477f44709e564da |
| NCT05078138 | post-completion duplicated analysis section | 39 / 2 | d5c2732ee098e4c360a68a9a1be0c010289854e11cead6e9d9374192b2bfc054 | fa22890eb575c61b427425d32c4469657939040d6176ca2af080de6ba7c3914f |
| NCT02969018 | post-completion SAP and leakage | 107 / 33 | 77849b765634e5506a442232d82cfa43d5fdde84e2dfd63c4598fc0df76fd652 | e9ee0491d017c50cd6549e06d493e5b89551dfef73a6c90bc71d4f65312fa20b |
| NCT01281813 | post-completion parent-trial continued access | 95 / 11 | bc3b87d0b6bf6d56993747e04e45bb0502a9218fa0c78f1ce97ec083a2a17844 | 416c84b6339a4b5f3d309a255591cad71a71d6b579da36a59ac6e2b551e361fc |
| NCT03988023 | protocol leakage | 57 / 25 | 549eca7c4959100c63eb09ef7ad74df7261fd44548f35b38b34fd3e8b783c2a3 | bd1572373da43d1d4307e818b5de2c5f500cca15fcaeb55ae21270cc62a82271 |

## Review gate

No Batch 115 family enters the registered benchmark. All eight slots must be replenished so the release intake remains 100 version-verified public drafts plus 20 actionable metadata candidates.
