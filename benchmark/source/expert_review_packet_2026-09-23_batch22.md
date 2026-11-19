# Expert Review Packet — Batch 22

Batch 22 produced no promotable study. One pair is held because material public content is redacted, and seven pairs failed a hard source-admissibility gate before requirements annotation.

## Screening decisions

- NCT04944290: `hold_public_redaction`. SAP physical page 7 redacts the allocation ratio, sample size and substantive per-protocol criteria; physical page 11 redacts the core primary-analysis model and related methods.
- NCT03172364: `excluded_wrong_document_type`. SAP physical pages 1-2 identify an amendment dated after primary/study completion, and physical pages 45-48 contain an addendum explicitly developed after unblinding during CSR preparation.
- NCT04090580: `excluded_wrong_document_type`. Both uploaded documents postdate primary/study completion, and SAP physical page 2 reports actual randomized counts, discontinuations, completers and baseline p-values.
- NCT02955602: `excluded_wrong_document_type`. SAP physical page 1 postdates study completion; physical page 36 records a fourth interim analysis and material changes to populations, models, subgroup analysis and live safety monitoring.
- NCT03251482: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 75-83 expose the populations, sample-size assumptions, primary efficacy and bleeding analyses, MCP-Mod, noninferiority criteria, multiplicity, interim analyses and safety summaries.
- NCT02993107: `excluded_wrong_document_type`. First SAP Version 1.0 on physical page 1 postdates primary/study completion, and physical page 9 frames it as the final analysis through database lock.
- NCT01818258: `excluded_wrong_document_type`. SAP physical pages 1, 3 and 14 establish a post-completion final-analysis and publication plan with final-report and manuscript-team updates.
- NCT01946789: `excluded_combined_protocol_sap_leakage`. The alleged SAP is a seven-page protocol extraction: physical pages 1-3 reproduce protocol front matter and physical pages 4-7 retain protocol internal page numbers 77-80; no independent reference SAP exists.

## Source audit

All 16 PDFs were downloaded from the ClinicalTrials.gov registry, hashed, page-counted and extracted by one-based physical page. NCT04944290 was additionally rendered at 180 DPI and OCR-checked to distinguish genuine black-box public redactions from text-extraction failure. Every decision-defining page was inspected. Reference SAPs remain annotation-only acquisition artifacts under the gitignored source tree.

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT04944290 | public-redaction hold | 67 / 16 | `491cb88d0ece30954ec130144cd18940d7e1edec1c1714cf744a3cbc08c58901` | `5b1758e5d3c6faf7d356fc38bb8fc0ffb0222ebff9be7a99a8fab5e54e514b6b` |
| NCT03172364 | wrong document type | 68 / 54 | `c457bc0ab7dbfe3fa4a05a9b73704fe3aaf649a2bd80961e7ce9fddd6fbf4f18` | `d934472b243dfee89c72d544bbe11747e12fabe99515a874501028eb74b56f6b` |
| NCT04090580 | wrong document type | 32 / 2 | `a43bd88de66dc133fa81c6643d89e19ab4c2424ded6b371df640e4528c84a20a` | `334c4b75add24d774e4c37b424e7ba835919dd245e47882516009f5958d7d991` |
| NCT02955602 | wrong document type | 88 / 36 | `d77877fcb0ba09a6970c241a3b91c742e888e35e66c8620361741c2071bcb021` | `fba777ca8a0e45ae80faae4082cad0ed8d99d1487e325145bf4f5d69d4f67853` |
| NCT03251482 | protocol leakage | 113 / 35 | `6c8ed8f89c3e372d31233ce2cfd49e4e783d3213128f026744d0920f64e9fc4b` | `5ecaebb48590dd812c9de8d0282755a0a14d0c925f975731d8cab9fcbb7341fd` |
| NCT02993107 | wrong document type | 140 / 51 | `f33554573e0a3e74dfda2a58875716a59660e71f5841e6171371ff71aaa53d34` | `6156a502f0aefd73d5664cd066ba11a4e5ef10dc49d21115bf1abaeb7dc73205` |
| NCT01818258 | wrong document type | 99 / 14 | `82ca41d0af8171b6d778c163e5617a4c8ef1d46d410ded72f1cd036d641f1dc1` | `a7a60ca6e22e8c28bf94c4883184e566bbfd5abffc6b2945c784c55f118355e8` |
| NCT01946789 | no independent SAP / protocol leakage | 82 / 7 | `3bc838c5beffe4d8694398c431cb12ddee54a0fb1b96e0adcd8532d6f7ad1b8e` | `0687f580cb06c6bf01a1a400421d6db6da68270bde11a8b464da32c548f92ada` |
