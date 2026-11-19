# Expert Review Packet: Batch 172

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 172 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 714 one-based physical pages; native text extraction recovered content from 690 pages, and all four scan-only SAP pages for NCT02196922 were OCRed. A total of 54 decisive physical pages were rendered and visually inspected in eight contact sheets. One candidate was promoted to a first-pass draft, six were excluded and one was held. The promotion remains draft_needs_expert_review and is not expert-approved or frozen.

## Promotions

- NCT01822353 -> PUBLIC-ORAL-IMMUNOTHERAPY-ADULT-001: the separate four-page protocol and two-page SAP print the exact title, NCT and 2012-10-19 date, before the month-level January 2013 actual start. The protocol defines prospective oral immunotherapy, egg/milk/nut cohorts, challenge and one-year pulmonary/immunologic assessments without disclosing the reference-only Wilcoxon, chi-square, t/Mann-Whitney or SPSS choices. Twenty-two atomic requirements retain unresolved endpoint hierarchy, desensitization success, populations, estimands, derivations, missingness, multiplicity and safety. The protocol ceiling is 90; registry actual enrollment 23 is conduct context only.

## Hold

- NCT02597673 — hold: the separate eight-page protocol and two-page SAP print the exact title, NCT and 2015-07-16 date, but the registry records actual start only as July 2015. Day-level ordering against first enrollment cannot be established, and neither selected PDF supplies an approval signature or other evidence proving pre-enrollment governance. It must remain outside the registered benchmark until that chronology is independently resolved.

## Exclusions

- NCT02730377 — exclude: protocol and SAP are dated 2020-01-14, after actual primary completion on 2019-08-05 and completion on 2019-08-12.
- NCT02585960 — exclude: SAP Version 3.0 dated 2018-09-19 follows actual primary and study completion on 2018-08-05.
- NCT02196922 — exclude: the scan-only four-page document labeled SAP uses retrospective executed-analysis wording and largely reproduces the protocol's methods rather than supplying an independent prospective hidden target.
- NCT02198794 — exclude: SAP dated 2019-12-03 reports realized N=143 randomized and two already conducted interim analyses, including a 2018-12-01 cutoff; the protocol additionally contains extensive executable analysis detail.
- NCT03261193 — exclude: protocol physical pages 19 and 24 already reproduce the two-page SAP's tests, Bonferroni rule, Cox model, censoring, alpha and sample-size calculation.
- NCT01314911 — exclude: the SAP and protocol state that efficacy results from the first 50 pilot subjects selected the primary endpoint and drove sample-size re-estimation; those subjects are then excluded from the primary analysis. The target is pilot/outcome-informed and protocol-leaked.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT01822353 | first-pass promotion | 4 / 2 | 1ac014f11a6a273c904eb88ae32e6615c838d0b52aec20b1d0261df48863337d | ae78ca644f5d02f26300cef85d5043a74b75c9ea025d14d1a508c24c7ee52056 |
| NCT02597673 | prospective-governance hold | 8 / 2 | f1ea37ef66b118156babc65e52df2a9875f1ab789e2baf7e4dc09fe5829918fe | a105e3fb41d6afcd31f685eebe8df29fc219e7db4b365d684e97c96a751bef1c |
| NCT02730377 | post-completion target | 79 / 44 | 4a524a5b13a68f65a3e884a01f3f1082e08c7c47e0479f50c3e5f7632db24ad0 | 1eebdd55e86a2656c8877976f705b7cfe97c4e03a377b182bab63f933b62557b |
| NCT02585960 | post-completion target | 122 / 83 | ac77544ce3f7e213ef0163b94d828a7df1a1b6132f1ed7cdff1e714ba685e1c6 | 63f9958b1af0e0a3c87cce86f422448d6d692760d82d20595287e4a706a3ee28 |
| NCT02196922 | executed/wrong document type | 16 / 4 | acc3476ed3ba8e0197fe42122da5dd564c1c8910adac78e62e9976badbce6b3a | 77d5571f0e86f4751d0ff432b44f378b1b4658863efb76f36dc7eba23f3c0a29 |
| NCT02198794 | conduct/interim-informed | 194 / 41 | bee9fd80f11c9eb45cf052515d9b0b302dd34bd603a8b052e96fabf48ffcdbd7 | ad3c1a2fff26c09252eb4bf9455c4bc6d4a1337e31f96545137ecc2ffcdd7bec |
| NCT03261193 | executable protocol leakage | 43 / 2 | d8c000421baab61364cc61a0c226ccbbbba72f77e223fe52a1fef467b679b2cf | 0ae140c01703a5d3344b182d6eb0d4543e06f663a6ce6127a9ef048ba1aac862 |
| NCT01314911 | pilot/outcome-informed and leaked | 53 / 17 | a0b7b3c95ad9e0b40c985c1905bc15005b048b796f70dcca2010a6dfd05ced71 | d9e2c44135b735a696ed7d88f543b61afb21de52c86ef78be9d3d7ed4822a961 |

## Gate interpretation

- Exact identity and document dates support pairing, but a day within a month-only registry start cannot be assumed to precede enrollment; this remains an explicit governance question for NCT02597673.
- A concise protocol may state design, endpoints and prospective sample size without disqualifying leakage when the reference-only analysis choices remain hidden.
- Realized enrollment, completed interim analyses, pilot-derived endpoint selection and post-completion dates are execution or outcome information and invalidate the reference target.
- Registry actual enrollment was never substituted for the prospective sample-size target.

## Replenishment

The six exclusions and one hold are removed from the actionable pool, and the promoted family becomes a registered public draft. Thirteen actionable slots are replenished from the official ClinicalTrials.gov API. Release-eligible intake remains 120: 107 public first-pass drafts and 13 actionable metadata candidates. The registered requirement total increases by 22 to 2,092, including 2,066 public and 26 private-pilot requirements.
