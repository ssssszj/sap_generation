# Expert Review Packet — Batch 39

## Scope

Batch 39 reviewed eight ClinicalTrials.gov protocol/SAP families. None passed the benchmark's independent-target gate. Seven model-visible protocols directly expose executable analysis methods. The remaining family also has an irreconcilable protocol-version mismatch and substantial protocol leakage.

All 16 selected PDFs and eight registry records were downloaded and hash-frozen. The two additional NCT03926130 protocol/SAP documents were also inspected to test whether the registry's alternate adult/adolescent pairing could rescue the family; it could not. Full text was extracted for all documents except the scan-only NCT05550337 SAP, whose protocol alone supplied decisive evidence. Covers and decisive statistical pages were rendered and visually checked.

## Exclusions

- `NCT01603602` — protocol pages 13–14 and 42–49 expose mITT/safety sets, ANCOVA/logistic models, MI/MMRM, alpha, gatekeeping and power.
- `NCT05550337` — protocol pages 63–67 expose populations, LOCF, CMH, ANOVA equivalence and superiority rules, alpha/multiplicity and simulation-based sample size.
- `NCT02548585` — protocol pages 12 and 111–115 contain a statistical-plan synopsis with populations, ANCOVA, missingness, interim analysis and detailed power.
- `NCT03926130` — the selected files mismatch the adolescent addendum protocol with the adult SAP; the alternative files reverse the mismatch, and both protocols expose NRI/MMRM, populations, sample size and multiplicity.
- `NCT02273960` — 2016 Amendment 6 cannot be governed by the 2015 draft SAP; protocol pages 6, 11 and 101–103 expose Bayesian adaptive dose modeling.
- `NCT03558997` — protocol pages 15 and 69–74 expose sets, 40-fold MI, ANCOVA/rank ANCOVA, LOCF sensitivity, multiplicity and sample size.
- `NCT02569710` — SAP page 10 cites protocol v8.1 rather than public v10; protocol pages 92–97 independently expose descriptive/CI, population, pooling and subgroup rules.
- `NCT01885078` — protocol pages 6–7 and 58–62 expose ITT, NRI/MI/mLOCF, MMRM, Kaplan-Meier/Cox, ANCOVA and sample-size methods.

## Review gate

No Batch 39 candidate enters the draft benchmark. All eight slots must be replenished; none may be assigned to train/dev/test.
