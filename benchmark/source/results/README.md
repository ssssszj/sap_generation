# Results

`reference_sanity_protocol_only.json` is a scorer sanity check against the local reference SAP. It is not a model baseline and must not be included in model rankings.

The sanity check is expected to expose some failures because the benchmark is evidence- and decision-oriented rather than a reference-copying metric. In v0.1 it flags missing sensitivity-analysis confirmation, incomplete second-eye handling, and incomplete depth-of-focus derivation framing.

`legacy_sanity_summary.json` and `legacy_sanity/` contain deterministic diagnostics for historical outputs. Their prompts, exact inputs, and decoding configurations were not frozen, so these files are for error mining only and are not controlled baseline comparisons.
