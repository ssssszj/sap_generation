import { createLLMClient, LLMClient } from "./llm-client";
import {
  TABLE_SHELL_ITEMS,
  FIGURE_SHELL_ITEMS,
  LISTING_SHELL_ITEMS,
  type TflStep,
  TFL_STEP_LABELS,
} from "./tfl-spec";

export interface TflGenerateInput {
  protocolText: string;
  crfText: string;
  sapText: string;
  onProgress?: (step: TflStep, status: "generating" | "done") => void;
}

export interface TflGenerateResult {
  tableShells: string;
  figureShells: string;
  listingShells: string;
  fullDocument: string;
}

const TFL_INTRO = `TFL shells 是预先设计好的输出模板，用于在分析实施前明确每个表格、图形和清单的展示结构与统计口径。Shells 不包含真实结果，仅包含标题、适用分析集、终点定义、分组方式、统计量与格式、缺失值处理展示、脚注与缩写、以及关键派生变量或计算规则的说明。其中 Table shells 与 Figure and graph shells 为并列的主要展示输出；Listing shells 则作为 Table shells 的补充，用于提供个体级或明细级数据以支撑表格汇总。其目标是对齐申办方、统计、医学写作与编程团队，减少后期因展示口径不一致导致的返工，并为 ADaM 变量规格、程序开发和 CSR 输出提供可追溯的“蓝图”。`;

function buildTableShellsPrompt(protocolText: string, crfText: string, sapText: string): string {
  const items = TABLE_SHELL_ITEMS.map((s, i) => `${i + 1}. ${s}`).join("\n");
  return [
    "你是一位临床研究统计与医学写作专家，正在根据 Protocol、CRF 和 SAP 撰写《Table shells》（表格壳）。",
    "",
    TFL_INTRO,
    "",
    "【要求】针对以下每类表格，输出对应的 shell 说明（纯文本）：标题、适用分析集、终点/变量定义、分组方式、统计量与格式、缺失值展示、脚注与缩写、派生变量或计算规则说明。不填写真实数据，仅定义结构与口径。",
    "",
    "【Table shells 清单】",
    items,
    "",
    "【Protocol 内容】（节选）",
    protocolText.slice(0, 25000),
    "",
    "【CRF 内容】（节选）",
    crfText.slice(0, 15000),
    "",
    "【SAP 全文】（节选，供统计口径与定义一致）",
    sapText.slice(-40000),
    "",
    "请按上述清单顺序，逐项输出 Table shells 的纯文本说明，不要使用 Markdown 表格语法，使用纯文本描述每张表的壳结构。",
  ].join("\n");
}

function buildFigureShellsPrompt(protocolText: string, crfText: string, sapText: string): string {
  const items = FIGURE_SHELL_ITEMS.map((s, i) => `${i + 1}. ${s}`).join("\n");
  return [
    "你是一位临床研究统计与医学写作专家，正在根据 Protocol、CRF 和 SAP 撰写《Figure and graph shells》（图形壳）。",
    "",
    TFL_INTRO,
    "",
    "【要求】针对以下每类图形，输出对应的 shell 说明（纯文本）：图形类型、标题、适用分析集、终点/变量定义、分组/分层、坐标轴与图例、统计量展示方式、脚注与缩写。不填写真实数据，仅定义结构与口径。",
    "",
    "【Figure and graph shells 清单】",
    items,
    "",
    "【Protocol 内容】（节选）",
    protocolText.slice(0, 25000),
    "",
    "【CRF 内容】（节选）",
    crfText.slice(0, 15000),
    "",
    "【SAP 全文】（节选）",
    sapText.slice(-40000),
    "",
    "请按上述清单顺序，逐项输出 Figure/graph shells 的纯文本说明，不要使用 Markdown，使用纯文本描述每张图的壳结构。",
  ].join("\n");
}

function buildListingShellsPrompt(protocolText: string, crfText: string, sapText: string): string {
  const items = LISTING_SHELL_ITEMS.map((s, i) => `${i + 1}. ${s}`).join("\n");
  return [
    "你是一位临床研究统计与医学写作专家，正在根据 Protocol、CRF 和 SAP 撰写《Listing shells》（清单壳），Listing shells 主要作为 Table shells 的个体级或明细级补充输出，用于支撑表格中的汇总信息。",
    "",
    TFL_INTRO,
    "",
    "【要求】针对以下每类清单，输出对应的 shell 说明（纯文本）：清单标题、适用分析集、包含变量/列定义、排序与筛选规则、脚注与缩写、派生变量或计算规则。不填写真实数据，仅定义结构与口径。",
    "",
    "【Listing shells 清单】",
    items,
    "",
    "【Protocol 内容】（节选）",
    protocolText.slice(0, 25000),
    "",
    "【CRF 内容】（节选）",
    crfText.slice(0, 15000),
    "",
    "【SAP 全文】（节选）",
    sapText.slice(-40000),
    "",
    "请按上述清单顺序，逐项输出 Listing shells 的纯文本说明，不要使用 Markdown，使用纯文本描述每份清单的壳结构。",
  ].join("\n");
}

async function generateOneCategory(
  client: LLMClient,
  step: TflStep,
  protocolText: string,
  crfText: string,
  sapText: string,
  onProgress?: (step: TflStep, status: "generating" | "done") => void
): Promise<string> {
  onProgress?.(step, "generating");
  const label = TFL_STEP_LABELS[step];
  let prompt: string;
  if (step === "table") prompt = buildTableShellsPrompt(protocolText, crfText, sapText);
  else if (step === "figure") prompt = buildFigureShellsPrompt(protocolText, crfText, sapText);
  else prompt = buildListingShellsPrompt(protocolText, crfText, sapText);

  const content = await client.chat(
    [
      {
        role: "system",
        content: `你是临床研究统计与医学写作专家，负责撰写 TFL shells（${label}），内容需与 Protocol、CRF 和 SAP 一致，仅定义展示结构与统计口径，不填真实结果。输出纯文本，禁止使用 Markdown。`,
      },
      { role: "user", content: prompt },
    ],
    { temperature: 0.3, maxTokens: 8192 }
  );
  onProgress?.(step, "done");
  return content.trim();
}

/**
 * 根据 Protocol、CRF、SAP 生成 TFL shells（Table / Figure / Listing）
 */
export async function generateTflShells(input: TflGenerateInput): Promise<TflGenerateResult> {
  const client = createLLMClient();
  const { protocolText, crfText, sapText, onProgress } = input;

  const tableShells = await generateOneCategory(
    client,
    "table",
    protocolText,
    crfText,
    sapText,
    onProgress
  );
  const listingShells = await generateOneCategory(
    client,
    "listing",
    protocolText,
    crfText,
    sapText,
    onProgress
  );
  const figureShells = await generateOneCategory(
    client,
    "figure",
    protocolText,
    crfText,
    sapText,
    onProgress
  );

  const fullDocument = [
    "TFL Shells（Tables, Figures, Listings）",
    "",
    "一、Table shells",
    "",
    tableShells,
    "",
    "二、Listing shells（作为 Table shells 的补充）",
    "",
    listingShells,
    "",
    "三、Figure and graph shells",
    "",
    figureShells,
  ].join("\n");

  return { tableShells, figureShells, listingShells, fullDocument };
}
