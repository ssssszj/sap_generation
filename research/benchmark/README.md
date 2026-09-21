# SAP Generation Benchmark

This directory contains the research benchmark for evidence-grounded Statistical Analysis Plan generation.

The current release is `v0.1-pilot`. It is intentionally small: one previously used ophthalmology device study is registered as `pilot_only`. It may be used to debug schemas, evaluators, prompts, and baseline runners, but it must not enter the frozen final test set.

## What is included

- A versioned task specification and data card.
- Study and document manifests with SHA-256 hashes.
- JSON Schemas for studies, documents, rubric items, gold requirements, predictions, and evaluation records.
- A general SAP rubric and an ophthalmology/IOL extension rubric.
- A first evidence-backed gold annotation set for the existing artificial intraocular lens study.
- Tools for stable DOCX paragraph extraction, benchmark validation, and deterministic scoring.

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

- The pilot contains one study family and cannot support generalization claims.
- The pilot study has already been used during product development, so it is excluded from final testing.
- DOCX evidence currently uses stable paragraph locators. Local LibreOffice rendering lacks the Chinese font mapping needed for trustworthy DOCX-to-page evidence mapping.
- The original `knowledge_bank/rubrics.json` remains a legacy generation/revision checklist. The benchmark rubric in this directory is independent and supports applicability and `N/A` decisions.

## Next release gate

`v0.2` requires 10-15 independently verified study families, 3-5 fully annotated studies, 150-250 evidence-backed requirements, at least three baseline runs, and an evaluator calibration report.
