# SAP Generation Benchmark

This directory contains the research benchmark for evidence-grounded Statistical Analysis Plan generation.

The current working release is `v0.3-development`. It contains one private `pilot_only` study, forty-seven version-verified public study families, and a 73-study metadata-screened acquisition pool. The forty-seven eligible registered studies plus the candidate pool form a 120-family release intake; the pilot remains development-only and is not counted toward that target. All forty-eight registered studies now have first-pass evidence-backed annotations, totaling 820 requirements (794 public and 26 private-pilot requirements); every set still requires independent expert review. None of the public studies has been assigned to a frozen train/dev/test split yet.

## What is included

- A versioned task specification and data card.
- Study and document manifests with SHA-256 hashes.
- JSON Schemas for studies, documents, rubric items, gold requirements, predictions, and evaluation records.
- A general SAP rubric and an ophthalmology/IOL extension rubric.
- A first evidence-backed gold annotation set for the existing artificial intraocular lens study.
- Tools for stable DOCX paragraph extraction, benchmark validation, and deterministic scoring.
- A screened public-source catalog, source audit, and hash-verifying downloader.
- A reproducible ClinicalTrials.gov metadata harvester, a 120-family scale plan, and a 24-study document-review queue.

## Benchmark tracks

- `protocol_only`: Protocol is the only study-specific model input.
- `protocol_crf`: Protocol and blank/annotated CRF are model inputs.
- `confirmed_decisions`: Protocol, optional CRF, and explicitly recorded human decisions are model inputs. This is an application track, not the primary research track.

Reference SAPs are never model inputs. They are annotation aids only. Requirements that cannot be inferred from the allowed input must be labelled `proposed` or `needs_confirmation`; they cannot be treated as hidden facts the model was expected to guess.

## Quick start

Run all structural checks:

```bash
python3 research/benchmark/tools/validate_benchmark.py
```

Refresh the metadata-screened acquisition pool from the official ClinicalTrials.gov API:

```bash
python3 research/benchmark/tools/build_candidate_pool.py --target 73 --max-pages 6
```

This command does not verify protocol/SAP version compatibility. It only identifies separate public uploads and creates a stratified review queue.

Fetch a public study family and verify the frozen file hashes:

```bash
python3 research/benchmark/tools/fetch_public_sources.py \
  --study-id PUBLIC-VIVID-001
```

Extract stable paragraph IDs from a DOCX:

```bash
python3 research/benchmark/tools/extract_docx_blocks.py \
  input/1-人工晶状体临床试验方案-A0版-20210930.docx \
  --document-id doc-pilot-iol-protocol-a0
```

Score a candidate SAP text with the deterministic subset of the pilot gold requirements:

```bash
python3 research/benchmark/evaluator/score_deterministic.py \
  --requirements research/benchmark/gold/PILOT-IOL-001/requirements.jsonl \
  --candidate candidate.txt \
  --track protocol_only
```

The deterministic scorer does not replace statistical review. Items without a deterministic matcher return `uncertain` and are routed to a calibrated semantic judge or a human reviewer.

## Current limitations

- Only forty-seven public families have first-pass annotations, and none has completed independent expert adjudication; 73 additional records are acquisition candidates, not finished benchmark questions.
- The pilot study has already been used during product development, so it is excluded from final testing.
- Public source PDFs are remote-only by default. They must be fetched and hash-verified before generation or evidence review.
- Fetched protocol/CRF inputs and reference SAPs are stored in separate `input/` and `reference/` directories to reduce accidental leakage.
- IMPACT is observational and is scored as an auxiliary protocol/CRF case, not as part of the primary randomized-trial aggregate.
- DOCX evidence currently uses stable paragraph locators. Local LibreOffice rendering lacks the Chinese font mapping needed for trustworthy DOCX-to-page evidence mapping.
- The original `knowledge_bank/rubrics.json` remains a legacy generation/revision checklist. The benchmark rubric in this directory is independent and supports applicability and `N/A` decisions.

## Next release gates

- `v0.3 collection`: continue promoting the remaining queued studies through download, hashing, version-chain checks, extraction QA, and first-pass annotation until all 120 public families are registered.
- `v0.4 annotation`: reach at least 30 annotation drafts and 15 independently adjudicated studies.
- `v1.0 frozen`: retain at least 100 independent, split-ready study families from the 120-family intake; freeze train/dev/test by study family; run at least three baselines and publish evaluator calibration.

At the 100-family release floor, the intended split is 40 train / 20 dev / 40 test. If all 120 eligible families pass, the stretch split is 60 / 20 / 40. See `scale_plan.md` for the statistical rationale and annotation budget.
