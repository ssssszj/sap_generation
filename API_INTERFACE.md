# SAP 后端接口文档

本文档描述当前服务对外提供的 SAP 核心内容生成、SAP 文档生成、文档导出以及浏览器演示接口。文档以当前代码实现为准。

## 1. 接入概览

### 1.1 Base URL

以部署地址为准。本地开发环境示例：

```text
http://localhost:3000
```

### 1.2 接口路径

正式 JSON 接口同时暴露两套等价路径：

| 推荐路径 | 兼容路径 |
| --- | --- |
| `/ai/v1/sap/core-content/generate` | `/api/ai/v1/sap/core-content/generate` |
| `/ai/v1/sap/core-content/regenerate` | `/api/ai/v1/sap/core-content/regenerate` |
| `/ai/v1/sap/document/generate` | `/api/ai/v1/sap/document/generate` |
| `/ai/v1/sap/document/generate-with-revision` | `/api/ai/v1/sap/document/generate-with-revision` |
| `/ai/v1/sap/document/export` | `/api/ai/v1/sap/document/export` |

新接入建议使用 `/ai/v1/...`。

### 1.3 两类调用方式

| 类型 | 用途 | 请求格式 | 响应格式 |
| --- | --- | --- | --- |
| 正式版本化接口 | 业务后端对接 | `application/json` | JSON 或导出文件 |
| 浏览器演示接口 | 现有本地页面 | `multipart/form-data` | JSON 或 NDJSON 流 |

正式接口不接收 Protocol/CRF 文件，由调用方将文件解析为文本后传入。演示接口可直接上传 `.pdf`/`.docx`/`.txt`/`.md`。

## 2. 通用约定

### 2.1 字符编码

- JSON 和 NDJSON 均使用 UTF-8。
- 文本字段不应使用 Base64。
- `protocolText`、`crfText` 和 `documentContent` 传入原始文本。

### 2.2 成功 JSON 包装

```json
{
  "code": 0,
  "data": {}
}
```

### 2.3 失败 JSON 包装

```json
{
  "code": 1,
  "message": "错误信息"
}
```

### 2.4 HTTP 状态码

| 状态码 | 含义 |
| --- | --- |
| `200` | 成功；流式接口仍需继续检查流内 `error` 事件 |
| `400` | 必填字段缺失、JSON 形式错误或业务校验失败 |
| `415` | 导出接口的 `Content-Type` 不是 `application/json` |
| `500` | 模型调用、生成、解析或导出失败 |

### 2.5 认证与 CORS

- 当前应用未实现业务层 API 认证、签名或租户校验。
- 当前未显式设置 CORS 响应头。
- 生产环境建议将服务放在 API Gateway/反向代理后，由网关负责认证、限流、CORS、请求体大小限制和审计。
- 前端跨域直调前，必须在部署层增加 CORS；同域部署或后端转发不需要 CORS。

### 2.6 长任务

- DeepSeek Flash 会产生内部推理 token，完整 SAP 可能需要数分钟到数十分钟。
- 正式文档生成接口是同步 JSON 接口，调用方的网关、HTTP 客户端和负载均衡器必须放宽超时。
- 浏览器演示版 SAP/TFL 接口使用 NDJSON 流实时传递进度。
- 调用方不应对完整文档请求进行无限自动重试，否则会重复消耗 token。

## 3. 公共数据结构

### 3.1 CoreContentItem

