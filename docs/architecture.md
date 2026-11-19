# SAP 生成系统架构

## 设计边界

DeepSeek Harness 负责通用智能体能力：Agent Loop、模型适配、工具注册、会话状态、运行事件与恢复。本系统不重写这些能力。应用层通过官方 Python SDK 启动 SDK profile，并可通过安装式 bundle 把确定性 SAP 工具暴露给模型。

SAP 应用层负责专业数据和质量门禁：

1. 材料接入层保留来源文件、位置和原文片段。
2. SAP-IR 层统一保存事实、统计决策、来源状态和待确认项。
3. 专项模块在同一 SAP-IR 上工作，不独立生成互相冲突的章节。
4. 规则引擎执行确定性检查，模型不能覆盖规则错误。
5. 章节生成器只读取 SAP-IR，不在写作阶段新增统计决策。
6. 导出层生成可编辑 SAP 和 TFL 表壳。

## 运行时序

```text
用户上传材料
  -> DocumentIngestor 解析并形成 EvidenceCorpus
  -> DeepSeek Harness 抽取带证据的 SAP-IR
  -> AnalysisDesignModule
  -> ComplexDataModule
  -> SafetyAnalysisModule
  -> TFLGenerationModule
  -> RuleEngine
  -> 人工确认和 SAP-IR 修订
  -> SectionGenerator
  -> SAPDocxExporter / TFLDocxExporter
```

Harness 不可用时，系统只执行保守的启发式证据抽取。该流程可以形成工作 SAP-IR 和待确认项，但不会把常用统计方法自动标记为方案规定。

## 来源状态

- `confirmed`：存在材料中的直接证据，必须带 `EvidenceRef`。
- `user_confirmed`：统计人员已经确认，可没有材料原文，但应在审核记录中说明。
- `inferred`：系统候选或推断，必须出现在审核范围内。
- `missing`：材料没有给出或尚未可靠识别。

## 高风险决策门禁

- 每个估计目标必须具有人群、变量、治疗条件、伴发事件策略和群体水平汇总。
- 每个估计目标恰好有一个主分析。
- 主分析必须明确模型、效应量、检验方法和分析人群。
- 伴发事件策略与缺失数据机制保持为不同对象。
- MNAR 假设需要敏感性分析。
- 安全性分析必须明确 TEAE 起止、MedDRA 版本、SOC/PT 和分母。
- TFL 必须引用有效分析方法和人群，并具有表号、行列、统计量、分母和脚注。

## 版本与回归策略

DeepSeek Harness 仍处于开发预览版。适配层不向领域模块暴露 SDK 类型，只提供 `complete_json` 协议。SDK 升级时运行三类回归：

1. 启动、模型初始化和显式 `DSH_HOME` 检查。
2. 同一 session ID 的连续调用和事件终止状态检查。
3. SAP-IR JSON Schema 生成、解析和错误回退检查。

