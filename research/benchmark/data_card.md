# SAP Generation Benchmark Data Card v0.1

## Current composition

The working benchmark contains 102 registered study families: one private pilot and 101 public annotation drafts.

- one private Chinese ophthalmology medical-device study marked `pilot_only`;
- VIVID, a public randomized behavioral study with a binary primary outcome;
- multimodal treatment for hemiplegic shoulder pain, a three-arm adaptive-randomized PNS/PT trial whose during-enrollment analysis attachment adds longitudinal mixed modeling, site checks and responder regression under an explicit provenance-review gate;
- ROKHyT, a nationwide randomized digital-hypertension pilot with stratified allocation, 12-month blood-pressure control, feasibility outcomes and a reference-only Mantel-Haenszel relative risk under an explicit during-conduct provenance gate;
- biobehavioral smoking cessation in adults living with HIV, a randomized standard-versus-tailored NRT study with biochemical abstinence verification, logistic and repeated-binary modeling, MNAR sensitivity, mediation and explicit sample-size/provenance gates;
- IMPACT, a public observational cohort with an exact protocol/CRF/TSAP triplet;
- ASCEND-D, a public phase 3 active-controlled study with continuous and time-to-event co-primary non-inferiority endpoints;
- SER-287, a public randomized phase 1b study retained partly as a missing-document challenge.
- dasiglucagon in congenital hyperinsulinism, a public pediatric Phase 2/3 crossover study with an open-label extension;
- Blood Pressure Control in Hypertensive Smokers, a public two-phase behavioral study with an abstinence-conditioned three-arm randomized analysis.
- pediatric NAFLD dietary treatment, a two-site controlled-feeding trial with MRI-PDFF and repeated measures;
- NOTE endometriosis, a double-dummy active-controlled pilot centered on estimation rather than superiority claims;
- VRC01 during analytic treatment interruption, a small Phase II HIV trial with exact binary and time-to-event methods.
- REDUCE PFO, a multinational randomized device trial with simultaneous time-to-event and MRI binary co-primary endpoints;
- imsidolimab in generalized pustular psoriasis, a three-arm Phase 3 trial with an explicit estimand, fixed-sequence multiplicity, multiple imputation, and adaptive sample-size review.
- Anchor/W-SUDs, a remote randomized digital intervention trial with attrition weighting and arm-specific per-protocol adherence thresholds.
- RESTORE in cerebrotendinous xanthomatosis, a rare-disease adult crossover trial with a separate open-label pediatric cohort.
- Wellness Programs for Brain-Injured Individuals, a randomized behavioral pilot emphasizing feasibility thresholds and descriptive analysis.
- Transcriptomic Signatures of Influenza Vaccine Responses, a randomized older-adult vaccine study with laboratory blocking, CQN normalization, and high-dimensional exploratory analyses.
- the cinacalcet pediatric extension study, a single-arm safety study with parent-study combined analyses, iPTH missing-data sensitivity methods, and growth endpoints.
- Engensis for diabetic foot ulcers, an early-terminated Phase III randomized trial with exact primary testing, layered sensitivity populations, and longitudinal wound analyses.
- PEG bowel preparation renal safety, an auxiliary prospective observational study with serial creatinine, eGFR, and electrolyte assessments and several unresolved statistical decisions.
- targeted upper-extremity rehabilitation after stroke, a severity-stratified randomized trial with a protocol-to-SAP change from percent-change ANOVA to repeated-measures modeling;
- Biobehavioral Pathways Underlying Alcohol Use and Health, a nonrandomized two-cohort feasibility intervention with six operational feasibility thresholds;
- total-knee-arthroplasty NMES, a randomized mechanistic rehabilitation study with fiber-level, mitochondrial, and functional outcomes;
- pediatric iron-deficiency anemia treated with ferric carboxymaltose, a Phase III active-controlled study with documented protocol-to-SAP population, imputation, laboratory-grading, and subgroup changes.
- collaborative-care rehabilitation after dysvascular transtibial amputation, a sex-stratified randomized trial with a protocol-to-SAP switch to maximum-likelihood repeated measures;
- technology-enhanced diabetes coaching, whose randomized TEC-versus-peer-support comparison is kept distinct from its observational usual-care cohort;
- G-FLIP plus vitamin C in advanced pancreatic cancer, a single-arm Phase II study with randomized vitamin-C timing only for acute safety;
- computerized e-SBI for risky alcohol use among women of childbearing age, a developmental randomized trial with GEE, imputation, and explicitly post-hoc drink-size analyses;
- VM202 for painful diabetic peripheral neuropathy, a Phase III fixed-sequence trial with continuous and responder repeated-measures models and extensive missing-data sensitivity analyses;
- twice-weekly versus thrice-weekly hemodialysis, a randomized crossover equivalence study using KDQOL-36 and a -5 to +5 margin.
- SELECT, an event-driven Phase 3b cardiovascular outcomes trial with an ITT treatment-policy estimand, group-sequential alpha spending, competing risks, and gated confirmatory endpoints;
- SC1401 sarecycline for acne, a Phase 3 placebo-controlled trial with lesion-count and IGA co-primary endpoints, center-adjusted methods, and explicit missing-data sensitivity analyses;
- NI071F2 RADIANCE, a three-stage rheumatoid-arthritis biosimilar trial combining asymmetric-margin efficacy biosimilarity with gated PK interchangeability after switching;
- physical telerehabilitation in veterans with multiple sclerosis, an assessor-blinded randomized trial with EDSS-stratified allocation, co-primary mobility outcomes, and longitudinal mixed models;
- CORIN, an open-label randomized Phase II adjuvant-icotinib trial with a three-year DFS proportion and supportive time-to-event analyses;
- CA209923 nivolumab in severe sepsis, a small randomized Phase 1b study centered on descriptive safety, noncompartmental PK, receptor occupancy, biomarkers, and immunogenicity.
- bertilimumab in ulcerative colitis, a small exploratory randomized study with a post-protocol mITT, safety-exposure, and missing-data reconciliation;
- CP007A Cat-PAD follow-up, a prospective annual durability study with inherited randomized groups, yearly populations, hierarchical annual testing, and multiple missing-data analyses;
- SILVER BULLET ivermectin in COVID-19, a compact randomized Phase II study retained with explicit population, safety-set, and malformed-hypothesis confirmation requirements;
- ULTIMATE II in relapsing multiple sclerosis, a Phase III active-controlled trial with negative-binomial relapse modeling, cross-study fixed-sequence testing, and blinded sample-size reassessment;
- SPECTRI lampalizumab in geographic atrophy, a Phase III sham-controlled ophthalmology trial whose final SAP supersedes the protocol's primary hierarchy and adds extensive MAR/MNAR sensitivity analyses.
- ProDERM, a randomized Phase III dermatomyositis trial with Week-16 TIS response, GDA-stratified CMH analysis, nonresponder handling, and an open-label extension;
- NNC0114-0006 in newly diagnosed type 1 diabetes, a four-arm double-dummy trial using relative MMTT C-peptide AUC and log-scale repeated-measures estimation;
- EINSTEIN Junior, an open-label pediatric VTE trial whose efficacy and bleeding comparisons are intentionally descriptive rather than powered non-inferiority claims;
- RECAST SLE, a three-arm exploratory Phase II trial with a composite BICLA plus oral-glucocorticoid response estimand and alpha-0.10 comparisons;
- B19-227 DSM265 relative bioavailability and food effect, a Phase I PK study with log-ANOVA contrasts and a 0.80–1.25 interval rule;
- obturator nerve block added to adductor canal block for total knee arthroplasty, a compact randomized trial retaining unresolved opioid derivation, population, and missing-data decisions;
- high-frequency-oscillation guidance in pediatric epilepsy surgery, a small randomized trial with time-to-event and binary seizure-free analyses and unresolved censoring details;
- SEPSIS-ACT, an adaptive Phase IIb/III selepressin trial with response-adaptive randomization, P&VFD, van Elteren testing, predictive probabilities, and Hochberg multiplicity.
- pediatric Prepopik dose ranging, an assessor-blind age-stratified study with Aronchick response, exact confidence intervals, and ITT nonresponse handling;
- oral DS107G in atopic dermatitis, a placebo-controlled Phase II study with a composite IGA responder, site-stratified CMH analysis, and observed-value versus LOCF analyses;
- aflibercept quality of life in DME, a single-arm Phase IV study with Week-52 NEI VFQ-25 change and LOCF, observed-case, multiple-imputation, MCID and repeated-measures analyses;
- ENLIGHTEN-2, an adaptive Phase III active-controlled schizophrenia trial with weight co-primary endpoints, CHW inference, conditional-power sample-size reassessment, fixed-sequence testing and MNAR sensitivity.
- emricasan after liver transplantation for HCV-related fibrosis, a Phase II screening trial whose SAP changes the protocol's ordinal Ishak analysis to a stage-dependent binary response and adds multiple-imputation sensitivity analyses;
- sedative effects on neurological function in eloquent-area glioma, a nonrandomized glioma-versus-control repeated-measures study with unresolved primary contrast, covariance, missingness and multiplicity choices;
- adjunctive naltrexone plus bupropion in obese cigarette-smoking adults with schizophrenia, a stratified randomized study using a Week-24 weight contrast and longitudinal mixed modeling;
- roxadustat for anemia in nondialysis-dependent CKD, a Phase III amendment-transition study with region-specific primary endpoints, MI ANCOVA, CMH analysis, fixed-sequence testing and MNAR sensitivity analyses.
- long-term rIX-FP in hemophilia B, a Phase IIIb extension with exposure-qualified inhibitor incidence, regimen-specific bleeding rates, fixed-sequence noninferiority and separate surgery and subcutaneous substudies;
- ultrasound-assisted labor epidural placement in patients with BMI at least 40, a compact randomized device study retaining unresolved analysis-set, missingness, site/provider and multiplicity decisions.
- SPARK right-ventricular pacing in heart failure with RBBB, a single-blind two-period crossover pilot with an unresolved binary-versus-continuous primary-endpoint definition and crossover-model choices;
- water exchange versus cap-assisted water-exchange colonoscopy, a multicenter randomized procedure study with sex-specific powering, O'Brien-Fleming interim monitoring, hierarchical site/provider effects and FDR-controlled exploratory analyses.
- home-based NMES or progressive exercise for subacute low back pain in active-duty service members, a three-arm longitudinal rehabilitation study with multiple strength, activity, mobility and patient-reported outcomes.
- Meds to Beds versus standard pharmacy pickup for hospitalized adults with heart failure, a two-arm pilot with adherence, 30-day health/utilization, feasibility and mechanism outcomes.
- mHealth for uncontrolled hypertension among adults experiencing homelessness, a two-site randomized mixed-methods study with blood-pressure, adherence, appointment-attendance, engagement and qualitative outcomes.
- paired-eye PRK pain control comparing CBD with codeine/acetaminophen, a randomized two-period crossover retaining unresolved pain-endpoint, unit-of-analysis, covariance and carryover decisions.
- venlafaxine for subcortical aphasia, a randomized longitudinal clinical and multimodal-neuroimaging study with WAB, task/rest fMRI and DTI analyses.
- neuropilates versus generalized exercise in chronic stroke, an assessor-blinded randomized feasibility pilot with an unresolved protocol-versus-registry primary-endpoint hierarchy and a missing randomized between-group analysis.
- TIGER prehospital high-sensitivity troponin testing, an open 2:1 randomized EMS trial retaining unresolved primary time-event terminology, post-randomization MI-population selection, MACE definition, missing-data and interim-monitoring decisions.
- long-term open-label valbenazine treatment for tardive dyskinesia, a single-arm fixed-dose-titration safety study with dose-trajectory groups, visit mapping, descriptive AIMS response and extensive safety displays.
- VA LC-DPP in Veterans with prediabetes, a single-arm mixed-methods feasibility pilot with recruitment, retention and adherence denominators, repeated metabolic and patient-reported outcomes, instrument scoring and qualitative directed-content analysis.
- intercostal-block timing in thoracoscopic surgery, a randomized perioperative comparison with repeated postoperative pain, analgesic-use, hospitalization and complication outcomes and a terse reference analysis plan requiring explicit methodological adjudication.
- PALMS-II web-based cognitive self-management in multiple sclerosis, a mixed-methods pilot with a qualitative adaptation phase and randomized assessor-blind feasibility phase, multiple cognitive, self-management, activity and sleep outcomes, and an intentionally under-specified reference ANCOVA requiring explicit adjudication.
- cerebral blood flow during propofol anesthesia, a randomized-order within-participant three-MAP experiment with carotid-flow derivation, gas corrections, REML repeated-measures and slope-interaction models, and unresolved covariance, partial-sequence and multiplicity decisions.
- EVAC-HF, a multicenter randomized PVC-suppression study with six-month LVEF change, prospective power assumptions, crossover-aware ITT analysis and unresolved estimand and missing-data choices;
- platelet-rich plasma for non-scarring alopecia, a randomized saline-controlled study with repeated photographic and trichoscopic outcomes and an intentionally terse reference analysis plan;
- peri-incisional multimodal injection for operative ankle fractures, a randomized blinded perioperative study with repeated pain, opioid-use, hospitalization and discharge outcomes and separately tracked prospective versus actual enrollment.
- D-cycloserine augmentation of panic-focused smoking cessation, a randomized behavioral trial with abstinence, lapse, relapse, psychological and mediation outcomes and an independent analysis document specifying logistic mixed models, Cox models, Bayesian-bootstrap mediation and pattern-mixture sensitivity analysis.
- IOPCL AMD-MAG for near vision in age-related macular degeneration, a unilateral early-feasibility device study with responder thresholds, positional-stability and safety targets, eye-level analysis and unresolved estimand, missingness and multiplicity decisions.
- AMC glaucoma surgery, a multicenter randomized AGV trial with stratum-adjusted analyses and unresolved primary-timepoint and surgeon-masking conflicts;
- PAFIT-IBD, a prospective pediatric single-arm exercise study with 20mSRT, accelerometry, longitudinal and mediation analyses and an unresolved primary-outcome hierarchy;
- FITSTART+, a parent-randomized digital alcohol-prevention study with student repeated outcomes, HGLMs, missingness sensitivity and unresolved sample-size and outcome-family decisions.

