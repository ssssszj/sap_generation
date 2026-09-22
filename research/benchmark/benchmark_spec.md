# SAP Generation Benchmark Specification v0.3-development

## Research question

Given the study documents allowed by a benchmark track, can a model produce an auditable SAP draft that is faithful to source facts, statistically executable, explicit about missing decisions, and internally consistent?

The benchmark evaluates decision quality rather than verbatim similarity to a reference SAP. A reference SAP is not assumed to be the only valid answer.

## Unit of independence

The independent unit is a study family. All protocol versions, SAP versions, CRFs, translations, generated outputs, synthetic variants, SFT examples, and preference pairs belonging to the same family must remain in one split.

## Primary scope

The primary benchmark covers these SAP components:

1. study objectives and design;
2. endpoints and analysis timepoints;
3. estimand attributes and intercurrent-event strategy when applicable;
4. analysis populations;
5. hypotheses, alpha allocation, and multiplicity;
6. primary and key secondary analysis methods;
7. missing data and sensitivity analysis;
8. visit windows and derivations;
9. safety analysis;
10. cross-section consistency and evidence traceability.

Cover formatting, table of contents, Word styling, and complete TFL shells are secondary tasks.

## Input tracks

### protocol_only

The model receives the protocol and versioned general guidance. The model must not receive the study's reference SAP, annotations derived only from that SAP, or human decisions that were not in the protocol.

### protocol_crf

The model receives the protocol and the matching blank or annotated CRF. Comparisons against `protocol_only` must use the same study subset.

### confirmed_decisions

The model additionally receives a structured record of human-confirmed decisions. Human effort and supplied fields must be reported separately.

## Required output package

Each run produces:

- the SAP draft;
- structured SAP-IR facts and decisions;
- evidence references used for material assertions;
- unresolved questions;
- model and decoding configuration;
- input hashes, prompt version, rubric version, token counts, latency, and failure state.

## Gold labels

Every gold requirement has one of four epistemic statuses:

- `explicit`: directly stated in allowed input;
- `derivable`: determinable by a frozen transformation rule;
- `proposed`: a method choice with more than one acceptable answer;
- `needs_confirmation`: not resolvable from allowed input.

Each requirement also records applicability, severity, acceptable values or conditions, and source evidence. `N/A` is distinct from pass.

## Evaluation

The primary metric is study-level critical pass rate: a study passes only if every applicable critical requirement passes and no critical unsupported assertion or contradiction is found.

Secondary metrics are:

- critical requirement pass rate;
- major requirement pass rate;
- key-fact precision and recall;
- required-content coverage;
- unsupported material assertion rate;
- cross-section contradiction count;
- evidence correctness and evidence coverage;
- statistical-method adequacy;
- missing-information handling;
- human revision time;
- model calls, tokens, latency, peak memory, and failure rate.

Lexical similarity, BLEU, ROUGE, BERTScore, and document-length ratio may be reported as diagnostics only. They are not primary quality metrics.

## Evaluator tiers

1. Deterministic rules evaluate schema validity, numbers, units, dates, identifiers, required terminology, and explicit contradictions.
2. A frozen semantic judge evaluates method adequacy and evidence-supported alternatives. It must emit `pass`, `fail`, or `uncertain`, evidence, and a reason.
3. Human review resolves uncertain and critical semantic items and is used to calibrate the automated evaluator.

Generation-time QA and benchmark evaluation are versioned separately. The final evaluator cannot be silently changed after final-test generation begins.

## Split and leakage policy

- The current ophthalmology case is `pilot_only`.
- Final test study families are selected before SFT and preference-data construction.
- Reference SAP text from dev/test studies is never included in retrieval indexes or training data.
- Test outputs are generated only after prompts, adapters, evaluator templates, and thresholds are frozen.
- Challenge variants inherit the source study's split and never count as additional independent studies.
- Newly collected public families remain in the `candidate` pool until version matching, source-rights review, annotation review, and leakage checks are complete.
- Public source PDFs are fetched by URL and verified against frozen SHA-256 hashes; reference SAPs are kept outside model-visible input directories.

## Versioning

Any change to task scope, rubric semantics, gold labels, model-visible inputs, evaluator prompts, thresholds, or aggregation rules requires a benchmark version bump and a changelog entry.

## Scale target

The release-eligible intake target is 120 independent public study families, with at least 100 retained after all release gates. The private pilot is development-only and does not count toward either number. At the 100-family floor, the intended split is 40 train, 20 dev, and 40 held-out test families; if all 120 pass, the stretch split is 60/20/40. A metadata-screened protocol/SAP pair is an acquisition candidate, not a benchmark-ready question; only independently adjudicated and split-ready families count toward the frozen release.
