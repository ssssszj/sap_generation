/**
 * TFL Shells 规范
 * Table / Figure / Listing shells 预定义项，用于 prompt 与进度展示
 */
export const TABLE_SHELL_ITEMS = [
  "Subject disposition summary",
  "Analysis populations summary (screened, enrolled, treated, ITT, PP, safety)",
  "Baseline demographics summary",
  "Baseline disease characteristics summary (as applicable)",
  "Treatment exposure and compliance summary (as applicable)",
  "Primary endpoint summary table",
  "Key secondary endpoint summary tables (as applicable)",
  "Subgroup summary tables for key endpoints (as applicable)",
  "Sensitivity analysis summary tables (as applicable)",
  "Overall AE summary table",
  "AE by SOC and PT summary table",
  "Serious AE summary table",
  "AE leading to discontinuation summary table",
  "Deaths summary table",
  "Laboratory summary tables (baseline and change from baseline)",
  "Laboratory shift tables (as applicable)",
  "Vital signs summary tables (baseline and change from baseline)",
  "ECG summary tables (as applicable)",
] as const;

export const FIGURE_SHELL_ITEMS = [
  "Subject flow diagram",
  "Primary endpoint figure (appropriate plot type)",
  "Key secondary endpoint figures (as applicable)",
  "Subgroup forest plots for key endpoints (as applicable)",
  "Time course plots for efficacy measures (as applicable)",
  "Kaplan Meier curves for time-to-event endpoints (as applicable)",
  "AE display figures (as applicable)",
  "Laboratory trend plots and shift visuals (as applicable)",
  "Vital signs trend plots (as applicable)",
] as const;

export const LISTING_SHELL_ITEMS = [
  "Discontinued patients listing",
  "Protocol deviations listing",
  "Patients excluded from efficacy analysis listing",
  "Patient-level demographics listing",
  "Compliance and or drug concentration listing (if available)",
  "Individual efficacy response listing",
  "Adverse event listing (each patient)",
  "Listings of deaths and other serious or significant adverse events",
  "Narratives of deaths and other serious or significant adverse events (if required)",
  "Abnormal laboratory values listing (each patient)",
  "Individual laboratory measurements listing by patient (when required)",
  "US archival individual patient data listings bundle (if required)",
] as const;

export type TflStep = "table" | "figure" | "listing";

export const TFL_STEP_LABELS: Record<TflStep, string> = {
  table: "Table shells",
  figure: "Figure and graph shells",
  listing: "Listing shells",
};
