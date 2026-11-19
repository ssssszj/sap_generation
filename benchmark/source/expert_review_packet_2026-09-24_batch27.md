# Expert Review Packet — Batch 27

Batch 27 promoted two studies, excluded five and placed one on governing-version hold. NCT05477875 and NCT03588572 passed identity, timing, prospective-document and protocol-leakage gates. NCT01667406 has an unreconciled Version 9 cover versus Version 8 body; three protocols expose the target analysis and one purported SAP contains completed-study facts.

## Promoted annotation drafts

### PUBLIC-PRK-CBD-OPIOID-001 / NCT05477875

- Identity and timing: protocol and separate one-page SAP share IRB202201660, the exact title, IRB version 03.09.04 and PI version/date 2024-05-22, before actual primary completion on 2025-01-22.
- Protocol-leakage gate: the protocol exposes the paired-eye randomized crossover, treatments, pain diary, visits and safety monitoring but not the reference SAP's JASP, Fisher-test, repeated-measures ANOVA, survey noncomparison or alpha decisions.
- Annotation: 19 atomic evidence-backed requirements spanning sequence randomization, treatment periods, pain and vision outcomes, crossover modeling, power, estimand, missingness, multiplicity and safety.
- Expert adjudication: reconcile protocol-versus-registry primary-pain definitions; define participant-level crossover factors and covariance; address period, sequence and carryover; correct the 70-eye unit-of-analysis concern; and complete missing-data and success rules.
- Input isolation: only input/protocol.pdf is model-visible; reference/sap.pdf remains annotation-only.

### PUBLIC-VENLAFAXINE-APHASIA-FMRI-001 / NCT03588572

- Identity and timing: independent protocol and SAP covers share the exact title, NCT03588572, institution and August 2018 date, before primary completion on 2019-07-01.
- Protocol-leakage gate: the protocol contains design, clinical outcomes, imaging acquisition and a sample-size calculation but not the SAP's task/rest fMRI preprocessing, seed-based connectivity, DTI tractography, inferential thresholds or repeated-measures choices.
- Annotation: 22 atomic evidence-backed requirements spanning clinical design, WAB/SLFT/PNT outcomes, analysis populations, longitudinal modeling, multimodal image processing, multiplicity, missingness, estimand and safety.
- Expert adjudication: complete allocation and masking details; designate the definitive WAB model; verify imaging thresholds and seeds; separate imaging-evaluable from clinical populations; and define study-level multiplicity, missing-data and intercurrent-event rules.
- Input isolation: only input/protocol.pdf is model-visible; reference/sap.pdf remains annotation-only.

## Screening decisions

- NCT06210035: excluded_wrong_document_type. The purported SAP states that 89 participants completed the study, says analyses were conducted and reports three observed adverse events.
- NCT03594227: excluded_combined_protocol_sap_leakage. Protocol physical pages 63-65 disclose analysis populations, LOCF, MMRM, model terms, confidence intervals, success rule, sensitivity and safety analyses.
- NCT03395184: excluded_combined_protocol_sap_leakage. Protocol physical pages 148-153 disclose sample size, type-I error, mITT, missing-data rules, primary/secondary models, safety and conditional-power interim analysis.
- NCT01667406: hold_version_reconciliation. The protocol cover/title pages say Version 9 dated 2015-02-01 while physical pages 2-20 retain Version 8 dated 2013-10-15; SAP Version 3.0 does not cite a governing protocol version.
- NCT04007198: excluded_combined_protocol_sap_leakage. Protocol physical pages 68-70 disclose populations, baseline and descriptive conventions, safety/PK/efficacy summaries, responders, Kaplan-Meier and exacerbation-rate analyses.
- NCT04082442: excluded_combined_protocol_sap_leakage. Protocol physical pages 12-16 expose endpoints, power and alpha assumptions, nonparametric tests, covariate adjustment, paired t tests, mixed-effects/GEE methods and interim analysis.

## Source audit

All 16 PDFs were obtained from ClinicalTrials.gov, hashed and page-counted. Identity and decision-defining statistical pages were text-extracted and rendered for visual inspection. Reference SAPs for promoted studies remain annotation-only acquisition artifacts under the gitignored source tree.

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT05477875 | promoted | 12 / 1 | de03cb4aed02f4359b7340f1ceb9d09217cb62e4822d67ec147c862af3d1e6cf | 4fd636f71f8c043aafb721e845cd8afc84cb1f45232a5b9b1d1ecbf3e1b465d0 |
| NCT03588572 | promoted | 9 / 6 | 368ebb4cf0b6fe760826190df72774bb906d64942996b75f06d667d3b428007d | 521c85adacc5b1d0b1bc36d7f04dc75e35ae8341be6ebb5ade9d8f0cf75815d5 |
| NCT06210035 | execution-informed SAP | 6 / 3 | d48b7f211fca8c5ea2ae3145486f1ecbab7f4157dc49dc08aad81e62968ff810 | 3c150669884c9f1260f8113ccf3afd12587e49961e2ad65ea36cec209ea7da27 |
| NCT03594227 | protocol leakage | 90 / 32 | a8b2a57ec6aa8847907f9351e003b7f0da70189f7b0ca322aa51678fe00895ac | 757f3425a7c8d7fd2b0f7b1ab6c8c75a5244a9b4950bdfa1eb71376bef83cf35 |
| NCT03395184 | protocol leakage | 205 / 31 | 1d9926739b3d78ad37d54197d4dbd8db5720901bd404769b0d3e6bc1b4e57b03 | 3bfa30a0b6ebbc1b54b1591ac6cc510d6a9c3430f650ae32231e0f9ffcf7d4e9 |
| NCT01667406 | version hold | 20 / 10 | 1bf9ea2aec95e53c61aa667e42fb5af10fbd10cf4480676b5f4c46cb3f735c65 | fb2f1a0da39ef210ced08dd9f901b2f0bb53bbedb69255fcd9fa2abc14fd484a |
| NCT04007198 | protocol leakage | 80 / 36 | 5b5889f3d51cbe45bea15a734dd9a5fdb171f3bb5807776bc178d251d47b0435 | 158e8a85c097ddf78ffd37905c812c71d0952324bdd65688511e483a22566ef6 |
| NCT04082442 | protocol leakage | 22 / 3 | bb82d28d10f45fcb3b06cbc8525fff063343423beedeb4e53e11ef3077c12b78 | 1d3ad0e09f9f9e32dfb7818bb2c3ca6ea31a71b15f49ca8dda8f19ef1985ac17 |