- ENRICH FCU-Heart, a 2:1 randomized Type 1 hybrid effectiveness-implementation pilot with maternal cardiovascular, child and implementation outcomes, a terse independent t-interval plan and unresolved endpoint hierarchy, race-stratum, estimand and missing-data decisions.
- active versus placebo TENS during outpatient endometrial biopsy, a double-blind randomized device study with repeated VAS outcomes, a baseline-adjusted primary regression and unresolved baseline-covariate, population, missingness and multiplicity decisions.
- Healthy Detours versus FatSecret in college students, a 12-week randomized digital-health trial with HEI, activity, sleep and quality-of-life outcomes, ANCOVA, a Hotelling omnibus test, longitudinal GLS, CACE and exploratory mediation.
- soluble epoxide hydrolase inhibition in insulin resistance, a double-blind two-period crossover mechanistic study with clamp-derived insulin sensitivity, vascular and tissue biomarkers, paired testing and explicit carryover, period, provenance and missing-data gates.
- diaphragm manual therapy or hypopressive exercise for rotator-cuff injury, a three-arm immediate pre/post physiotherapy study whose terse reference plan leaves endpoint hierarchy, sample size, baseline adjustment, multiplicity and missingness for expert adjudication.
- HOME DM-BAT, a randomized behavioral-activation trial in low-income older adults with type 2 diabetes whose exact-date protocol/analysis-plan pair supports a 12-month HbA1c mixed-effects analysis under explicit post-completion provenance and control-description gates.
- Abriendo Caminos 2, a multisite family-randomized childhood-obesity prevention study with nested longitudinal BMI-percentile and behavioral outcomes, an exploratory multilevel mixture model, and explicit governing-pair, 250-versus-500-family, allocation-unit and model-selection gates.
- PPI initiation or withdrawal in decompensated cirrhosis, a nonrandomized paired microbiota study whose exact-date one-page analysis plan supplies Wilcoxon and Kruskal-Wallis methods while leaving feature derivation, group contrast, sample size, confounding, missingness and multiplicity unresolved; the already-published compensated and healthy cohorts are excluded.
- therapeutic drug monitoring of mycophenolate mofetil in lupus nephritis, a prerecruitment randomized trial with a binary 12-month remission endpoint, ITT analysis, unadjusted and adjusted comparisons, and explicit parallel-versus-sequential, masking, remission-definition, alpha, sample-size and missing-data gates.
- HCV video versus brochure education delivery, a prerecruitment nonrandomized matched behavioral study with repeated knowledge assessment and explicit group-label, endpoint-hierarchy, matching, clinic, sample-size, missing-data and multiplicity gates.
- DIPPER SafeBreak Vascular, a randomized open-label hospital device trial with conditional noninferiority/superiority, therapy-delay and recurrent PIV-complication outcomes, and explicit margin, population, censoring, missingness and power gates.
- long versus short radial introducer sheaths, a prerecruitment randomized interventional-cardiology pilot with Doppler-ultrasound RAO, procedural complications, Fisher and Mann-Whitney reference methods, and explicit masking, population, missing-ultrasound, multiplicity and sample-size gates.
- Reward Re-Training versus supportive group therapy for binge eating, a remote randomized pilot with feasibility thresholds, four-time-point multilevel models, mediation, structured missing-data sensitivity analyses and explicit allocation, population, percent-change, multiplicity and power gates.
- over-the-counter SARS-CoV-2 antigen-test evaluation, a prospective paired diagnostic-accuracy study with lay-user antigen testing, trained-collector RT-PCR comparison, valid-run and discordance rules, PPA/NPA thresholds, symptom and Ct summaries, and explicit sample-size, interval, missingness, multiplicity and dependence gates.
- active choice versus GP-like advice for hypothetical cardiovascular risk, a prerecruitment randomized web experiment with three immediate psychological primary outcomes, endpoint-specific regressions, composite and coding rules, prospective n=724, and explicit instrument-version, age-range, bundled-estimand, confounder, modifier and multiplicity gates.
- mirror-aided resisted cross-education versus unresisted mirror therapy after stroke, a prerecruitment randomized home-rehabilitation pilot with repeated strength and impairment outcomes, supplementary paired tests, and explicit registry-binding, masking, endpoint-hierarchy, between-group, feasibility, safety, missingness, multiplicity and sample-size gates.

