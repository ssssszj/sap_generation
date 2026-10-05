# Benchmark Scale Plan: 120 Study Families

## Decision

The release-eligible collection target is 120 independent public study families. The private pilot is tracked separately and never counts toward this target. The intended frozen release contains 100 or more usable questions after version review, source-rights review, extraction QA, duplicate removal, and annotation adjudication. The 120-family intake target deliberately allows about 15-20% attrition.

**2026-10-02 closeout:** the user stopped acquisition after 107 public families had received complete first-pass annotations. The terminal audit retained 66 drafts, held 21, and excluded 20. The original 120-family intake and 100-family frozen-release floor were therefore not met. This document preserves the original scale rationale; the delivered initial set is explicitly smaller and not frozen.

A question is one study family with one allowed input package and one SAP-generation task. Alternative tracks, protocol amendments, translations, and synthetic variants do not increase the independent question count.

## Why 100+ is a reasonable graduation-project scale

- It is large enough to prevent a few hand-picked trials from dominating the aggregate result.
- A 100-study evaluation has a worst-case binomial standard error of about 5 percentage points for a pass rate. A 40-study held-out test has a worst-case standard error of about 8 percentage points, so effect sizes and paired confidence intervals must be reported.
- It supports meaningful stratification by design and endpoint type, but not strong claims for every therapeutic area. Ten domains with only 4-10 test studies each remain descriptive subgroup analyses.
- The main bottleneck is not source discovery. It is version matching and evidence-backed annotation. Therefore, collection size and annotation maturity are reported separately.

## Proposed split after all release gates pass

| Split | Families | Intended use |
|---|---:|---|
| train | 40 | SFT examples and evaluator-development material |
| dev | 20 | prompt, decoding, and post-training selection |
| test | 40 | one-time held-out comparison and ablations |
| total | 100 | minimum frozen release |

If more than 100 families pass, expand train to at most 60 while keeping dev/test at 20/40. If fewer than 100 pass, do not silently fill the gap with variants from the same study. Either collect replacements or publish a smaller, honestly labelled release.

## Maturity layers

1. **Metadata screened**: registry reports separate protocol and SAP uploads; basic study metadata are present.
2. **Pair verified**: files are downloaded and hashed; study identifiers and the exact protocol version cited inside the SAP agree; extraction is usable.
3. **Annotation draft**: study-specific evidence and gold requirements have a complete first pass.
4. **Adjudicated**: a second reviewer resolves disagreements and critical items; leakage review is complete.
5. **Split ready**: the study family is assigned once, with all derivatives kept in the same split.

Only layers 4-5 count as benchmark-ready questions. Metadata-screened records are an acquisition queue, not evidence that the benchmark already contains that many valid questions.

## Stratification targets

The final 100+ questions should cover at least:

- 12 broad therapeutic domains, with no single domain above 20%;
- drug, device, behavioral, procedure, and mixed interventions;
- continuous, binary, count/rate, ordinal, repeated-measure, and time-to-event endpoints;
- superiority, non-inferiority, and equivalence hypotheses;
- parallel, crossover, factorial, cluster-randomized, single-arm, and adaptive or group-sequential designs where public pairs are available;
- simple, medium, and high-complexity protocols;
- at least 15 protocol+CRF cases for the paired input-track analysis.

## Annotation budget

Full free-form expert review of 120 generated SAPs is too expensive for a graduation project. Use a tiered answer key:

- all split-ready studies: 10-20 critical/major evidence-backed requirements and deterministic key facts;
- all dev/test studies: complete semantic rubric adjudication;
- a calibration subset of at least 15 studies: duplicate independent annotation and revision-time measurement;
- train studies: structured SAP-IR and reference-assisted targets, with human review focused on critical statistical decisions.

This design keeps the benchmark large while concentrating scarce statistical review on the claims that determine whether post-training improved the model.
