# Expert Review Packet: Batch 131

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 131 queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,189 physical pages. Every page was text-extracted; 179 scan-only pages were OCRed, and 144 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT01475786 — exclude: the SAP follows actual primary completion, while protocol physical pages 49-51 expose the populations, endpoints and executable efficacy, safety and pharmacokinetic analyses.
- NCT02057198 — exclude: both selected documents are post-completion, and the three-page alleged SAP is written as a completed-analysis methods/report document.
- NCT02115139 — exclude: the alleged SAP is a Statistical Results Report containing observed populations, result tables and realized analyses; the protocol also exposes the executable program.
- NCT02689258 — exclude: the SAP follows primary and study completion, the multistage cohort design incorporates conduct-informed decisions, and protocol physical pages 63-66 expose the target methods.
- NCT02706717 — exclude: the SAP follows primary and study completion and records completed SMC review of interim safety reports; protocol physical pages 55-59 expose the executable target.
- NCT02924727 — exclude: the selected PDF mixes prospective and post-completion amendments, including conduct-informed re-estimation and analysis changes, while the protocol independently exposes the target.
- NCT03211858 — exclude: protocol Amendment 2 physical pages 7-9 and 83-90 substantially reconstruct the otherwise pre-primary SAP.
- NCT03897075 — exclude: SAP Version 2.0 follows primary completion and has an internally unclean effective-date/governing-amendment chain; both documents expose post-primary or executable analysis details.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT01475786 | post-primary + protocol leakage | 103 / 19 | `6cd8c5121f7004539e2230e582354b7e5fd92967ee72d31c5f8db97a6324fdd0` | `d05aafeb6b1e02043ee33191cf1f424f02e007b54e3555024958c64500cbc3f1` |
| NCT02057198 | post-completion wrong document type | 6 / 3 | `010e20fa05cdf269983fcf658d85ee803702449a59271ab60f104e7ae7793d78` | `8297ad996648367ecfc81f933df45000d2d954c0be34c7495d9448f788888db8` |
| NCT02115139 | results report + protocol leakage | 93 / 36 | `3b62600f6c26d334217335828cd6717701bf8c5160b6afeddcec7e51added737` | `735789cf89a7a10cbe1c283cc737a633dd00bbae9dc494226fba3571d41937f4` |
| NCT02689258 | post-completion + adaptive conduct + leakage | 89 / 43 | `eb99d861ab2b4cc621177b34d232c5b785ee561099053e2e5601422ff164308f` | `808291d8ecb63d081c41d8e11b8d859e76eb25635da6a606ae2f316d4277a2d8` |
| NCT02706717 | post-completion + interim conduct + leakage | 117 / 8 | `0e0bbf0b5e0207d0b68c7ff379f076153bfacdd4d1affd7e2bca95346dac55fa` | `5064350a4919c58e376657c2eefca40e868aaf172a1a9fed812a2aaec1a6a81d` |
| NCT02924727 | mixed-version conduct-informed bundle + leakage | 200 / 105 | `6a0cc29bbefb24c4aadb5f4eec3cca1b45e2518fec89648dbf374184d9f676a1` | `e80af6721cca7f45e0cc4de99c6798f06a06245dcc505e929bc83cc170379574` |
| NCT03211858 | protocol-embedded target leakage | 116 / 74 | `9d0c17032a86c0d1fef8df6bcf328bcd5da3fbaa2f3267ea886cf87f91cd975e` | `ebb24fa7c78e324552218d4d2504a2d8bd423c4d69b0b98cfcf319df0329d2ea` |
| NCT03897075 | post-primary + version-chain conflict + leakage | 115 / 62 | `9e671b7676175f1d7498b69df43dfd1f41828aed74199df9fefb6d3e56279497` | `78bb218c4a88e97f1f133cdf543715c8ad3a87627446e6ff7ed655c282d8a7eb` |

## Gate interpretation

- A SAP dated before primary completion did not rescue NCT03211858 because its model-visible protocol reconstructs the target analysis.
- A legacy effective-date footer did not establish prospective governance for NCT03897075 because the stated governing amendment and displayed SAP version postdate that footer and the final SAP postdates primary completion.
- A prospective section inside a mixed PDF was not separated from later conduct-informed amendments for NCT02924727; the selected public reference package as a whole is not a clean frozen target.
- Registry actual enrollment was used only to assess conduct chronology and was never substituted for a prospective sample-size target.

## Replenishment

All eight excluded slots were replenished from the official API. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates.
