/**
 * SAP（统计分析计划）章节规范
 * 规定 SAP 文档需要包含的章节结构
 */
export interface SapSection {
  id: string;
  title: string;
  titleEn?: string;
  subsections: string[];
  description: string;
}

export const SAP_SPEC: SapSection[] = [
  {
    id: "0",
    title: "文档信息与版本控制",
    titleEn: "Document Control",
    subsections: [
      "0.1 标题页（研究题目/方案号/申办方/统计负责人）",
      "0.2 版本历史与修订摘要（含原因、影响范围）",
      "0.3 审批签字（统计、临床、数据管理等）",
      "0.4 盲态与定稿节点说明（如：数据库锁定/揭盲前定稿）",
    ],
    description: "文档元信息、版本历史、审批与定稿节点",
  },
  {
    id: "1",
    title: "研究概述",
    titleEn: "Study Overview / Trial Registration",
    subsections: [
      "1.1 研究背景与目的（与方案/登记信息一致）",
      "1.2 研究设计摘要（随机/对照/盲法、中心数、随访框架）",
      "1.3 治疗组/器械组/暴露信息（组别定义、使用规则、对照）",
      "1.4 随机化与分层因素（如有：中心、基线严重度等）",
    ],
    description: "研究背景、设计摘要、组别与随机化",
  },
  {
    id: "2",
    title: "分析目标、指标与口径",
    titleEn: "Objectives, Endpoints, Definitions",
    subsections: [
      "2.1 主要目的与主要终点（定义 + 时间窗 + 评价规则）",
      "2.2 次要目的与次要终点（同上）",
      "2.3 探索性终点（如有）",
      "2.4 终点/变量精确定义与派生规则总览（避免事后变更口径）",
    ],
    description: "主要/次要/探索性终点及精确定义",
  },
  {
    id: "3",
    title: "估计目标与干预事件处理",
    titleEn: "Estimands / Intercurrent Events",
    subsections: [
      "3.1 主要 estimand 四要素（人群、变量、干预事件处理策略、汇总指标）",
      "3.2 关键干预事件（停用/交叉/补救治疗/失访/死亡等）及处理策略",
      "3.3 与敏感性分析的对应关系（用于检验结论稳健性）",
    ],
    description: "Estimand 与干预事件处理策略",
  },
  {
    id: "4",
    title: "样本量与把握度",
    titleEn: "Sample Size / Power",
    subsections: [
      "4.1 样本量依据（主要终点、效应量假设、I/II 类错误、脱落率）",
      "4.2 计算方法与参数来源（文献/先导/历史数据）",
      "4.3 期中/再估计规则（如适用：α 消耗/盲态要求）",
    ],
    description: "样本量、把握度与期中分析规则",
  },
  {
    id: "5",
    title: "分析集定义",
    titleEn: "Analysis Populations / Sets",
    subsections: [
      "5.1 ITT / 全分析集（FAS）定义与排除规则",
      "5.2 符合方案集（PPS）定义与“重大方案违背”口径",
      "5.3 安全性集（SS）/ 暴露集定义（至少一次给药/植入等）",
      "5.4 其他专用分析集（PK、影像、实验室等，如适用）",
    ],
    description: "FAS、PPS、SS 等分析集定义",
  },
  {
    id: "6",
    title: "统计原则",
    titleEn: "Statistical Principles",
    subsections: [
      "6.1 显著性水平与置信区间（单/双侧；α 分配）",
      "6.2 多重性控制（多终点/多比较/多时间点：层级/门控/调整方法）",
      "6.3 分层与协变量调整原则（预设协变量清单）",
      "6.4 期中分析与数据监查（IDMC、提前终止规则）",
      "6.5 揭盲与盲态审核（谁可见、何时可见、留痕要求）",
    ],
    description: "显著性水平、多重性、协变量、期中与揭盲",
  },
  {
    id: "7",
    title: "数据处理规则",
    titleEn: "Data Handling Rules",
    subsections: [
      "7.1 访视窗与时间点归属（窗口、提前/延后规则）",
      "7.2 基线定义（baseline 取值规则）",
      "7.3 派生变量算法（变化值、百分比变化、Responder 规则等）",
      "7.4 缺失值处理（主分析 + 敏感性：按适用性说明）",
      "7.5 离群值与数据转换（识别规则、变换/截尾、敏感性方案）",
      "7.6 方案违背分类与处理（是否影响入集/分析口径）",
      "7.7 数据一致性与完整性（清理原则、审计追溯要求）",
    ],
    description: "访视窗、基线、派生、缺失、离群、方案违背",
  },
  {
    id: "8",
    title: "统计方法",
    titleEn: "Statistical Methods",
    subsections: [
      "8.1 总体描述（人口学/基线/暴露/依从性：统计量与展示方式）",
      "8.2 主要终点分析（模型、估计量、CI、检验、协变量、缺失处理）",
      "8.3 次要终点分析（与多重性策略一致）",
      "8.4 安全性分析（AE/SAE、实验室、生命体征、器械缺陷等：口径与分母）",
      "8.5 亚组分析（预设亚组、交互作用检验、森林图规则）",
      "8.6 敏感性分析（改变缺失机制/干预事件处理/入集规则等）",
      "8.7 其他分析（如适用：生存、重复测量、复发事件等）",
    ],
    description: "描述、主要/次要/安全性/亚组/敏感性分析",
  },
  {
    id: "9",
    title: "输出与呈现规范",
    titleEn: "TFL Shell & Reporting Conventions",
    subsections: [
      "9.1 Table/Figure/Listing 总清单（仅计划输出，不写结果）",
      "9.2 格式规则（小数位、单位、排序、分层、统计量口径）",
      "9.3 关键图形（KM、趋势图、森林图等）生成规则",
    ],
    description: "TFL 清单、格式与图形规则",
  },
  {
    id: "10",
    title: "软件、编程与质控",
    titleEn: "Software / QC",
    subsections: [
      "10.1 统计软件与版本（SAS/R 等）",
      "10.2 程序验证与复核（双编程/独立复核/日志留存）",
      "10.3 可追溯性（输入数据版本、运行环境、输出留存）",
    ],
    description: "软件、验证与可追溯性",
  },
  {
    id: "11",
    title: "与方案差异与变更记录",
    titleEn: "Deviations / SAP Changes",
    subsections: [
      "11.1 与方案统计章节差异（如有）",
      "11.2 SAP 内部变更（版本间差异、对结论影响评估）",
    ],
    description: "与方案差异及 SAP 变更记录",
  },
  {
    id: "12",
    title: "参考文献",
    titleEn: "References",
    subsections: [],
    description: "参考文献列表",
  },
];
