# 评价标准（rubrics.json）与 docx 对齐说明

## 权威来源

- **标准文件**：`SAP 候选 PDF 对齐参考 SAP PDF 的二元检查清单与确定性评分标准.docx`（与仓库内 `sap_rubric.docx` 为同内容副本时可互相替换）
- **机器可读导出**：`sap_rubric_plain.txt`（由 docx 用 Mammoth 提取的纯文本）
- **结构化 JSON**：`rubrics.json`（由 `scripts/build-rubrics-from-plain.js` 从 `sap_rubric_plain.txt` **自动生成**）

更新 docx 后请依次执行：

1. 将新 docx 覆盖 `knowledge_bank/sap_rubric.docx`（或复制为同名文件）
2. `node scripts/extract-sap-rubric.js` → 重新生成 `sap_rubric_plain.txt`
3. `node scripts/build-rubrics-from-plain.js` → 重新生成 `rubrics.json`

## 与执行摘要可能存在的差异

docx **执行摘要**中写「内容准确性 64 项、合计权重 80.00」，而从 **正文表格**按固定行结构解析得到的 CA 行数、权重合计可能与摘要不一致（例如合并单元格、排版差异）。`rubrics.json` 顶部的 `alignment_note` 与 `scoring_framework.dimensions[].parsed_*` 会记录**解析结果**；若与 Word 目视不一致，请以 Word 原表为准，并重新导出 `sap_rubric_plain.txt` 后再生成 JSON。

## 在 SAP 生成中的用法

`lib/sap-generator.ts` 在 **第二步「按评价标准修订」** 时，会注入 **完整** `rubrics.json`（不按 SAP 章节裁剪）。若单次请求过长，可在 `.env.local` 设置 `SAP_RUBRIC_MAX_CHARS`（整数）截断注入长度；不设或为 `0` 表示不截断。
