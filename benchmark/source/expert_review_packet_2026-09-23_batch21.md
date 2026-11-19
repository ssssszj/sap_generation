# Expert Review Packet — Batch 21

Batch 21 promoted one version-verified study and rejected seven pairs at the source-admissibility gate.

## Promoted study

### PUBLIC-HF-MEDS-TO-BEDS-001 / NCT03402750

- Study: *Heart Failure Medication Adherence*.
- Version chain: the independent six-page protocol Version 6 and four-page SAP Version 1 share the exact study identity, NCT03402750 and 2018-07-19 date; both precede the 2019-04-08 primary completion.
- Leakage check: the protocol defines the pilot design, planned sample, measures and follow-up but gives no executable statistical methods, alpha, multiplicity or success hierarchy.
- Annotation: 24 atomic evidence-backed requirements cover the two randomized discharge-medication conditions, planned n=60, baseline/30-day assessments, 60-day record window, adherence, physical health, readmission, death, feasibility, acceptability, mechanisms and analysis choices.
- Review focus: adjudicate medication-possession-ratio derivation; correct the reference plan's questionable assumption diagnostics and generic chi-square fallback; complete allocation, population, missingness, multiplicity, effect-reporting and safety decisions.

## Rejected pairs

- NCT03124381: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 33-34 already expose the primary endpoint, sequential noninferiority/superiority gate, 15-point margin, alpha/FWER rule, ANCOVA and LOCF.
- NCT03378635: `excluded_wrong_document_type`. Both uploads are embedded in a 2019 Clinical Trial Report; SAP Final 1 is dated after 2018 primary and study completion.
- NCT02914561: `excluded_wrong_document_type`. SAP Final Version 2.0 is dated after primary/study completion and targets the CSR final analysis after earlier DMC/end-of-induction analyses.
- NCT03061201: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 47-49 already expose the populations, descriptive primary/secondary analysis and interim/DMC plan; the SAP also records extensive execution-stage revisions.
- NCT02975336: `excluded_wrong_document_type`. IAP Version 4.0 explicitly says it was updated because of study termination and changes post-primary analyses and long-term-extension content.
- NCT07573423: `excluded_wrong_document_type`. The alleged 2020 protocol uses completed-study language, cites a 2025-accessed source and has inconsistent completion dates; the SAP says enrollment was complete.
- NCT01921387: `excluded_combined_protocol_sap_leakage`. The alleged two-page SAP is copied verbatim from protocol physical pages 32-34, which already contain the complete statistical plan.

## Source audit

All 16 PDFs were downloaded from ClinicalTrials.gov, hashed, page-counted and extracted by one-based physical page. The promoted pair's cover and substantive pages and every exclusion-defining page were visually inspected. Reference SAPs remain annotation-only artifacts under the gitignored source tree.

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT03402750 | promoted | 6 / 4 | `5ea45a19a7f72b47e1d087267eb82b3038e09a3f6355ca792d25a82d2bc281d2` | `6206601c79e6beb392c71f6af0280216a24218ef29d9dda25e66bb801592caf5` |
| NCT03124381 | protocol leakage | 73 / 32 | `daeadd71b197329afc0dfdeb519a82097e8a6acaa7aee54ece418a3fc9717c01` | `80a12cf5495b411b1d5ea787d515736837d2f84f1d2433c52420f8538d042fd1` |
| NCT03378635 | wrong document type | 404 / 38 | `da9ebbb0453a2050ccbc59340725718189dee262ebc5cdebaa95373766981d64` | `de9b94ce2b42ebd2facd183df8125a491e6748012175ef8824b6e9de69214ff4` |
| NCT02914561 | wrong document type | 161 / 255 | `a12e288d3a9e67b8a8d4bfe5c78d458fdd98d4d5b77d98ab65e4b8ac5687f9c2` | `624cba653b5eaf8f6d4ba9c8693d1e21e52d98bfb483e03bc2835623b5b4dd92` |
| NCT03061201 | protocol leakage | 87 / 34 | `715ec4c68637a66212c696f715c70d5869384717d415d2e495e17fa7f6b08447` | `7dcc13011759cecf4c61fc569f235926838d9a80d237ae54b5e379a717c9faba` |
| NCT02975336 | wrong document type | 205 / 198 | `f52c14fbbb2de815e0193632805beea8c66e8e8d2cb1232bc82c6f90078efdb3` | `5334aa3954c5acccbd687db7244cf247cb6b113931a8b5372bfa163e675837a7` |
| NCT07573423 | wrong document type | 5 / 4 | `3535cb5bb574393e17dbb59f583c20d63282537ea1f382ab2febbfe92b0b0d6c` | `ab6e5f9f2737f7416e673429cd4f432987f32666f03dc704d007334bed8af063` |
| NCT01921387 | protocol leakage | 48 / 2 | `e919578c636cddc1f6043466a8b0b2c4fed91e559f0b89b52381eec9507ddfb7` | `c798f6e928ac345832d188733fb30f434eaeb4de261d11c603a12f377e62a22a` |
