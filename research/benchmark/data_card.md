# SAP Generation Benchmark Data Card v0.1

## Current composition

The working benchmark contains twenty-nine registered study families:

- one private Chinese ophthalmology medical-device study marked `pilot_only`;
- VIVID, a public randomized behavioral study with a binary primary outcome;
- IMPACT, a public observational cohort with an exact protocol/CRF/TSAP triplet;
- ASCEND-D, a public phase 3 active-controlled study with continuous and time-to-event co-primary non-inferiority endpoints;
- SER-287, a public randomized phase 1b study retained partly as a missing-document challenge.
- dasiglucagon in congenital hyperinsulinism, a public pediatric Phase 2/3 crossover study with an open-label extension;
- Blood Pressure Control in Hypertensive Smokers, a public two-phase behavioral study with an abstinence-conditioned three-arm randomized analysis.
- pediatric NAFLD dietary treatment, a two-site controlled-feeding trial with MRI-PDFF and repeated measures;
- NOTE endometriosis, a double-dummy active-controlled pilot centered on estimation rather than superiority claims;
- VRC01 during analytic treatment interruption, a small Phase II HIV trial with exact binary and time-to-event methods.
- REDUCE PFO, a multinational randomized device trial with simultaneous time-to-event and MRI binary co-primary endpoints;
- imsidolimab in generalized pustular psoriasis, a three-arm Phase 3 trial with an explicit estimand, fixed-sequence multiplicity, multiple imputation, and adaptive sample-size review.
- Anchor/W-SUDs, a remote randomized digital intervention trial with attrition weighting and arm-specific per-protocol adherence thresholds.
- RESTORE in cerebrotendinous xanthomatosis, a rare-disease adult crossover trial with a separate open-label pediatric cohort.
- Wellness Programs for Brain-Injured Individuals, a randomized behavioral pilot emphasizing feasibility thresholds and descriptive analysis.
- Transcriptomic Signatures of Influenza Vaccine Responses, a randomized older-adult vaccine study with laboratory blocking, CQN normalization, and high-dimensional exploratory analyses.
- the cinacalcet pediatric extension study, a single-arm safety study with parent-study combined analyses, iPTH missing-data sensitivity methods, and growth endpoints.
- Engensis for diabetic foot ulcers, an early-terminated Phase III randomized trial with exact primary testing, layered sensitivity populations, and longitudinal wound analyses.
- PEG bowel preparation renal safety, an auxiliary prospective observational study with serial creatinine, eGFR, and electrolyte assessments and several unresolved statistical decisions.
- targeted upper-extremity rehabilitation after stroke, a severity-stratified randomized trial with a protocol-to-SAP change from percent-change ANOVA to repeated-measures modeling;
- Biobehavioral Pathways Underlying Alcohol Use and Health, a nonrandomized two-cohort feasibility intervention with six operational feasibility thresholds;
- total-knee-arthroplasty NMES, a randomized mechanistic rehabilitation study with fiber-level, mitochondrial, and functional outcomes;
- pediatric iron-deficiency anemia treated with ferric carboxymaltose, a Phase III active-controlled study with documented protocol-to-SAP population, imputation, laboratory-grading, and subgroup changes.
- collaborative-care rehabilitation after dysvascular transtibial amputation, a sex-stratified randomized trial with a protocol-to-SAP switch to maximum-likelihood repeated measures;
- technology-enhanced diabetes coaching, whose randomized TEC-versus-peer-support comparison is kept distinct from its observational usual-care cohort;
- G-FLIP plus vitamin C in advanced pancreatic cancer, a single-arm Phase II study with randomized vitamin-C timing only for acute safety;
- computerized e-SBI for risky alcohol use among women of childbearing age, a developmental randomized trial with GEE, imputation, and explicitly post-hoc drink-size analyses;
- VM202 for painful diabetic peripheral neuropathy, a Phase III fixed-sequence trial with continuous and responder repeated-measures models and extensive missing-data sensitivity analyses;
- twice-weekly versus thrice-weekly hemodialysis, a randomized crossover equivalence study using KDQOL-36 and a -5 to +5 margin.

All twenty-eight public studies have first-pass annotations. Together with the private pilot, the registered set contains 508 evidence-backed requirements: 482 for the public studies and 26 for the private pilot. All public families remain unsplit until independent review and leakage checks are complete.

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

Public documents are therefore remote-only by default. The downloader verifies their frozen SHA-256 hashes after retrieval. A source being publicly downloadable is not treated as blanket permission to redistribute it in this repository.

## Known biases

- only twenty-eight public studies have first-pass gold annotations, with no completed expert adjudication;
- English-language public sources dominate the expansion set;
- the only current protocol/CRF pair is observational;
- unusually detailed protocol statistics;
- ophthalmology-specific endpoint and eye-handling rules;
- prior exposure during system development;
- reference SAPs may contain operational choices not inferable from the protocol;
- registry availability favors completed studies with results-reporting obligations.

## Planned v0.3 composition

The release-eligible intake contains 120 independent study families, of which 92 remain metadata-screened acquisition candidates and twenty-eight are version-verified annotation drafts. The frozen release floor is 100 independently adjudicated families, with a 40/20/40 train/dev/test split. The next annotation sprint should continue promoting design-diverse pairs while expert review proceeds independently on the existing drafts.
