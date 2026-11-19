# SAP 生成与审核系统

这是一个全新目录下实现的临床试验统计分析计划生成系统。它不依赖原仓库分支，按开题报告和答辩材料中的架构重新组织：DeepSeek Harness 提供通用 Agent Loop、模型调用、工具、会话和运行记录；本项目负责证据定位、SAP-IR、专项统计模块、规则检查、人工确认和 Word 输出。

系统定位是“生成可审核草稿”，不是替代统计专家作出方案中没有规定的统计决策。缺少证据的选择会进入待确认事项，不会被默认方法伪装成方案事实。

## 已实现能力

- 支持 DOCX、PDF、TXT 和 Markdown 研究材料接入，按来源文件和位置形成证据块。
- 通过官方 `deepseek-harness-sdk` 启动 DeepSeek Harness 的 SDK profile，复用 Agent Loop、模型适配、会话和事件日志。
- 以版本化 `SAP-IR` 保存研究设计、样本量、随机化、访视、终点、估计目标、分析集、分析方法、推导规则、伴发事件、缺失数据、安全性规则和 TFL 规格。
- 将证据提取拆为研究设计、终点与估计目标、分析人群与安全性、统计分析四个领域调用，避免一次性巨大 JSON 导致的遗漏和 max-token 失败。
- 统计分析方法设计模块只保留方案支持的方法；方案沉默时生成精确待确认项，不再仅根据终点类型自动套用 ANCOVA、Logistic 或负二项模型。
- 复杂数据处理模块分别维护 `IntercurrentEventPlan` 与 `MissingDataPlan`；不会为所有终点自动填入 MAR、MNAR、tipping point 或固定的伴发事件策略。
- 安全性分析模块显式记录 TEAE 时间窗、MedDRA 版本、SOC/PT 层级和分母；不会把疗效人群临时当作安全性人群。
- TFL 规格模块：把分析方法转换为 `TFLSpec`，输出可编辑 Word 表壳并与分析人群、方法和分母建立引用。
- 确定性规则引擎：检查引用、必填字段、主分析唯一性、来源状态、安全性口径和 TFL 完整性。
- 验证修复闭环：结构错误触发最多两轮最小 JSON Pointer patch 修复；仍有错误时阻断导出。
- SAP 正文按13个章节顺序生成；生成每个章节时都会携带此前全部章节、统一 SAP-IR 和研究级一致性合同，最后再执行一次全篇一致性审查。
- 条件化决策支持模块覆盖 native 基线最常见的失分点：样本量与分析人群、主分析合同、估计目标、伴发事件、缺失数据、敏感性分析、安全性、变量推导和具体 TFL 表壳。模块输出始终标记为 `conditional_proposal` 或 `unresolved`，不会冒充方案事实。
- Benchmark 评分：内置七类专项 Rubrics，可使用确定性规则评分，也可通过 DeepSeek Harness 执行 LLM-as-a-Judge。
- FastAPI 与本地审核界面：创建项目、上传材料、执行生成、查看检查问题和下载产物。
- SQLite 运行记录：保存项目、运行状态、阶段事件、Harness 会话 ID 和产物索引。
- Word 输出遵循表格单元格零缩进要求，不用空格或制表符制造单元格段首空白。

## 目录结构

```text
sapgen_rebuild/
  deepseek-plugin/       DeepSeek Harness 可安装工具 bundle
  docs/                  架构和数据契约
  examples/              可离线运行的示例 Protocol 与 SAP-IR
  reference/             从开题材料提取的结构化需求
  src/sapgen/
    domain/              SAP-IR 与规则引擎
    harness/             DeepSeek Harness SDK 适配层
    ingest/              文档解析与证据块
    modules/             四个 SAP 专项模块
    exporters/           SAP 与 TFL Word 导出
    web/                 本地审核界面
  tests/                 单元和端到端测试
```

## 安装

推荐使用 Python 3.11 或更高版本并创建独立虚拟环境。

```powershell
cd D:\Lab\sap_generation
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev,harness]"
Copy-Item .env.example .env
$node = 'C:\path\to\node-v22-or-newer\node.exe'
$env:PATH = "$(Split-Path $node);$env:PATH"
pnpm install --frozen-lockfile --registry=https://registry.npmjs.org
```

在 `.env` 或当前进程环境中设置 `DEEPSEEK_API_KEY`。如使用兼容端点，再设置 `DEEPSEEK_BASE_URL`。DeepSeek Harness 要求显式的 `DSH_HOME`，本项目默认使用 `.runtime/dsh-home`，不会读取用户目录中的隐式配置。

DeepSeek Harness 仍处于开发预览阶段。本项目固定 Python SDK `0.2.1rc2`，并固定 npm 运行时 `0.2.1-rc.5`。所有调用集中在 `harness/deepseek.py`，便于上游破坏性变更时替换。

