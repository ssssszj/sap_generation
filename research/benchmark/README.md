# SAP Generation Benchmark

This directory contains the initial evidence-grounded Statistical Analysis Plan generation benchmark.

## Initial delivery status

Collection stopped by user decision on 2026-10-02. The final audit covers all 107 registered public annotation drafts and produces this conservative disposition:

| Disposition | Studies | Included in initial question set |
|---|---:|---|
| `keep_draft` | 66 | yes |
| `hold_version_or_provenance` | 21 | no |
| `exclude_post_primary_or_execution_informed` | 20 | no |
| private `pilot_only` | 1 | no |

All 107 public studies have a protocol package, a separate reference SAP, a first-pass `requirements.jsonl`, and an `annotation_status.json`. Together they contain 2,066 public requirements; the private pilot adds 26. The delivered question set is [final_audit/initial_draft_question_set.json](final_audit/initial_draft_question_set.json), containing only the 66 `keep_draft` studies. It remains `draft_needs_expert_review`: none of the questions is expert-approved, split-ready, or frozen.

The complete 107-row disposition record is [final_audit/questions.jsonl](final_audit/questions.jsonl). It binds each study to its input and reference documents, registry chronology, requirement count, unresolved version questions, audit gates, and terminal disposition. The source chronology used by that audit is frozen in [final_audit/registry_chronology.jsonl](final_audit/registry_chronology.jsonl).

## Package layout

- `manifests/studies.jsonl`: 107 public annotated drafts plus one private pilot. A manifest `status=verified` records the historical pair-review stage; it is not the final eligibility decision.
- `manifests/documents.jsonl`: frozen document IDs, roles, paths, SHA-256 hashes, versions, dates, and source URLs.
- `gold/<STUDY_ID>/requirements.jsonl`: atomic, evidence-backed criteria for judging a generated SAP.
- `gold/<STUDY_ID>/annotation_status.json`: draft status, unresolved decisions, and expert-review requests.
- `final_audit/initial_draft_question_set.json`: authoritative 66-study initial question list.
- `final_audit/questions.jsonl`: authoritative 107-study final audit and dispositions.
- `screening/candidate_catalog_archived_2026-10-02.jsonl`: 13 metadata-only records archived when acquisition stopped. They are neither questions nor exclusions.
- `expert_review_packet_*.md`: acquisition and annotation provenance for the reviewed batches.

Public source PDFs are kept in gitignored `sources/public/<NCT>/input/` and `reference/` directories. The manifest retains URLs and frozen hashes so a consumer can refetch and verify them. Reference SAPs are annotation aids only and must never enter a model-visible prompt.

## Benchmark tracks

- `protocol_only`: protocol is the only study-specific model input.
- `protocol_crf`: protocol and blank/annotated CRF are model inputs.
- `confirmed_decisions`: protocol, optional CRF, and explicit human decisions are model inputs.

Requirements that cannot be inferred from the allowed input are labelled `proposed` or `needs_confirmation`; they must not be scored as hidden facts the model was expected to guess.

## Validation

Run the structural validator and the independently reproducible final-audit check:

```bash
python3 research/benchmark/tools/validate_benchmark.py
python3 research/benchmark/tools/finalize_initial_benchmark.py --check
python3 research/benchmark/tools/audit_initial_delivery.py
git diff --check -- research/benchmark
```

The validator checks references, hashes for locally present files, count consistency, candidate disjointness, annotation counts, final-audit coverage, and exact agreement between `keep_draft` rows and the delivered question set. Passing it does not replace statistical expert review.

To fetch a frozen public source by manifest ID and verify its hash:

```bash
python3 research/benchmark/tools/fetch_public_sources.py \
  --study-id PUBLIC-ORAL-IMMUNOTHERAPY-ADULT-001
```

## Important limitations and next gate

- The usable initial set has 66 drafts, below the historical 100-family frozen-release floor. No 40/20/40 frozen split is claimed.
- Twenty-one fully annotated studies remain quarantined until version binding or prospective provenance is independently resolved.
- Twenty selected targets fail the strict pre-primary/outcome-uninformed gate; their annotations are retained as audit artifacts but are not benchmark questions.
- Evidence locators and statistical decisions still require independent expert adjudication.
- English-language public studies dominate, and source availability favors completed trials.
- Source redistribution rights have not been established; the repository therefore distributes identifiers, URLs, hashes, and derived annotations rather than the public PDFs.

The next release gate is expert review of the 66 retained drafts, followed by evaluator calibration and family-level train/dev/test freezing. Reopening acquisition is a separate decision; the archived 13 metadata records do not silently reactivate.
