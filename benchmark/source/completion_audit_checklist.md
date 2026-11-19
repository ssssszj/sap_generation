# Initial Benchmark Completion Audit

## Objective and release boundary

The user set a final collection ceiling of 100 retained questions. The concrete initial deliverable is therefore:

1. finish first-pass annotations for every one of the 141 registered public studies;
2. audit every study against source separation, prospective chronology, version/provenance, leakage, requirements, and package-integrity gates;
3. deliver only studies that clear those gates as draft questions;
4. close the actionable review queue when 100 retained questions are reached;
5. retain the private pilot outside the public question set; and
6. label all retained questions `draft_needs_expert_review`, never expert-approved or frozen.

## Prompt-to-artifact checklist

| ID | Requirement | Artifact/evidence | Verified result |
|---|---|---|---|
| C01 | Audit every registered public draft | `final_audit/questions.jsonl` | 141 unique rows exactly cover the 141 non-pilot study IDs |
| C02 | Deliver a usable initial question list | `final_audit/initial_draft_question_set.json` | 100 IDs, exactly equal to the audit's `keep_draft` rows |
| C03 | Stop at the authorized ceiling | archived catalog, empty review queue, config | actionable candidate count is 0 after reaching 100 retained questions |
| C04 | Keep the private pilot out | `PILOT-IOL-001`, `splits/pilot.json` | one `pilot_only` study; absent from the 100-study question set |
| C05 | Protocol and independent reference SAP per audited study | study/document manifests and local packages | final audit resolves input/reference document IDs and local frozen files for all 141 |
| C06 | Reference SAP never model-visible | document roles and `input/` versus `reference/` paths | checked per row by final audit |
| C07 | Prospective governing version chain | registry chronology, document dates, annotation questions | 100 pass the draft-level gate; all 34 additions have SAP dates before exact actual start; 21 held; 20 fail |
| C08 | Independent study families | unique `study_family_id` and NCT binding | one row per registered family; no family crosses splits |
| C09 | No executable protocol leakage | batch review packets and final review | retained rows passed the final draft leakage review |
| C10 | No results/CSR/execution-informed target | registry chronology and selected reference text | 20 post-primary or execution-informed targets excluded |
| C11 | Complete first-pass annotations | `gold/*/requirements.jsonl` | 141 public files, 2,589 items, 12-25 items per study; the retained 100 contain 1,771 items |
| C12 | Evidence locators | requirement evidence plus page-range audit | every item has document ID, locator and excerpt; all 34 additions pass normalized excerpt replay on the cited physical pages (with the documented OCR exception for scan-only NCT03231228); expert semantic adjudication remains required |
| C13 | Prospective sample-size rule | requirements and review packets | actual enrollment is not accepted as a substitute for the prospective target |
| C14 | Honest annotation maturity | 141 `annotation_status.json` files | all say `draft_needs_expert_review`; zero expert-approved/frozen |
| C15 | Package integrity | validator and final-audit script | unique IDs, resolvable references, count-matched statuses, and exact question-set agreement |
| C16 | Batch provenance | historical packets plus the 2026-10-05 expansion packet and changelog | the 34 additions have an explicit review packet; VIVID and IMPACT are covered by the terminal audit rather than a historical packet |
| C17 | Machine validation | `validate_benchmark.py` | must finish with zero errors; warnings are reported, not treated as approval |
| C18 | JSON/JSONL and patch integrity | direct parser checks and `git diff --check` | required at delivery |
| C19 | Scope isolation | Git status/diff | only `research/benchmark/` may be staged or committed |
| C20 | Release-size claim | README, data card, config | 141 annotated, 100 retained, 21 held, 20 excluded, 0 expert-approved/frozen |

## Required command gates

```bash
python3 research/benchmark/tools/finalize_initial_benchmark.py --check
python3 research/benchmark/tools/audit_initial_delivery.py
python3 research/benchmark/tools/validate_benchmark.py
git diff --check -- research/benchmark
```

The user-authorized collection ceiling has been met: 141 public studies are fully annotated and dispositioned, and 100 defensible drafts are exported explicitly. This completes acquisition and first-pass annotation, but it does not mean expert adjudication or a frozen benchmark release is complete.
