# SAP 三步生成接口文档

本文档面向网站后端调用方。当前项目提供三类核心能力：核心内容确定、SAP Markdown 生成、Markdown 转 docx/pdf。

## 通用约定

- Base URL：以部署环境为准，本文示例使用相对路径。
- 成功响应统一格式：

```json
{
  "code": 0,
  "data": {}
}
```

- 失败响应统一格式：

```json
{
  "code": 1,
  "message": "错误信息"
}
```

- `protocolText` 与 `crfText` 由网站后端负责从文件中解析后传入。本项目正式接口不接收文件上传。
- SAP 生成接口直接返回 Markdown 字符串；如需下载文件，调用导出接口把 Markdown 转为 docx 或 pdf。

---

## 1. 生成待确认 Synopsis 核心内容

调用时机：用户上传/选择 Protocol 与 CRF 后，AI 服务按系统内置的固定核心内容清单逐项生成“完整 SAP 生成前”的待确认 Synopsis 内容。

功能定位：

- 本接口只用于完整 SAP 生成前的关键内容确认。
- 本接口不生成完整 SAP 正文，也不生成 TFL shells。
- 生成内容用于让用户确认 SAP 所依赖的关键统计口径，包括 Protocol 承接内容、统计指标、结果展示方向、统计方法、分析集和关键统计规则。
- 最终用户看到的是简洁、连贯、可确认的前置确认内容，不是带有来源状态标签的抽取表。

跨章节总原则：

- Protocol 优先承接。
- 凡 Protocol 已经明确的研究目的、研究设计、终点定义、访视窗口、样本量、分析集、主要统计方法、缺失值处理、中间事件策略、安全性窗口和方案偏离规则，AI 必须直接承接，不得重写或替换。

内置固定清单：

| ID | 标题 | 确认重点 |
| --- | --- | --- |
| `protocol-carryover` | Protocol 承接内容 | 研究目的、研究设计、终点定义、访视窗口、样本量、安全性窗口、方案偏离规则等 |
| `statistical-endpoints` | 统计指标与终点口径 | 主要/次要/探索性指标定义、分析时间点、评价窗口、派生规则、成功判定或方向性解释 |
| `result-presentation` | 结果展示方向 | 分组、排序、描述统计、效应量、置信区间、图表方向和解释口径 |
| `statistical-methods` | 统计方法 | 主要统计模型、检验方法、协变量/分层因素、多重性控制、敏感性分析和中间事件处理 |
| `analysis-populations` | 分析集 | FAS/ITT、PPS、SS 等分析集定义、纳入/排除规则、重大方案违背与特殊病例归属 |
| `key-statistical-rules` | 关键统计规则 | 缺失值处理、基线定义、访视窗归属、派生变量算法、安全性窗口、方案偏离处理和跨章节一致性规则 |

说明：内部 prompt 可能使用“章节目的与概要 / 关键内容要素 / 关键词 / 标准与依从性 / 撰写建议与注意事项”等字段辅助生成，但这些不是最终展示给用户的固定正文小标题，接口返回内容中不应按这些标签展示。

请求：

```http
POST /ai/v1/sap/core-content/generate
Content-Type: application/json
```

```json
{
  "protocolText": "string, Protocol 全文",
  "crfText": "string, CRF/aCRF 全文"
}
```

字段说明：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `protocolText` | string | 是 | 研究方案全文 |
| `crfText` | string | 是 | CRF/aCRF 全文 |

响应：

```json
{
  "code": 0,
  "data": {
    "coreContents": [
      {
        "id": "protocol-carryover",
        "title": "Protocol 承接内容",
        "content": "string, AI 生成的该项核心内容",
        "confirmed": false
      },
      {
        "id": "statistical-endpoints",
        "title": "统计指标与终点口径",
        "content": "string, AI 生成的该项核心内容",
        "confirmed": false
      }
    ]
  }
}
```

前端交互建议：列表中的每一项都展示“确认”和“反馈重新生成”。用户确认后，业务侧将该项 `confirmed` 置为 `true`；如用户反馈，则调用下一接口。页面展示时不要把内容渲染成抽取表，也不要额外展示“来源状态”标签。

---

## 2. 根据反馈重新生成某项核心内容

调用时机：用户对某一项核心内容提供反馈，需要 AI 只重写该项内容。

请求：

```http
POST /ai/v1/sap/core-content/regenerate
Content-Type: application/json
```

```json
{
  "protocolText": "string, Protocol 全文",
  "crfText": "string, CRF/aCRF 全文",
  "item": {
    "id": "endpoints",
    "title": "主要/次要终点与成功判定",
    "content": "string, 当前待修改内容",
    "confirmed": false
  },
  "feedback": "请补充主要终点的访视窗口，并避免写未在方案中出现的探索性终点。",
  "allCoreContents": [
    {
      "id": "study-design",
      "title": "研究设计与总体口径",
      "content": "string",
      "confirmed": true
    },
    {
      "id": "endpoints",
      "title": "主要/次要终点与成功判定",
      "content": "string",
      "confirmed": false
    }
  ]
}
```

响应：

