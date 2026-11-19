# Expert Review Packet: Batch 145

## Scope and status

Eight official ClinicalTrials.gov protocol/SAP pairs at the Batch 145 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from the 828 physical pages in the 16 PDFs; the scan-only 50-page NCT04967508 SAP was recovered with full-page OCR. A total of 326 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight pairs were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03152552 — exclude: the SAP follows early termination, documents analysis changes caused by the termination decision and is substantially exposed by the protocol's executable MCP-Mod/ANCOVA/MI/MMRM program.
- NCT03811093 — exclude: the unversioned SAP is post-completion, conflicts with the protocol's age range and mostly repeats the protocol's sample size, outcomes, independent t-tests and alpha.
- NCT04967508 — exclude: the approved CSR SAP follows primary completion and incorporates completed Week-28 analysis, blinded review, COVID-19 and Ukraine-war deviations; the protocol also exposes the primary equivalence program.
- NCT02992119 — exclude: the SAP follows completion, uses executed-study wording and is substantially exposed by the protocol's sample size, populations and immunogenicity summaries.
- NCT03426267 — exclude: the post-completion SAP cites Protocol Amendment 03 while the selected public protocol is Amendment 02, and material target analysis content is publicly redacted.
- NCT02582866 — exclude: the extension SAP is chronologically prospective, but the model-visible protocol already gives the Safety Set, descriptive program, TEAE attribution, deviation/missing-data rules, interim policy and parent-determined sample size.
- NCT01296932 — exclude: the revised adaptive TSAP documents conduct-era endpoint changes and event-time DLT definitions, cites later protocol versions than the selected input and is substantially exposed by that input.
- NCT02177123 — exclude: the SAP is post-completion, cites Protocol Version 1.3 rather than selected Version 1.4-NL and contains realised implementation metadata including ITT N=101.

## Frozen evidence

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT03152552 | termination-informed target plus leakage | 83 / 36 | `10bc71d37d16dfd574aa2f4cbd1425750ad59b5baad4aa46e624b69914d4c1ad` | `64cd5ad58c86c6510e60879c98530d1e7449e46996753e3b839b033bb17141f2` |
| NCT03811093 | post-completion unreconciled target plus leakage | 10 / 5 | `012143ee22e94e5c7d40bf4a4d339bbb10760d5eb81107ea1409632d8107b9b5` | `73b884b94994a22481dd4d305d57f2d4730cb97808e478b5d901b5b035953f80` |
| NCT04967508 | post-primary execution-informed target plus leakage | 79 / 50 | `4bd7732e8382c57d158e724a1fde9eea4738bae531a80d5f2064f2cf91067ede` | `a6cdb651dbc4bd93c06a42cb8d3878e6ea25b06a172c2fb0c72aac2b14d9182b` |
| NCT02992119 | post-completion executed target plus leakage | 55 / 19 | `f359685372cc8298c2432e9cb72e928fab4ba4738f203f5a4b489fe835369330` | `7320a0a12f332527937794c9ab9e3d952c6acf520f112e73067230625094d05e` |
| NCT03426267 | post-completion version-mismatched/redacted target | 80 / 34 | `4a3a4fabf3186da668e9ef9ddc88b1f8f770c0304e85edb5e44c2f1c42ca7bc9` | `82a06b2e63e71f971b8125e544c344c816c6c47ceda2a15dc742adba8f6338a7` |
| NCT02582866 | protocol-embedded target leakage | 48 / 19 | `fbb51b5ee2a7c424448d853a294f9874928fde88942d6efa7a985e8f6392c97e` | `b009a4e4150f414b2f5a2b03df612d59c65d6e80faf2bab60a9f4e026801637c` |
| NCT01296932 | adaptive conduct-informed/version-mismatched target plus leakage | 113 / 51 | `218e6ad0a0d96d8bc22b2b628f5ba44d129e4496cab8cd818b1c2651ce79c1f7` | `a8f18091e0842192e864cbefa0bd1d46f07ffda8320fd31642b3e2601e89e683` |
| NCT02177123 | post-completion governing-version mismatch | 61 / 27 | `83ff0bdc3285c80b36cb218f6a02ab842cc8d9f4dd6665f464e16f40b2eb7170` | `4d355069a09b514a29f3d14f65e799b111863202934fea0f34bffc608e571751` |

## Gate interpretation

- A SAP approved before final study completion still fails when it follows primary completion and incorporates a completed main analysis, blinded-review decisions or realised conduct disruptions.
- Early termination and adaptive dose escalation are not automatic exclusions, but a target is execution-informed when its own history says realised termination, DLT or cohort information changed endpoints, populations or analysis methods.
- A same-study extension is not automatically a duplicate family. NCT02582866 fails because the extension protocol exposes its own target analysis, not merely because eligibility depends on parent SP0994.
- Design, endpoint and sample-size overlap alone is insufficient for leakage. The leakage decisions here additionally rely on exposed analysis populations, executable models/tests, imputation, estimands/margins, time-to-event rules, safety attribution or interim/adaptive rules.
- Registry actual dates were used as chronology evidence only, never as a prospective sample-size substitute.

## Replenishment

All eight non-promotable slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
