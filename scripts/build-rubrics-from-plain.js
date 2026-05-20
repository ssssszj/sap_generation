/**
 * 从 knowledge_bank/sap_rubric_plain.txt（由 docx 提取）生成 knowledge_bank/rubrics.json
 * 运行: node scripts/build-rubrics-from-plain.js
 */
const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");
const src = path.join(root, "knowledge_bank", "sap_rubric_plain.txt");
const dst = path.join(root, "knowledge_bank", "rubrics.json");

const text = fs.readFileSync(src, "utf8");
const lines = text.split(/\r?\n/);

function skipEmpty(from) {
  let i = from;
  while (i < lines.length && !String(lines[i]).trim()) i++;
  return i;
}

function takeBlock(startIdx) {
  const idLine = skipEmpty(startIdx);
  const id = lines[idLine]?.trim();
  if (!id || !/^(CA-|SS-|ST-)/.test(id)) return null;
  const question = (lines[idLine + 2] ?? "").trim();
  const weight = (lines[idLine + 4] ?? "").trim();
  const dimension = (lines[idLine + 6] ?? "").trim();
  const evidence_tool = (lines[idLine + 8] ?? "").trim();
  const machine = (lines[idLine + 10] ?? "").trim();
  return {
    id,
    weight: parseFloat(weight) || 0,
    dimension,
    binary_check: question,
    evidence_tool,
    machine_detectable: machine,
    nextIndex: skipEmpty(idLine + 11),
  };
}

const executiveSummaryLines = [];
let i = 0;
for (; i < lines.length; i++) {
  const line = lines[i];
  if (line.trim() === "ID" && lines[i + 1]?.trim() === "二元检查项（是/否，一行填空式）") {
    break;
  }
  if (i >= 2) executiveSummaryLines.push(line);
}
const executive_summary_text = executiveSummaryLines.join("\n").trim();

const hardGatesLine = lines.find((l) => l.includes("硬闸门（示例")) || "";
const hard_gates = [
  {
    id: "G1",
    trigger: "CA-03=0（关键数值/日期/单位归一化后不一致）",
    cap: "Overall_final ≤ 49.00",
  },
  {
    id: "G2",
    trigger: "CA-POP01=0 或 CA-POP02=0 或 CA-POP03=0（FAS/PPS/SS 任一数据集定义不一致）",
    cap: "Overall_final ≤ 49.00",
  },
  {
    id: "G3",
    trigger: "CA-HYP01=0 或 CA-HYP02=0（主要终点检验假设不一致）",
    cap: "Overall_final ≤ 49.00",
  },
  {
    id: "G4",
    trigger: "CA-MISS01=0（主要终点缺失值处理不一致）",
    cap: "Overall_final ≤ 49.00",
  },
  {
    id: "G5",
    trigger: "CA-IC01…CA-IC07 任意为 0（入选标准条款出现状态/文本不一致）",
    cap: "Overall_final ≤ 49.00",
  },
];

const inclusion_rule =
  lines
    .find((l) => l.includes("入选标准 7 条") && l.includes("适用性"))
    ?.trim() ||
  "若参考SAP不出现该条款且候选也不出现→判“是”；若参考出现→候选必须出现且逐字一致才判“是”。";

// 找到第一个 CA-01 行
let start = lines.findIndex((l) => l.trim() === "CA-01");
if (start < 0) throw new Error("CA-01 not found");

const content_accuracy = [];
while (start < lines.length) {
  const row = takeBlock(start);
  if (!row || !row.id.startsWith("CA-")) break;
  content_accuracy.push({
    id: row.id,
    weight: row.weight,
    dimension: row.dimension,
    binary_check: row.binary_check,
    evidence_tool: row.evidence_tool,
    machine_detectable: row.machine_detectable,
  });
  start = row.nextIndex;
}

let ssStart = lines.findIndex((l) => l.trim() === "SS-01");
const semantic_similarity = [];
if (ssStart >= 0) {
  start = ssStart;
  while (start < lines.length) {
    const row = takeBlock(start);
    if (!row || !row.id.startsWith("SS-")) break;
    semantic_similarity.push({
      id: row.id,
      weight: row.weight,
      dimension: row.dimension,
      binary_check: row.binary_check,
      evidence_tool: row.evidence_tool,
      machine_detectable: row.machine_detectable,
    });
    start = row.nextIndex;
  }
}

let stStart = lines.findIndex((l) => l.trim() === "ST-01");
const style_tone = [];
if (stStart >= 0) {
  start = stStart;
  while (start < lines.length) {
    const row = takeBlock(start);
    if (!row || !row.id.startsWith("ST-")) break;
    style_tone.push({
      id: row.id,
      weight: row.weight,
      dimension: row.dimension,
      binary_check: row.binary_check,
      evidence_tool: row.evidence_tool,
      machine_detectable: row.machine_detectable,
    });
    start = row.nextIndex;
  }
}

const sumCA = content_accuracy.reduce((s, x) => s + x.weight, 0);
const sumSS = semantic_similarity.reduce((s, x) => s + x.weight, 0);
const sumST = style_tone.reduce((s, x) => s + x.weight, 0);

const alignmentNote =
  "执行摘要中写「内容准确性 64 项、合计权重 80.00」；从 docx 提取的正文表格解析得到 CA 项数为 " +
  content_accuracy.length +
  "，权重合计为 " +
  Math.round(sumCA * 100) / 100 +
  "。若与 Word 原表不一致，请以 Word 为准并重新运行本脚本从更新后的 sap_rubric_plain.txt 生成 rubrics.json。";

const rubric = {
  source_document:
    "SAP 候选 PDF 对齐参考 SAP PDF 的二元检查清单与确定性评分标准.docx",
  extracted_text_file: "knowledge_bank/sap_rubric_plain.txt",
  executive_summary: executive_summary_text,
  alignment_note: alignmentNote,
  scoring_framework: {
    method: "二元（是/否）加权，权重两位小数，总和 100.00；输出总体 0–100 与各维度 0–100",
    dimensions: [
      {
        key: "content_accuracy",
        name: "内容准确性",
        declared_weight: 80.0,
        declared_item_count: 64,
        parsed_item_count: content_accuracy.length,
        parsed_weight_sum: Math.round(sumCA * 100) / 100,
        note:
          "declared_item_count 来自 docx 执行摘要；parsed_* 来自正文表格逐行解析，二者可能因排版/合并单元格产生差异",
      },
      {
        key: "semantic_similarity",
        name: "语义相似度",
        declared_weight: 12.0,
        declared_item_count: 10,
        parsed_item_count: semantic_similarity.length,
        parsed_weight_sum: Math.round(sumSS * 100) / 100,
      },
      {
        key: "style_tone",
        name: "风格/语气",
        declared_weight: 8.0,
        declared_item_count: 8,
        parsed_item_count: style_tone.length,
        parsed_weight_sum: Math.round(sumST * 100) / 100,
      },
    ],
    export_fields_per_item:
      "check_id, dimension, weight, pass(0/1), evidence_tool, machine_detectable(Y/N)",
    cap_formula: "overall_final = min(overall_raw, cap)（闸门封顶）",
  },
  hard_gates,
  hard_gates_raw_line: hardGatesLine,
  inclusion_criteria_rule_for_IC: inclusion_rule,
  checklists: {
    content_accuracy,
    semantic_similarity,
    style_tone,
  },
};

fs.writeFileSync(dst, JSON.stringify(rubric, null, 2), "utf8");
console.log(
  "Wrote",
  dst,
  "CA:",
  content_accuracy.length,
  "SS:",
  semantic_similarity.length,
  "ST:",
  style_tone.length
);
