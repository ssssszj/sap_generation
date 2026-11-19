# Expert Review Packet: Batch 165

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 165 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 1,023 one-based physical pages; native text extraction recovered content from 934 pages, and full-page OCR recovered all 74 pages of the scan-only NCT04927247 protocol, yielding 1,008 pages with reviewable text. A total of 50 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT04103034 — exclude: SAP Final Version 3.0 dated 2020-09-17 follows actual primary/study completion on 2020-09-14. Physical page 21 also defines summaries for visits missed or not performed, dropouts, early terminations and protocol deviations due to realized COVID-19 effects. The target is post-completion and COVID/conduct-informed.
- NCT04998201 — exclude: SAP Version 2 dated 2023-09-08 follows actual primary completion on 2023-02-10 and study completion on 2023-08-14. The preceding Version 1 dated 2023-04-14 is itself post-primary-completion, so the public chain does not supply a prospective target.
- NCT03020199 — exclude: SAP Amendment 10 dated 2023-08-18 follows actual primary completion on 2021-11-30 and study completion on 2023-06-16. Physical pages 2 and 48-50 record repeated interim and CSR work, June 2023 early termination, and analyses added on the basis of Week 104 main-study results. The target is post-completion, outcome- and conduct-informed.
- NCT03450915 — exclude: SAP Version 2 dated 2020-07-08 follows actual primary completion on 2020-07-02. Physical pages 5-7 and 41 explicitly use a blinded review of Season 1 data to revise analyses and add endpoints and sensitivity analyses. The target is post-primary and blinded-data-informed.
- NCT04927247 — exclude: although SAP Version 1 dated 2023-08-10 precedes actual termination on 2023-11-24, physical page 11 states that the protocol-specified interim efficacy analysis will not be performed due to the early termination of the study. Protocol physical pages 55-57 also specify the ITT population, CMH primary analysis, missing-equals-failure handling, negative-binomial analysis, fixed testing hierarchy and O'Brien-Fleming/Lan-DeMets interim/final design, substantially reconstructing the target.
- NCT03841604 — exclude: SAP Version 1 dated 2021-01-25 precedes actual primary completion, but physical page 11 says a blinded review used primary-endpoint data from 26 completed participants as of June 2020 and observed SD 1.43 to revise the sample-size SD to 1.50, in the context of COVID-affected recruitment. The target is actual-data- and COVID/conduct-informed.
- NCT02107703 — exclude: SAP Version 4 dated 2016-07-08 precedes actual primary completion and states that it predates the first efficacy interim, but physical pages 8 and 11 encode a safety-driven dose change, approximately 180 participants already enrolled at 200 mg, and expansion of the target to approximately 630 participants. The target is accumulated-conduct- and realized-enrollment-informed.
- NCT04005352 — exclude: SAP Final Amendment 4 dated 2022-10-20 follows actual primary/study completion on 2022-09-09. Physical page 4 states that the amendment was created after the Week 32 interim database lock and records interim-, COVID- and emergency-safety-responsive changes. The target is post-completion, interim- and conduct-informed.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT04103034 | post-completion/COVID-informed target | 15 / 38 | `155d434f7ad9dcf466fc4c93b157adfffb253d1a6f3481fe5188ad16c554699b` | `d98182d25ac7a8ab016f329448a689dc874468ac70d6c3b610140abc5043f097` |
| NCT04998201 | post-primary/post-completion target chain | 77 / 35 | `3394e1c4020f57880153b30de1f213772db6b5e012e4016ef1f542ea6501ca66` | `3f53820d2c789db782caf4d923071a64ca7402bf6ec9cfcfbe189e14e27f0469` |
| NCT03020199 | post-completion/outcome/conduct-informed target | 83 / 70 | `a201fba895fa303a1af7cc0437c3ac0489f822c238a69c19d6b9456cf3262510` | `ee430acc97d869bec218aafb68f900ea72c262afdca15151e5e93e39d9c62408` |
| NCT03450915 | post-primary/blinded-data-informed target | 189 / 51 | `d12f8d7444a0b757a148ed140387c5106752d322dc32f6fec5578af70f43d789` | `eeff6703cefb91a538b2df8ad01250d194f0e1eb5494d2affd87988d875755b1` |
| NCT04927247 | termination-informed target and protocol leakage | 74 / 24 | `d528d5e6f0bd172b17cb781f51b2136fad979364a871b04db534f7e19c1fd560` | `94da33ec0596442219df9affae73ea0916cf6b6fc606a55292545c4345e54662` |
| NCT03841604 | actual-data/COVID-informed target | 66 / 32 | `a5abb936848294c393ec43cc4126dd29319c0f947eb994c33640435db1944875` | `d0e17bf233505ac2927c7fc0fe29762b2b865549f7aa77cc82cc8c0930460e6b` |
| NCT02107703 | accumulated-conduct/realized-enrollment-informed target | 104 / 34 | `4f59091ec0d2974f4506b5cfe2e680309293c2bbc9bb88ef897d46eb1ebc9085` | `6cb4ce41ddc39d410b276e223c7d726c1aad75a6a16f02ef4261d8ec65ec10aa` |
| NCT04005352 | post-completion/interim/conduct-informed target | 81 / 50 | `6e47ed2c371fd93a454d19418586830474ffd719b6ffb9400edbe8f9b72adb09` | `d5dbc976cd803515ed47f209e7413e6c6113025fb62a39e696ead864746112a3` |

## Gate interpretation

- A target finalized after actual primary or study completion is excluded even if it is labeled final and even when an earlier public version also postdates primary completion.
- A nominally pre-completion target is still unsuitable when it responds to early termination, realized enrollment, blinded aggregate endpoint data, interim results, safety-driven dose changes, COVID disruption or other accumulated conduct.
- Protocol leakage requires substantive reconstructability. NCT04927247 exposes populations, primary and secondary models, missing-data handling, hierarchy and alpha-spending design, not merely design or endpoint names.
- A statement that a document predates an efficacy interim does not cure earlier safety- or enrollment-informed changes.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
