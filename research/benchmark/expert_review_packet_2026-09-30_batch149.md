# Expert Review Packet: Batch 149

## Scope and status

Eight official ClinicalTrials.gov study packages at the Batch 149 review-queue head were reviewed against prospective-version, outcome-uninformed, protocol-leakage, study-family and document-type gates. Native text was extracted from all 1,188 physical pages in the 16 selected PDFs. The 126-page NCT05162586 IAP was additionally OCRed in full because its embedded font encoding impeded reliable extraction, and 143 decisive one-based physical pages were rendered and visually inspected in eight contact sheets. All eight candidates were excluded; all decisions remain first-pass screening requiring independent expert review.

## Decisions

- NCT03354429 — exclude: the four-day-pre-completion SAP repeatedly changed event counts, power, interim timing, futility thresholds and on-treatment rules during recruitment, while the protocol independently exposes the executable Cox, hierarchical, subgroup and interim program.
- NCT04064411 — exclude: the SAP is pre-primary-completion and matches Protocol Amendment 3/3.1, but that protocol already exposes the analysis sets, noninferiority MMRM, margin, covariates, confidence-interval rule, secondary models, sample size and no-interim/no-multiplicity decisions; the SAP also adds COVID- and conduct-specific analyses.
- NCT05162586 — exclude: IAP v4 follows completion after adaptive interim analyses and a partial-lock primary analysis, with late changes to populations, scope, models, time windows, imputation and safety outputs; the protocol also exposes the adaptive and primary programs.
- NCT03107377 — exclude: SAP v2 follows completion and adds relaxed eligibility, repeat-enrolment, reinfection-by-visit and sensitivity handling; the protocol already exposes populations, no-imputation/analyzable-case rules, Chi-square testing and sample size.
- NCT03682302 — exclude: SAP v11 follows completion and adds detailed observed-data, missing-time, post-discharge opioid and NCA PK handling, while the protocol already exposes the executable PK, efficacy and safety program.
- NCT02638103 — exclude: the pre-completion SAP amendment is regulatory- and realized-enrollment-informed, governs a pivotal-study-dependent extension and prospectively schedules an interim data cut/CSR after pivotal unblinding; its protocol already exposes the analysis core.
- NCT01588184 — exclude: the extension-study final SAP follows a performed and medically reviewed interim safety analysis, updates shells already used in that analysis and was revised for final reporting; the protocol also exposes the executable safety and time-to-event program.
- NCT03452033 — exclude: the SAP and approval follow study completion, and the protocol already exposes the dose-specific powering, ITT/safety populations, descriptive program, two-sided 0.05 rule, missing-data policy and no-interim decision.

## Frozen evidence

| Candidate | Decision | Protocol / selected SAP pages | Protocol SHA-256 | Selected SAP SHA-256 |
|---|---|---:|---|---|
| NCT03354429 | late conduct-informed target plus leakage | 76 / 18 | `896d832ada7824fb12e67ce4a4324cb97197d1f0ed124a9340e7b74e68b6c216` | `8486ae911b70181992bd77484e532ef21e3f922f330c61824dfb95dfa6760ce4` |
| NCT04064411 | protocol leakage plus COVID/conduct additions | 79 / 64 | `b2acca1dba65fdf90ac32e04794c8c262ce3a566b9e60bd1103741feb61fe588` | `717bc957ad25c0085bcb57ba9c276d9d3c108b58be0f61bcca6a3bb6e3a90401` |
| NCT05162586 | post-completion adaptive-interim target plus leakage | 165 / 126 | `39ce7dd20fa2415a897de5f696941248aedcddce43d2113a3e6765984cc49af0` | `12e7dc9028945c3c275ba99b5f63e34b12485cab3ed8d51a23459deac0320649` |
| NCT03107377 | post-completion changed target plus leakage | 76 / 25 | `d83ad68ddee5a74080cbee9fa413f9c831a0eb152fcff0cd0b43057dd8691b72` | `3c66b6212861951df0df6cd270ae9a59e97279b7fd0f553a65cfee89d9035b80` |
| NCT03682302 | post-completion conduct-informed target plus leakage | 59 / 112 | `fc169ec34c6b4e7a412efa16805c5d1d6dabbe668287e5e62bd66d341144f918` | `18cfda1d5caead6eb3a0296f65525732209e2001da8c5f730d3f60dbb2031e51` |
| NCT02638103 | regulatory/study-family/interim-informed target plus leakage | 182 / 87 | `6a4f9ba0948c2a79d2653d58c1249a16f2643d00cb162a2de785795b8c1ec48e` | `90f67462b5bf2278351b31d42aada38cba9f5fb7ae6394b7c55a0dfb1a3e3202` |
| NCT01588184 | performed-interim extension target plus leakage | 65 / 75 | `03ab8e63c43d40261cff6bfb6ed41793a1bff678912c5800a70471be92c456f1` | `acfea800b414cb0ad7130038d57decc5624e0ddf5dc57f330478b6cc4295128c` |
| NCT03452033 | post-completion target plus leakage | 55 / 28 | `203577e2798ff9cf81b2f497f7779ab9ea3e1a0caf39a462b0c6da939c587821` | `fd0012cd3f7104d841910e657b9091de690f8403543a7a25fefc81f0c0edb88a` |

## Gate interpretation

- A SAP dated shortly before primary completion is not automatically prospective when its revision history records recruitment-era changes to event counts, power, interim decisions or observed study assumptions.
- A pre-completion plan can still fail when the model-visible protocol supplies enough analysis sets, models, covariates, missing-data rules, margins or interim procedures to reconstruct the target. Endpoint names and a sample-size target alone were not treated as leakage.
- A planned adaptive design does not rescue a final IAP issued after the adaptive analyses, partial database lock and study completion; the selected target must itself be outcome-uninformed.
- Extension studies were rejected only when the selected plan materially depends on parent-study treatment, baseline or unblinding state, or when an already-performed extension interim analysis informed the final target.
- Registry actual dates were used only for chronology and never as prospective sample-size targets.

## Replenishment

All eight non-promotable slots are replenished from the official ClinicalTrials.gov API. The release-eligible intake remains 120: 106 public first-pass drafts and 14 actionable metadata candidates. No requirements or registered document artifacts are added in this batch.
