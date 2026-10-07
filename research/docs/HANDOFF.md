# SAP 毕业设计换机 Handoff

更新时间：2026-10-07

远程仓库：`git@github.com:ssssszj/sap_generation.git`

工作分支：`thesis/sap-benchmark-posttraining`

## 1. 当前结论

Benchmark 的“采集＋首轮标注＋终审草案筛选”阶段已经完成，当前远程分支应包含：

- 141 个完成首轮标注的公开研究，共 2,589 条 Requirements；
- 100 道 `keep_draft` 题目，共 1,771 条 Requirements；
- 21 个 `hold_version_or_provenance`；
- 20 个 `exclude_post_primary_or_execution_informed`；
- 1 个私有 Pilot，共 26 条 Requirements，不计入公开 100 题；
- 总 Requirements 数为 2,615；
- 候选队列已清零，采集在 100 道保留草案处停止。

这 100 道题全部是 `draft_needs_expert_review`。当前 **0 道**完成独立专家审定，**0 道**进入冻结 train/dev/test 划分。因此可以用于流程调试和探索性 Baseline，但不能把它们写成“100 道最终金标准”。

## 2. 新电脑获取代码

```bash
git clone --branch thesis/sap-benchmark-posttraining --single-branch \
  git@github.com:ssssszj/sap_generation.git
cd sap_generation
git status -sb
git log --oneline -5
```

若仓库已存在：

```bash
git fetch origin
git switch thesis/sap-benchmark-posttraining
git pull --ff-only origin thesis/sap-benchmark-posttraining
```

不要从 `main` 继续 Benchmark 工作，也不要把该分支强推覆盖。

## 3. 权威状态文件

- `research/benchmark/final_audit/initial_draft_question_set.json`：100 道保留草案的权威清单。
- `research/benchmark/final_audit/questions.jsonl`：141 个公开研究的终审结果。
- `research/benchmark/final_audit/registry_chronology.jsonl`：终审使用的注册时间信息。
- `research/benchmark/manifests/studies.jsonl`：研究清单。
- `research/benchmark/manifests/documents.jsonl`：文档 URL、角色、日期、路径与 SHA-256。
- `research/benchmark/gold/<STUDY_ID>/requirements.jsonl`：逐题评价要求。
- `research/benchmark/gold/<STUDY_ID>/annotation_status.json`：标注状态、争议与专家复核请求。
- `research/benchmark/data_card.md`：数据卡和限制。
- `research/docs/SAP_毕业设计研究方案_2026-10-07.md`：当前完整毕设方案。

不要根据专家复核包的文件名或批次号推算题目数量；最终数量只认 `final_audit` 产物。

## 4. 换机后先运行的验证

Benchmark 验证不依赖 Node.js：

```bash
python3 research/benchmark/tools/finalize_initial_benchmark.py --check
python3 research/benchmark/tools/audit_initial_delivery.py
python3 research/benchmark/tools/validate_benchmark.py
git diff --check -- research/benchmark research/docs plan
```

预期结果：三个检查均成功；`validate_benchmark.py` 为 `errors: []`，并可能报告私有 Pilot 的两个既有语义复核 warning。warning 不代表 Benchmark 已通过专家审定。

## 5. 公共源文件不会全部随 Git 迁移

公开 Protocol/SAP 的大部分 PDF 位于 `research/benchmark/sources/public/`，受 `.gitignore` 管理。Git 中保存 URL、路径和冻结哈希，而不是把全部源文件作为可重分发数据提交。

需要某个研究时按 manifest 重新下载并校验：

```bash
python3 research/benchmark/tools/fetch_public_sources.py \
  --study-id PUBLIC-ORAL-IMMUNOTHERAPY-ADULT-001
```

不传 `--study-id` 或 `--document-id` 会尝试获取全部公开文档，数据量和耗时较大。参考 SAP 只用于标注/评价，绝不能放入生成模型的可见输入。