```ts
type CoreContentItem = {
  id: string;
  title: string;
  content: string;
  confirmed?: boolean;
};
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | string | 稳定业务标识 |
| `title` | string | 展示标题 |
| `content` | string | 核心内容正文 |
| `confirmed` | boolean | 用户是否已确认；重新生成后为 `false` |

系统固定生成以下 6 项：

| `id` | `title` |
| --- | --- |
| `protocol-carryover` | Protocol 承接内容 |
| `statistical-endpoints` | 统计指标与终点口径 |
| `result-presentation` | 结果展示方向 |
| `statistical-methods` | 统计方法 |
| `analysis-populations` | 分析集 |
| `key-statistical-rules` | 关键统计规则 |

### 3.2 SapCoverMeta

```ts
type SapCoverMeta = {
  studyTitle?: string;
  studyTitleEn?: string;
  protocolNo?: string;
  version?: string;
  date?: string;
  sponsor?: string;
  leadStatistician?: string;
};
```

`date` 建议使用 `YYYY-MM-DD`。若 Fact Sheet 从 Protocol 抽取到明确版本号或日期，生成器可用抽取值回填 `version`/`date`。

### 3.3 SapOutlineInput

```ts
type SapOutlineInput = {
  id?: string;
  title?: string;
  titleEn?: string;
  level?: number;
  description?: string;
  subsections?: Array<string | SapOutlineInput>;
  children?: SapOutlineInput[];
};
```

支持三种形式：

1. 树形：一级章节使用 `children` 传二级标题。
2. 简化树形：一级章节使用 `subsections` 传字符串或对象。
3. 扁平形式：数组中一级项使用 `level: 1`，后续二级项使用 `level: 2`。

`title` 必须直接包含章节编号，例如 `2 分析目标、指标与口径`、`2.1 主要目的与主要终点`。`id` 为业务标识，不会自动拼接到标题。

## 4. 正式 JSON 接口

### 4.1 生成待确认核心内容

```http
POST /ai/v1/sap/core-content/generate
Content-Type: application/json
```

请求：

```json
{
  "protocolText": "Protocol 全文",
  "crfText": "CRF/aCRF 全文"
}
```

| 字段 | 类型 | 必填 | 约束 |
| --- | --- | --- | --- |
| `protocolText` | string | 是 | `trim()` 后不能为空 |
| `crfText` | string | 是 | `trim()` 后不能为空 |

成功响应：

```json
{
  "code": 0,
  "data": {
    "coreContents": [
      {
        "id": "protocol-carryover",
        "title": "Protocol 承接内容",
        "content": "AI 生成的待确认内容",
        "confirmed": false
      }
    ]
  }
}
```

### 4.2 根据反馈重新生成某项核心内容

```http
POST /ai/v1/sap/core-content/regenerate
Content-Type: application/json
```

请求：

```json
{
  "protocolText": "Protocol 全文",
  "crfText": "CRF/aCRF 全文",
  "item": {
    "id": "statistical-endpoints",
    "title": "统计指标与终点口径",
    "content": "当前内容",
    "confirmed": false
  },
  "feedback": "请补充主要终点的访视窗口。",
  "allCoreContents": [
    {
      "id": "protocol-carryover",
      "title": "Protocol 承接内容",
      "content": "已确认内容",
      "confirmed": true
    }
  ]
}
```

| 字段 | 类型 | 必填 | 约束 |
| --- | --- | --- | --- |
| `protocolText` | string | 是 | 非空 |
| `crfText` | string | 是 | 非空 |
| `item` | CoreContentItem | 是 | `id`、`title`、`content` 必须非空 |
| `feedback` | string | 是 | 非空 |
| `allCoreContents` | CoreContentItem[] | 否 | 建议传入，用于保持与其他项一致 |

成功响应：

```json
{
  "code": 0,
  "data": {
    "coreContent": {
      "id": "statistical-endpoints",
      "title": "统计指标与终点口径",
      "content": "按反馈重新生成的内容",
      "confirmed": false
    }
  }
}
```

### 4.3 生成 SAP Markdown（单次章节生成）

```http
POST /ai/v1/sap/document/generate
Content-Type: application/json
```

请求：

```json
{
  "protocolText": "Protocol 全文",
  "crfText": "CRF/aCRF 全文",
  "coreContents": [
    {
      "id": "protocol-carryover",
      "title": "Protocol 承接内容",
      "content": "用户已确认内容",
      "confirmed": true
    }
  ],
  "outline": [
    {
      "id": "2",
      "title": "2 分析目标、指标与口径",
      "titleEn": "Objectives, Endpoints, Definitions",
      "description": "主要/次要/探索性终点及精确定义",
      "children": [
        {
          "id": "2.1",
          "title": "2.1 主要目的与主要终点",
          "level": 2
        },
        {
          "id": "2.2",
          "title": "2.2 次要目的与次要终点",
          "level": 2
        }
      ]
    }
  ],
  "meta": {
    "studyTitle": "中文研究题目",
    "studyTitleEn": "English Study Title",
    "protocolNo": "PROT-001",
    "version": "1.0",
    "date": "2026-11-03",
    "sponsor": "申办方",
    "leadStatistician": "统计负责人"
  }
}
```

| 字段 | 类型 | 必填 | 约束 |
| --- | --- | --- | --- |
| `protocolText` | string | 是 | 非空 |
| `crfText` | string | 是 | 非空 |
| `coreContents` | CoreContentItem[] | 是 | 非空；任一项 `confirmed === false` 时拒绝生成 |
| `outline` | SapOutlineInput[] | 是 | 非空；规范化后至少保留一个非空 `title` |
| `meta` | SapCoverMeta | 否 | 封面元数据 |

说明：

- `coreContents` 建议所有项显式传 `confirmed: true`。
- 服务会先从 Protocol/CRF 抽取 Fact Sheet，再按 `outline` 顺序串行生成每章。
- 本接口不执行 rubric/Hard Gates 二次修订流程。
- 该接口是同步长请求，成功前不返回中间进度。

成功响应：

```json
{
  "code": 0,
  "data": {
    "documentContent": "完整 SAP Markdown 字符串",
    "contentType": "text/markdown",
    "coverMeta": {
      "studyTitle": "中文研究题目",
      "studyTitleEn": "English Study Title",
      "protocolNo": "PROT-001",
      "version": "1.0",
      "date": "2026-11-03",
      "sponsor": "申办方",
      "leadStatistician": "统计负责人"
    },
    "sections": [
      {
        "id": "2",
        "title": "2 分析目标、指标与口径",
        "titleEn": "Objectives, Endpoints, Definitions",
        "content": "该章节正文"
      }
    ]
  }
}
```

### 4.4 生成 SAP Markdown（带 Revision）

```http
POST /ai/v1/sap/document/generate-with-revision
Content-Type: application/json
```

请求和响应与 4.3 完全相同。差异在执行流程：

1. 生成章节草稿。
2. 使用 `rubrics.json` 修订。
3. 对 G1–G5 逐项执行 Hard Gates QA。
4. 检测到本地规则问题时再执行一次定向修复。

该接口的模型调用次数、耗时和 token 消耗显著高于 4.3，建议仅在明确需要自动 QA 时使用。

### 4.5 导出 DOCX/PDF

```http
POST /ai/v1/sap/document/export
Content-Type: application/json
```

请求：

```json
{
  "format": "docx",
  "filename": "SAP-v1.0",
  "documentContent": "# 统计分析计划\n\n## 1 研究概述\n\n正文..."
}
```

| 字段 | 类型 | 必填 | 约束 |
| --- | --- | --- | --- |
| `format` | `"docx" \| "pdf"` | 是 | 其他值返回 `400` |
| `filename` | string | 否 | 不需扩展名；服务会去除非法文件名字符，最长取 120 字符 |
| `documentContent` | string | 二选一 | 生成接口返回的 Markdown |
| `markdown` | string | 二选一 | `documentContent` 的别名；两者同时存在时优先 `markdown` |

成功响应不使用 JSON 包装：

| `format` | `Content-Type` |
| --- | --- |
| `docx` | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` |
| `pdf` | `application/pdf` |

