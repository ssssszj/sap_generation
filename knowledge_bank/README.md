# SAP drafting guidance

The former `knowledge_bank/sap_guides.md` was reviewed against the current
13-chapter DSH generation plan. Its reusable chapter checks are distilled in
[`src/sapgen/chapter_guidance.py`](../src/sapgen/chapter_guidance.py) and are
supplied to both chapter generation and final chapter review. The guide is not
loaded wholesale: several examples and conventional defaults in it would be
unsafe to treat as study-specific decisions.

The statistical principles were checked against the official
[ICH E9 Statistical Principles for Clinical Trials](https://database.ich.org/sites/default/files/E9_Guideline.pdf)
and [ICH E9(R1) Estimands and Sensitivity Analysis](https://database.ich.org/sites/default/files/E9-R1_Step4_Guideline_2019_1203.pdf).
They serve as methodology references, not as study evidence. The PDFs are not
sent to the model and do not populate the SAP-IR. The earlier Chinese PDF copies
remain accessible in Git history at commit `3605a9f`.

Protocol/CRF evidence and the SAP-IR remain authoritative for study facts.
Benchmark rubrics and reference answers are outside this guidance path.
