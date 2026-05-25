import { SAP_SPEC, SapSection } from "./sap-spec";
import { createLLMClient, LLMClient } from "./llm-client";
import { findSapGuidesForSubsections } from "./sap-guides";
import fs from "fs";
import path from "path";

export interface SapGenerateInput {
  protocolText: string;
  crfText: string;
  /** 可选：用于封面的元数据，LLM 也可从 protocol 中抽取 */
  meta?: SapCoverMeta;
  /** 用户确认后的核心内容，作为全篇事实与写作锚点 */
  coreContent?: CoreContentItem[];
  /** 用户确认后的大纲；未传时使用默认 SAP_SPEC */
  sections?: SapSection[];
  /** 可选：每完成一章时回调，用于前端进度展示 */
  onProgress?: (current: number, total: number, section: SapSection) => void;
}

export interface CoreContentRequestItem {
  id?: string;
  title: string;
  description?: string;
}

export interface CoreContentItem {
  id: string;
  title: string;
  content: string;
  confirmed?: boolean;
}

export interface SapCoverMeta {
  studyTitle?: string;
  studyTitleEn?: string;
  protocolNo?: string;
  version?: string;
  date?: string;
  sponsor?: string;
  leadStatistician?: string;
}

export interface SapSectionOutput {
  section: SapSection;
  content: string;
}

export interface SapGenerateResult {
  coverMeta: SapCoverMeta;
  sections: SapSectionOutput[];
  fullDocument: string;
}

type SapFacts = {
  study_title?: string;
  protocol_no?: string;
  version?: string;
  date?: string;
  primary_endpoints?: Array<{
    name?: string;
    definition?: string;
    time_window?: string;
    success_rule?: string;
  }>;
  hypotheses?: { type?: string; alpha?: string; H0?: string; H1?: string };
  analysis_sets?: { FAS?: string; PPS?: string; SS?: string };
  missing_data?: { primary_endpoint?: string; other?: string; sensitivity?: string };
  key_numbers_dates_units?: Array<{ field?: string; value?: string; unit?: string; source?: string; evidence?: string }>;
  inclusion_criteria?: string[];
  terminology_style?: { inequality?: string; ci_style?: string; alpha_style?: string };
  dof_rule?: {
    threshold?: string;
    interpolation?: string;
    smoothing?: string;
    continuity?: string;
    formula_text?: string;
  };
  second_eye_policy?: {
    inconsistent_implant?: string;
    efficacy_usage?: string;
    dedicated_set?: string;
  };
  sample_size_scope?: {
    statistical_assumptions?: string;
    operational_constraints?: string;
  };
  consistency_anchors?: {
    primary_endpoint_unit?: string;
    second_eye_handling?: string;
    primary_missing_main?: string;
    primary_missing_sensitivity?: string;
    hypothesis_direction_bcdva?: string;
    hypothesis_direction_dciva?: string;
    hypothesis_direction_dof?: string;
    visit_window_main?: string;
    visit_anchor_timepoint?: string;
  };
};

const DEFAULT_COVER: SapCoverMeta = {
  studyTitle: "—",
  studyTitleEn: "—",
  protocolNo: "—",
  version: "",
  date: "",
  sponsor: "—",
  leadStatistician: "—",
};

function readKnowledgeFile(relativePath: string): string {
  try {
    const filePath = path.join(process.cwd(), "knowledge_bank", relativePath);
    return fs.readFileSync(filePath, "utf8");
  } catch {
    return "";
  }
}

/** 与 knowledge_bank/sap_hard_gates.md 对齐；逐条独立维护，修改时请同步更新 md。 */
const SAP_HARD_GATE_G1 =
  "G1（关键数值/日期/单位）：样本量、访视窗、阈值、版本号与日期格式等凡 Protocol/CRF 已给出的，须全文一致沿用；同一概念统一量纲与单位写法，禁止前后矛盾或混用不等价数值。";
const SAP_HARD_GATE_G2 =
  "G2（分析集 FAS/PPS/SS）：凡涉及分析集须给出可操作的纳入/剔除规则。若 Protocol/参考 SAP 将研究定义为“器械/植入物”试验，则 FAS/PPS 的纳入基准须以“完成手术并植入（人工晶状体/器械）”为前提，禁止仅按“随机分组/意向治疗”即可纳入；SS 的纳入基准须以“植入后具备安全性评价数据/随访安全性评估依据”为前提，禁止仅凭“接受过一次手术植入”而不具备安全性评价数据。PPS 在 FAS 基础上剔除重大方案违背；须与各章节口径一致，未在输入/事实表中出现的前提不得编造。";
const SAP_HARD_GATE_G3 =
  "G3（主要终点假设 H0/H1）：凡主要终点涉及检验须明确 H0/H1、不等号方向、检验类型（优效/非劣/等效）及界值（若有）；须与统计原则章及分析方法章一致。";
const SAP_HARD_GATE_G4 =
  "G4（主要终点缺失值）：须具名主分析缺失策略（如 LOCF/MI/完整病例/不填补等）并与敏感性分析区分；凡涉及缺失须全文口径一致。";
const SAP_HARD_GATE_G5 =
  "G5（入选标准）：若写入选标准须与 Protocol/CRF 一致（CA-IC01～CA-IC07 眼科示例：双眼白内障成年、Emery≤Ⅳ级、术前 BCDVA 0.3 logMAR（0.5）或更差及对侧眼指征、术后预期 BCDVA 优于 0.2 logMAR（0.6）、除白内障外介质透明、光焦度正 5.0D～36.0D、知情同意与随访）；不得改写阈值/分级；未在输入中出现不得编造。";

/** 硬阀门 G1–G5 单条文案（用于分步 QA 与章节草稿提示词）。 */
const SAP_HARD_GATES: readonly string[] = [
  SAP_HARD_GATE_G1,
  SAP_HARD_GATE_G2,
  SAP_HARD_GATE_G3,
  SAP_HARD_GATE_G4,
  SAP_HARD_GATE_G5,
];

/** 单次 QA 修订时：除当前硬阀门外，保持正文与输出形式不变。 */
const QA_SINGLE_GATE_STYLE_PRESERVE =
  "保持纯文本（禁止 Markdown 标题符号、表格语法、代码块）、禁止占位符（TBD/待补充/待定等）与口语/第一人称；除为满足本条硬阀门所必需的修改外，尽量少改无关句子和结构。";

const NON_REDUNDANCY_CONSTRAINTS = [
  "避免重复定义：若前文已完整定义 FAS/PPS/SS，本章仅做“引用式”一致性表述，不要逐字重复整段定义。",
  "避免把 Protocol 运营执行细节写入统计正文（如中心入组配额、执行排期、现场操作流程）；除非该信息直接进入统计假设、样本量计算或分析模型。",
  "本章只写统计必要信息：定义需“精确+可执行+可追溯”，避免叙述性冗长背景。",
].join("\n");

const CONSISTENCY_LOCK_CONSTRAINTS = [
  "若事实表提供“一致性锚点”，必须全篇锁定并保持一致：主终点分析单位（第一只术眼/双眼平均值）、第二术眼处理、缺失值主分析策略、H0/H1 方向、主终点访视窗口。",
  "禁止在不同章节出现相互冲突的口径（例如前文写“双眼平均值”，后文又改写为“第一只术眼”）。",
  "对于 logMAR 终点，方向判断必须与“数值越小越好”的语义一致；若输入未明确方向，不得自定结论方向。",
].join("\n");

const CORE_CONTENT_CONSTRAINTS = [
  "用户已确认的核心内容是全篇 SAP 的最高优先级业务口径之一，必须在每一章节中严格承接。",
  "凡核心内容已经确认的研究设计、终点定义、时间窗、样本量、分析集、统计方法、缺失值处理、多重性、展示口径、方案偏离规则等，不得在章节正文中改写、弱化、替换或引入冲突说法。",
  "若当前章节需要展开某个核心内容，只能在不改变原意的前提下细化执行细节；不得新增与核心内容相反的新假设、新分析集定义、新终点口径或新统计方法。",
  "若 sap_guides.md、rubrics、事实表、前文 SAP 或当前章节草稿与用户已确认核心内容存在表述冲突，必须优先保持核心内容口径，并用中性、可追溯的方式写作，禁止自行纠偏到相反口径。",
  "输出前必须自检：本章是否与用户已确认核心内容逐项一致；如有冲突，必须先修正冲突再输出。",
].join("\n");

