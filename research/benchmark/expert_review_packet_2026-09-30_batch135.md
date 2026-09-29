# Expert Review Packet: Batch 135

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 135 review-queue head were reviewed against the prospective-version, protocol-leakage, study-family and source-quality gates. The 16 PDFs contain 1,052 physical pages. Every page was text-extracted; the 122-page NCT03332771 protocol and 32-page NCT02863575 SAP were fully OCRed. A total of 117 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded and none survived promotion. This remains first-pass work requiring independent expert review.

## Decisions

- NCT02979587 — exclude: SAP Version 5.1 is post-primary and records additions and snapshot-specific handling of TPV 25/mTPV 25 cohorts, pooling with a separate Native study and a new efficacy criterion not explicit in the protocol.
- NCT03332771 — exclude: SAP Version 3 is post-completion and explicitly post-database-lock; the OCR-verified protocol also exposes the executable population, MMRM, testing, missingness and multiplicity program.
- NCT02497469 — exclude: the SAP is post-primary and binds to unavailable Protocol Amendment 7 rather than the selected original protocol; the selected protocol independently exposes a substantial executable plan.
- NCT04211389 — exclude: the SAP is post-completion, cites an unavailable later amendment and incorporates COVID-19 conduct and modified populations; the selected protocol also exposes the executable plan.
- NCT02729038 — exclude: the protocol substantially reconstructs the prospective RAP through exact analysis populations, ANOVA, regression, confidence-interval and safety/exploratory programs.
- NCT02863575 — exclude: the protocol reproduces the SAP's sample size, populations, ANCOVA, survival analyses, derivations, time windows and missing-data rules; the scan-only SAP was fully OCRed to verify the duplication.
- NCT02124564 — exclude: Final SAP Amendments 1 and 2 were made after a Dry Run and Data Evaluation Meeting, adding actual-enrollment status and new analyses; the protocol independently exposes much of the target.
- NCT06072833 — exclude: the protocol states that 18 people had already been screened and six positive-screen AYAs received the intervention during beta testing, with learned procedures carried into the full pilot and its one-page SAP.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02979587 | post-primary, family-dependent and execution-informed | 174 / 24 | `50698e2f51002db8e3d77d143f0bf4c60e34735e32b04553a24c9b72555a34be` | `67468812a4fcaeb1926b5f025911b2596c90e3acadc88f7a1e68f17a3c636914` |
| NCT03332771 | post-completion/post-lock target plus protocol leakage | 122 / 96 | `0d6bc339eac7aa9ab18a3f5fd0bb871aa5c68e05075770b0cc887234cb400126` | `ac3d7dede3dd79195e9519c1299f75eeddf354fca0653051f980b3bdd77862c7` |
| NCT02497469 | post-primary/version-mismatched target plus leakage | 84 / 53 | `a1fa643c6a61eec0b43f5d3e97933ec6f35022ebe92cf5b1986bfb9bf1c6fb47` | `ec28ed91032d0fb5635ef448b664c018faddd67954f96c2bca453f40536bb5d4` |
| NCT04211389 | post-completion/version-mismatched and COVID-informed target plus leakage | 88 / 42 | `a3c47f095abc3a91040220351e17b56377fbdc7a04476e4b2743c0fa4ee605d5` | `01ba03675616a04de38c78c260bebd4beafe20114a69d5fd8fd6d7a4ed7331ab` |
| NCT02729038 | protocol-embedded target leakage | 85 / 59 | `01b3e3b9a30c96a1b0276fe2ed53461d3a36e7854965563106dbcbc923570a98` | `2585a77d2602f598ce146158e308a7cbbb09c014afe78ac8bd5b5d6ecc046879` |
| NCT02863575 | protocol-embedded target leakage | 68 / 32 | `87c5cc8f5dd324e63fafdad7d1c1aed3faaa88d0a774219f400af96d24b13017` | `c1f3b0a68b5914606af9ddeed2b89f0459ca5358b552297c5c962292a1a77021` |
| NCT02124564 | dry-run/data-evaluation-informed target plus leakage | 66 / 47 | `10462a6b50559be1ea244c5ae1d11cc6986dac4404c640f8e109078214bb1352` | `2e8ed97b3250a49c6d9673ac33808173554a688e6737b7c35608d5740caa7615` |
| NCT06072833 | beta-stage execution-informed target | 11 / 1 | `8482343d15f214bbfedf593411c0045489c09251e75c50645ecc59376c714782` | `0319317a9639740d68e15b807ce9b72e2c76010d342fd8ce110157ffc4675242` |

## Gate interpretation

- A SAP signed after primary completion or after database lock is not rescued by calling its methods prospective; NCT02979587, NCT03332771, NCT02497469 and NCT04211389 fail the chronology gate.
- A selected public protocol cannot stand in for a later amendment cited by the SAP. NCT02497469 and NCT04211389 therefore also fail governing-version reconciliation.
- Protocol disclosure of design, endpoints or sample size alone is permitted, but NCT02729038 and NCT02863575 disclose the analysis populations, models, contrasts, missing-data rules and reporting details needed to reconstruct the target.
- Dry TFL review, a Data Evaluation Meeting and beta-stage experience are accumulated conduct. NCT02124564 and NCT06072833 are excluded without needing to infer whether outcome values were directly unblinded.
- Registry actual enrollment and dates were used only for chronology checks and were not substituted for prospective sample-size targets.

## Replenishment

All eight excluded slots are to be replenished from the official API. The release-eligible intake remains 120: 104 public first-pass drafts and 16 actionable metadata candidates.
