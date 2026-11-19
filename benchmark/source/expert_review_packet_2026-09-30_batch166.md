# Expert Review Packet: Batch 166

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 166 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. The 16 selected PDFs contain 1,165 one-based physical pages; text extraction recovered content from 1,118 pages. A total of 44 decisive physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT04213807 — exclude: the Final SAP dated 2021-03-18 follows actual primary completion on 2020-12-29 and study completion on 2021-03-08. Physical page 27 retains cohort-progression interim reviews, and physical pages 28-29 state no analysis or data issues despite finalization after completion. The selected target is post-completion.
- NCT05048719 — exclude: SAP Version 3 dated 2022-10-24 follows actual primary/study completion on 2022-09-30. Physical page 5 says it was approved after all participants completed Week 26 and safety follow-up and records added analyses and revisions, following Version 2 prepared around an interim analysis. The target is post-completion and interim/conduct-informed.
- NCT03451851 — exclude: SAP Amendment 1 dated 2023-12-04 follows actual primary completion on 2023-07-19, while the selected Protocol Amendment 5 is still later, dated 2024-08-29. SAP physical page 7 changes a co-primary endpoint in response to FDA feedback, and physical pages 16 and 22 describe interim PK review and sponsor unblinding after completed Part 1 data. The selected package is post-primary, regulatory/conduct-informed and governing-version-mismatched.
- NCT02527681 — exclude: SAP Final Version 2.0 dated 2020-08-17 follows actual primary/study completion on 2020-02-25. Physical page 5 replaces the planned three cohorts with the realized fact that only Cohort 1 completed because of very low recruitment. The target is post-completion and realized-enrollment-informed.
- NCT05008835 — exclude: SAP Version 1.0 dated 2022-09-21 and approved through 2022-09-30 precedes actual primary completion but follows termination on 2022-08-08. Physical pages 10 and 39 state that 61 participants had been randomized and replace planned inferential analyses because of the early termination. The target is termination- and realized-enrollment-informed.
- NCT03872453 — exclude: SAP Version 2.0 dated 2019-11-15 follows actual primary completion on 2019-10-31 and study completion on 2019-11-11. Physical page 8 records extensive revisions to endpoint comparisons, subgroup analyses, rescue-medication derivations, missing/failure hierarchies, time-to-event algorithms and safety outputs. The target is post-completion and conduct-informed.
- NCT02129556 — exclude: the selected SAP dated 2015-08-11 anticipates Amendment 1 and adds a PD-L1-negative cohort, but the selected governing protocol is later Amendment 1 Version 2.1 dated 2016-01-11. Protocol physical pages 91-95 already expose the 3+3 dose rules, Simon two-stage design, cohort decision rules, analysis populations, confidence intervals, Kaplan-Meier analyses, safety monitoring and correlative methods, substantially reconstructing the target. The selected chain is governing-version-mismatched and protocol-leaking.
- NCT04092907 — exclude: the SAP is dated 2019-07-10, after actual primary completion on 2019-07-03 and on the same date as actual study completion. Same-day ordering cannot establish prospective finalization, and no earlier version chain is publicly established. The target is post-primary.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT04213807 | post-completion target | 212 / 29 | `9d343e13ca61910432e519c8e6ca6dc685f5c73b10e33ee2743841b124dc2bae` | `bd8cfff7c443f97fdf8eb4877584469a9b185db0201e59a7ef124ffe3402dc6e` |
| NCT05048719 | post-completion/interim-informed target | 117 / 43 | `e6ff20a4ea29d513ae4daf168a121f98a0bc78ccdbfae515ef43971306dd2b6a` | `c0bee55be0ea9b3618f6e2573c67024b7b719b1750087e757f61a9eb12a02ab9` |
| NCT03451851 | post-primary/regulatory/conduct-informed and mismatched package | 153 / 54 | `506e63aba79f93ea64397a2488550374cd92c99638ccff1bcf5394a7b727e6a2` | `6c2cda3588e9a5dba7ccd9b426c925a984b46e80b10d8d6d8e7f8522f9ed9194` |
| NCT02527681 | post-completion/realized-enrollment-informed target | 51 / 12 | `1b534e3d758654d5bbd7c6776b572589a7969b3941e00ef6c9827775aad561c0` | `cca7bb052b760200fdc82ca99011640df8f5ecd09098b85c74185f164904ece9` |
| NCT05008835 | termination/realized-enrollment-informed target | 91 / 45 | `27fd26156ead29124fb1cbf8aa5bd85fe3a7e794455ea7f17510efad59f3cd14` | `a848f33b8cf0d203102ec123415ec64096481a7df6aafd987ac990c0c55b40eb` |
| NCT03872453 | post-completion/conduct-informed target | 67 / 68 | `e6bf9a4429687097c6f3c19d2eb42fbbecd46ea5ead7d97d1dec6b3a50f8b8e9` | `3c7ffbc74d875f12702dd7b6904a9fb28ee8e223f7446ca846695642a7d1d06e` |
| NCT02129556 | governing-version mismatch and protocol leakage | 106 / 17 | `4744d44732632392c2b6b386af8f61d30bcc642422f8097c705eb80d407d9207` | `819786a209134bf804f21b590569b4abc227fd6d75b116daab546b5d76ef18e0` |
| NCT04092907 | post-primary target | 80 / 20 | `c2840205eae3a5504c500db7a84a71e33cd4ddffef3b75b6c7ca29e32ffb3492` | `c7cfb694710a5330ebcb703f2a49da8b3595815f6b3bcc396546d37f18760d72` |

## Gate interpretation

- Completion chronology is a hard gate: an SAP finalized after primary or study completion is not rescued by a claim that analyses were planned or by an earlier protocol date.
- Same-day study completion and SAP dates do not establish within-day prospectiveness.
- A pre-completion SAP is still excluded when it explicitly responds to termination, realized enrollment or completed cohort data.
- A later selected protocol cannot govern an earlier SAP without an explicit reconciliation chain; protocol leakage is independently disqualifying when it exposes the executable populations, decision rules, models, confidence intervals and monitoring plan.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight excluded slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
