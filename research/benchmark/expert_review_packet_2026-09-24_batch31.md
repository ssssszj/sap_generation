# Expert Review Packet — Batch 31

Batch 31 promoted one public study and rejected seven source pairs. All 16 source PDFs were obtained from ClinicalTrials.gov, hashed, page-counted and text-extracted. Covers and decision-defining pages were visually rendered; all five pages of the promoted protocol/SAP pair were inspected.

## Promoted study

### PUBLIC-NEUROPILATES-STROKE-001 / NCT04491279

- Version evidence: the independent three-page protocol and two-page SAP have the exact title and creation date of 2020-08-04, before study start on 2020-10-30. Both retain an unassigned NCT placeholder because they were created shortly after registry submission and before the public posting. Exact title, sponsor and intervention establish the study identity.
- Leakage check: protocol physical pages 1-3 describe the design, intervention and outcomes but contain no executable primary model, analysis population, missing-data, multiplicity, alpha or sample-size plan.
- Reference-only decision: SAP physical page 2 specifies Excel/SPSS and separate within-group before-after paired t tests. This is recorded only on the `confirmed_decisions` track and is not treated as an adequate randomized treatment-effect analysis.
- Critical endpoint conflict: protocol physical page 3 labels both Timed Up and Go and Motor Assessment Scale as primary; the registry lists only Motor Assessment Scale as primary and Timed Up and Go as secondary. Requirement R007 forces explicit reconciliation.
- Critical analysis gap: the randomized between-group contrast, repeated-measures handling through three months, populations, missing data, multiplicity and prospective sample-size rationale all remain `needs_confirmation`.
- Annotation: 22 evidence-backed requirements; status `draft_needs_expert_review`.

## Screening decisions

- NCT03897465: `excluded_wrong_document_type`. The protocol is the SLALOM Lomatuell Pro versus UrgoTul study, while the purported SAP belongs to a different Suprasorb C post-market study and records observed protocol deviations.
- NCT03191396: `excluded_wrong_document_type`. The public files are CSR appendix packages and the embedded SAP postdates both primary and study completion.
- NCT02340819: `excluded_wrong_document_type`. SAP Version 2 says it incorporates Stage 4 data for the final CSR and follows an interim analysis.
- NCT04173494: `excluded_wrong_document_type`. The SAP postdates actual primary completion.
- NCT03334396: `excluded_wrong_document_type`. The post-primary SAP is a database-lock-era update with analysis changes and a random seed.
- NCT02412436: `excluded_wrong_document_type`. Both available public SAP versions postdate actual primary and study completion.
- NCT07795203: `excluded_wrong_document_type`. The SAP-slot upload is an ethics/project application rather than an SAP; the protocol also exposes an executable statistical plan.

## Source audit

The source PDFs remain local, gitignored screening artifacts. Reference SAPs are annotation aids only and must never be passed to the generation model.

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT04491279 | promoted | 3 / 2 | a49ddcc704000c98b817ae2b199e854abb995bc5b63ca2904d380a3c16a48639 | 4b19489776af34613fd00001e6313e1c79ee6424943aec1538dea00d91b054f3 |
| NCT03897465 | mismatched SAP | 48 / 23 | 1a584c7e3e61cfe7375f88af0704df827a9d84010c21a8e0e95ba21b8f3814cf | bc05decb6f85bfd13673b978824135359c77ebea8e4ee3e39d50117b22b1a0d1 |
| NCT03191396 | post-completion CSR appendix | 140 / 25 | 07b11bce2a077253af43b99b3a455c86bdc66aa1f389fddb9cf9fd71c8f3e396 | 8a0078ffa692bf975fe278e198590b06917a4b3e939de80d682d79a09de7b4cb |
| NCT02340819 | execution-informed final-CSR SAP | 439 / 35 | e1b04c8a634f469d8312be8c972305a79ead3c09432100c99a3a54ecfbc3e76f | 847a870bfe72e71c3e39fdb4ae50e2ac812636079b33a8ad29af0cab9b421d86 |
| NCT04173494 | post-primary SAP | 140 / 56 | db8cf5a2535a811862611624d7aab99b27f553ad510f99c9f3bc9884c47be22f | 49632cd6530c17c7bbe55fbf61f8cb281fe7a63b497947c283a6a82e6e4ebcb9 |
| NCT03334396 | post-primary database-lock update | 104 / 80 | 606f69293e506297e693369db3610987d4aa37c5c08f3e409353f1017e805b6f | 90495c8928fe23a14678cfe6f852c9937629b730fd100032433ad50f5a2e7324 |
| NCT02412436 | post-completion SAP | 75 / 16 | b78381c8d089601b5ee66f72ad24f7676910cc6c7e2de516a7162dc8c67e2170 | d9d8148663782d8c1750282c63204ac7a0dbc6acea3281ce49672c3fa6b29b20 |
| NCT07795203 | non-SAP ethics application | 17 / 2 | 499f1b256f373f70c7cf579cf940762cf226cd6ff90ee16f0f88dc782ac5b3f2 | 944029fe57fe7c70e13bdba61845058f1c2347748f83fc6afa2edf81b46d71dd |