const PLACEHOLDER_WORDS = [
  "TBD",
  "XXX",
  "待补充",
  "待定",
  "略",
  "同上",
  "见上",
  "后续补充",
  "placeholder",
];

function findHardGateIssues(text: string, sectionId: string): string[] {
  const issues: string[] = [];
  const t = text || "";

  // 风格硬约束（可确定性检测）
  if (/[#]{1,6}\s/.test(t)) issues.push("出现 Markdown 标题符号（#），违反“纯文本”要求");
  if (/```/.test(t)) issues.push("出现代码块（```），违反“纯文本”要求");
  if (/\b(我认为|我们将|下面将|本文将|你可以|建议你)\b/.test(t)) issues.push("出现口语/第一人称/对话腔措辞");

  const hit = PLACEHOLDER_WORDS.filter((w) => t.includes(w));
  if (hit.length) issues.push(`出现占位符/禁词：${hit.join("、")}`);

  // 章节关键覆盖（弱确定性，但能避免漏大项）
  if (sectionId === "5") {
    const hasFas = /\b(FAS|全分析集)\b/.test(t);
    const hasPps = /\b(PPS|符合方案集)\b/.test(t);
    const hasSs = /\b(SS|安全性集|安全性分析集)\b/.test(t);
    if (!hasFas) issues.push("第 5 章缺少 FAS（或全分析集）定义或提及");
    if (!hasPps) issues.push("第 5 章缺少 PPS（或符合方案集）定义或提及");
    if (!hasSs) issues.push("第 5 章缺少 SS（或安全性集）定义或提及");

    // G2 常见误写兜底：若出现“仅随机/ITT”趋势但缺少“手术/植入”纳入基准关键词，提示需要重审
    const likelyItT = /(随机分组|意向治疗|ITT|一经随机|按随机)/.test(t);
    const missingImplantKw = !/(手术|植入|人工晶状体|IOL|implant|implanted)/i.test(t);
    if (likelyItT && hasFas && missingImplantKw) {
      issues.push("疑似将 FAS 写成仅随机/ITT 即纳入，需核对是否应以“手术并植入”作为纳入基准（G2）");
    }

    // SS 常见误写兜底：出现“仅接受一次手术植入”但缺少“安全性评价/评估”关键词
    const likelyOnceImplant = /(仅接受|接受过一次|一次手术|手术植入.*一次|一次植入)/.test(t) && /(植入|implant|implanted)/i.test(t);
    const missingSafetyEvalKw = !/(安全性评价|安全性评估|安全性数据|随访安全|AE|TEAE|adverse event)/.test(t);
    if (likelyOnceImplant && hasSs && missingSafetyEvalKw) {
      issues.push("疑似将 SS 写成仅一次手术植入即可纳入，需补足“植入后安全性评价数据/随访安全性评估依据”（G2）");
    }
  }
  if (sectionId === "6") {
    if (!/(H0|原假设)/.test(t) || !/(H1|备择假设)/.test(t)) issues.push("第 6 章缺少 H0/H1 明确陈述");
    if (!/(α|alpha)/.test(t)) issues.push("第 6 章缺少显著性水平（α）陈述");
  }
  if (sectionId === "7") {
    if (!/(缺失|missing)/.test(t)) issues.push("第 7 章缺少缺失值处理描述");
    if (!/(LOCF|多重插补|MI|不填补)/.test(t)) issues.push("第 7 章缺少明确可执行的缺失值处理策略措辞");
  }
  if (sectionId === "8") {
    if (!/(模型|ANCOVA|CMH|MMRM|Cox|Log-rank|回归)/.test(t)) issues.push("第 8 章缺少主要统计模型/方法的可执行描述");
  }
  if (sectionId === "2" || sectionId === "7") {
    const hasDof = /(DOF|焦深|离焦)/i.test(t);
    if (hasDof) {
      const hasMaxMinOnly = /(最大.*最小.*差值|max\s*-\s*min)/i.test(t);
      const hasInterp = /(插值|interpolation|样条|spline|线性插值)/i.test(t);
      const hasContinuity = /(连续区间|连续范围|不连续区间|contiguous|continuous)/i.test(t);
      if (hasMaxMinOnly && (!hasInterp || !hasContinuity)) {
        issues.push("DOF/离焦算法定义疑似不严谨：仅给出 max-min 或差值，未明确插值方法与连续/不连续区间判定规则");
      }
    }
  }
  if (sectionId === "3" || sectionId === "5" || sectionId === "8") {
    const hasSecondEye = /(第二术眼|2nd eye|second eye)/i.test(t);
    const hasInconsistentImplant = /(不一致植入|不同晶体|不同 IOL|不同人工晶状体|mismatch)/i.test(t);
    const stillEfficacyUse = /(支持性分析|纳入.*疗效|用于疗效分析|efficacy)/i.test(t);
    const hasExcludeOrDedicated = /(不纳入.*疗效|仅.*安全性|单独分析集|专用分析集|separate set)/i.test(t);
    if (hasSecondEye && hasInconsistentImplant && stillEfficacyUse && !hasExcludeOrDedicated) {
      issues.push("第二术眼处理与干预一致性疑似冲突：不一致植入时仍纳入疗效分析，未明确排除或单独分析集策略");
    }
  }
  if (sectionId === "4") {
    if (/(各中心最少|各中心最多|中心入组配额|enrollment cap|入组上限)/i.test(t)) {
      issues.push("第 4 章包含运营执行型入组配额描述，建议仅保留样本量统计假设/参数来源/计算方法");
    }
  }

  // 关键口径冲突拦截：主终点分析单位
  const hasBinocularAvg = /(双眼平均|双眼均值|双眼.*平均值)/.test(t);
  const hasFirstEyeOnly = /(第一只术眼|首眼|1st eye|first eye)/i.test(t);
  if (hasBinocularAvg && hasFirstEyeOnly && /主要终点|主要疗效|主分析/.test(t)) {
    issues.push("主终点分析单位冲突：同一文本同时出现“双眼平均值”与“第一只术眼”口径，需统一为单一锚点");
  }

  // 关键口径冲突拦截：缺失值主分析策略
  const hasCcMain = /(完整病例|complete case)/i.test(t) && /(主分析|主要分析)/.test(t);
  const hasLocfMain = /(LOCF|末次观测结转)/i.test(t) && /(主分析|主要分析)/.test(t);
  if (hasCcMain && hasLocfMain) {
    issues.push("缺失值主分析策略冲突：同一文本同时把完整病例与 LOCF 写为主分析策略");
  }

  // 关键口径冲突拦截：logMAR 方向与优效/非劣假设符号
  const hasLogmarBetterLower = /(logMAR).*(越小越好|值越小.*越好)/i.test(t) || /(越小越好).*(logMAR)/i.test(t);
  const hasDeltaGtZeroForSuperiority = /(试验组\s*[-－−]\s*对照组|试验组减对照组).*(>\s*0|大于\s*0).*(优效|superior|superiority)/i.test(t);
  if (hasLogmarBetterLower && hasDeltaGtZeroForSuperiority) {
    issues.push("假设方向疑似错误：logMAR 已定义“越小越好”时，优效方向不应写为“试验组减对照组 > 0”");
  }

  // 关键口径冲突拦截：访视窗口锚点
  const hasWindowPm14 = /(±\s*14|正负\s*14\s*天)/.test(t);
  const hasSecondEyeDay180 = /(第二只术眼).*(180\s*天|第\s*180\s*天)/.test(t);
  const hasSixMonthGeneric = /(术后\s*6\s*个月|6\s*month)/i.test(t);
  if (hasWindowPm14 && hasSecondEyeDay180 && hasSixMonthGeneric && /主要终点|主要疗效/.test(t)) {
    issues.push("访视窗口锚点疑似不一致：主终点同时出现“术后6个月窗口”与“第二术眼第180天锚点”，需统一时间锚点");
  }

  return issues;
}

function findConsistencyAnchorIssues(
  text: string,
  sectionId: string,
  facts: SapFacts | null
): string[] {
  const issues: string[] = [];
  const t = text || "";
  const anchors = facts?.consistency_anchors;
  if (!anchors) return issues;

  const unit = (anchors.primary_endpoint_unit ?? "").trim();
  const secondEye = (anchors.second_eye_handling ?? "").trim();
  const missMain = (anchors.primary_missing_main ?? "").trim();
  const missSens = (anchors.primary_missing_sensitivity ?? "").trim();
  const dirBcdva = (anchors.hypothesis_direction_bcdva ?? "").trim();
  const dirDciva = (anchors.hypothesis_direction_dciva ?? "").trim();
  const dirDof = (anchors.hypothesis_direction_dof ?? "").trim();
  const winMain = (anchors.visit_window_main ?? "").trim();
  const winAnchor = (anchors.visit_anchor_timepoint ?? "").trim();

  // 仅在高度相关章节触发，避免无关章节误报
  const inEndpointChapters = /^(2|3|7|8)$/.test(sectionId);
  const inPopulationOrMethodChapters = /^(3|5|7|8)$/.test(sectionId);
  const inHypothesisChapters = /^(2|6|8)$/.test(sectionId);

  if (inEndpointChapters && unit) {
    if (/双眼/.test(unit) && /(第一只术眼|首眼|1st eye|first eye)/i.test(t)) {
      issues.push(`一致性锚点冲突：主终点分析单位应为「${unit}」，当前章节出现“第一只术眼/首眼”口径`);
    }
    if (/(第一只术眼|首眼|1st eye|first eye)/i.test(unit) && /(双眼平均|双眼均值|双眼.*平均值)/.test(t)) {
      issues.push(`一致性锚点冲突：主终点分析单位应为「${unit}」，当前章节出现“双眼平均值”口径`);
    }
  }

  if (inPopulationOrMethodChapters && secondEye) {
    if (/不纳入|仅安全性|单独分析集|专用分析集/i.test(secondEye) && /(不影响主要终点|仍纳入.*主要终点|继续纳入.*疗效)/.test(t)) {
      issues.push(`一致性锚点冲突：第二术眼处理应为「${secondEye}」，当前章节仍将不一致植入纳入主要疗效`);
    }
  }

  if (inPopulationOrMethodChapters && missMain && /(主分析|主要分析)/.test(t)) {
    if (/完整病例|complete case/i.test(missMain) && /(LOCF|末次观测结转)/i.test(t) && /(主分析|主要分析)/.test(t)) {
      issues.push(`一致性锚点冲突：缺失值主分析应为「${missMain}」，当前章节将 LOCF 写入主分析`);
    }
    if (/(LOCF|末次观测结转)/i.test(missMain) && /(完整病例|complete case)/i.test(t) && /(主分析|主要分析)/.test(t)) {
      issues.push(`一致性锚点冲突：缺失值主分析应为「${missMain}」，当前章节将完整病例写入主分析`);
    }
  }
  if (inPopulationOrMethodChapters && missSens) {
    if (/敏感性/.test(t) && missMain && missSens && missMain === missSens) {
      issues.push("一致性锚点疑点：主分析与敏感性分析锚点相同，需核对是否误填导致无法区分");
    }
  }

  if (inHypothesisChapters) {
    const hasLogmarBetterLower = /(logMAR).*(越小越好|值越小.*越好)/i.test(t) || /(越小越好).*(logMAR)/i.test(t);
    if (dirDciva && /<\s*0|小于\s*0|试验组减对照组<0/.test(dirDciva) && hasLogmarBetterLower && /(试验组\s*[-－−]\s*对照组|试验组减对照组).*(>\s*0|大于\s*0).*(DCIVA|中视力|优效)/i.test(t)) {
      issues.push(`一致性锚点冲突：DCIVA 方向应为「${dirDciva}」，当前章节出现“>0 优效”口径`);
    }
    if (dirBcdva && /<\s*0|小于\s*0|>\s*-?0\.?1|大于\s*-?0\.?1/.test(dirBcdva) && /(BCDVA|远视力)/i.test(t)) {
      // 方向字段已由事实抽取锁定，此处不做复杂解析，只在明显反向词出现时提醒
      if (/(试验组\s*[-－−]\s*对照组).*(>\s*0|大于\s*0).*(优效)/i.test(t) && /<\s*0|小于\s*0/.test(dirBcdva)) {
        issues.push(`一致性锚点冲突：BCDVA 方向应为「${dirBcdva}」，当前章节出现反向优效口径`);
      }
    }
    if (dirDof && /<\s*0|小于\s*0/.test(dirDof) && /(试验组\s*[-－−]\s*对照组).*(>\s*0|大于\s*0).*(DOF|焦深|优效)/i.test(t)) {
      issues.push(`一致性锚点冲突：DOF 方向应为「${dirDof}」，当前章节出现反向优效口径`);
    }
  }

  if (inEndpointChapters && (winMain || winAnchor)) {
    if (winMain && /(±\s*14|正负\s*14\s*天)/.test(winMain) && /(±\s*14|正负\s*14\s*天)/.test(t) === false && /(主要终点|主要疗效)/.test(t)) {
      issues.push(`一致性锚点缺失：主终点访视窗口应为「${winMain}」，当前章节未体现对应窗口口径`);
    }
    if (winAnchor && /第一只术眼|首眼|1st eye|first eye/i.test(winAnchor) && /(第二只术眼).*(180\s*天|第\s*180\s*天)/.test(t)) {
      issues.push(`一致性锚点冲突：访视时间锚点应为「${winAnchor}」，当前章节出现“第二术眼第180天”锚点`);
    }
  }

  return issues;
}

/** 完整评价标准（由 knowledge_bank/rubrics.json 生成，与评分标准 docx 对齐） */
let SAP_RUBRIC_DOC: Record<string, unknown> | null = null;

function loadFullRubricDoc(): Record<string, unknown> | null {
  if (SAP_RUBRIC_DOC) return SAP_RUBRIC_DOC;
  try {
    const filePath = path.join(process.cwd(), "knowledge_bank", "rubrics.json");
    const text = fs.readFileSync(filePath, "utf8");
    SAP_RUBRIC_DOC = JSON.parse(text) as Record<string, unknown>;
  } catch {
    SAP_RUBRIC_DOC = null;
  }
  return SAP_RUBRIC_DOC;
}

/** 每次修订注入完整 rubrics（不按章节裁剪）。可选 SAP_RUBRIC_MAX_CHARS 限制长度。 */
function formatFullRubricsForPrompt(): string {
  const doc = loadFullRubricDoc();
  if (!doc) return "";
  const raw = JSON.stringify(doc, null, 2);
  const max = parseInt(process.env.SAP_RUBRIC_MAX_CHARS?.trim() || "0", 10);
  if (max > 0 && raw.length > max) {
    return (
      raw.slice(0, max) +
      "\n\n...[已按 SAP_RUBRIC_MAX_CHARS 截断；设为 0 或不设则注入完整 rubrics]"
    );
  }
  return raw;
}

async function reviseByRubric(
  client: LLMClient,
  section: SapSection,
  draft: string,
  facts: SapFacts | null,
  previousSapContent: string,
  coreContent?: CoreContentItem[]
): Promise<string> {
  const fullRubrics = formatFullRubricsForPrompt();
  if (!fullRubrics.trim()) return draft.trim();

  const factsText = formatFactsForPrompt(facts).slice(0, 6000);
  const coreText = formatCoreContentForPrompt(coreContent).slice(0, 12000);
  const prev = previousSapContent.trim() ? previousSapContent.slice(-12000) : "";

  const subs = section.subsections.length
    ? section.subsections.map((s) => `- ${s}`).join("\n")
    : "（无子节）";

  const prompt = [
    "你是临床研究统计与质量审阅专家。",
    "请根据下方「完整评价标准」（knowledge_bank/rubrics.json，与《SAP 候选 PDF 对齐参考 SAP PDF 的二元检查清单与确定性评分标准》docx 对齐）对候选章节进行修订。",
    "该标准为：二元（是/否）加权清单 + 三维（内容准确性 / 语义相似度 / 风格语气）+ 硬闸门 G1–G5；修订目标是在不臆造 Protocol/CRF 未提供信息的前提下，使本章正文在这些检查项下更可能被判定为「通过」。",
    "不要求逐条复述清单编号；但正文应覆盖与本章相关的关键统计口径（分析集、假设、缺失值、术语与符号风格等），并与事实表一致。",
    "必须遵守输出约束：",
    "1) 只输出修订后的章节正文纯文本，不输出解释/打分/变更说明/清单自检表。",
    "2) 禁止 Markdown（不要出现 #、##、代码块 ``` 等）。",
    "3) 禁止口语/第一人称（我认为/我们将/下面将/本文将/你可以/建议你 等）。",
    "4) 禁止占位符词：TBD、XXX、待补充、待定、略、同上、见上、后续补充、placeholder。",
    "5) 不得增删子节标题：必须保留草稿中的子节标题行，并在其下修订正文；子节顺序必须与 section.subsections 一致。",
    "6) 若事实表含一致性锚点（主终点分析单位、第二术眼处理、缺失值主分析、假设方向、访视窗口），必须与锚点完全一致，不得前后冲突。",
    "7) 必须与用户已确认的核心内容保持一致；若修订会导致与核心内容冲突，禁止该修订。",
    "",
    `【本章节】${section.id} ${section.title}${section.titleEn ? ` / ${section.titleEn}` : ""}`,
    `【子节要求（标题必须逐字保留与顺序一致）】\n${subs}`,
    "",
    "【核心内容一致性约束（最高优先级，必须全部遵守）】",
    CORE_CONTENT_CONSTRAINTS,
    "",
    "【完整评价标准 rubrics.json（全文）】",
    fullRubrics,
    coreText ? `\n【用户已确认的核心内容（全篇必须严格一致）】\n${coreText}` : "",
    factsText ? `\n【事实表节选（用于一致性）】\n${factsText}` : "",
    prev ? `\n【此前 SAP（节选）】\n${prev}` : "",
    "",
    "【候选章节正文（待修订）】",
    draft.trim(),
  ].join("\n");

  const revised = await client.chat(
    [
      {
        role: "system",
        content:
          "你是临床研究统计与质量审阅专家。按用户给定的评分标准修订章节正文，必须保持与用户已确认核心内容一致，输出纯文本。",
      },
      { role: "user", content: prompt },
    ],
    { temperature: 0.2, maxTokens: 2048 }
  );

  return revised.trim();
}

function formatFactsForPrompt(facts: SapFacts | null): string {
  if (!facts) return "";
  const lines: string[] = [];
  const pushIf = (label: string, v?: string) => {
    const s = (v ?? "").trim();
    if (s) lines.push(`${label}${s}`);
  };

  pushIf("研究题目：", facts.study_title);
  pushIf("方案号：", facts.protocol_no);
  pushIf("版本/日期：", [facts.version, facts.date].filter(Boolean).join(" / "));

  const pe = facts.primary_endpoints?.filter(Boolean) ?? [];
  if (pe.length) {
    lines.push("主要终点（节选）：");
    for (const p of pe.slice(0, 3)) {
      const name = (p.name ?? "").trim();
      const def = (p.definition ?? "").trim();
      const tw = (p.time_window ?? "").trim();
      const sr = (p.success_rule ?? "").trim();
      lines.push(
        `- ${[name, def, tw ? `时间窗：${tw}` : "", sr ? `成功判定：${sr}` : ""].filter(Boolean).join("；")}`
      );
    }
  }

  const hyp = facts.hypotheses ?? {};
  if ((hyp.H0 ?? "").trim() || (hyp.H1 ?? "").trim()) {
    lines.push("主要终点假设（节选）：");
    pushIf("  类型：", hyp.type);
    pushIf("  α：", hyp.alpha);
    pushIf("  H0：", hyp.H0);
    pushIf("  H1：", hyp.H1);
  }

  const sets = facts.analysis_sets ?? {};
  if ((sets.FAS ?? "").trim() || (sets.PPS ?? "").trim() || (sets.SS ?? "").trim()) {
    lines.push("分析集定义（节选）：");
    pushIf("  FAS：", sets.FAS);
    pushIf("  PPS：", sets.PPS);
    pushIf("  SS：", sets.SS);
  }

  const miss = facts.missing_data ?? {};
  if ((miss.primary_endpoint ?? "").trim()) {
    lines.push("缺失值处理（节选）：");
    pushIf("  主要终点：", miss.primary_endpoint);
    pushIf("  其他：", miss.other);
    pushIf("  敏感性：", miss.sensitivity);
  }

  const style = facts.terminology_style ?? {};
  if ((style.inequality ?? "").trim() || (style.ci_style ?? "").trim() || (style.alpha_style ?? "").trim()) {
    lines.push("术语/符号风格（节选）：");
    pushIf("  不等号：", style.inequality);
    pushIf("  CI：", style.ci_style);
    pushIf("  α：", style.alpha_style);
  }

  const dof = facts.dof_rule ?? {};
  if (
    (dof.threshold ?? "").trim() ||
    (dof.interpolation ?? "").trim() ||
    (dof.smoothing ?? "").trim() ||
    (dof.continuity ?? "").trim() ||
    (dof.formula_text ?? "").trim()
  ) {
    lines.push("DOF 规则（节选）：");
    pushIf("  阈值：", dof.threshold);
    pushIf("  插值：", dof.interpolation);
    pushIf("  曲线处理：", dof.smoothing);
    pushIf("  连续性：", dof.continuity);
    pushIf("  公式表述：", dof.formula_text);
  }

  const eye2 = facts.second_eye_policy ?? {};
  if ((eye2.inconsistent_implant ?? "").trim() || (eye2.efficacy_usage ?? "").trim() || (eye2.dedicated_set ?? "").trim()) {
    lines.push("第二术眼策略（节选）：");
    pushIf("  不一致植入处理：", eye2.inconsistent_implant);
    pushIf("  疗效分析使用：", eye2.efficacy_usage);
    pushIf("  专用分析集：", eye2.dedicated_set);
  }

  const ssScope = facts.sample_size_scope ?? {};
  if ((ssScope.statistical_assumptions ?? "").trim() || (ssScope.operational_constraints ?? "").trim()) {
    lines.push("样本量范围（节选）：");
    pushIf("  统计假设：", ssScope.statistical_assumptions);
    pushIf("  运营约束：", ssScope.operational_constraints);
  }

  const anchors = facts.consistency_anchors ?? {};
  if (
    (anchors.primary_endpoint_unit ?? "").trim() ||
    (anchors.second_eye_handling ?? "").trim() ||
    (anchors.primary_missing_main ?? "").trim() ||
    (anchors.primary_missing_sensitivity ?? "").trim() ||
    (anchors.hypothesis_direction_bcdva ?? "").trim() ||
    (anchors.hypothesis_direction_dciva ?? "").trim() ||
    (anchors.hypothesis_direction_dof ?? "").trim() ||
    (anchors.visit_window_main ?? "").trim() ||
    (anchors.visit_anchor_timepoint ?? "").trim()
  ) {
    lines.push("一致性锚点（全文锁定，节选）：");
    pushIf("  主终点分析单位：", anchors.primary_endpoint_unit);
    pushIf("  第二术眼处理：", anchors.second_eye_handling);
    pushIf("  缺失值主分析：", anchors.primary_missing_main);
    pushIf("  缺失值敏感性：", anchors.primary_missing_sensitivity);
    pushIf("  BCDVA 方向：", anchors.hypothesis_direction_bcdva);
    pushIf("  DCIVA 方向：", anchors.hypothesis_direction_dciva);
    pushIf("  DOF 方向：", anchors.hypothesis_direction_dof);
    pushIf("  主终点访视窗口：", anchors.visit_window_main);
    pushIf("  访视时间锚点：", anchors.visit_anchor_timepoint);
  }

  return lines.length ? lines.join("\n") : "";
}

function formatCoreContentForPrompt(coreContent?: CoreContentItem[]): string {
  const confirmedItems = (coreContent ?? []).filter(
    (item) => item.confirmed !== false && item.content.trim()
  );
  if (!confirmedItems.length) return "";
  return confirmedItems
    .map((item, index) => {
      const title = item.title.trim() || `核心内容 ${index + 1}`;
      return `【${title}】\n${item.content.trim()}`;
    })
    .join("\n\n");
}

export const SYSTEM_CORE_CONTENT_ITEMS: CoreContentRequestItem[] = [
  {
    id: "protocol-carryover",
    title: "Protocol 承接内容",
    description:
      "确认研究目的、研究设计、终点定义、访视窗口、样本量、安全性窗口、方案偏离规则等 Protocol 已明确内容，并要求后续 SAP 直接承接。",
  },
  {
    id: "statistical-endpoints",
    title: "统计指标与终点口径",
    description:
      "确认主要/次要/探索性指标的定义、分析时间点、评价窗口、派生规则、成功判定或方向性解释。",
  },
  {
    id: "result-presentation",
    title: "结果展示方向",
    description:
      "确认结果展示的分组、排序、描述统计、效应量、置信区间、图表方向和解释口径。",
  },
  {
    id: "statistical-methods",
    title: "统计方法",
    description:
      "确认主要统计模型、检验方法、协变量/分层因素、多重性控制、敏感性分析和中间事件处理策略。",
  },
  {
    id: "analysis-populations",
    title: "分析集",
    description:
      "确认 FAS/ITT、PPS、SS 等分析集定义、纳入/排除规则、重大方案违背与特殊病例归属。",
  },
  {
    id: "key-statistical-rules",
    title: "关键统计规则",
    description:
      "确认缺失值处理、基线定义、访视窗归属、派生变量算法、安全性窗口、方案偏离处理和跨章节一致性规则。",
  },
];

const SYNOPSIS_CONFIRMATION_PROMPT = [
  "SAP 生成前确认 Synopsis Prompt",
  "用途：用于完整 SAP 生成前的关键内容确认。",
  "使用说明：本 prompt 用于生成完整 SAP 前的确认内容，不用于生成完整 SAP 正文，也不用于生成 TFL shells。",
  "作用：在完整 SAP 分章节生成前，先让用户确认 SAP 所依赖的关键统计口径，包括 protocol 承接内容、统计指标、结果展示方向、统计方法、分析集和关键统计规则。",
  "输出要求：最终用户看到的应是一份简洁、连贯、可确认的前置确认内容，而不是带有来源状态标签的抽取表。",
  "禁止在输出中出现以下 AI 生成提示字段作为固定正文小标题：章节目的与概要、关键内容要素、关键词、标准与依从性、撰写建议与注意事项。",
  "跨章节总原则：Protocol 优先承接。凡 protocol 已经明确的研究目的、研究设计、终点定义、访视窗口、样本量、分析集、主要统计方法、缺失值处理、中间事件策略、安全性窗口和方案偏离规则，AI 必须直接承接，不得重写或替换。",
].join("\n");

export async function generateCoreContent(
  protocolText: string,
  crfText: string
): Promise<CoreContentItem[]> {
  const client = createLLMClient();
  const requestedItems = SYSTEM_CORE_CONTENT_ITEMS;
  const requestedItemsText = requestedItems.length
    ? requestedItems
        .map((item, index) => {
          const id = item.id?.trim() || `core-${index + 1}`;
          const desc = item.description?.trim();
          return `${index + 1}. id=${id}; title=${item.title.trim()}${desc ? `; description=${desc}` : ""}`;
        })
        .join("\n")
    : "";
  const prompt = [
    SYNOPSIS_CONFIRMATION_PROMPT,
    "",
    "请根据 Protocol 与 CRF 生成 SAP 写作前需要用户确认的 Synopsis 核心内容。",
    "这些内容会作为后续 SAP 全文生成的事实锚点，因此必须可追溯、具体、谨慎；输入未提供的信息不得臆造。",
    "只输出严格 JSON 数组，不要输出 Markdown 或解释文字。",
    "数组每项字段：id（短横线命名）、title（中文标题）、content（可给用户确认的完整文本）。",
    "必须严格按照系统固定核心内容列表逐项生成，数量、id、title 均与列表一致：",
    requestedItemsText,
    "",
    "每个 content 的写法要求：",
    "1) 写成给用户确认的连贯段落或简洁条目，不写抽取表，不写“来源状态/已识别/未识别”等标签。",
    "2) 直接承接 Protocol 已明确内容，不改写、不替换、不自行优化研究设计或统计口径。",
    "3) 若 Protocol/CRF 未明确某项，使用谨慎表述说明该项未明确，等待用户确认；不得编造。",
    "4) 不生成完整 SAP 正文，不生成 TFL shells，不输出章节正文小标题。",
    "",
    "【Protocol】",
    protocolText.slice(0, 45000),
    "",
    "【CRF】",
    crfText.slice(0, 25000),
  ].join("\n");

  const raw = await client.chat(
    [
      {
        role: "system",
        content:
          "你是临床研究统计专家。请生成完整 SAP 前的 Synopsis 确认内容，只输出严格 JSON。",
      },
      { role: "user", content: prompt },
    ],
    { temperature: 0.1, maxTokens: 4096 }
  );

  try {
    const parsed = JSON.parse(raw.trim()) as Array<Partial<CoreContentItem>>;
    return parsed
      .map((item, index) => ({
        id: item.id?.trim() || `core-${index + 1}`,
        title: item.title?.trim() || `核心内容 ${index + 1}`,
        content: item.content?.trim() || "",
        confirmed: false,
      }))
      .filter((item) => item.content);
  } catch {
    return [
      {
        id: "core-content",
        title: "核心内容",
        content: raw.trim(),
        confirmed: false,
      },
    ];
  }
}

export async function reviseCoreContentItem(input: {
  protocolText: string;
  crfText: string;
  item: CoreContentItem;
  feedback: string;
  allCoreContent?: CoreContentItem[];
}): Promise<CoreContentItem> {
  const client = createLLMClient();
  const allCore = formatCoreContentForPrompt(input.allCoreContent);
  const prompt = [
    SYNOPSIS_CONFIRMATION_PROMPT,
    "",
    "请根据用户反馈，重新生成指定的 SAP 生成前 Synopsis 核心内容项。",
    "要求：只输出修订后的该项正文纯文本，不输出 JSON、标题、解释或 Markdown。",
    "不得臆造 Protocol/CRF 未提供的信息；若反馈与正式输入冲突，应采用谨慎表述并保持可追溯。",
    "输出应是给用户确认的简洁连贯内容，不得写成抽取表，不得出现来源状态标签，不得生成完整 SAP 正文或 TFL shells。",
    "",
    `【核心内容项】${input.item.title}`,
    "",
    "【当前内容】",
    input.item.content,
    "",
    "【用户反馈】",
    input.feedback,
    allCore ? `\n【其他核心内容（用于保持一致）】\n${allCore}` : "",
    "",
    "【Protocol】",
    input.protocolText.slice(0, 30000),
    "",
    "【CRF】",
    input.crfText.slice(0, 18000),
  ].join("\n");

  const content = await client.chat(
    [
      {
        role: "system",
        content:
          "你是临床研究统计专家。按反馈修订一项核心内容，只输出修订后的正文纯文本。",
      },
      { role: "user", content: prompt },
    ],
    { temperature: 0.15, maxTokens: 2048 }
  );

  return { ...input.item, content: content.trim(), confirmed: false };
}

async function extractSapFacts(client: LLMClient, protocolText: string, crfText: string): Promise<SapFacts | null> {
  const hardGates = readKnowledgeFile("sap_hard_gates.md").slice(0, 12000);
  const schema = readKnowledgeFile("sap_fact_schema.md").slice(0, 9000);

  const prompt = [
    "请从下列 Protocol 与 CRF 中抽取“SAP 事实表（Fact Sheet）”。",
    "要求：只输出严格 JSON（不要输出任何解释文字、不要用 Markdown）。",
    "规则：凡输入未提供的信息，字段填空字符串或空数组；不得臆造。",
    "",
    "特别要求（用于 G2 分析集一致性抽取）：",
    "1) analysis_sets.FAS/PPS/SS：必须定位 Protocol/CRF 中对 FAS/PPS/SS 的明确定义句（包含纳入基准与排除/归类逻辑），并把这些“定义要点”原样写入字段；不得把 FAS 写成仅按随机分组/ITT/随意暴露即可纳入的泛定义。",
    "2) 若 Protocol/CRF 明确为器械/植入物试验：FAS/PPS 纳入基准须包含“完成手术并植入”的前提；SS 纳入基准须包含“植入后安全性评价数据/随访安全性评估依据”的前提；若任一前提在输入中找不到，则不得臆造，字段保持空字符串。",
    "3) 若出现焦深（DOF）或离焦曲线相关规则，必须提取：阈值、是否要求连续区间、插值方法、平滑处理、是否允许不连续区间；若仅看到“max-min”但无插值/连续性说明，须原样记录到 dof_rule.formula_text，并将 dof_rule.interpolation / dof_rule.continuity 留空。",
    "4) 若出现 second-eye / 第二术眼策略，必须提取“不同晶体/不一致植入”时是否纳入疗效分析、是否仅安全性分析、是否单独分析集。",
    "5) 样本量字段中区分统计假设与运营约束：统计学参数进入 sample_size_scope.statistical_assumptions；中心配额/执行限制进入 sample_size_scope.operational_constraints（若无则留空）。",
    "6) consistency_anchors 必填（若输入存在相关信息）：抽取并锁定主终点分析单位（第一只术眼或双眼平均值）、第二术眼处理、缺失值主分析与敏感性策略、BCDVA/DCIVA/DOF 的比较方向、主终点访视窗口及时间锚点；存在冲突时优先采用 Protocol/CRF 明确条款并保持全字段自洽。",
    "",
    "【硬阀门（用于抽取重点）】",
    hardGates,
    "",
    "【事实表字段规范】",
    schema,
    "",
    "【Protocol】",
    protocolText.slice(0, 45000),
    "",
    "【CRF】",
    crfText.slice(0, 25000),
  ].join("\n");

  let raw: string;
  try {
    raw = await client.chat(
      [
        {
          role: "system",
          content:
            "你是临床研究统计专家，擅长从文本中抽取结构化事实。严格输出 JSON，禁止输出解释文字。",
        },
        { role: "user", content: prompt },
      ],
      { temperature: 0.0, maxTokens: 3072 }
    );
  } catch (err) {
    throw new Error(`Fact Sheet 抽取失败：${err instanceof Error ? err.message : String(err)}`);
  }

  try {
    return JSON.parse(raw.trim()) as SapFacts;
  } catch {
    return null;
  }
}

async function qaReviseSection(
  client: LLMClient,
  section: SapSection,
  draft: string,
  facts: SapFacts | null,
  previousSapContent: string,
  coreContent?: CoreContentItem[]
): Promise<string> {
  const factsText = formatFactsForPrompt(facts).slice(0, 8000);
  const coreText = formatCoreContentForPrompt(coreContent).slice(0, 12000);
  const prev = previousSapContent.slice(-20000);
  const sectionHead = `【本章节】${section.id} ${section.title}${section.titleEn ? ` / ${section.titleEn}` : ""}`;

  let current = draft.trim();

  for (let i = 0; i < SAP_HARD_GATES.length; i++) {
    const gateId = `G${i + 1}`;
    const gateRule = SAP_HARD_GATES[i];
    const prompt = [
      `你将对候选章节正文做第 ${i + 1}/${SAP_HARD_GATES.length} 步 QA 修订：本轮**仅**检查并优化下面这一条硬阀门【${gateId}】，不要因其他评分项大幅重写全文。`,
      "",
      "【本条硬阀门（唯一本轮优化目标）】",
      gateRule,
      "",
      QA_SINGLE_GATE_STYLE_PRESERVE,
      "",
      "【核心内容一致性约束（最高优先级，必须全部遵守）】",
      CORE_CONTENT_CONSTRAINTS,
      "",
      "不得添加与 Protocol/CRF 及事实表冲突的新信息；若无法确认，保持中性可执行表述。",
      "不得添加、保留或改写任何与用户已确认核心内容冲突的说法；如果当前正文与核心内容冲突，本轮必须优先修正冲突。",
      "必须遵守一致性锁定：主终点分析单位、第二术眼处理、缺失值主分析策略、假设方向、访视窗口不得与事实表锚点冲突。",
      ...(gateId === "G2"
        ? [
            "",
            "G2 额外约束（针对分析集纳入基准）：",
            "禁止把 FAS/PPS 解释为“仅随机分组/仅按意向治疗即可纳入”。",
            "禁止把 SS 解释为“仅接受过一次手术植入即可纳入”，必须体现“植入后安全性评价数据/随访安全性评估依据”。",
          ]
        : []),
      "输出：只输出修订后的章节正文纯文本，不要输出变更说明、自检表或前言。",
      "",
      sectionHead,
      ...(coreText ? ["", "【用户已确认的核心内容（全篇必须严格一致）】", coreText] : []),
      ...(factsText ? ["", "【事实表（节选，用于一致性）】", factsText] : []),
      "",
      "【此前 SAP（节选，用于与全篇口径一致）】",
      prev,
      "",
      "【当前章节正文（请在本轮仅按上述单条硬阀门修订）】",
      current,
    ].join("\n");

    const revised = await client.chat(
      [
        {
          role: "system",
          content:
            "你是临床研究统计与质量审阅专家。本轮只落实用户给出的单条硬阀门（G1–G5 之一），同时必须保持与用户已确认核心内容一致；只输出修订后的正文纯文本。",
        },
        { role: "user", content: prompt },
      ],
      { temperature: 0.1, maxTokens: 4096 }
    );
    current = revised.trim();
  }

  return current;
}

function buildSectionPrompt(
  section: SapSection,
  protocolText: string,
  crfText: string,
  previousSapContent: string,
  facts: SapFacts | null,
  coreContent: CoreContentItem[] | undefined,
  includeHardGates: boolean
): string {
  const subs = section.subsections.length
    ? section.subsections.map((s) => `- ${s}`).join("\n")
    : "（无子节）";
  const { guide, unmatchedSubsections } = findSapGuidesForSubsections(section.subsections);
  const prevSap = previousSapContent.trim()
    ? `\n【此前已生成的 SAP 全文】（供上下文与口径一致性参考）\n${previousSapContent.slice(-30000)}\n`
    : "";
  const lines: string[] = [];

  const HARD_GATES = SAP_HARD_GATES.join("\n\n");

  const STYLE_CONSTRAINTS = [
    "禁止使用 Markdown（#、##、- 表格语法等）。",
    "禁止口语/对话腔/第一人称（如“我认为/我们将/下面将”）。",
    "禁止占位符词（TBD/XXX/待补充/待定/略/同上/见上/后续补充 等）。如输入信息不足：必须写成“未在 Protocol/CRF 中提供该信息，因此本节按标准模板给出可执行写法，待定稿后以最终文件为准”，但不得出现上述占位符词表。",
    "必须使用一致的统计术语与符号写法（FAS/PPS/SS、LOCF、ANCOVA、α、CI、≤/≥ 等），全篇风格统一。",
    "必须按子节逐一输出，子节标题必须逐字使用【子节要求】给出的行，且顺序一致。",
  ].join("\n");

  const MUST_COVER_BY_SECTION: Record<string, string> = {
    // 2: 目标与终点
    "2": [
      "必须给出：主要/次要终点的精确定义（变量、时间窗、评价规则）、派生规则口径（如 responder/变化值等）。",
      "若涉及 DOF/离焦曲线：必须明确是“连续区间宽度”还是其他定义，并写清阈值、插值方法、曲线平滑/去噪方法、是否允许不连续区间；禁止仅写“max-min”而不定义计算细节。",
    ].join("\n"),
    // 3: Estimand/干预事件
    "3": [
      "必须明确：estimand 四要素（人群、变量、干预事件处理策略、汇总指标），并把关键干预事件与敏感性分析一一对应。",
      "若出现 second-eye/第二术眼且存在不一致植入：必须与干预一致性原则对齐，明确是否排除其疗效分析、是否仅保留安全性分析或归入专用分析集；不得同时宣称“干预不一致”却仍纳入主要疗效估计。",
    ].join("\n"),
    // 4: 样本量与把握度
    "4": [
      "必须聚焦统计内容：样本量假设、参数来源、计算方法、功效与显著性水平。",
      "除非 Protocol 明确要求且与统计推断直接相关，不要展开中心入组配额/执行排期等运营约束细节。",
    ].join("\n"),
    // 5: 分析集
    "5": [
      "必须覆盖并可执行：FAS/ITT、PPS、SS（至少一次给药/植入等）的纳入与剔除规则；重大方案违背口径；特殊场景（随机后未治疗等）归集规则。",
      "避免重复冗长：若前文已定义分析集，本章保留规范定义；其余章节仅引用，不重复大段定义。",
    ].join("\n"),
    // 6: 统计原则
    "6": [
      "必须明确：显著性水平（单/双侧、α 分配/多重性策略）、主要终点检验假设 H0/H1（含方向）、CI 水平与解释规则。",
      "若终点采用 logMAR，假设方向与判定阈值必须与“数值越小越好”语义一致；不得出现方向与语义相反的 H0/H1。",
    ].join("\n"),
    // 7: 数据处理规则
    "7": [
      "必须明确：访视窗、基线定义、派生变量算法、缺失值主策略（如 LOCF/MI/不填补等）与敏感性方案、离群值处理规则。",
      "若涉及 DOF 计算：写明连续区间判定、插值/平滑方法、缺失/不连续处理规则，确保可复现。",
    ].join("\n"),
    // 8: 统计方法
    "8": [
      "必须明确：主要终点统计模型（如 ANCOVA/混合模型/CMH 等按数据类型匹配）、协变量/分层因素、效应量/CI 计算、中心效应/交互检验（如适用）。",
      "统计方法章不得重定义分析集与缺失值主策略；若需提及，仅引用第 5/7 章既定口径，保持一致且简洁。",
    ].join("\n"),
    // 11: 偏离与变更
    "11": [
      "必须明确：与方案差异、SAP 版本变更记录、对结论影响评估与追溯方式。",
    ].join("\n"),
  };
  const mustCover = MUST_COVER_BY_SECTION[section.id] ?? "";
  const factsText = formatFactsForPrompt(facts);
  const coreText = formatCoreContentForPrompt(coreContent);
  const customSectionGuidance = unmatchedSubsections.length
    ? [
        "以下二级章节未在 knowledge_bank/sap_guides.md 中按标题匹配到预置指导：",
        ...unmatchedSubsections.map((subsection) => `- ${subsection}`),
        "请仅对上述未匹配二级章节，基于已确认核心内容、Protocol/CRF 和前文 SAP 口径自主生成正文。",
        "所有章节内容均须与全篇统计口径一致、避免重复前文。",
      ].join("\n")
    : section.subsections.length
      ? ""
      : [
          "本章未提供二级章节，无法按二级标题匹配 knowledge_bank/sap_guides.md 指导。",
          "请基于已确认核心内容、Protocol/CRF 和前文 SAP 口径自主生成本章内容。",
        ].join("\n");

  lines.push(
    "你是一位临床研究统计专家，正在根据研究方案（Protocol）、病例报告表（CRF）及此前已生成的 SAP 内容，撰写《统计分析计划》（SAP）的当前章节。",
    "",
    `【本章节】${section.id} ${section.title}${section.titleEn ? ` / ${section.titleEn}` : ""}`,
    `【本章说明】${section.description}`
  );

  if (guide && guide.trim()) {
    lines.push(
      "",
      "【二级章节撰写指导（按传入二级标题从 knowledge_bank/sap_guides.md 匹配；如与核心内容/Protocol/CRF 冲突，以已确认核心内容和正式输入为准）】",
      guide.slice(0, 12000)
    );
  }

  lines.push(
    "",
    "【子节要求】请按以下子节逐一撰写，内容需与 Protocol/CRF 及前文一致、口径可追溯：",
    subs,
    "",
    "【写作与风格约束（必须全部遵守）】",
    STYLE_CONSTRAINTS,
    "",
    "【去重复与统计范围约束（必须遵守）】",
    NON_REDUNDANCY_CONSTRAINTS,
    "",
    "【核心内容一致性约束（最高优先级，必须全部遵守）】",
    CORE_CONTENT_CONSTRAINTS,
    "",
    "【一致性锁定约束（必须遵守）】",
    CONSISTENCY_LOCK_CONSTRAINTS,
    ...(includeHardGates
      ? ["", "【评分硬阀门（G1–G5，必须全部遵守）】", HARD_GATES]
      : []),
    ...(factsText ? ["", "【事实表（节选，用于一致性与避免自相矛盾）】", factsText.slice(0, 8000)] : []),
    ...(coreText ? ["", "【用户已确认的核心内容（全篇必须遵守）】", coreText.slice(0, 12000)] : []),
    ...(customSectionGuidance ? ["", "【新增章节自主生成要求】", customSectionGuidance] : []),
    ...(mustCover ? ["", "【本章必覆盖要点（必须全部覆盖）】", mustCover] : []),
    "",
    "【Protocol 内容】",
    protocolText.slice(0, 30000),
    "",
    "【CRF 内容】",
    crfText.slice(0, 20000),
    prevSap,
    includeHardGates
      ? "请仅输出本章节的正文内容，纯文本格式。不要输出任何前言/解释/评分项/清单编号等元文本，直接从第一个子节标题开始。输出前请先在脑中逐条自检：用户已确认核心内容一致性 + G1–G5 + 风格约束 + 本章必覆盖要点 + 子节顺序与标题逐字一致；若不满足，必须自行改写到满足后再输出。"
      : "请仅输出本章节的正文内容，纯文本格式。不要输出任何前言/解释/清单编号等元文本，直接从第一个子节标题开始。仅需确保：用户已确认核心内容一致性 + 风格约束 + 子节顺序与标题逐字一致。"
  );

  return lines.join("\n");
}

async function generateOneSection(
  client: LLMClient,
  section: SapSection,
  protocolText: string,
  crfText: string,
  previousSapContent: string,
  facts: SapFacts | null,
  coreContent?: CoreContentItem[]
): Promise<SapSectionOutput> {
  /** 仅当某章生成结果为空白时重试；有正文章节内容即接受，不因本地硬规则未通过而整章重试 */
  const maxAttempts = 5;

  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    // 第一步：生成草稿（不强制注入硬阀门，先写出结构与关键内容）
    const draftPrompt = buildSectionPrompt(
      section,
      protocolText,
      crfText,
      previousSapContent,
      facts,
      coreContent,
      false
    );

    let draft: string;
    try {
      draft = await client.chat(
        [
          {
            role: "system",
            content:
              "你是临床研究统计专家。根据 Protocol/CRF 写出 SAP 指定章节草稿，输出纯文本，不要 Markdown。",
          },
          { role: "user", content: draftPrompt },
        ],
        { temperature: 0.3, maxTokens: 2048 }
      );
    } catch (err) {
      throw new Error(
        `第 ${section.id} 章 Draft 失败（attempt ${attempt}）：${
          err instanceof Error ? err.message : String(err)
        }`
      );
    }

    // 第二步：根据评分标准（rubrics.json）修订，尽可能接近 5 分
    let afterRubric: string;
    try {
      afterRubric = await reviseByRubric(
        client,
        section,
        draft.trim(),
        facts,
        previousSapContent,
        coreContent
      );
    } catch (err) {
      throw new Error(
        `第 ${section.id} 章 Rubric 修订失败（attempt ${attempt}）：${
          err instanceof Error ? err.message : String(err)
        }`
      );
    }

    // 第三步：硬阀门 QA —— qaReviseSection 内对 G1–G5 各调用 1 次 LLM（共 5 次），每次只优化一条硬阀门
    let revised: string;
    try {
      revised = await qaReviseSection(
        client,
        section,
        afterRubric,
        facts,
        previousSapContent,
        coreContent
      );
    } catch (err) {
      throw new Error(
        `第 ${section.id} 章 Hard Gates 修订失败（attempt ${attempt}）：${
          err instanceof Error ? err.message : String(err)
        }`
      );
    }

    let issues = [
      ...findHardGateIssues(revised, section.id),
      ...findConsistencyAnchorIssues(revised, section.id, facts),
    ];
    if (issues.length) {
      // 在硬阀门阶段做“只修错不加戏”的二次修订
      const coreText = formatCoreContentForPrompt(coreContent).slice(0, 12000);
      const fixPrompt = [
        "你将对章节正文做一次“只修错不加戏”的二次修订。",
        "目标：修复下列问题清单中的每一条；不得添加与输入冲突的新事实；只输出最终正文。",
        "必须保持与用户已确认核心内容一致；若问题修复方案会导致与核心内容冲突，必须改用不冲突的修复方案。",
        "",
        "【核心内容一致性约束（最高优先级，必须全部遵守）】",
        CORE_CONTENT_CONSTRAINTS,
        "",
        `【本章节】${section.id} ${section.title}${
          section.titleEn ? ` / ${section.titleEn}` : ""
        }`,
        ...(coreText ? ["", "【用户已确认的核心内容（全篇必须严格一致）】", coreText] : []),
        "",
        "【问题清单（必须逐条修复）】",
        issues.map((x) => `- ${x}`).join("\n"),
        "",
        "【当前正文】",
        revised,
      ].join("\n");

      revised = (
        await (async () => {
          try {
            return await client.chat(
              [
                {
                  role: "system",
                  content:
                    "你是临床研究统计与质量审阅专家。只修复指定问题，并保持与用户已确认核心内容一致；不输出解释，只输出修订后的正文纯文本。",
                },
                { role: "user", content: fixPrompt },
              ],
              { temperature: 0.1, maxTokens: 2048 }
            );
          } catch (err) {
            throw new Error(
              `第 ${section.id} 章 Hard Gates 二次修复失败（attempt ${attempt}）：${
                err instanceof Error ? err.message : String(err)
              }`
            );
          }
        })()
      ).trim();
      issues = [
        ...findHardGateIssues(revised, section.id),
        ...findConsistencyAnchorIssues(revised, section.id, facts),
      ];
    }

    if (!revised.trim()) {
      if (attempt < maxAttempts) continue;
      throw new Error(`章节 ${section.id} 生成结果为空，已重试 ${maxAttempts} 次仍失败`);
    }

    return { section, content: revised.trim() };
  }

  return { section, content: "" };
}

function buildCoverTable(meta: SapCoverMeta): string {
  const v = (s: string | undefined) => s?.trim() || "—";
  return [
    `研究题目 / Study Title：${v(meta.studyTitle)} / ${v(meta.studyTitleEn)}`,
    `方案号 / Protocol No.：${v(meta.protocolNo)}`,
    `版本号 / Version：${v(meta.version)}`,
    `日期 / Date：${v(meta.date)}`,
    `申办方 / Sponsor：${v(meta.sponsor)}`,
    `统计负责人 / Lead Statistician：${v(meta.leadStatistician)}`,
    "",
  ].join("\n");
}

function buildToc(sections: SapSection[]): string {
  const lines = ["目录", ""];
  for (const s of sections) {
    const title = s.titleEn ? `${s.title} / ${s.titleEn}` : s.title;
    lines.push(`${s.id} ${title}`);
  }
  lines.push("");
  return lines.join("\n");
}

function escapeMarkdownTableCell(value: string | undefined): string {
  return (value?.trim() || "—").replace(/\|/g, "\\|").replace(/\r?\n/g, "<br>");
}

function formatSectionContentAsMarkdown(content: string): string {
  return content
    .split(/\r?\n/)
    .map((line) => {
      const trimmed = line.trim();
      if (/^\d+\.\d+\s+\S/.test(trimmed)) return `### ${trimmed}`;
      return line;
    })
    .join("\n")
    .trim();
}

function buildMarkdownDocument(
  coverMeta: SapCoverMeta,
  sectionOutputs: SapSectionOutput[]
): string {
  const lines: string[] = [];
  lines.push("# 统计分析计划（Statistical Analysis Plan）");
  lines.push("");
  lines.push("| 字段 | 内容 |");
  lines.push("| --- | --- |");
  lines.push(`| 研究题目 / Study Title | ${escapeMarkdownTableCell(coverMeta.studyTitle)} / ${escapeMarkdownTableCell(coverMeta.studyTitleEn)} |`);
  lines.push(`| 方案号 / Protocol No. | ${escapeMarkdownTableCell(coverMeta.protocolNo)} |`);
  lines.push(`| 版本号 / Version | ${escapeMarkdownTableCell(coverMeta.version)} |`);
  lines.push(`| 日期 / Date | ${escapeMarkdownTableCell(coverMeta.date)} |`);
  lines.push(`| 申办方 / Sponsor | ${escapeMarkdownTableCell(coverMeta.sponsor)} |`);
  lines.push(`| 统计负责人 / Lead Statistician | ${escapeMarkdownTableCell(coverMeta.leadStatistician)} |`);
  lines.push("");
  lines.push("## 目录");
  lines.push("");
  for (const { section } of sectionOutputs) {
    const title = section.titleEn ? `${section.title} / ${section.titleEn}` : section.title;
    lines.push(`- ${section.id} ${title}`);
  }
  lines.push("");

  for (const { section, content } of sectionOutputs) {
    const heading = section.titleEn
      ? `${section.id} ${section.title} / ${section.titleEn}`
      : `${section.id} ${section.title}`;
    lines.push(`## ${heading}`);
    lines.push("");
    lines.push(formatSectionContentAsMarkdown(content));
    lines.push("");
  }
  return lines.join("\n").trim() + "\n";
}

function buildPreviousSapContent(
  coverMeta: SapCoverMeta,
  sectionOutputs: SapSectionOutput[],
  outline: SapSection[] = SAP_SPEC
): string {
  const parts: string[] = [];
  parts.push("统计分析计划 (Statistical Analysis Plan)");
  parts.push("");
  parts.push(buildCoverTable(coverMeta));
  parts.push(buildToc(outline));
  for (const { section, content } of sectionOutputs) {
    const heading = section.titleEn
      ? `${section.id} ${section.title} / ${section.titleEn}`
      : `${section.id} ${section.title}`;
    parts.push(heading);
    parts.push("");
    parts.push(content);
    parts.push("");
  }
  return parts.join("\n");
}

function mergeDocument(coverMeta: SapCoverMeta, sectionOutputs: SapSectionOutput[]): string {
  return buildMarkdownDocument(coverMeta, sectionOutputs);
}

/**
 * 根据 Protocol 与 CRF 文本，调用各章节 Agent 生成 SAP，并合并为完整文档
 */
export async function generateSap(input: SapGenerateInput): Promise<SapGenerateResult> {
  const client = createLLMClient();
  const coverMeta: SapCoverMeta = { ...DEFAULT_COVER, ...input.meta };

  // 先抽取事实表：降低 G1–G5 违约概率，提升一致性
  const facts = await extractSapFacts(client, input.protocolText, input.crfText);
  // 用事实表回填封面版本日期，避免使用运行时“当前日期”造成 CA-02 类错误。
  if (facts?.version?.trim()) coverMeta.version = facts.version.trim();
  if (facts?.date?.trim()) coverMeta.date = facts.date.trim();

  const outline = input.sections?.length ? input.sections : SAP_SPEC;
  const sectionOutputs: SapSectionOutput[] = [];
  const total = outline.length;
  for (let i = 0; i < outline.length; i++) {
    const section = outline[i];
    const previousSap = buildPreviousSapContent(coverMeta, sectionOutputs, outline);
    const out = await generateOneSection(
      client,
      section,
      input.protocolText,
      input.crfText,
      previousSap,
      facts,
      input.coreContent
    );
    sectionOutputs.push(out);
    input.onProgress?.(i + 1, total, section);
  }

  const fullDocument = mergeDocument(coverMeta, sectionOutputs);
  return { coverMeta, sections: sectionOutputs, fullDocument };
}