```json
{
  "code": 0,
  "data": {
    "coreContent": {
      "id": "endpoints",
      "title": "主要/次要终点与成功判定",
      "content": "string, 按反馈重新生成后的内容",
      "confirmed": false
    }
  }
}
```

说明：

- 本接口只返回被重写的单项核心内容。
- 重新生成后仍应让用户再次确认。
- `allCoreContents` 可选，但建议传入，用于保持其他已确认核心内容的一致性。

---

## 3. 生成 SAP Markdown 文档

调用时机：后端已经拿到 Protocol、CRF、用户确认后的核心内容、用户编辑后的大纲后，直接生成完整 SAP 文档。无需单独调用“大纲确认”接口。

请求：

```http
POST /ai/v1/sap/document/generate
Content-Type: application/json
```

```json
{
  "protocolText": "string, Protocol 全文",
  "crfText": "string, CRF/aCRF 全文",
  "coreContents": [
    {
      "id": "study-design",
      "title": "研究设计与总体口径",
      "content": "string, 用户已确认内容",
      "confirmed": true
    },
    {
      "id": "endpoints",
      "title": "主要/次要终点与成功判定",
      "content": "string, 用户已确认内容",
      "confirmed": true
    }
  ],
  "outline": [
    {
      "id": "0",
      "title": "文档信息与版本控制",
      "titleEn": "Document Control",
      "subsections": [
        "0.1 标题页（研究题目/方案号/申办方/统计负责人）"
      ],
      "description": "文档元信息、版本历史、审批与定稿节点"
    }
  ],
  "meta": {
    "studyTitle": "中文研究题目",
    "studyTitleEn": "English Study Title",
    "protocolNo": "PROT-001",
    "version": "1.0",
    "date": "2026-05-12",
    "sponsor": "申办方",
    "leadStatistician": "统计负责人"
  }
}
```

字段说明：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `protocolText` | string | 是 | 研究方案全文 |
| `crfText` | string | 是 | CRF/aCRF 全文 |
| `coreContents` | array | 是 | 用户已确认的核心内容列表 |
| `outline` | array | 是 | 后端传入的用户编辑后大纲 |
| `meta` | object | 否 | 封面元数据 |

响应：

```json
{
  "code": 0,
  "data": {
    "documentContent": "# 统计分析计划（Statistical Analysis Plan）\n\n| 字段 | 内容 |\n| --- | --- |\n...",
    "contentType": "text/markdown",
    "coverMeta": {
      "studyTitle": "中文研究题目",
      "studyTitleEn": "English Study Title",
      "protocolNo": "PROT-001",
      "version": "1.0",
      "date": "2026-05-12",
      "sponsor": "申办方",
      "leadStatistician": "统计负责人"
    },
    "sections": [
      {
        "id": "0",
        "title": "文档信息与版本控制",
        "titleEn": "Document Control",
        "content": "string, 该章节正文"
      }
    ]
  }
}
```

说明：

- `documentContent` 是完整 Markdown 文档，可直接存储或交给前端富文本/Markdown 渲染器展示。
- 本接口不返回 Word/docx/pdf；如需文件，调用下一节导出接口。
- 每个章节生成前都会按章节名匹配 `sap_guides.md` 指导；匹配不到的章节由模型结合已确认核心内容、Protocol/CRF 和前文 SAP 自主生成。

---

## 4. Markdown 转 docx/pdf

调用时机：后端已经拿到或保存了 SAP Markdown，需要转换成 Word 或 PDF 文件。

请求：

```http
POST /ai/v1/sap/document/export
Content-Type: application/json
```

```json
{
  "format": "docx",
  "filename": "SAP-v1.0",
  "markdown": "# 统计分析计划\n\n## 1 研究概述\n\n正文..."
}
```

字段说明：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `format` | string | 是 | `docx` 或 `pdf` |
| `filename` | string | 否 | 下载文件名；不需要带扩展名 |
| `markdown` | string | 否 | SAP Markdown 文档正文；与 `documentContent` 二选一 |
| `documentContent` | string | 否 | SAP Markdown 文档正文；兼容生成接口返回字段 |

成功响应：

- `format=docx`：返回 `application/vnd.openxmlformats-officedocument.wordprocessingml.document` 二进制文件。
- `format=pdf`：返回 `application/pdf` 二进制文件。
- 响应头包含 `Content-Disposition: attachment`。

---

## 推荐调用流程

1. 后端解析 Protocol/CRF，得到 `protocolText`、`crfText`。
2. 调用 `/ai/v1/sap/core-content/generate`，AI 按系统固定核心内容清单生成各项内容。
3. 前端逐项展示核心内容；每项可确认，或调用 `/ai/v1/sap/core-content/regenerate` 按反馈重写。
4. 后端收集用户编辑后的大纲。
5. 调用 `/ai/v1/sap/document/generate`，一次性传入 `protocolText`、`crfText`、`coreContents`、`outline`，得到完整 SAP Markdown 文档。
6. 如需下载，调用 `/ai/v1/sap/document/export`，以 JSON 传入 Markdown，把文档转成 docx 或 pdf。
