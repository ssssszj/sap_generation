# Expert Review Packet — Batch 06

## PUBLIC-BRAIN-WELLNESS-001

- 17 requirements; all remain `draft_needs_expert_review`.
- Confirm that descriptive statistics, rather than formal treatment-effect testing, are the active pilot analysis.
- Keep the mixed random-effects model on SAP page 3 explicitly scoped to a future efficacy study.
- Review recruitment, retention, participation, fidelity, blinding, and acceptability thresholds for operational fidelity.
- Resolve the primary depression/anxiety hierarchy, pilot sample size, analysis populations, missing-data handling, and exact descriptive summaries.

## PUBLIC-INFLUENZA-TRANSCRIPTOMICS-001

- 15 requirements; all remain `draft_needs_expert_review`.
- Confirm whether the baseline-to-Day-28 HAI Wilcoxon comparison is the single confirmatory primary analysis or part of an exploratory program.
- Review laboratory blocking, same-subject adjacency, failed-assay handling, and CQN normalization.
- Adjudicate multiplicity across vaccine, sex, immune, transcriptomic, mediation, and pathway analyses.
- Resolve analysis populations, missing visits and assays, effect summaries and confidence intervals, randomization implementation, and adverse-event summaries.

## Version and source decisions

- `NCT02600637`: protocol and SAP share the exact title, NCT identifier, and 2019-04-05 date; both three-page PDFs were visually checked and no complete target SAP is embedded in the protocol.
- `NCT03603509`: protocol Version 7 and the SAP share the exact title, NCT identifier, and 2019-05-19 date; key design/analysis pages and both SAP pages were visually checked, with no complete target SAP embedded in the protocol.
- `NCT02173379`: `hold_public_redaction`; governing version identifiers are redacted and cannot be inferred from matching metadata.
- `NCT02796677`, `NCT02407054`, `NCT02301897`, and `NCT00928447`: `hold_version_reconciliation`; the available version/date chain is absent or inconsistent.
- `NCT03856047`, `NCT05025345`, `NCT02176018`, and `NCT04707014`: `excluded_combined_protocol_sap_leakage`; the protocol reproduces substantial target analysis content.
- `NCT03556293` and `NCT04697836`: `excluded_wrong_document_type`; the uploaded analysis documents are retrospective completed-study summaries.
- `NCT03342027` and `NCT02337361` remain candidates and were not adjudicated in this batch.

## Source audit

