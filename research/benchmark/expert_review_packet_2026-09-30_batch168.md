# Expert Review Packet: Batch 168

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 168 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 1,050 one-based physical pages; text extraction recovered content from 1,047 pages. A total of 33 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT04270747 — exclude: SAP v2.0 dated 2022-05-26 precedes actual primary completion, but physical pages 2-3 document DMC-agreed ADA windows, alignment to the final AE CRF, COVID-19 disposition/deviation/exposure analyses, a model replacement for anticipated non-convergence, and regulator-driven estimand changes. The target is monitoring-, conduct-, CRF- and regulatory-informed.
- NCT05227677 — exclude: SAP Version 1.0 dated 2024-10-09 follows actual primary completion on 2024-08-31. Physical page 13 additionally identifies five individual participants and how protocol-ineligible or erroneous randomizations will be counted. The target is post-primary and realized-participant-informed.
- NCT03952559 — exclude: SAP Version 3 dated 2022-06-01 follows actual primary completion on 2022-04-24, while the selected public protocol is the later I4V-MC-JAIP(c) dated 2023-02-14 and the SAP identifies I4V-MC-JAIP(b) as governing. Physical page 8 also places Version 1 after production transfer for the first DMC meeting. The package is post-primary, governing-version-mismatched and monitoring-informed.
- NCT03484533 — exclude: SAP Version 1.0 dated 2021-10-08 identifies Protocol Version 3.1 dated 2019-03-17, while the selected public protocol is later Version 4.1 dated 2020-05-22. Physical page 17 prespecifies a subgroup using assessments before April 2020 specifically as pre-COVID-19 observations, after the pandemic had affected conduct. The target is governing-version-mismatched and COVID/conduct-informed.
- NCT05139030 — exclude: SAP Version 1.2 dated 2022-12-08 follows actual primary/study completion on 2022-07-11. The selected target is post-completion.
- NCT03971071 — exclude: SAP Amendment 1 v2.0 dated 2022-12-10 follows actual primary completion on 2022-12-01. Its physical pages 2-3 add observed-cohort sensitivity analyses, COVID-related deviations and post-COVID adverse-event summaries. The target is post-primary and conduct-informed.
- NCT01781429 — exclude: the Final SAP dated 2017-06-23 is a later-stage document: physical page 37 says the 2015 SAP was finalized for Part 1 and the current version was revised for Amendments 5-7 and Part 2 TFLs; physical page 28 plans analysis of the already-enrolled Part 1 cohort to support MTD/RP2D decisions. The target is dose-escalation- and accumulated-conduct-informed.
- NCT04181593 — exclude: SAP Version 1 dated 2020-11-05 predates actual completion but physical pages 9-11 increase randomized recruitment from 300 to 320 because subjects had already missed visits due to COVID-19, define handling for already delayed visits and COVID early terminations, and use a protocol whose physical page 36 calls back subjects who had already completed Day 84. The target is realized-retention- and COVID/conduct-informed.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT04270747 | monitoring/regulatory/conduct-informed target | 92 / 41 | `26c7b43bb7af1a0da1b81ee1a80fb4b287368ccf6c99a6cb61bc68e19f142229` | `5869659d936db14629349621a8d1604999ffe14322d120014ae1ad2957055fb8` |
| NCT05227677 | post-primary/realized-participant-informed target | 17 / 19 | `45fa611a3a14b86745bfbc8e969a248ad830b0058f9133f028e60071d91a0f48` | `ec400fcd259368291721b91cb9878b93f8b52714700393341dc4402ce23a3492` |
| NCT03952559 | post-primary/mismatched/monitoring-informed package | 169 / 94 | `888665b9e9798784054df725081e4c52c2e7f7990e448e5baf2863d5a0dd94f3` | `78094aad531f0ce44f6968482de9c610fb2cb389a256bf69e4e5aa2abaf1cdee` |
| NCT03484533 | governing-version mismatch and COVID/conduct-informed target | 45 / 19 | `87f5721b6cb7ed684ecc2b6a2ece72f01b5920196c4eeb947edfa5fecf88ece3` | `9a4b2fa13611db444595a9d5ff6ecd64bceba6be3fc2980b3a024769f546337d` |
| NCT05139030 | post-completion target | 69 / 43 | `25270ea9b29845e8074b97c888f0381b543bb27faa2183ccd2f238878367efa0` | `083d401ea872258e729592aa696e4a513e34ab512b387dcd62e6b94f18c823d5` |
| NCT03971071 | post-primary/conduct-informed target | 206 / 53 | `8e1bd894ce5e17f9a1778ace78ea05f15c0e1324c26a896ab47ae8c4df29d466` | `729970d0908725d787d82070e8b8720995d0455a3680a99fdd9dd3a57867ee57` |
| NCT01781429 | dose-escalation/accumulated-conduct-informed target | 73 / 38 | `95359ba1044c30e31b3c76d0601aee7dda9f9ab496a6470877c6a4f7854f9daf` | `28c8ed4c958594bd54edbb0733ff92856bdbda31b42ba2115397da892eefdce2` |
| NCT04181593 | realized-retention/COVID/conduct-informed target | 55 / 17 | `7bfab33a456c12b60ebf2eea6bf5c7bc44e0bb7f4031ca9a5fd3a8be297c8aa8` | `621f411c93e0eb80296d340653b152b0a2c7be2655453d7f8de5f32e4d6ec407` |

## Gate interpretation

- An SAP finalized after actual primary completion is not prospective even when the study continues long-term follow-up.
- Pre-primary chronology alone is insufficient when revisions explicitly respond to DMC decisions, final CRFs, COVID disruptions, participant-level deviations, realized retention or completed dose-escalation stages.
- A governing protocol version named by the SAP cannot be silently replaced with a later public amendment.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
