# Expert Review Packet — Batch 80

## Scope

Batch 80 reviewed eight ClinicalTrials.gov document families. No family met the benchmark's prospective, independent and non-leaking protocol/SAP requirements. Four families were excluded because the selected analysis material was retrospective, post-completion or not a distinct prospective governing SAP; four were excluded because the model-visible protocol already exposed an executable target, with post-completion defects in two of those families. All 16 PDFs and eight registry records were downloaded and hash-frozen. Text-bearing files were extracted by one-based physical page; the scan-only NCT03080961 SAP and NCT05579730 protocol were fully rendered and OCRed before the decisive pages were reviewed.

## Decisions

- `NCT02213458` — `excluded_wrong_document_type`. Both files are dated 2018-08-06 after 2018-03-08 completion; SAP pages 3-4 say QDRS replaced FAST after study initiation, so the upload cannot establish a prospective governing plan.
- `NCT02608476` — `excluded_combined_protocol_sap_leakage`. Protocol pages 8-11 expose hierarchy, sample size, analysis sets, MI, logistic regression, ANCOVA, sensitivity and safety analyses. The SAP postdates completion and reports actual enrollment and sites.
- `NCT02692560` — `excluded_wrong_document_type`. The 2018-02-12 files are excerpts from a published article after February 2017 data completion; protocol page 1 explicitly records finished collection.
- `NCT05816551` — `excluded_wrong_document_type`. Both files postdate 2024-09-30 completion; the selected protocol is itself titled Statistical Analysis Plan and mixes prospective with completed-conduct wording.
- `NCT03678506` — `excluded_combined_protocol_sap_leakage`. Protocol page 17 reproduces the one-page statistical upload's power, threshold, Kaplan-Meier, HR and interim rules.
- `NCT05579730` — `excluded_combined_protocol_sap_leakage`. Protocol pages 45-52 disclose success criteria, alpha allocation, ANCOVA, populations, detailed MI/MNAR rules, sensitivity analyses, sample size and no-interim rule.
- `NCT03080961` — `excluded_combined_protocol_sap_leakage`. Protocol pages 28-30 disclose sample size, confidence-limit success, Wilcoxon test, AT/PP sets, missingness and endpoint analyses; OCR confirmed the scan-only SAP's identity and matching Version 5.0 citation.
- `NCT02830074` — `excluded_combined_protocol_sap_leakage`. Protocol pages 10-12 disclose ITT/MI, complete-case sensitivity, mixed models, ANCOVA, subgroups and power; the two-page replacement plan postdates study completion.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02213458 | wrong document type | 4 / 5 | 666f0da8f297dbf6df8e65353e6a03c83d4a2d0f3ec98c404a8d2d77411f8feb | d5dac4e0103df3761b3041c4560990b6b42534310d9fe97ace565849a80c91e1 |
| NCT02608476 | protocol leakage | 56 / 41 | fb9c94899284c7ced9611640dd2ac32f29bb7e4392c6c75174cb068e28250d38 | af389c5d54b1e30082961732d2b2ffcfd436357450ec4d5ec0d60f66b8fb0a8e |
| NCT02692560 | wrong document type | 9 / 1 | f4b38c68b37280d2e1e410f1bbf1e7321ed8c29e03831dfcb2d1ef55343e947a | d1f147939459bae1a98affe7f755c95bfe6b82357946e72098f5a60d57518778 |
| NCT05816551 | wrong document type | 4 / 2 | bebcf3cbf934107178c00566ab5b925076826797e1c85701cf3d610043c01aa6 | 181506d238551ab083ed969cb232b4fde6ed6c0c04faf20a217503068d8ab869 |
| NCT03678506 | protocol leakage | 37 / 1 | f093e604231342b34f21a94996dfbec655d453daa5725f229e9ba17830f29b2e | a36fb2846d3352afef49ce8a999dc21b857b2a278960c78d803a5d807cd647d5 |
| NCT05579730 | protocol leakage | 69 / 21 | e187e74e3dd2256074f7e530c09751867a2421f587b2795ecac918ea308f4bb5 | ccd3d786270a627d43b3b118d7c9e254837acaa6076fe42bea72d6cecf645b9f |
| NCT03080961 | protocol leakage | 49 / 26 | d4314c3fef6518bba243a643f7b1a4636e2951ef9d1d7c9bad67794074b771eb | 7b6db3ff368213e0ff1f1f049b30829644eda20c20cedf6a54886f848b394170 |
| NCT02830074 | protocol leakage | 20 / 2 | ecffceece329a4ddeb0dd898065e7238172a5278cce07a8f8fde02b0347eba23 | 4b5625fb0450d3dc935287666835f509526868a7ddec4e7f2146fa8d28192562 |

## Review gate

No Batch 80 family is eligible for a generated-SAP prompt or requirements annotation. Reference SAPs remain annotation evidence only and must never be included in protocol-only model inputs. All eight decision records remain outside the actionable candidate pool; their replenishment candidates require fresh document-level verification and cannot be counted as annotated studies.
