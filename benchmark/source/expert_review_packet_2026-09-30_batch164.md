# Expert Review Packet: Batch 164

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 164 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 985 one-based physical pages; text extraction recovered content from 956 pages. A total of 60 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT04098172 — exclude: SAP Version AB dated 2020-02-25 follows Version AA dated 2019-12-18 and was finalized during conduct. Physical page 2 says it added endpoint analysis after the initial SAP release; physical page 5 says enrollment happened more quickly than anticipated and records the realized approximately 39-40 enrolled subjects. The selected target is realized-enrollment- and conduct-informed.
- NCT04965935 — exclude: the INFINITI Data Analysis Plan is dated 2025-03-07, after actual primary/study completion on 2024-08-30. Physical page 8 additionally says blood urea was not collected at Visit 4 and changes the analysis to the Visit 3-to-Visit 9 contrast. The target is post-completion and observed-data-informed.
- NCT01705977 — exclude: RAP Amendment Version 1 dated 2020-09-22 was created after the Week 52 double-blind period was unblinded on 2019-01-02, after Statistical Analysis Complete on 2019-02-07 and after multiple interim reporting efforts. Physical pages 5, 8, 10, 51 and 52 also document post-treatment database cuts and COVID-19 additions. The target is unblinded-, interim-, COVID- and execution-informed.
- NCT03446053 — exclude: SAP Version 1.0 dated 2019-12-04 follows actual primary/study completion on 2019-02-07; even the selected Protocol Version 2.0 dated 2019-05-17 is post-completion. No prospective public protocol/SAP package exists in the selected chain.
- NCT04888585 — exclude: Protocol Version 2 physical pages 38-41 already specify the ITT and safety populations, final analysis timing, CMH primary analysis, NRI-MI for categorical endpoints, MMRM for continuous endpoints, covariates, MCP-Mod dose-response analysis, subgroup analyses, safety summaries, multiplicity policy and sample-size assumptions. This substantially reconstructs the target. The protocol change appendix on physical pages 60-64 also says the ITT and intercurrent-event rules were changed to align with prior trials, removes a substudy because enough subjects could not be enrolled and permits fewer kits after unblinding.
- NCT03815916 — exclude: SAP Final Version 1 dated 2021-05-19 was finalized during conduct shortly before actual completion on 2021-06-07. Physical pages 8, 10, 13 and 18 explicitly adapt treatment duration, per-protocol eligibility, primary-endpoint timing and compliance to realized COVID-19 restrictions and delayed Week 12 scans; physical page 3 records sponsor-comment revisions. The target is COVID- and conduct-informed.
- NCT02101021 — exclude: SAP Final Analysis Version 1.0 dated 2017-07-10 follows actual primary/study completion on 2017-04-10. Its empty revision table does not establish an earlier prospective SAP. The target is post-completion.
- NCT03956225 — exclude: SAP Approved Version 3.0 dated 2020-11-09 follows actual primary/study completion on 2020-10-24. Physical page 19 describes it as the second revision based on Protocol Version 3.0, while material revision details are publicly redacted. The selected target is post-completion and lacks a prospective, reviewable finalization chain.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT04098172 | realized-enrollment/conduct-informed target | 64 / 18 | `23ebf97afb74c10a10008f07a9a6ec0dbbe41b3025c6af852705a2555f139159` | `ad0b8cbe56ff4f677c95b73c6ed4214108a62785bfe85d00ba4f3da57b195664` |
| NCT04965935 | post-completion/observed-data-informed target | 51 / 8 | `1a02511d65d7c99e7cc7e314e912bd40baf86893701a6956c652489c85e57acb` | `36eac404d0b9f4a0ae4f78e008068d635bd9764ee7d2b4b76db479c1abf6e930` |
| NCT01705977 | unblinded/interim/COVID-informed target | 114 / 122 | `1b4927ba4855456b33335c7d00fd071d712ee0ee867a06bad44929c6062ebc9e` | `79078d86c7a1baf6c103167a5fdb8e80270bfec275b93def0dea90b942d443d0` |
| NCT03446053 | post-completion package | 61 / 32 | `38996dced9788ab0bed439f5c5729ae69fbac4cb9ffe0400da3e4c6c003c793c` | `bbe51d97fae17f9ab7fd55292ef596d69cf8dc21c4494382dc841555281a96f6` |
| NCT04888585 | protocol leakage and conduct-informed package | 71 / 62 | `65d1e0f65f9534698ddd46f40fc86d972521f031b2cbeff48dbf56868c26f386` | `336bd066b7aaf0cc1b4ae0d2467ded918ca87c593f25803979e50ca4367ee344` |
| NCT03815916 | COVID/conduct-informed target | 136 / 21 | `d45921febb25b832f19109463c25d80be00c988ec6a47cb2b32cd753f381345e` | `d97885b8bbce7e8aedab8af5c7f8e1f298fdfcb13e93e7aa0ee418bd7839ef34` |
| NCT02101021 | post-completion target | 94 / 39 | `635ddf1c89b9abb7228c0eecdf8715165f0600021fa5dd29622aa741e30bd932` | `9e1bcf10b8f79b22ecde8639f7e7ec21a47ae9865f0dd28080582161d70d3321` |
| NCT03956225 | post-completion/redacted revision chain | 68 / 24 | `2de39aac076a1ac1c62129bf2b682edb0abd547686acf70eb7d0a50ab9e8ca8a` | `9544f29135204970e3de9871d06529d004577b2b89e5985422e7a219e0e9414d` |

## Gate interpretation

- A target finalized after actual primary completion is excluded even when its public revision table is empty or the document is labeled final.
- A target finalized before completion is still unsuitable when it records realized enrollment, missed collections, delayed visits, COVID restrictions, sponsor review or execution-responsive population and endpoint rules.
- Protocol leakage requires substantive reconstructability. NCT04888585 exposes the populations, tests and models, covariates, missing-data methods, dose-response work, subgroups, multiplicity and sample-size assumptions, not merely the design or endpoint names.
- A later protocol cannot supply a prospective chain when both protocol and SAP postdate completion.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