私有 Pilot 的原始文件、密钥、`.env`、本地缓存和未获授权材料不会随远程仓库迁移，需要通过单独的受控方式复制。

## 6. 下一阶段的正确顺序

1. 统计/临床专家复核 100 道保留草案，优先审 Critical/Major Requirements、证据语义和 `needs_confirmation` 边界。
2. 对专家淘汰项按相同准入规则一对一补位，保持 100 个独立研究家族。
3. 做研究家族和近重复检查，冻结 Benchmark v1.0 及文件哈希。
4. 冻结建议的 40 train / 20 dev / 40 test；同一研究的版本、章节、翻译、合成变体和偏好对必须在同一侧。
5. 校准确定性检查＋冻结版 LLM Judge＋人工复核三级评价器。
6. 在统一输入和推理预算下运行 7–9B/14B/27–32B 级 Baseline。
7. 仅使用 train 家族构造 SFT 数据并训练，在 dev 上选择模型，最后一次性运行 test。
8. 只有 SFT 后仍存在稳定错误且偏好信号可靠时，再做 DPO；GRPO 仅作为可选扩展，不是毕业必要条件。
9. 完成私有化部署、人工修改时间和断网验收。

## 7. 评价口径

主要指标建议使用研究级 `Critical Pass Rate`：只有该研究所有适用 Critical Requirements 通过，且不存在严重虚构或矛盾，才记为通过。

同时报告：

- Critical/Major Requirement 通过率；
- 关键事实精确率和召回率；
- 必要内容覆盖率；
- 无依据断言率；
- 内部矛盾数；
- 证据引用正确率；
- 方法充分性与信息不足处理；
- 人工修改时间；
- token、时延、显存和失败率。

LLM Judge 按 Requirements 逐条判断并给出证据，不要只输出一个不可解释的总分。

## 8. 数据泄漏红线

- reference SAP 永远不能进入模型可见输入、RAG 索引或提示模板。
- 测试家族不能用于 SFT、偏好数据、提示词调优、阈值选择或 Judge 训练。
- 同一研究家族的任何派生数据必须留在同一个 split。
- `confirmed_decisions` 只能包含明确记录的人类决策，并与 `protocol_only` 分开报告。
- 公开可下载不等于可以重新分发；对外发布前重新核对来源条款。

## 9. 当前不应宣称的内容

- 不应称“100 道专家审核完成”或“最终 Benchmark 已冻结”。
- 不应声称 SFT、DPO 或 RL 已提升效果；训练和盲测尚未开始。
- 不应把 2,615 条 Requirements 说成 2,615 个独立研究或题目。
- 不应把 hold/exclude 研究加入题目数量。
- 不应把私有 Pilot 计入公开 100 题或最终测试。

## 10. 应用运行（需要时）

Benchmark 文档工作不需要安装前端依赖。需要运行现有 Web 原型时，再执行：

```bash
npm ci
npm run dev
```

不要提交 `.env` 或 API Key。最终实验需要把模型地址、模型版本、提示版本、输入哈希、随机种子和推理参数写入运行记录。

## 11. 本次推送范围

本次文档提交只包含：

- `plan/` 下的项目概览、结构、进度和任务包；
- `research/docs/SAP_毕业设计研究方案_2026-10-07.md`；
- `research/docs/HANDOFF.md`。

本机工作树中已有的应用代码、package 文件、Electron 目录、开题 DOCX/PPTX 及其他用户改动没有并入本次文档提交。换机后如果仍需要这些未提交内容，应从旧电脑单独保留；不要误以为它们已经在远程分支中。

## 12. 首个接续任务

不要继续盲目扩题。首先从 100 道保留草案中生成专家复核清单，按研究分组输出 Critical/Major Requirement、证据定位、开放版本问题和需要仲裁的统计决策；先用 5—10 道题试跑专家流程，测量单题耗时和分歧类型，再安排完整复核。
