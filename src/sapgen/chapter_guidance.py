"""Study-independent SAP drafting checks, distilled from the former guide.

The old knowledge_bank/sap_guides.md supplies the chapter checklist. ICH E9
and E9(R1) supply the general principles of prespecification and alignment of
objective, estimand, estimator, and sensitivity analysis. This module contains
no protocol facts, benchmark rubric, or reference SAP content.
"""

GUIDANCE_BOUNDARY = (
    "These are general drafting checks, not study evidence or mandatory choices. "
    "Use a check only when relevant to the study design and supported by the SAP-IR. "
    "Never infer a method, threshold, population, timepoint, or decision rule from "
    "this guidance. Mark an unsupported choice as proposed for confirmation or "
    "unresolved, consistent with the SAP-IR."
)

CHAPTER_GUIDANCE: dict[str, str] = {
    "section-overview": (
        "Keep the objective, design, arms, control, masking, treatment periods, and "
        "follow-up consistent with the protocol. Distinguish planned design from "
        "analysis decisions; do not assert a phase, registration, or approval status "
        "that is absent from the source."
    ),
    "section-randomization-sample": (
        "Separate allocation ratio, randomization method, strata, concealment, and "
        "analysis adjustment. For sample size, distinguish planned N from the "
        "calculation assumptions, effect size, variability/event rate, power, alpha, "
        "and attrition; report only supported values and their source."
    ),
    "section-endpoints-estimands": (
        "Keep each objective tied to its endpoint, measure, timepoint, and analysis "
        "role. When a treatment effect is targeted, distinguish treatment, population, "
        "variable, intercurrent-event strategy, and population-level summary. Do not "
        "fabricate an estimand for descriptive or exploratory questions."
    ),
    "section-populations": (
        "Specify membership and exclusions in operational terms, and state which "
        "population applies to each analysis. Keep randomized assignment distinct "
        "from treatment received and from safety exposure; do not impose ITT, PPS, "
        "or safety-set defaults without support."
    ),
    "section-conventions": (
        "Clarify summary statistics, precision, confidence intervals, reference "
        "baseline, analysis visit, strata/covariates, and software only when applicable. "
        "Do not convert descriptive analyses into tests or supply a conventional "
        "alpha level by default."
    ),
    "section-methods": (
        "For each supported endpoint, link the target question to the population, "
        "outcome, comparison, estimator/model, covariates, effect measure, interval, "
        "and decision rule. Keep the primary analysis aligned with the estimand and "
        "with the study design; make descriptive methods explicit when appropriate."
    ),
    "section-complex-data": (
        "Identify relevant intercurrent events separately from missing observations. "
        "Align each supported strategy and missing-data assumption with the target "
        "estimand and primary estimator. A sensitivity analysis should probe a "
        "specific assumption while targeting the same estimand; do not add routine "
        "imputation or hypothetical strategies without source support."
    ),
    "section-multiplicity-interim": (
        "Tie any multiplicity family, hierarchy, adjusted alpha, interim look, and "
        "stopping rule to a documented confirmatory objective. Distinguish an "
        "interim analysis from routine monitoring; do not create a testing family "
        "or alpha-spending design by convention."
    ),
    "section-safety": (
        "Keep the safety denominator, treatment attribution, observation window, "
        "event and participant counts, and coding levels consistent. Include severity, "
        "seriousness, relatedness, discontinuations, deaths, laboratory data, and "
        "vital signs where collected and supported; avoid assumed TEAE windows."
    ),
    "section-derivations": (
        "Make supported baseline selection, visit assignment, time origin, units, "
        "change or responder calculation, and partial-date handling reproducible. "
        "Check that derived variables match endpoint wording and collected data."
    ),
    "section-tfl": (
        "Link each planned output to an analysis and specify population, rows, "
        "columns, denominator, units, summaries, and essential footnotes. Distinguish "
        "planned shells from unsupported display details."
    ),
    "section-clarifications": (
        "List only decisions that materially affect implementation or interpretation. "
        "Name the missing source detail and affected analysis; avoid repeating the "
        "same question across chapters."
    ),
    "section-traceability": (
        "Map material design facts, endpoint definitions, analysis choices, and "
        "changes from the protocol to their source locators. Keep proposed choices "
        "separate from protocol-specified facts."
    ),
}


def chapter_guidance(chapter_id: str) -> str:
    """Return bounded guidance for a known chapter, without adding study facts."""
    detail = CHAPTER_GUIDANCE.get(chapter_id)
    return f"{GUIDANCE_BOUNDARY}\n{detail}" if detail else GUIDANCE_BOUNDARY