For every adjudicated candidate below, the title/version pages and the pages supporting the admission, hold, document-type, or leakage decision were visually inspected; hashes and page counts were then checked from the downloaded public PDFs.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT02600637 | protocol | 3 | `563eec653c93ffee43bc5b757e3c4c9c5120f83dd8b91b2851bb14bcde42e0bb` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/37/NCT02600637/Prot_000.pdf) |
| NCT02600637 | SAP | 3 | `d4092540d8ce8b698d31a2fadbf9e3b3d89da0f7542ee1cc3b4ed489d1621b36` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/37/NCT02600637/SAP_001.pdf) |
| NCT03603509 | protocol | 38 | `219f9d97a84aefc5088a41a216e1d72da29efeafe9846114e3fe8d969faca9f8` | [Prot_001.pdf](https://cdn.clinicaltrials.gov/large-docs/09/NCT03603509/Prot_001.pdf) |
| NCT03603509 | SAP | 2 | `dd6c3c5e1a2f7fb3c703782f8a9cb07bf293c78f25af8045e79ad7b080e80f2e` | [SAP_003.pdf](https://cdn.clinicaltrials.gov/large-docs/09/NCT03603509/SAP_003.pdf) |
| NCT02173379 | protocol | 245 | `235b3354afca80d53bcf3c6de2495e8cbe0f7eb4434451fb56d9742039aecbd7` | [Prot_003.pdf](https://cdn.clinicaltrials.gov/large-docs/79/NCT02173379/Prot_003.pdf) |
| NCT02173379 | SAP | 37 | `4a2f4fb39b9ded9b512d3c42ab1510cbef3a1078f1d02e8f36ae754c73d8fb62` | [SAP_004.pdf](https://cdn.clinicaltrials.gov/large-docs/79/NCT02173379/SAP_004.pdf) |
| NCT03856047 | protocol | 110 | `7f89dc6be3054adba243740db0022920c208fdb09cc26e7ec1ddb06681000873` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/47/NCT03856047/Prot_000.pdf) |
| NCT03856047 | SAP | 25 | `74edde66640d50bdfb5362bfd8af1226da3e5c5d6d0fe619a293df104c0b47a2` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/47/NCT03856047/SAP_001.pdf) |
| NCT05025345 | protocol | 87 | `67f61dd99e06437498ed228c752107c415f74ab02c2f15ee4fb87583570da518` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/45/NCT05025345/Prot_000.pdf) |
| NCT05025345 | SAP | 20 | `b5fb9b6d2fdeca026ec8c3b8cb83f2397c4e8adbffa5c42fbe395a4772032a97` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/45/NCT05025345/SAP_001.pdf) |
| NCT02796677 | protocol | 137 | `1ad2476d3675430767d1b0d8b4463b147d5339bb831ae8aac25be73a94dd60dd` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/77/NCT02796677/Prot_000.pdf) |
| NCT02796677 | SAP | 114 | `b9bc1ae555dac1bc4a7ee65bfac8c97fc6e8ded55501398b7b355765d85d7a16` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/77/NCT02796677/SAP_001.pdf) |
| NCT03556293 | protocol | 39 | `949fbbf4a888870fa810015c8ed5f6dc64b459330ced5537e6c192a9de398dfa` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/93/NCT03556293/Prot_000.pdf) |
| NCT03556293 | SAP | 2 | `f45b9322df59562728d3bbe12ab35e9749beca3a270c50dcd60d724840c6a57f` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/93/NCT03556293/SAP_001.pdf) |
| NCT02407054 | protocol | 96 | `428be7851db3ae31b20f00718671527847a4b84763e51f274716d890c3a80d4c` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/54/NCT02407054/Prot_000.pdf) |
| NCT02407054 | SAP | 36 | `c03db817f56fa0c86fdfcfc988bd3ac3d24e54c5539341e5c0791e95c15315dd` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/54/NCT02407054/SAP_001.pdf) |
| NCT02176018 | protocol | 21 | `c87232d1cc9040cc6442b6e581a4b5f3ca9fbe0f48f01bc09175bf68888d9095` | [Prot_001.pdf](https://cdn.clinicaltrials.gov/large-docs/18/NCT02176018/Prot_001.pdf) |
| NCT02176018 | SAP | 3 | `6fa051e825dacfc70f99d175e7654256722b7d04c0d82ecb2c9117b6b8fd5ca9` | [SAP_000.pdf](https://cdn.clinicaltrials.gov/large-docs/18/NCT02176018/SAP_000.pdf) |
| NCT02301897 | protocol | 113 | `bacf8ddbc6c77473e181165a3bb33e74cbe8224b22381c2a0ad9c589ce5db30f` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/97/NCT02301897/Prot_000.pdf) |
| NCT02301897 | SAP | 32 | `50b0ad8554fe6100916107512e913bf71dd1dabe7fc17b3a33fabe672b657fcd` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/97/NCT02301897/SAP_001.pdf) |
| NCT00928447 | protocol | 53 | `fbfd3d8fe1c05d9caefa1deee6f458fd3ae399d0d6c08d3cbb39ced78ff2df58` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/47/NCT00928447/Prot_000.pdf) |
| NCT00928447 | SAP | 64 | `9cbeca9730ed3d77710db73b244fae23e6c29d9268b21962b8981272ec847bdf` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/47/NCT00928447/SAP_001.pdf) |
| NCT04697836 | protocol | 3 | `5f51adfca3c8d8c49fd7e75762aecfa81c8c9e0e99cc1d63f2fea67d1830f753` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/36/NCT04697836/Prot_000.pdf) |
| NCT04697836 | SAP | 2 | `3b64156d6705b15d68fac8a7153a498df783cc5988c3d1e3accaf6fc12331b9e` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/36/NCT04697836/SAP_001.pdf) |
| NCT04707014 | protocol | 9 | `62cd4d4db6623c86465950152045887813e8e29fc35ae5da5706988a6760bcdf` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/14/NCT04707014/Prot_000.pdf) |
| NCT04707014 | SAP | 2 | `0359ab6d8b8680a6299d830a35ecb8d1d4bc165afd7566112aff99fa13af8b57` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/14/NCT04707014/SAP_001.pdf) |

The local PDFs are acquisition artifacts under the gitignored source tree. The manifest or this packet records their public URLs and frozen hashes; the PDFs are not committed.
