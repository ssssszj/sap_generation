# SAP 事实表（Fact Sheet）字段规范（强制 JSON）

生成 SAP 前，先从 Protocol/CRF 抽取“事实表”，用于后续各章节写作与一致性约束。输出必须为 **严格 JSON**，不得包含解释文字。

## JSON Schema（简化版）

```json
{
  "study_title": "",
  "protocol_no": "",
  "version": "",
  "date": "",
  "primary_endpoints": [
    { "name": "", "definition": "", "time_window": "", "success_rule": "" }
  ],
  "hypotheses": {
    "type": "", 
    "alpha": "",
    "H0": "",
    "H1": ""
  },
  "analysis_sets": {
    "FAS": "",
    "PPS": "",
    "SS": ""
  },
  "dof_rule": {
    "threshold": "",
    "interpolation": "",
    "smoothing": "",
    "continuity": "",
    "formula_text": ""
  },
  "second_eye_policy": {
    "inconsistent_implant": "",
    "efficacy_usage": "",
    "dedicated_set": ""
  },
  "sample_size_scope": {
    "statistical_assumptions": "",
    "operational_constraints": ""
  },
  "consistency_anchors": {
    "primary_endpoint_unit": "",
    "second_eye_handling": "",
    "primary_missing_main": "",
    "primary_missing_sensitivity": "",
    "hypothesis_direction_bcdva": "",
    "hypothesis_direction_dciva": "",
    "hypothesis_direction_dof": "",
    "visit_window_main": "",
    "visit_anchor_timepoint": ""
  },
  "missing_data": {
    "primary_endpoint": "",
    "other": "",
    "sensitivity": ""
  },
  "key_numbers_dates_units": [
    { "field": "", "value": "", "unit": "", "source": "protocol|crf", "evidence": "" }
  ],
  "inclusion_criteria": [
    "..."
  ],
  "terminology_style": {
    "inequality": "≤≥|<= >=",
    "ci_style": "95% CI|95%置信区间",
    "alpha_style": "α|alpha"
  }
}
```

## 规则

- 若输入未提供某字段：填空字符串 `\"\"` 或空数组 `[]`，不得臆造。
- `key_numbers_dates_units` 尽量覆盖关键数值/日期/单位（用于 G1 一致性约束）。
- `analysis_sets/hypotheses/missing_data/inclusion_criteria` 是优先字段（对应 G2/G3/G4/G5）。
- 若存在 DOF/离焦曲线内容：必须拆分 `dof_rule`（阈值、插值、平滑、连续性、公式文本）。
- 若存在第二术眼策略：必须拆分 `second_eye_policy`（不一致植入时的处理、疗效是否使用、是否专用分析集）。
- 样本量相关内容需拆分到 `sample_size_scope`：统计假设与运营约束分开填写。
- 必须抽取 `consistency_anchors`，作为全文锁定口径：
  - `primary_endpoint_unit`：如“第一只术眼”或“双眼平均值”；
  - `second_eye_handling`：对侧眼不一致植入时如何处理；
  - `primary_missing_main` 与 `primary_missing_sensitivity`：主分析与敏感性分析缺失策略；
  - `hypothesis_direction_*`：各主要终点比较方向（结合量表方向，如 logMAR 越小越好）；
  - `visit_window_main` 与 `visit_anchor_timepoint`：主终点访视窗与时间锚点。

