# 旧版前端接口兼容说明

从 `main` 合并前的 Next.js 接口保留路径和返回格式。本地默认地址为
`http://127.0.0.1:3000`，启动命令：

```powershell
.\.venv\Scripts\sapgen.exe serve --harness
```

正式 JSON 接口同时支持 `/ai/v1/sap` 和 `/api/ai/v1/sap` 前缀：

| POST 路径后缀 | 成功响应 `data` | 主要输入 |
| --- | --- | --- |
| `/core-content/generate` | `coreContents`（六项 `id/title/content/confirmed`） | `protocolText`, `crfText` |
| `/core-content/regenerate` | `coreContent` | 上述文本、`item`, `feedback`, 可选 `allCoreContents` |
| `/document/generate` | `documentContent`, `contentType`, `coverMeta`, `sections` | 上述文本、已确认 `coreContents`, `outline`, 可选 `meta` |
| `/document/generate-with-revision` | 同上 | 同上 |
| `/document/export` | DOCX/PDF 附件 | `format`, `documentContent` 或 `markdown`, 可选 `filename` |

成功 JSON 是 `{"code":0,"data":...}`；请求校验失败返回 HTTP 400 与
`{"code":1,"message":"..."}`，服务失败返回 HTTP 500 与相同错误包装。
导出要求 `application/json`，否则返回 HTTP 415。成功导出含
`Content-Type`、`Content-Length`、`Content-Disposition`。

旧版浏览器上传接口也保留：

| POST 路径 | 成功结果 |
| --- | --- |
| `/api/generate-core-content` | `{"items":[...]}` |
| `/api/revise-core-content` | `{"item":{...}}` |
| `/api/generate-sap` | `application/x-ndjson`：`status`、`progress`、`done` 或 `error` 事件 |
| `/api/generate-tfl-shells` | `application/x-ndjson`：`progress`、`done` 或 `error` 事件 |

上传字段维持 `protocol`、`crf` 文件及原有 JSON 文本字段。上传错误为
`{"error":"..."}`。DSH 输出的实际正文可能与旧模型不同；这里保证的是
HTTP 路径、请求字段、响应字段及流事件格式。`generate-with-revision`
当前与 `generate` 共享 DSH 审核管线。
