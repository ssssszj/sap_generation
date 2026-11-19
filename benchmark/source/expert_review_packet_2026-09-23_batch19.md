# Expert Review Packet — Batch 19

Batch 19 produced no promotable study. All eight pairs failed a hard source-admissibility gate before requirements annotation.

## Screening decisions

- NCT03223883: `excluded_wrong_document_type`. The protocol and two-page SAP are both dated 2024-08-19, after actual primary and study completion on 2023-01-25, without a version history or pre-completion approval chain.
- NCT02832063: `excluded_wrong_document_type`. SAP Version 1.0 (2017-07-21) and Version 2.0 (2017-08-28) both postdate actual primary and study completion on 2017-07-19.
- NCT02906930: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 77-92 contain the executable estimand, ANCOVA, multiple-imputation, sensitivity, safety and interim plan. SAP Version 1.0 is also dated after primary completion.
- NCT02057718: `excluded_wrong_document_type`. SAP Amendment 3 physical page 6 says it was finalized after database lock and after multiple interim analyses, and records execution-driven changes.
- NCT02234323: `excluded_combined_protocol_sap_leakage`. Protocol physical pages 87-90 expose the analysis sets, ABR derivation, inhibitor-incidence interval, safety analyses, interim plan and sample-size rationale.
- NCT02951533: `excluded_combined_protocol_sap_leakage`. The 242-page bundle contains four SAPs for different analysis times, while supplied Protocol Amendment INT-2 postdates primary completion and physical pages 71-74 already expose the confirmatory Week-24 plan.
- NCT06949176: `excluded_wrong_document_type`. The file labeled SAP is visibly a three-page informed-consent form; no independent reference SAP exists.
- NCT04623242: `excluded_wrong_document_type`. Both supplied documents postdate primary completion, and SAP physical page 9 states that interim analyses had already been conducted and reviewed by the DMC.

## Source audit

All 16 PDFs were downloaded from the ClinicalTrials.gov registry, hashed, page-counted and extracted by one-based physical page. Title/version pages and the pages establishing post-completion timing, execution-informed changes, wrong document type or target leakage were rendered and visually inspected. Reference SAPs remain annotation-only acquisition artifacts under the gitignored source tree.

| Candidate | Role | Pages | SHA-256 | Public source |
| --- | --- | ---: | --- | --- |
| NCT03223883 | protocol / SAP | 6 / 2 | 590a719fcf00f1dbdb7e9796e979196cb0827845d35e67103f09523dcb259a1d / ca1bd4c93c8fa23af3c0b9518bdb839d61604e52b56d9f4b35de54df381e208f | [record](https://clinicaltrials.gov/study/NCT03223883) |
| NCT02832063 | protocol / SAP | 51 / 26 | 2ddb28ec73b0bb50b11a61b482385238faa1a81860b65ea833e869c1acaf6fc5 / 92df6152dadc8e1dfd8ac6489429835d8cbc669ad756e6b2d4e954961b2c6f46 | [record](https://clinicaltrials.gov/study/NCT02832063) |
| NCT02906930 | protocol / SAP | 148 / 36 | cc1028ed23e0dbccb2d71d4750c75d30b35423a3c6007496191807b9121c4e79 / 6960c24de41de6fd314b48002367e369e830a5fb0c0f5ea956e6e36e3189b0fc | [record](https://clinicaltrials.gov/study/NCT02906930) |
| NCT02057718 | protocol / SAP | 233 / 108 | 6cef10f456928ceef2c17b7863dfe589121a3b69f36e83cb098524846df3f8cb / 2e5cdd287df858cf54c971c2563a382b85bd47b443b870adcb2df49cbf9aeed9 | [record](https://clinicaltrials.gov/study/NCT02057718) |
| NCT02234323 | protocol / SAP | 106 / 71 | 3cba9337934f17ae4f80977bbe20d4f136a5912ac5327355958cd6ee522cd9b7 / 8592d3c323f8792465cc8f5f122f260efe8f2adc96f1cabde1890a790249df10 | [record](https://clinicaltrials.gov/study/NCT02234323) |
| NCT02951533 | protocol / SAP | 98 / 242 | 26fa078b9639e365d5727788908cd41091d86f38c221e2045fb0c74604da1fd2 / 6175cccbc37850a8abbb998cb4ca6af42636bcf7d5ebc4753b4cc8c865325d2f | [record](https://clinicaltrials.gov/study/NCT02951533) |
| NCT06949176 | protocol / SAP | 13 / 3 | 902bd8fe515c05f44a6b3213d96332ea73dd0530e980fccbf4c5fbdba891f7dc / bc37908979cde3f871abc2f0005d96d386f46a94f4a4b16642c25753fdc73441 | [record](https://clinicaltrials.gov/study/NCT06949176) |
| NCT04623242 | protocol / SAP | 265 / 141 | 89f33f26d9428307541679049e3968f92c0945868e085a21ca0dccc4805411cf / ceda74d29f80200f5a763657ddf9a93310658308f0a0e57826c3e2106661c2b1 | [record](https://clinicaltrials.gov/study/NCT04623242) |
