# Expert Review Packet — Batch 32

Batch 32 produced no promotion. One protocol embeds the complete target analysis, while the other seven SAP packages are post-primary, post-completion, retrospective or materially informed by trial execution. All 16 PDFs were downloaded from ClinicalTrials.gov, hashed, page-counted and text-extracted. Every cover and each decision-defining date, version-history or execution-informed page was visually checked.

## Screening decisions

- NCT07230873: `excluded_combined_protocol_sap_leakage`. The one-page protocol calls itself a combined protocol/SAP and exposes actual enrollment and the complete inferential plan.
- NCT03981744: `excluded_wrong_document_type`. The approved SAP postdates actual primary completion.
- NCT03268005: `excluded_wrong_document_type`. The embedded SAP postdates completion and is packaged as CTR Appendix 16.1.9.
- NCT03657160: `excluded_wrong_document_type`. SAP v3 records COVID-19-driven enrollment termination, cancels the planned primary EOT analysis and removes prespecified analyses.
- NCT04816591: `excluded_wrong_document_type`. Both SAP Revision 3 and its governing Protocol Version 4 postdate primary completion.
- NCT03364309: `excluded_wrong_document_type`. Public SAP v2 postdates completion and only claims approval before final database lock; the unavailable v1 was the pre-unblinding version.
- NCT02440789: `excluded_wrong_document_type`. SAP v5 postdates completion and explicitly permits changes based on observed findings.
- NCT02825849: `excluded_wrong_document_type`. The SAP is a retrospective summary stating actual 17-versus-5 enrollment and already calculated outcomes.

## Source audit

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
| --- | --- | ---: | --- | --- |
| NCT07230873 | protocol/SAP leakage | 1 / 4 | 84dde11510f0d3981e849a4e8237c4952c2833c169ebc1d633a2547947693875 | 27cf68326eddb7e67783aba271e395557030e7e6d6024c8039d72efeff6d48a7 |
| NCT03981744 | post-primary SAP | 121 / 52 | ed8877816f68e4accc7eae90d42633385bfc60ab64a38f6583b1b181637f651e | 06c218b75de86b4c1f3d9aee258a309297a71b7d208aed68135bf78e77ab378a |
| NCT03268005 | post-completion CTR appendix | 253 / 31 | 62c95ef43917c277d11e88abdb70e05fa9463ef23f0526f9f7fc6fc60b8bf9f3 | 264c7bfa88956061cea7239652053c5ce10961f34a8b7dd4cd6e614944107411 |
| NCT03657160 | execution-informed terminated-study SAP | 124 / 48 | 3cecd2497da56330e48e38a0163edcf174f95ef4c42f5428348e568a10b88d58 | a8b95c43a97c115d6382743215c9a9cfa6387a521b4d56259f439f1f5a206541 |
| NCT04816591 | post-primary protocol/SAP | 83 / 38 | 4c4afee2c531e2c2fe060b43f52d7b929cc0a8231cb11f6ba3a843914c8b6f24 | 1c5a46011b31a1d863b8674a878f0bc478e703de54172ea1888aa0fd3a2e044c |
| NCT03364309 | post-completion SAP v2 | 108 / 86 | 96406e5e426d6ed7edc71c9da3419fa7954d4eb4e8885c74976198fb3b2d457e | c1480264fde86e83dec92c3ed18a5161b1cb33c52abca53413496cad9613e041 |
| NCT02440789 | post-completion execution-informed SAP | 86 / 17 | b36eb9d12fdc1caf8cb0873f32015863561c0f3edd2cb54ae46da1eddbedcfe9 | adbb9c056ae7f854f7d0d3dffe3d916c0a5801269aa2a6e589cbc192ac543147 |
| NCT02825849 | retrospective executed-method summary | 3 / 2 | 4cdf6812dd24f4d4fd1f3eafccee8e23c06b5faf90df9493213b7d17b89d296f | 569a03a45daa700a9d134d431e32336a7c73bf745785df3342befcc857c91871 |

The PDFs remain local gitignored audit artifacts. Reference SAPs are never model inputs.
