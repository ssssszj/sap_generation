# Expert Review Packet - Batch 120

## Scope and decision boundary

Batch 120 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen selected official PDFs, eight official registry records and the additional earlier Cohort 1 SAP for NCT02128217 were downloaded sequentially and SHA-256 frozen. The selected pairs contain 2,122 physical PDF pages; the alternative SAP adds 17 pages. Native text was extracted page by page, all 39 empty-text pages were separately rendered and OCRed, and 99 decisive identity, chronology, version, analysis and leakage pages were rendered into 14 contact sheets and visually compared with the originals. Seven candidates are excluded and one is placed on governing-version hold. No Batch 120 candidate enters the registered benchmark.

## Decisions

- NCT02164578 — exclude: Protocol Version 6 physical pages 11-12 and 57-59 disclose the executable populations, endpoints, tests, alpha, power assumptions, sample sizes, missingness, interim and primary comparison program.
- NCT02896192 — exclude: Protocol Amendment 13 physical pages 12, 29 and 74 disclose the responder hypothesis, exact-binomial test, alpha, missing-as-nonresponse rule, power scenarios, endpoint and safety program. The SAP's outcome-access controls and prior-study variance inputs were checked and are not mislabeled as current-trial outcome use; protocol leakage is independently dispositive.
- NCT04090411 — exclude: SAP Version 3 is post-primary, the protocol amendment was altered for quicker-than-expected enrollment, and protocol pages 29 and 90-95 expose the executable estimand, missingness, populations, sample size, PK unblinding and interim program.
- NCT02576795 — exclude: the SAP cites Protocol Amendment 8, which is included in full inside the public 1,221-page bundle. Amendment 8 pages 280 and 368-370 expose the substantive descriptive/longitudinal, missingness, interim, population, sample-size, PD and safety program.
- NCT02880852 — exclude: the SAP cites the original 2016-01-26 protocol rather than public Amendment 1, but amended protocol pages 50-53 already expose the no-hypothesis, population, sample-size, all-data, no-interim, safety and PK/PD program.
- NCT02128217 — hold: the selected Cohort 2 SAP was prepared after all participants completed treatment and after primary completion; the public Version 2 protocol also exposes its analysis. The separately reviewed prospective Cohort 1 SAP governs missing Protocol Version 1, so no public prompt/reference pair is both prospective and version-aligned.
- NCT04844879 — exclude: the same-day Version 7 pair is post-primary, and the purported SAP is the statistical section of the protocol; the three-page prompt discloses the complete noninferiority/sample-size program.
- NCT04271046 — exclude: both documents are post-completion, and protocol pages 21-23 disclose the target, power, ITT, GEE, robust-error, covariate, inverse-probability-weighting and multiple-imputation program.

## Frozen file inventory

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT02164578 | protocol leakage | 96 / 37 | e74f544ef0a3095122dbd5fde22da8acb1e0bb6f2cf7cef8a5a50b89abb45bbd | baf4761901aab4caed24af81d23cb9c5232ba377f6637d2c35e94acc04e46525 |
| NCT02896192 | protocol leakage | 104 / 67 | 6743ac5328046a823c844b24d3ce9399ff13e607bd464403343cde0908acc8d1 | 62d338034b7e8c83d05a3852de43c039f0f45c353da8c77f8870ba467b256709 |
| NCT04090411 | post-primary, enrollment-informed amendment and leakage | 159 / 76 | 8a96ecae422785366ede328ce771e5069d930bc4992004a12da8a9bb1bc71ce2 | ff43ef355436d82778ef8d69044f381cc5c928ca98239a81739e863ec34d0c37 |
| NCT02576795 | governing Amendment 8 embedded in prompt bundle | 1,221 / 39 | 6f37857982cff279942351558fc0bf4e392de0b3a26b94bc76597503d8c91bc4 | 0dd5a7aac553dd70b7da317147af10f33b97e04d794fa58bdbcbe6d1371f82e9 |
| NCT02880852 | protocol leakage | 82 / 46 | ef462f57d81a227416caace1e1119e8e65db35ce47959bd3a93512fe989aa5de | ea00c840bdc73ee4a2e7791fc19a6b71754eff32eeb6f14658c7aed51b51f4c6 |
| NCT02128217 | governing-version hold | 138 / 16 | 05373defe916023fcbd64fb4c902d0f78ccf8b11910fad43a7fe5133cab55213 | 5ea71b1c193ca864832f6ef6a5fcd1a198ca891683822eb327d0d5c7bb0b403f |
| NCT04844879 | post-primary and non-independent SAP | 3 / 3 | 7058c7d0bc78b0d89797148379201ba9700bdf3048abaaf94adb140edf465062 | 7a0f9d04ed5412c7b1f6fbe1b972b4177e380d5151d5bd5020f748efc27d422d |
| NCT04271046 | post-completion and protocol leakage | 33 / 2 | 64c3f0500b404b6dcddf4dd4af2def9b9f314948f2b6c9ec80d729c621ebaad5 | 2c905cf02ab28ee32da4f999d3355a207d24e8c69216ea14a42bf88fc936faaa |

The alternative NCT02128217 Cohort 1 SAP Version 1.0 dated 2014-07-07 has 17 pages and SHA-256 `eae06a0c435c0fbcd3ccc5f8f14631d310607877b95ee496f13134b445c27106`. It explicitly cites Protocol Version 1.0 finalized 2014-01-02, which is not among the public registry documents.

## Review gate

No Batch 120 candidate is promoted. NCT02128217 may only be reconsidered if the complete Protocol Version 1.0 governing the prospective Cohort 1 SAP becomes publicly available and passes leakage review. All eight slots must be replenished from the official registry pool, preserving 101 public first-pass drafts plus 19 actionable metadata candidates.
