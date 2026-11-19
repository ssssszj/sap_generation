# Expert Review Packet - Batch 122

## Scope and decision boundary

Batch 122 reviewed eight metadata candidates from the public ClinicalTrials.gov queue. Sixteen official PDFs and eight official registry records were downloaded sequentially and SHA-256 frozen. The pairs contain 1,266 one-based physical PDF pages. Native text was extracted page by page; 92 scan-only or empty-text pages were separately rendered and OCRed, including the complete NCT02916706 protocol/SAP pair. A total of 151 decisive identity, chronology, version, analysis, conduct and leakage pages were rendered into 21 contact sheets and visually compared with the originals. No candidate survives the prospective, outcome-uninformed and prompt/reference-independence gates.

## Decisions

- NCT02232399 — exclude: the 2017-11-06 draft SAP follows actual completion on 2017-04-25, while protocol pages 42-43 already expose the primary t-test, secondary/descriptive program, exploratory regressions, sample size and power.
- NCT02916706 — exclude: Final SAP Version 2.0 follows actual primary completion and has post-primary revisions; the scan-only protocol pages 6-7 already expose alpha, ANCOVA, MMRM and logistic analyses.
- NCT04237116 — exclude: the final SAP is post-completion and explicitly replaces planned analyses after low-recruitment termination; protocol pages 61-66 also disclose the original executable program.
- NCT03196297 — exclude: the 690-page public protocol bundle contains the governing Version 4 statistical section and exposes the hierarchical CPoC, negative-binomial, offset, population, MAR, sensitivity, sample-size and interim/main-part program.
- NCT03160885 — exclude: Protocol Version 5 pages 82-104 disclose the analysis sets, hierarchical multiplicity, estimands, CMH analysis, nonresponder handling, multiple imputation, pattern-mixture sensitivities and safety program.
- NCT02400671 — exclude: SAP Version 5.6 is post-completion and records changes driven by observed baseline subgroups and the realized 10%/greater-than-40% missing-data pattern.
- NCT03354572 — exclude: the separately uploaded two-page statistical document is a verbatim extraction of protocol pages 27-28, and the protocol also contains the sample-size calculation.
- NCT02246439 — exclude: the selected SAP artifact inseparably appends a post-unblinding supplement that uses observed age cut points and an actual treatment-misallocation case; protocol pages 30-32 also disclose the executable main plan.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT02232399 | post-completion and protocol leakage | 70 / 17 | 88103c3824169d46e834b509f1f087052764ed30e5ea874812254dda5739f224 | 074f06904d62143266b4ebd1c749292a3aad4e667230ea17c06f02c92d88d7a1 |
| NCT02916706 | post-primary and protocol leakage | 56 / 30 | 6d61d36a2323e8c4fd0dc565db0165f372e5a1e2397b9bc05f4df4c5ae806e0a | 6798248eeeb8b6a6e829205a419782a61d6636626b96a32c931dd9e3537a4536 |
| NCT04237116 | termination-informed and protocol leakage | 76 / 16 | f9ff707f0069f7abb9a633bbd8cd7a2ee20ea901a86049b3a7794eed263088b1 | cab8e1e129e059634cc0c62b32d69da340d5211618f7776d40f25d1e12085dd2 |
| NCT03196297 | protocol leakage | 690 / 16 | 4b9c46c7f68f7d53984696f9b2c90a0712c145ef014a1d7481ac6e3056513fca | ed45e5c99b0ffc3285c7745f06f50528d61bb81ae68aef60a957d5ea42b3ba4e |
| NCT03160885 | protocol leakage | 158 / 33 | b994e438ee130e1683158604138b899cfca44fcb7640df79a11106d57b6d02bc | a3a95e727d8e9647cd34d534f19628fb150905f90a2444edce84cf2f2583f8f0 |
| NCT02400671 | post-completion and conduct-informed | 36 / 14 | 0a20f4a95307692e9d2f087e9c64ae94214f0bee60f6005855d9bf449128b8e2 | cb23ff3c5f0b8a0234e3906a813192bb453cd69777a147c5983f00a5e298878c |
| NCT03354572 | complete target leakage in protocol | 36 / 2 | 201dd3a8ba44a7a70ae61a68d5c2ab691ad6bce69514f99b54abeafb6bd79599 | cf3551f9177f2d7ccc995fcd6311bd0d040d645fad4168348dfb34ec6210fe19 |
| NCT02246439 | mixed pre-unblinding/post-unblinding reference and protocol leakage | 41 / 21 | fe85de3cda27118f040cfef6d2b37c3b74633517453d9cc26c72786858567b06 | d8a28ef38060f9ae4271b673e44938b364aa273e26589f8c1595764bb95adb7c |

## Review gate

No Batch 122 candidate enters the registered benchmark. All eight non-actionable slots were replenished from the official API, preserving 102 public first-pass drafts plus 18 actionable metadata candidates. The new queue begins with NCT02476006, NCT02944383, NCT04375878, NCT03263091, NCT03211247, NCT02409290, NCT05832918 and NCT05015478.
