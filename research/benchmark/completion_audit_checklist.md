# Initial Benchmark Completion Audit Checklist

## Objective and release boundary

The requested initial deliverable is exactly 120 **public** SAP-generation benchmark questions. A question counts only after its source documents, prospective governing version chain, study-family independence, protocol-only leakage boundary and first-pass evidence-backed requirements have been reviewed. The private pilot does not count. Metadata-screened candidates do not count. Excluded or held families must be replaced rather than reducing the target.

The initial benchmark may remain `draft_needs_expert_review`; it must not be represented as expert-approved or as a frozen release. Reference SAPs are annotation evidence only and must never appear in model-visible inputs.

## Prompt-to-artifact coverage

| ID | Required deliverable or gate | Concrete artifact/evidence | Completion rule | Current state |
|---|---|---|---|---|
| C01 | Exactly 120 public questions | `manifests/studies.jsonl`; one non-pilot row per public study | 120 public rows, all `status=verified` | Incomplete: 104 |
| C02 | No candidate counted as a completed question | `screening/candidate_catalog.jsonl`; `screening/candidate_pool_summary.json` | candidate count is 0 at delivery | Incomplete: 16 after Batch 126 replenishment |
| C03 | Private pilot excluded from the 120 target | `PILOT-IOL-001` study row and configuration scale target | exactly one `pilot_only` row; public count evaluated separately | Covered; recheck at final audit |
| C04 | Frozen public protocol and reference SAP for every question | `manifests/documents.jsonl` and local `sources/public/<NCT>/input/` plus `reference/` packages | every public study resolves to model-visible input document(s) and a separately identified reference SAP with SHA-256 and page count/source provenance | Audit pending for all 120 |
| C05 | Reference SAP never model-visible | document `role`, paths and study package layout | reference documents occur only under annotation-only `reference/`; no prompt/input manifest includes a reference-SAP path | Audit pending for all 120 |
| C06 | Prospective governing version chain | study/document notes, annotation status and batch review packets | protocol/SAP identity and dates are supported by document-internal evidence and precede outcome-informed milestones; uncertainty is held, not guessed | Audit pending for all 120 |
| C07 | Independent study families | `study_family_id`, registry identifiers, notes and review packets | no parent/extension/rollover/shared-SAP family is split into multiple questions | Audit pending for all 120 |
| C08 | No executable target leakage in model-visible protocol | model-visible PDF plus batch review packet | protocol may state design/endpoints/sample size, but must not expose enough target analysis detail to reconstruct the reference plan | Audit pending for all 120 |
| C09 | No results/CSR/retrospective/execution-informed reference | reference PDF, registry chronology and review packet | reference is a defensible prospective governing analysis document; post-primary or observed-conduct material is excluded | Audit pending for all 120 |
| C10 | Evidence-backed first-pass annotation for every public question | `gold/<study_id>/requirements.jsonl` | one file per public study; normally 12–25 atomic, judgeable items; every item cites source evidence | Incomplete: 104 files |
| C11 | One-based physical-PDF locators | all public `requirements.jsonl` evidence arrays | every PDF locator uses the verified one-based physical page and its cited text is present there | Audit pending for all requirements |
| C12 | No actual enrollment substituted for prospective target | requirement wording, protocol evidence and review packet | sample-size requirement uses prospective target; actual enrollment may only be separately identified as conduct context | Audit pending for all 120 |
| C13 | Annotation status and unresolved decisions exposed | `gold/<study_id>/annotation_status.json` | every public study has a count-matched status file; unresolved statistical/version issues are explicit; no false expert approval | Incomplete until 120; existing files require final count/status audit |
| C14 | Domain and method coverage represented accurately | study design/endpoint metadata and `data_card.md` | metadata agrees with source evidence; summary counts are generated from manifests | Final reconciliation pending |
| C15 | Candidate/review/exclusion state is disjoint | candidate catalog, study manifest, `manifests/exclusions.jsonl` | validator reports no overlap among registered, held/excluded and actionable candidates | Recheck each batch and at delivery |
| C16 | Prompt-to-artifact package integrity | study `document_ids`, document paths/hashes, gold IDs | every study, document and requirement ID resolves uniquely; no orphan or cross-study reference | Final validator plus explicit audit pending |
| C17 | Complete batch provenance | `expert_review_packet_*.md` and `CHANGELOG.md` | every reviewed family has a promotion/exclusion/hold rationale and frozen hashes | Ongoing |
| C18 | Machine-readable benchmark validation | `python3 research/benchmark/tools/validate_benchmark.py` | zero errors; warnings individually reviewed rather than ignored | Run after every batch and at delivery |
| C19 | JSON/JSONL parse integrity | direct parse of all benchmark `.json` and `.jsonl` files | all records parse; no duplicate IDs; no blank malformed lines | Run after every batch and at delivery |
| C20 | Clean patch and scoped commits | `git diff --check -- research/benchmark`; Git history/status | no whitespace errors; each batch committed only under `research/benchmark/`; unrelated user changes untouched | Run after every batch and at delivery |
| C21 | Final real per-question audit | `final_audit/questions.jsonl` (to be created) | exactly 120 rows, each recording pass/fail and evidence for C04–C13 and C16; no unchecked row | Not started |
| C22 | Initial delivery documentation | `README.md`, `data_card.md`, config, manifests, gold, final audit report | all counts agree with actual files; limitations and draft status are explicit | Final reconciliation pending |

## Required command gates

Run and retain the outputs at final delivery:

```bash
python3 research/benchmark/tools/build_candidate_pool.py --target 0 --max-pages 6
python3 research/benchmark/tools/validate_benchmark.py
git diff --check -- research/benchmark
```

The pool builder's `--target 0` behavior must be verified before relying on it; if it is not a supported no-op, candidate exhaustion must instead be demonstrated directly from the catalog and summary. Validation is necessary but not sufficient: its implementation must be inspected against C01–C22, and missing checks must be added or performed by the final-audit script.

## Delivery decision

Do not declare the objective complete while any row above is incomplete, weakly evidenced or uncertain. A green validator alone is not completion evidence. The terminal gate is a real 120-row question audit plus zero actionable candidates, zero validator errors and reconciled release documentation.
