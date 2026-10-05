# Expert Review Packet: Expansion to 100 Questions

## Scope and status

This batch adds 34 independent ClinicalTrials.gov study families to the 66-study retained baseline and stops collection at exactly 100 draft questions. Each selected family has a separate model-visible protocol and reference-only SAP, a frozen source URL and SHA-256 hash, actual primary-completion chronology, and 12-25 first-pass evidence-backed requirements. All additions remain `draft_needs_expert_review`; none is expert-approved or frozen.

The full terminal audit now covers 141 annotated public drafts: 100 retained, 21 held for version or provenance resolution, and 20 excluded from the initial question set. The private pilot remains outside the public set.

## Newly retained families

The following 34 registry families were added after manual review of document identity, chronology, prospective wording, protocol leakage, and family independence:

`NCT06814470`, `NCT04755660`, `NCT03701113`, `NCT03198000`, `NCT05516134`, `NCT03256253`, `NCT05016960`, `NCT03231228`, `NCT03954626`, `NCT03744780`, `NCT03835325`, `NCT03876171`, `NCT03835403`, `NCT05430854`, `NCT05307523`, `NCT03397277`, `NCT04239612`, `NCT03332004`, `NCT04674111`, `NCT04126031`, `NCT03324659`, `NCT03805412`, `NCT05001165`, `NCT04026503`, `NCT03308877`, `NCT03576976`, `NCT04858035`, `NCT04759157`, `NCT03203291`, `NCT04596085`, `NCT05012657`, `NCT05013762`, `NCT02816723`, and `NCT05208593`.

## Final replacement audit

Six initially selected candidates were removed before the first 100-question materialization:

- `NCT02676895` — hold: the SAP is based on Protocol v3.0, but the available prompt document is Protocol v1.0.
- `NCT06340854`, `NCT05014919`, `NCT02746991`, and `NCT02890381` — exclude: the model-visible protocols substantially disclose the target statistical plan.
- `NCT03387813` — exclude: its SAP added a COVID-19 sensitivity analysis after study conduct began.

Their replacements were `NCT03231228`, `NCT05430854`, `NCT05307523`, `NCT03332004`, `NCT03324659`, and `NCT05001165`. A subsequent strict semantic audit removed nine more formerly retained families. `NCT02593825` has only a month-level actual start; `NCT02041494` and seven other post-start families (`NCT03212144`, `NCT03210402`, `NCT03529981`, `NCT03704116`, `NCT03691428`, `NCT04786184`, and `NCT05319977`) lacked affirmative evidence that the selected target was finalized before unblinding and independently of accumulating outcomes. They were replaced one-for-one by `NCT03576976`, `NCT04858035`, `NCT04759157`, `NCT03203291`, `NCT04596085`, `NCT05012657`, `NCT05013762`, `NCT02816723`, and `NCT05208593`.

The following cases require particular expert attention:

- `NCT03231228`: SAP explicitly binds to protocol HC-G-H-1601 v2.0 and states that analysis was specified before database lock; the protocol is scan-only and evidence extraction uses page-aligned OCR.
- `NCT03835403`: the target is post-start, but no formal interim analysis was planned; only an independent DSMB could review grouped unblinded safety results while investigators remained blinded. Confirm the exception independently.
- `NCT05430854`: protocol and SAP explicitly bind v1. The SAP is two days after actual start, has an empty revision history, and the protocol requires finalization before database lock; verify that it remained outcome-uninformed.
- `NCT05307523`: files share official title and date in one registry record, but their contemporaneous NCT fields are blank; confirm this provenance chain independently.
- `NCT03332004`: files share date, title, investigator, and protocol identifier 736513.A287/C.E./2013 and predate actual start by almost three years. The protocol does not disclose the SAP's Simon design, diagnostic-performance calculations, McNemar comparisons, or ROC analysis.
- `NCT03324659`: both files share the study title and predate actual start, but state that an NCT number was not yet available; confirm the registry binding. The protocol gives only a broad descriptive/effect-size/correlation framework, while the SAP fixes endpoint-specific tests, thresholds, and repeated-measures MANOVA.
- `NCT05001165`: the SAP was uploaded before actual start. Both files share date, title, PI, and institution but state that the NCT number was not yet assigned; the protocol was uploaded later and is not chronology evidence. Confirm the binding, and confirm that the SAP was not replaced after its pre-start upload.
- `NCT04759157`, `NCT03203291`, and `NCT04596085`: each selected SAP predates the selected protocol revision, but the paired registry-hosted documents share an explicit NCT or protocol identifier and both predate actual start; confirm that each later protocol remains the governing model input.
- `NCT05208593`: the same-date protocol and SAP share title and unique protocol ID `IRB20201070D`, but both predate NCT assignment; confirm their registry binding.
- `NCT03576976`, `NCT04858035`, `NCT05012657`, `NCT05013762`, and `NCT02816723`: all have exact pre-start target dates and substantial analysis detail unique to the SAP; recheck that no protocol section materially reconstructs the hidden methods.

## Expert-review priorities

1. Recheck the governing protocol/SAP identity and chronology for every added family, especially the six replacement cases above.
2. Verify all one-based physical PDF page locators and quoted evidence against the frozen hashes.
3. Adjudicate every `confirmed_decisions` item and every `needs_confirmation` item; reference-only facts must never be treated as inferable in `protocol_only`.
4. Confirm that protocol-visible content does not make the hidden SAP substantially reconstructable.
5. Confirm that no wording, amendment, interim decision, or realized enrollment reveals outcome- or conduct-informed target construction.
6. Keep the collection capped at 100; if expert review removes a family, replace it one-for-one with another independent family.