响应头包含：

```text
Content-Length: <bytes>
Content-Disposition: attachment; filename="..."; filename*=UTF-8''...
```

失败时返回通用 JSON 错误包装。

## 5. 浏览器演示接口

这些接口为当前 `/` 页面使用的上传/流式接口。若业务后端已能解析文件，优先使用第 4 节的正式 JSON 接口。

### 5.1 上传文件生成核心内容

```http
POST /api/generate-core-content
Content-Type: multipart/form-data
```

| FormData 字段 | 类型 | 必填 |
| --- | --- | --- |
| `protocol` | File | 是 |
| `crf` | File | 是 |

支持扩展名：`.pdf`、`.docx`、`.txt`、`.md`。

成功响应：

```json
{
  "items": [
    {
      "id": "protocol-carryover",
      "title": "Protocol 承接内容",
      "content": "...",
      "confirmed": false
    }
  ]
}
```

失败响应：

```json
{
  "error": "错误信息"
}
```

### 5.2 上传文件重新生成某项核心内容

```http
POST /api/revise-core-content
Content-Type: multipart/form-data
```

| FormData 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `protocol` | File | 是 | Protocol 文件 |
| `crf` | File | 是 | CRF/aCRF 文件 |
| `item` | string | 是 | `CoreContentItem` 的 JSON 字符串 |
| `feedback` | string | 是 | 用户反馈 |
| `allItems` | string | 否 | `CoreContentItem[]` 的 JSON 字符串 |

成功响应：

```json
{
  "item": {
    "id": "statistical-endpoints",
    "title": "统计指标与终点口径",
    "content": "修订后内容",
    "confirmed": false
  }
}
```

### 5.3 流式生成 SAP

```http
POST /api/generate-sap
Content-Type: multipart/form-data
Accept: application/x-ndjson
```

| FormData 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `protocol` | File | 是 | Protocol 文件 |
| `crf` | File | 是 | CRF/aCRF 文件 |
| `meta` | string | 否 | `SapCoverMeta` JSON 字符串 |
| `coreContent` | string | 否 | `CoreContentItem[]` JSON 字符串 |
| `outline` | string | 否 | `SapSection[]` JSON 字符串；不传时使用系统默认 13 章 |

注意：该接口的 `outline` 直接使用内部 `SapSection` 结构，二级标题字段名为 `subsections: string[]`，不是正式接口的 `children`。