当前官方 `0.2.1rc2` Windows runtime wheel 在部分环境会缺少 `node-addon-require-builtin-win32-x64-msvc`。项目因此提供官方 npm runtime 回退。运行上述 pnpm 命令后，在 `.env` 中把 `SAPGEN_DSH_NODE` 指向 Node.js 22.19 或更高版本，`SAPGEN_DSH_JS` 保持默认值即可。该回退仍运行官方 DeepSeek Harness，只替换启动载体。

注意：安装 npm 依赖时也必须让 Node.js 22.19+ 位于 `PATH` 最前面，否则 DSH 的
postinstall 会被旧版系统 Node 执行并失败。

## 启动 Web 系统

启用 DeepSeek Harness：

```powershell
.\.venv\Scripts\sapgen.exe serve --harness
```

仅运行规则模式：

```powershell
.\.venv\Scripts\sapgen.exe serve
```

浏览器访问 `http://127.0.0.1:3000`。旧版前端接口保持在同一端口：
`/ai/v1/sap/...` 和 `/api/ai/v1/sap/...` 两组 JSON 路由，以及
`/api/generate-core-content`、`/api/revise-core-content`、`/api/generate-sap`、
`/api/generate-tfl-shells` 上传路由。使用 `serve --harness` 时由 DSH 生成内容。
请求和响应字段见 [旧版接口兼容说明](docs/legacy-api.md)。

## CLI 示例

使用示例 SAP-IR 跑完整专项模块和导出链路，无需 API key：

```powershell
.\.venv\Scripts\sapgen.exe generate `
  --name "ABC-101 demo" `
  --input .\examples\demo_protocol.txt `
  --ir .\examples\demo_ir.json
```

直接从研究材料抽取 SAP-IR 并使用 DeepSeek Harness：

```powershell
.\.venv\Scripts\sapgen.exe generate `
  --name "Protocol generation" `
  --input D:\data\protocol.docx `
  --input D:\data\crf.pdf `
  --harness `
  --strict-harness
```

`--strict-harness` 会在 Harness 或模型调用失败时直接报错。省略该选项时，系统保留证据和待确认项，回退到确定性流程。

## 安装 DeepSeek Harness 工具插件

Python SDK 集成已经满足应用内的 Harness 调用。若还希望让 DeepSeek Harness 中的模型直接调用 `sap_validate_ir`、`sap_enrich_ir`、`sap_export_docx` 和 `sap_export_tfl`，可安装本项目的 bundle：

```powershell
$node = $env:SAPGEN_DSH_NODE
$dsh = (Resolve-Path 'node_modules/@deepseek-ai/dsh/lib/bin.js').Path
$env:DSH_HOME = (Resolve-Path '.runtime/dsh-home').Path
$env:SAPGEN_WORKSPACE_ROOT = (Resolve-Path '.').Path
$env:SAPGEN_PYTHON = (Resolve-Path '.venv\Scripts\python.exe').Path
& $node $dsh --profile sapgen --from-default-profile sdk --dump-default-config | Out-Null
& $node $dsh plugin --profile sapgen add file:./deepseek-plugin
$env:SAPGEN_DSH_PROFILE = 'sapgen'
```

安装或更新 bundle 后重启 Harness profile。插件对所有输入和输出路径执行工作区边界检查。

## 测试

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\ruff.exe check src tests
```

没有 API key 时，测试使用假 Harness 验证 JSON 契约和会话调用，不会发起模型请求。真实 Harness 的烟雾测试需要单独设置凭据。

## 20题 DSH 评测

先执行不调用模型的环境检查：

```powershell
.\scripts\run-dsh-benchmark.ps1 -Phase preflight
```

开始新的20题批次：

```powershell
.\scripts\run-dsh-benchmark.ps1 -Phase all -RunMode New
```

中断后续跑当前批次：

```powershell
.\scripts\run-dsh-benchmark.ps1 -Phase all -RunMode Resume
```

`New` 会保留旧批次、获取缺失的公开协议、重新构建输入并隔离新批次结果。运行结束后
脚本输出 DSH 均分、native LLM 基线和同题配对差值；当当前仓库没有 native 运行结果时，
使用 `benchmark/baselines/direct_llm_native_scores.csv` 中不含答案内容的冻结历史分数。

## 产物

每次运行在 `.runtime/data/<project-id>/runs/<run-id>/` 中生成：

- `sap-ir.json`：统一分析决策与来源状态。
- `validation-report.json`：结构化规则问题。
- `sap-draft.md`：便于版本对比的草稿。
- `sap-draft.docx`：可编辑 SAP 草稿。
- `tfl-shells.docx`：可编辑 TFL 表壳。

统计人员应先处理阻断性待确认事项，再将推断记录改为 `user_confirmed`，最后重新运行检查和导出。

