# Expert Review Packet: ASCEND-D and SER-287

## Scope

This packet covers the first-pass annotations added on 2026-09-23:

- `PUBLIC-ASCENDD-001`: 22 requirements;
- `PUBLIC-SER287-001`: 18 requirements.

The annotations were created from the verified governing protocols. The reference SAPs were used only to identify discrepancies, missing operational detail, and possible hidden decisions. They were not treated as model-visible input for the `protocol_only` track.

## Requested review decision for every requirement

For each JSONL record, please record:

1. **Accept / edit / reject** the requirement.
2. Whether `applies` is correct for each listed track.
3. Whether the epistemic status is correct: `explicit`, `derivable`, `proposed`, or `needs_confirmation`.
4. Whether severity is correctly classified as `critical`, `major`, or `minor`.
5. Whether the evidence page and excerpt directly support the requirement.
6. Whether `acceptable_values` admit all statistically defensible protocol-faithful answers without admitting a material error.
7. Whether the requirement is independently scorable or should be split/merged.

Please preserve the raw first-pass record before adjudication so inter-annotator disagreement can be measured.

## ASCEND-D: priority adjudication items

- `R012`: Is the Hgb estimand accurately characterized as treatment policy for interruption/discontinuation, rescue ESA, and transfusion, with a hypothetical strategy for death before EP end?
- `R014`: Is it correct to require an explicit question for PP exclusions when the protocol defers the operational list to the RAP?
- `R017`: Which missing-Hgb details are indispensable for an executable SAP, and should omission be critical?
- `R018`: Does the gatekeeper plus Holm-Bonferroni wording correctly represent the familywise testing strategy?
- `R022`: Are RAP-level MACE censoring rules necessary for a critical pass, or should the protocol-level rule receive partial credit?

## SER-287: priority adjudication items

- `R007`: For protocol-only evaluation, should mITT remain required even though the later reference SAP deleted it?
- `R009`: Should the protocol's “complete remission” definition be scored as the only valid answer, or represented as an unresolved version conflict?
- `R013`: Are the named missing-data methods sufficient for partial credit without endpoint-level operational rules?
- `R018`: What minimum microbiome details make the primary analysis executable without the unavailable separate microbiome plan?
- Confirm whether the descriptive, non-conclusive nature of all comparisons is sufficiently emphasized across the rubric.

## Adjudication output

After review, update each requirement in place, increment `annotation_version`, change `status` in `annotation_status.json` to `expert_adjudicated` only when all critical items are resolved, and add an adjudication note summarizing disagreements and decisions. Do not promote either study to a frozen split before this is complete.
