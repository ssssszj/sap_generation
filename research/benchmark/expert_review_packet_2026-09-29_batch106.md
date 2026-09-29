# Expert Review Packet - Batch 106

## Scope and decision boundary

Batch 106 reviewed the first eight remaining metadata candidates from the public ClinicalTrials.gov queue. All 16 official PDFs and eight registry records were downloaded, byte counts checked against registry metadata, SHA-256 frozen and extracted page by page. Forty-six decisive cover, chronology, version, statistical-leakage and retrospective-method pages were rendered from the original PDFs and visually inspected. No family is promoted; all eight are excluded.

## Exclusions

- NCT04743856 — protocol and analysis-section covers are dated 2025-11-03, after 2024 primary and final completion.
- NCT03990883 — SAP Version 3.0 is dated 2022-09-29 after 2022-02-15 completion; its history records during-run and final updates.
- NCT00799266 — protocol physical pages 54-61 disclose the analysis sets, ANCOVA, covariates, LOCF, sensitivity analyses, no-interim decision and power calculation.
- NCT02943460 — SAP dated 2018-03-21 follows actual 2018-02-28 primary completion, without evidence of a pre-outcome freeze.
- NCT03597022 — uploaded target is explicitly an additional post-hoc analysis plan for publishing, dated after termination/completion.
- NCT02576938 — protocol physical pages 41-42 disclose allocation, power, population, NRI, hierarchical comparisons, MMRM/MAR, sensitivity and safety rules.
- NCT05534061 — despite a pre-start cover label, SAP physical page 2 describes already treated participants and analyses already performed across a nine-month follow-up.
- NCT01377844 — protocol physical pages 46-50 disclose missingness, multiplicity, power, populations, treatment attribution, tests, repeated measures, safety and interim policy.

## Frozen file inventory

| Candidate | Decision | Protocol / SAP pages | Protocol SHA-256 | SAP SHA-256 |
|---|---|---:|---|---|
| NCT04743856 | post-completion analysis section | 62 / 2 | `6c553dbc65a6f1fe425d8b57b84de037be091c69a5ea87aff22d10b3ca009877` | `528870fd573f9cae3f233728f864c848c28b01119de1735de70ae295f597fb95` |
| NCT03990883 | post-completion final SAP | 141 / 66 | `1fd91a47da5b668fd1931c3c16c7bba9bb46c8d6a16d982a28ca7e1e8fbc8b78` | `27bc100d43246b73063b47e4f90a6f9d64deea7a96de91b62d39b85969677dec` |
| NCT00799266 | protocol leakage | 79 / 25 | `8b61c8255d1546328d54737818036e3c5044e047dcf67a23487daeedb8f18e71` | `6125ed193d85fec5deb9f5e414c12838e328a28ed29fa745e91d7f0fe5eb695d` |
| NCT02943460 | post-primary SAP | 89 / 65 | `c8e1075592f4e7675a1c2054e2baae7809b3a10de47441bc6473773dcd9cd9e8` | `c0fe8a8d367eaf35dfee392d912672a29b5bfad324b1ee4ca4c999e8da9eb192` |
| NCT03597022 | post-hoc publication plan | 97 / 23 | `b3c925d2f5d2074f92bedf3ad948d79eb10ccbf71ec7ebe0f861d35bf4edcc52` | `cae868a3c367b8d9d3564d7cb9bacc5444a4753ebb361317f8717efd5b549098` |
| NCT02576938 | protocol leakage | 80 / 31 | `5e9122e1a3d30da3f4aa2c8fda5e94e5f3d722ea505df8b1fcdb265bcfcf1b8e` | `fea333e0b1640edc8682f59f264507fb5f9fffcec40a90cec06c5fbd811e386c` |
| NCT05534061 | retrospective executed methods | 15 / 2 | `225129e3a3d75c6f1b3167ec07dec3c3cea4607854c478acc56cd3fff91136e0` | `63a47d5bba1dc3944c28d75d7f01db1005c4939c5e6c76931f8e71fffd9a400b` |
| NCT01377844 | protocol leakage | 61 / 137 | `71ef7cc81f2ddf3d9ac6d3b8ff78628a9d9a40cca5fa40cc3b8501014f7cf822` | `1e24f8389e4454789e47c7776027d150f8770a383fedad6f709d71adc30e148b` |

## Review gate

None of these eight families enters the registered benchmark. Their slots must be replenished from the official metadata source so registered public drafts plus actionable candidates remain exactly 120.
