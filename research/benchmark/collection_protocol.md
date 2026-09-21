# Study Collection and Pairing Protocol v0.1

## Candidate inclusion

A study family is eligible when it has:

- a full interventional trial protocol or a protocol with sufficient statistical sections;
- a distinct SAP suitable for annotation and discrepancy analysis;
- identifiable study ID, title, versions, and dates;
- readable files with recoverable tables and key statistical content;
- source terms compatible with the intended internal use.

A matching CRF is desirable but not required for the primary track.

Public availability alone is insufficient. The exact protocol version cited by the SAP must be available, or the family remains on hold. A later protocol upload cannot be silently paired with an earlier SAP.

## Exclusion

Exclude or quarantine:

- SAP-only studies without a matching protocol;
- protocol/SAP pairs with unresolved study-ID mismatch;
- duplicate or near-duplicate study families;
- files missing critical pages;
- combined documents where target SAP content cannot be cleanly isolated from model input;
- documents whose extraction cannot preserve key equations or tables;
- study families already used extensively during development when selecting the final test set.

Every exclusion is logged with a reason; excluded documents are not silently discarded.

## Pairing checklist

For each candidate:

1. match study ID and official title;
2. record protocol and SAP version/date;
3. identify amendments and SAP revisions;
4. check whether SAP cites a later protocol version;
5. confirm population, interventions, randomization, primary endpoints, and planned sample size agree at a coarse level;
6. hash every file;
7. assign a study-family ID before splitting;
8. record language, domain, intervention type, design, hypothesis type, and endpoint type;
9. record redistribution constraints;
10. assign `candidate`, `verified`, `pilot_only`, or `excluded` status.

For public remote documents, also record the canonical URL, byte-level SHA-256 hash, internal document version/date, retrieval date, page count, encryption status, and whether text extraction preserves the statistical sections. Raw source files are not committed unless redistribution terms have been reviewed.

## Public-source promotion states

- `screened`: metadata suggests a useful family, but documents have not been inspected.
- `hold_version_mismatch`: the SAP cites a protocol or CRF version that is not available.
- `verified`: identifiers, versions, dates, coarse design facts, hashes, and text extractability have been checked.
- `annotated_draft`: first-pass requirements exist but still need statistical and second-annotator review.
- `split_ready`: source rights, leakage audit, version chain, and annotation review are complete.

## Pilot sampling plan

The first 10-15 verified families should collectively include:

- continuous, binary, and time-to-event primary endpoints;
- superiority and non-inferiority designs;
- drug and device studies;
- at least one study with multiplicity control;
- at least one study with repeated measurements;
- at least one long-document challenge where key evidence appears late.

The goal is statistical-design coverage, not broad disease representativeness at v0.2.
