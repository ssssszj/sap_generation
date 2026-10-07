# Task packet: current thesis plan and handoff

## Objective

Update the graduation-project plan and handoff to the completed 100-question draft benchmark state, commit only the intended research documentation, and push the existing thesis branch without force.

## Required facts

- 100 retained draft questions, not expert-approved/frozen.
- 141 public annotated drafts: 100 keep, 21 hold, 20 exclude.
- 2,589 public requirements; 1,771 in the retained 100; 2,615 including the private pilot.
- Three benchmark command gates return zero errors; the validator still reports two pre-existing private-pilot warnings.
- The existing 179 unpushed commits are all under `research/` and form the benchmark construction history.

## Files in scope

- `plan/project-overview.md`
- `plan/outline.md`
- `plan/progress.md`
- `plan/task-packets/2026-10-07-thesis-plan-and-handoff.md`
- `research/docs/SAP_毕业设计研究方案_2026-10-07.md`
- `research/docs/HANDOFF.md`
- `/Users/bytedance/school/handoff.md` (external synchronized copy; not in Git)

The superseded `research/docs/SAP_毕业设计研究方案_2026-09-11.md` is renamed to the current date so its Git history is preserved.

## Out of scope

- Application code, package files, Electron files, and other user-owned dirty changes.
- Expert adjudication, split freezing, model training, final evaluation, or deployment.
- Editing the existing DOCX/PPTX opening materials unless explicitly requested later.

## Verification gates

1. Parse and count the final-audit JSON/JSONL artifacts.
2. Run all three benchmark validation commands.
3. Run `git diff --check` on the documentation and benchmark paths.
4. Confirm staged files are exactly the scoped files.
5. Confirm the remote branch is an ancestor and the outgoing commits touch only `research/` plus this documentation task's `plan/` files.
6. Push with a normal non-force `git push origin thesis/sap-benchmark-posttraining`.
