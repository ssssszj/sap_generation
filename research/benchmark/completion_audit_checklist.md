# Initial Benchmark Completion Audit

## Objective and release boundary

The user stopped acquisition and chose the currently annotated public collection. The concrete initial deliverable is therefore:

1. finish first-pass annotations for every one of the 107 registered public studies;
2. audit every study against source separation, prospective chronology, version/provenance, leakage, requirements, and package-integrity gates;
3. deliver only studies that clear those gates as draft questions;
4. archive the 13 metadata-only candidates without counting them as questions or exclusions;
5. retain the private pilot outside the public question set; and
6. label all retained questions `draft_needs_expert_review`, never expert-approved or frozen.

## Prompt-to-artifact checklist

| ID | Requirement | Artifact/evidence | Verified result |
|---|---|---|---|
| C01 | Audit every registered public draft | `final_audit/questions.jsonl` | 107 unique rows exactly cover the 107 non-pilot study IDs |
| C02 | Deliver a usable initial question list | `final_audit/initial_draft_question_set.json` | 66 IDs, exactly equal to the audit's `keep_draft` rows |
| C03 | Do not count stopped candidates | archived catalog, empty review queue, config | 13 metadata-only records archived; actionable candidate count is 0 |
| C04 | Keep the private pilot out | `PILOT-IOL-001`, `splits/pilot.json` | one `pilot_only` study; absent from the 66-study question set |
| C05 | Protocol and independent reference SAP per audited study | study/document manifests and local packages | final audit resolves input/reference document IDs and local frozen files for all 107 |
| C06 | Reference SAP never model-visible | document roles and `input/` versus `reference/` paths | checked per row by final audit |
| C07 | Prospective governing version chain | registry chronology, document dates, annotation questions | 66 pass at draft gate; 21 held; 20 fail |
| C08 | Independent study families | unique `study_family_id` and NCT binding | one row per registered family; no family crosses splits |
| C09 | No executable protocol leakage | batch review packets and final review | retained rows passed the final draft leakage review |
| C10 | No results/CSR/execution-informed target | registry chronology and selected reference text | 20 post-primary or execution-informed targets excluded |
| C11 | Complete first-pass annotations | `gold/*/requirements.jsonl` | 107 public files, 2,066 items, 12-25 items per study |
| C12 | Evidence locators | requirement evidence plus page-range audit | every item has document ID, locator and excerpt; numeric locators remain within PDF page counts; semantic confirmation is an expert-review gate |
| C13 | Prospective sample-size rule | requirements and review packets | actual enrollment is not accepted as a substitute for the prospective target |
| C14 | Honest annotation maturity | 107 `annotation_status.json` files | all say `draft_needs_expert_review`; zero expert-approved/frozen |
| C15 | Package integrity | validator and final-audit script | unique IDs, resolvable references, count-matched statuses, and exact question-set agreement |
| C16 | Batch provenance | 172 review packets plus changelog | 105 public studies appear in batch packets; VIVID and IMPACT are covered by the terminal audit rather than a historical packet |
| C17 | Machine validation | `validate_benchmark.py` | must finish with zero errors; warnings are reported, not treated as approval |
| C18 | JSON/JSONL and patch integrity | direct parser checks and `git diff --check` | required at delivery |
| C19 | Scope isolation | Git status/diff | only `research/benchmark/` may be staged or committed |
| C20 | Release-size claim | README, data card, config | 107 annotated, 66 retained, 21 held, 20 excluded, 0 frozen |

## Required command gates

```bash
python3 research/benchmark/tools/finalize_initial_benchmark.py --check
python3 research/benchmark/tools/audit_initial_delivery.py
python3 research/benchmark/tools/validate_benchmark.py
git diff --check -- research/benchmark
```

The historical 120-intake and 100-frozen-floor targets are not met and are not completion proxies. Completion of this initial delivery means the selected 107-study collection is fully annotated and dispositioned, with the 66 defensible drafts exported explicitly. It does not mean expert adjudication or a frozen benchmark release is complete.
