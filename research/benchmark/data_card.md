# SAP Generation Benchmark Data Card v0.1

## Current composition

The current benchmark contains one Chinese ophthalmology medical-device study involving bilateral artificial intraocular lens implantation. It is a pipeline pilot, not a representative evaluation corpus.

The local study package contains a protocol, a CRF, an annotated CRF candidate, and a later reference SAP. The protocol and reference SAP versions are separated by time and must be treated as a version-matching risk until manually confirmed.

## Permitted use

The pilot may be used to:

- test document extraction and evidence locators;
- refine rubric applicability rules;
- debug baseline generation and scoring;
- build an initial error taxonomy;
- estimate annotation time.

It must not be used as a frozen final test case because it has already influenced prompts, hard gates, and implementation decisions in the existing system.

## Evidence locator policy

- Native PDFs use one-based page numbers plus a text excerpt.
- DOCX files use stable one-based paragraph IDs such as `p0406` plus a text excerpt.
- Table evidence uses table and row IDs emitted by the extraction tool.
- Page mapping for DOCX will be added only after a Chinese-capable deterministic renderer is available.

Local LibreOffice rendering was inspected during v0.1 construction and showed missing Chinese glyphs. This does not affect native DOCX text extraction, but it prevents trustworthy page-level citation from the rendered copy.

## Privacy and redistribution

The manifest records local paths and hashes but does not copy source clinical documents into the benchmark directory. Redistribution permission has not been established. A public release must contain only authorized files or source identifiers, URLs, hashes, schemas, and derived annotations permitted by the source terms.

## Known biases

- single disease area and device type;
- unusually detailed protocol statistics;
- ophthalmology-specific endpoint and eye-handling rules;
- Chinese language only in the pilot;
- prior exposure during system development;
- reference SAP may contain operational choices not inferable from the protocol.

## Planned v0.2 composition

The next release targets 10-15 independent study families spanning continuous, binary, and time-to-event endpoints; superiority and non-inferiority designs; and drug and device interventions. Three to five studies will receive full evidence-backed annotation before the rubric is frozen.