响应 `Content-Type`：

```text
application/x-ndjson
```

每行是一个独立 JSON 对象，行尾为 `\n`。

状态事件：

```json
{"type":"status","message":"正在抽取 Fact Sheet（结构化事实表）..."}
```

章节进度事件：

```json
{
  "type": "progress",
  "current": 2,
  "total": 13,
  "section": {
    "id": "1",
    "title": "1 研究概述",
    "titleEn": "Study Overview / Trial Registration"
  }
}
```

完成事件：

```json
{
  "type": "done",
  "result": {
    "success": true,
    "coverMeta": {},
    "fullDocument": "完整 SAP Markdown",
    "sectionsCount": 13
  }
}
```

流内错误事件：

```json
{
  "type": "error",
  "error": "错误信息"
}
```

重要：响应流建立后，HTTP 状态通常已经是 `200`。因此不能只检查 `response.ok`，还必须解析每个 NDJSON 事件并处理 `type: "error"`。

### 5.4 流式生成 TFL Shells

```http
POST /api/generate-tfl-shells
Content-Type: multipart/form-data
Accept: application/x-ndjson
```

| FormData 字段 | 类型 | 必填 |
| --- | --- | --- |
| `protocol` | File | 是 |
| `crf` | File | 是 |
| `sapText` | string | 是 |

进度事件：

```json
{"type":"progress","step":"table","status":"generating"}
{"type":"progress","step":"table","status":"done"}
{"type":"progress","step":"listing","status":"generating"}
{"type":"progress","step":"listing","status":"done"}
{"type":"progress","step":"figure","status":"generating"}
{"type":"progress","step":"figure","status":"done"}
```

`step` 枚举：`table | listing | figure`。`status` 枚举：`generating | done`。

完成事件：

```json
{
  "type": "done",
  "result": {
    "tableShells": "Table shells 正文",
    "figureShells": "Figure shells 正文",
    "listingShells": "Listing shells 正文",
    "fullDocument": "合并后 TFL Markdown/纯文本"
  }
}
```

错误事件与 5.3 相同。

### 5.5 浏览器解析 NDJSON 示例

```ts
async function readNdjson(response: Response) {
  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new Error(body.error || `HTTP ${response.status}`);
  }

  const reader = response.body?.getReader();
  if (!reader) throw new Error("响应流不可读");

  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n");
    buffer = lines.pop() ?? "";

    for (const line of lines) {
      if (!line.trim()) continue;
      const event = JSON.parse(line);
      if (event.type === "error") throw new Error(event.error);
      if (event.type === "status") console.log(event.message);
      if (event.type === "progress") console.log(event);
      if (event.type === "done") return event.result;
    }
  }

  if (buffer.trim()) {
    const event = JSON.parse(buffer);
    if (event.type === "error") throw new Error(event.error);
    if (event.type === "done") return event.result;
  }

  throw new Error("响应流在返回 done 前结束");
}
```

## 6. 推荐调用流程

### 6.1 业务后端集成

1. 业务后端解析 Protocol/CRF，得到 `protocolText` 和 `crfText`。
2. 调用 `/ai/v1/sap/core-content/generate`。
3. 前端展示 6 项核心内容，支持确认和反馈重生成。
4. 业务后端保存已确认的 `coreContents` 和用户编辑后的 `outline`。
5. 调用 `/ai/v1/sap/document/generate`生成 Markdown。
6. 需要强化自动 QA 时，将第 5 步替换为 `/generate-with-revision`。
7. 调用 `/ai/v1/sap/document/export` 导出 DOCX/PDF。

### 6.2 现有浏览器页面

1. 上传 Protocol/CRF 到 `/api/generate-core-content`。
2. 在浏览器中确认核心内容与大纲。
3. 上传文件和 JSON 字段到 `/api/generate-sap`，解析 NDJSON 进度流。
4. 需要 TFL 时调用 `/api/generate-tfl-shells`。

## 7. 生产接入注意事项

- 当前正式 JSON SAP 生成接口不流式返回进度。若网关无法承受长连接，建议在业务后端增加任务队列、任务 ID 和状态查询层。
- 当前没有生成任务幂等键。调用方自动重试前应确认前一请求已失败，避免重复耗费。
- 当前 TFL 只有浏览器 multipart/NDJSON 接口，尚未提供 `/ai/v1/...` JSON 版本。
- 不要将七牛云 `QNY_API_KEY` 下发给前端；密钥只存放在本服务的 `.env.local`/部署环境变量中。
- Protocol/CRF 可能包含敏感信息，业务方需根据合规要求配置传输加密、访问控制、数据留存和日志脱敏。