All 101 public studies have first-pass annotations. Together with the private pilot, the registered set contains 1,948 evidence-backed requirements: 1,922 for the public studies and 26 for the private pilot. All public families remain unsplit until independent review and leakage checks are complete.

The local study package contains a protocol, a CRF, an annotated CRF candidate, and a later reference SAP. The protocol and reference SAP versions are separated by time and must be treated as a version-matching risk until manually confirmed.

## Permitted use

The pilot may be used to:

- test document extraction and evidence locators;
- refine rubric applicability rules;
- debug baseline generation and scoring;
- build an initial error taxonomy;
- estimate annotation time.

It must not be used as a frozen final test case because it has already influenced prompts, hard gates, and implementation decisions in the existing system.

## Evidence locator policy

- Native PDFs use one-based page numbers plus a text excerpt.
- DOCX files use stable one-based paragraph IDs such as `p0406` plus a text excerpt.
- Table evidence uses table and row IDs emitted by the extraction tool.
- Page mapping for DOCX will be added only after a Chinese-capable deterministic renderer is available.

Local LibreOffice rendering was inspected during v0.1 construction and showed missing Chinese glyphs. This does not affect native DOCX text extraction, but it prevents trustworthy page-level citation from the rendered copy.

## Privacy and redistribution

The manifest records local paths and hashes but does not copy source clinical documents into the benchmark directory. Redistribution permission has not been established. A public release must contain only authorized files or source identifiers, URLs, hashes, schemas, and derived annotations permitted by the source terms.

Public documents are therefore remote-only by default. The downloader verifies their frozen SHA-256 hashes after retrieval. A source being publicly downloadable is not treated as blanket permission to redistribute it in this repository.

## Known biases

- only 101 public studies have first-pass gold annotations, with no completed expert adjudication;
- English-language public sources dominate the expansion set;
- the only current protocol/CRF pair is observational;
- unusually detailed protocol statistics;
- ophthalmology-specific endpoint and eye-handling rules;
- prior exposure during system development;
- reference SAPs may contain operational choices not inferable from the protocol;
- registry availability favors completed studies with results-reporting obligations.

## Planned v0.3 composition

The release-eligible intake contains 120 study-family slots, of which 19 remain metadata-screened acquisition candidates and 101 are version-verified annotation drafts. Candidate independence remains provisional until document-level review. The frozen release floor is 100 independently adjudicated families, with a 40/20/40 train/dev/test split. The next annotation sprint should continue promoting design-diverse pairs while expert review proceeds independently on the existing drafts.
