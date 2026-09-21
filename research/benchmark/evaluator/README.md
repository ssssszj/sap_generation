# Evaluator

The evaluator is deliberately separate from the generation-time rubric revision prompt in `lib/sap-generator.ts`.

`score_deterministic.py` implements only surface-verifiable checks. It returns `uncertain` for method adequacy, unresolved decisions, or other items that require semantic or human judgement. A later semantic judge must consume only the candidate passage, the relevant requirement, and the allowed evidence; it must not see a full reference SAP.

Before final testing, the semantic judge prompt, model, decoding settings, thresholds, and escalation policy must be frozen and calibrated against human labels.
