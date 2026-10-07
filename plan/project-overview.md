# Project overview

## Project

Evidence-constrained Statistical Analysis Plan (SAP) generation benchmark, post-training research, and private-deployment prototype for the graduation thesis.

## Current research claim boundary

- Completed: acquisition, first-pass evidence-backed annotation, terminal audit, and packaging of an initial 100-question draft benchmark.
- Not completed: statistical expert adjudication, evaluator calibration, frozen family-level split, SFT/DPO training, final experiments, human utility study, or offline deployment acceptance.
- The 100 questions remain `draft_needs_expert_review`; zero questions are expert-approved or frozen.

## Current benchmark facts (2026-10-07)

- 141 public study families have first-pass annotations, containing 2,589 requirements.
- Terminal disposition: 100 `keep_draft`, 21 `hold_version_or_provenance`, 20 `exclude_post_primary_or_execution_informed`.
- The retained 100 questions contain 1,771 requirements.
- One private pilot contains 26 requirements and is outside the public question set.
- Total requirements including the private pilot: 2,615.
- All 34 studies added to the prior 66-question baseline have exact-dated reference SAPs before actual study start. This statement does not automatically apply to all of the earlier 66.

## Deliverables

1. A versioned, auditable SAP-generation benchmark with source isolation and family-level leakage controls.
2. A calibrated hybrid evaluator combining deterministic checks, evidence-conditioned semantic judging, and expert adjudication.
3. A structured evidence/SAP-IR workflow and small-model SFT plus error-directed preference optimization.
4. Reproducible baseline, ablation, robustness, human-utility, and deployment experiments.
5. A private-deployment demonstration system and a thesis that reports both positive and negative findings honestly.

## Primary artifacts

- `research/benchmark/final_audit/initial_draft_question_set.json`: authoritative 100-question draft set.
- `research/benchmark/final_audit/questions.jsonl`: terminal disposition of all 141 public drafts.
- `research/docs/SAP_毕业设计研究方案_2026-10-07.md`: current complete thesis plan.
- `research/docs/HANDOFF.md`: repository handoff and exact continuation commands.

## Scope guardrails

- Reference SAPs are annotation/evaluation assets and must never be model-visible inputs.
- Study families, versions, chapters, derived instances, and preference pairs stay in one split.
- Benchmark construction completion must not be described as expert approval or experimental success.
- User-owned application changes are outside the current documentation commit.
