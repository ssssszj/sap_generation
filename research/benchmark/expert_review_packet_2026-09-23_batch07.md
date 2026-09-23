# Expert Review Packet — Batch 07

## PUBLIC-CINACALCET-EXT-001

- 23 requirements; all remain `draft_needs_expert_review`.
- Confirm that the complete Amendment 3 dated 2016-03-16, together with the narrowly scoped superseding amendment dated 2016-06-01, is an acceptable governing model input for SAP v2.0.
- Verify the Safety, Efficacy, SOC, and two per-protocol analysis-set definitions and their endpoint-specific binding.
- Adjudicate the primary incidence confidence intervals, follow-up-time-adjusted rates, IPW model, repeated-measures sensitivity model, and missing-iPTH derivations.
- Keep extension-only descriptive analyses separate from combined parent-plus-extension summaries and do not imply randomization within the extension.
- Confirm that SAP-only operational decisions remain `confirmed_decisions` or protocol-only confirmation requests rather than hidden protocol-only facts.

## Version and source decisions

- `NCT02341417`: promoted. SAP v2.0 dated 2016-05-24 explicitly cites protocol Amendment 3 dated 2016-03-16. The public protocol bundle contains the complete Amendment 3, and the subsequent 2016-06-01 superseding amendment explicitly limits its changes to administrative/typographical corrections in Section 10.4.4 safety thresholds.
- `NCT02279173`: `hold_version_reconciliation`. SAP v1.2 cites the original protocol dated 2014-01-15, while the public bundle provides a complete 2014-08-15 Amendment 2 protocol plus amendment records, not a complete original governing protocol. Reversing amendment diffs is not accepted as model-input reconstruction.
- `NCT04435600`: `hold_public_redaction`. The version chain can be bridged, but material risankizumab dose values are redacted in the public documents.
- `NCT01682356` and `NCT02075437`: `excluded_wrong_document_type`; the analysis uploads are retrospective completed-study notes rather than prospective governing SAPs.
- `NCT03955055`: `excluded_wrong_document_type`; the purported SAP is a Data Safety Monitoring Board Charter.
- `NCT00116337` and `NCT03342027`: `excluded_combined_protocol_sap_leakage`; their protocols substantially reproduce the separate SAPs' core analysis content.

## Source audit

For every candidate below, title/version pages and the pages supporting the admission, hold, document-type, redaction, or leakage decision were visually inspected. Page counts and SHA-256 hashes were checked from the frozen public PDFs.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT02341417 | protocol | 192 | `484b4474913c6feb4a81f7cd74fea65843f99d08e7149667fcf2c140366f92bc` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/17/NCT02341417/Prot_000.pdf) |
| NCT02341417 | SAP | 37 | `656b4c347d949e5b0ed2c7851334ddbde93d390ea32ad314ccf319c2a31b9283` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/17/NCT02341417/SAP_001.pdf) |
| NCT01682356 | protocol | 19 | `033d9ef7bc4cb0177f18439b852f4afa57d95ae8b7ede606e5ae8242dea796f7` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/56/NCT01682356/Prot_000.pdf) |
| NCT01682356 | SAP | 2 | `21567839ee38911106d18a9a6f0030fd5384b454b3d32f12c2c199c219dd4b` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/56/NCT01682356/SAP_001.pdf) |
| NCT00116337 | protocol | 16 | `4a6a078a56a687f2c66571050a13771dfd39046475aa12efb1ebe53fd219ea90` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/37/NCT00116337/Prot_000.pdf) |
| NCT00116337 | SAP | 4 | `dc200b13ff6c581fefc9f6bb4225c0e9a908f4bff90dc814d5b0673255d6b404` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/37/NCT00116337/SAP_001.pdf) |
| NCT03955055 | protocol | 20 | `51985c2d535c58ec42277583a3d0076f716a47d7568a52eb74531048965617e7` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/55/NCT03955055/Prot_000.pdf) |
| NCT03955055 | uploaded SAP slot | 7 | `17fc3fc24b3930b5b594d4ace70d5b76b2b0413bbd92ccb57243ff6d28ac4f7d` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/55/NCT03955055/SAP_001.pdf) |
| NCT02279173 | protocol bundle | 116 | `f0329feaa9a2bf38c9cbd41c4f25bdca80cd9476a7794dea9541a0cc31f06fb5` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/73/NCT02279173/Prot_000.pdf) |
| NCT02279173 | SAP | 15 | `3de3706584883de86b5a2a6b1b36936c689a68dd3fd736ecb9c440133f17cce5` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/73/NCT02279173/SAP_001.pdf) |
| NCT04435600 | protocol | 53 | `6d06fee09b933c479c5db4bafe55bbcd04892c00f5ab55cb588b44b3ff9c4395` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/00/NCT04435600/Prot_000.pdf) |
| NCT04435600 | SAP | 50 | `a19dd24f99f3834e0005fb98b3f9f4c50a069a82a944f0722bb8402b2778b6aa` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/00/NCT04435600/SAP_001.pdf) |
| NCT03342027 | protocol/IRB bundle | 86 | `a3959c9bea04e60ab20c6cb1f701c51b5e5eb2002356578a9a8a84683df4a323` | [Prot_ICF_000.pdf](https://cdn.clinicaltrials.gov/large-docs/27/NCT03342027/Prot_ICF_000.pdf) |
| NCT03342027 | SAP | 2 | `9c61364ef0af660a7cf74bb3132ab57aec4c1c619ec5b5195cd20dfa7d4f4091` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/27/NCT03342027/SAP_001.pdf) |
| NCT02075437 | protocol | 29 | `8975a06b2a9d5dddb93745e2daf8cde40e7d6e5899017d16bb469d4eab8ef719` | [Prot_000.pdf](https://cdn.clinicaltrials.gov/large-docs/37/NCT02075437/Prot_000.pdf) |
| NCT02075437 | SAP | 2 | `115050f9df9cc114d429f32f91031443dd9799adcd6ece67f00bf06dffbf0863` | [SAP_001.pdf](https://cdn.clinicaltrials.gov/large-docs/37/NCT02075437/SAP_001.pdf) |

The local PDFs are acquisition artifacts under the gitignored source tree. Their URLs, hashes, and page counts are recorded here or in the manifest; PDFs are not committed.
