# Expert Review Packet - Batch 100

## Scope and decision boundary

Batch 100 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. All 16 PDFs and eight registry records were frozen locally and extracted page by page. Decisive identity, chronology, CSR packaging, executed-method and target-leakage pages were rendered and visually inspected. One family is promoted as a first-pass annotation draft and seven are excluded. Seven open slots are replenished so the intake remains 120 public families.

## Promotion

- `NCT04204447` -> `PUBLIC-HCV-EDUCATION-DELIVERY-001`. The five-page protocol and independent three-page Statistical Analysis Plan print the same NCT, title and 2018-06-30 date and predate actual 2019-11-27 study start. The protocol defines a prospective nonrandomized matched video-versus-brochure education study without leaking the reference-only generalized mixed model, logistic model, alpha or power table. Twenty requirements were added. The reversed Group-A/B labels, primary knowledge endpoint, questionnaire scoring, visit contrast, analysis population, matching and clinic adjustment, estimand, missingness, multiplicity, safety and the plan's off-target first-appointment power calculation require expert adjudication.

## Exclusions

- `NCT03012828` — protocol pages 60-64 expose endpoint derivation, populations, sample size, missingness, confidence intervals, the primary concentration-QTc mixed model, hysteresis rule and covariance structure.
- `NCT02735421` — the interim plan postdates actual primary completion, and the protocol also exposes the interim analysis, LOCF, populations and power calculation.
- `NCT03751657` — both selected documents are Clinical Trial Report appendices dated after study completion.
- `NCT01976104` — the final plan postdates primary completion and is CSR-packaged; the protocol also records outcome-informed endpoint and sample-size changes.
- `NCT02436135` — the final plan postdates terminated-study completion by more than two months.
- `NCT02198664` — the final plan postdates completion and cites Protocol Amendment 3.1 rather than selected Amendment 3.
- `NCT02313675` — both short documents describe already executed recruitment, treatment and analyses rather than a prospective governing pair.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03012828 | protocol leakage | 83 / 40 | 2236121d5c685da918470352e98780f38c5d8c6dfa384f16ec08d7c802c99ded | 761364df90d0d95cee3ea0daa255f6ce60b0c34fa722b6d2406af22c4d12d204 |
| NCT02735421 | post-primary interim plan and leakage | 100 / 38 | d8178629ce24790c78d4512c4c31f011b75e61acc1a5a03f62f4b88d1db7a52a | 30af43a606a44b0db6e0dc796940e7c5940c568ecc31f83f3926a4f91bbd4523 |
| NCT03751657 | post-completion CSR appendices | 98 / 27 | a4690681a515caf1d6f7f13df09f267c707f2eac6a7769daca52c27f0244857e | e28bdc0286a906cd273a48f4c000f820db2ea30574ea7823811f420bffcfceb7 |
| NCT01976104 | post-primary outcome-informed CSR plan | 101 / 30 | 95a97c593582d2414998a76f9b76b53e9160b719b58ade981d41318ae92e9066 | 6ade597bb516560c241afb86f236495bc766f253054b23929e5a11dabdb77f3e |
| NCT02436135 | post-completion plan | 111 / 39 | 14f800c0ff1803936655944ca9171a2855d82b357bc25a59ea4d6faf1b9c617d | 221c5555ae1d28a18e529e6b640014ab1e8b7d302abd65dbbf2c16c0da074e18 |
| NCT02198664 | post-completion version mismatch | 130 / 29 | bc7b9976373d1721a3121a4e372df7e30e9d038a539f57c384c9919cea395e15 | 874ae755727112c17297dcfe275bbac5e850a0ec0e7547adb49d1cd62f41a14d |
| NCT04204447 | promoted prerecruitment draft | 5 / 3 | 4fd7611ae0efa3f2bfdf5264cf4a317bc7ddaa93f2088fe369c04f057e44bdb6 | 29715a101daaf5eeed7476a0123939677eea1a1e7fc9cd960b576f4ade502ced |
| NCT02313675 | retrospective executed-method summary | 2 / 2 | 9f909a02a627bdff2113596cca27970828a62e8ab3e86471c529aecdf5cd241d | d2a1b8228602307b14cc25cfcb90a2cf871c131ae38e561b7c365c22390ae30b |

## Review gate

The promoted family remains `draft_needs_expert_review`; it is not expert-approved or split-frozen. Its reference plan remains annotation-only and must never be model-visible. The seven exclusions do not enter the completed-question count.
