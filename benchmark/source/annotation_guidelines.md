# SAP Benchmark Annotation Guidelines v0.1

## Annotation objective

Annotators identify what a candidate SAP must state, what evidence supports it, whether it is applicable, and how severe an error would be. They do not copy a reference SAP into the gold set.

## Source priority

1. Governing protocol and verified amendments.
2. Explicit, version-matched CRF collection structure.
3. Recorded human-confirmed decisions for the `confirmed_decisions` track only.
4. General guidance for method adequacy, never for inventing study facts.
5. Reference SAP as an annotation aid and discrepancy detector, not as unquestioned truth.

When sources conflict, preserve both statements, identify the conflict, and assign `needs_confirmation` until an authorized decision is available.

## Epistemic status

- `explicit`: directly supported by allowed source text.
- `derivable`: follows from a documented deterministic transformation, such as a unit conversion.
- `proposed`: one of several defensible method choices; the proposal must be conditional.
- `needs_confirmation`: the available input is insufficient or conflicting.

Annotators must not label a reference-SAP-only detail as `explicit` in the `protocol_only` track.

## Applicability

Mark `applies=false` only when the study design makes the item irrelevant. Omission by the candidate does not make a requirement inapplicable. For example, a missing non-inferiority analysis remains applicable when the protocol defines a non-inferiority primary endpoint.

## Severity

- `critical`: can change the clinical/statistical conclusion, primary estimand, analysis population, type-I error, primary missing-data handling, or cause a material unsupported assertion.
- `major`: materially reduces executability or reviewability but does not directly reverse the primary conclusion.
- `minor`: style, terminology, or presentation problem with low risk of changing analysis.

## Pass, fail, N/A, uncertain

- `pass`: the candidate satisfies the requirement with no material contradiction.
- `fail`: required content is wrong, missing, unsupported, or internally contradictory.
- `na`: the gold requirement is not applicable to this study or track.
- `uncertain`: available evidence or evaluator capability is insufficient; send to adjudication.

A correct statement does not compensate for a separate critical omission. Style points cannot offset a critical statistical error.

## Evidence annotation

Every explicit or derivable study-specific requirement needs:

- document ID and verified version;
- stable locator;
- minimal supporting excerpt;
- acceptable value or acceptable set;
- derivation rule if status is `derivable`.

Use one-based PDF pages. Use stable `pNNNN` paragraph IDs for DOCX until trustworthy page mapping is available.

## Reference SAP disagreements

If the reference SAP differs from the protocol:

1. do not silently adopt the reference SAP;
2. record the discrepancy;
3. determine whether a verified amendment or human decision explains it;
4. otherwise label it `needs_confirmation`;
5. exclude unresolved disputed items from automatic preference-pair generation.

## Double annotation and adjudication

At least a stratified subset of critical and major items must be independently annotated by two people. Record raw labels before discussion. Resolve disagreements through an adjudication note that states the evidence and final rationale.

Recommended pilot target: 100-200 double-labelled requirement decisions, intentionally including rare critical errors and reasonable alternative methods.
