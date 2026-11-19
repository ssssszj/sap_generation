from __future__ import annotations

from typing import Any

SAP7_RUBRICS: list[dict[str, Any]] = [
    {
        "rubric_id": "SAP7-ESTIMAND-001",
        "category": "确定估计目标",
        "description": (
            "估计目标需要同时明确目标人群、治疗条件、终点变量、伴发事件处理策略和"
            "群体汇总方式，并与方案中的研究目标保持一致。"
        ),
        "weight": 2.0,
        "critical": True,
    },
    {
        "rubric_id": "SAP7-PRIMARY-METHOD-001",
        "category": "选择主分析方法",
        "description": (
            "主分析需要根据终点类型、试验设计和数据特点，明确模型、效应量及检验方法，"
            "使分析规则能够直接执行。"
        ),
        "weight": 2.0,
        "critical": True,
    },
    {
        "rubric_id": "SAP7-SENSITIVITY-001",
        "category": "敏感性分析",
        "description": (
            "敏感性分析需要围绕主分析的关键假设设计，说明改变哪些假设，以及如何检验"
            "主要结论的稳健性。"
        ),
        "weight": 1.5,
        "critical": False,
    },
    {
        "rubric_id": "SAP7-ICE-001",
        "category": "处理伴发事件",
        "description": (
            "停药、换药、救援治疗或死亡发生后，要根据试验要评估的治疗效果，确定相应的数据处理策略。"
        ),
        "weight": 2.0,
        "critical": True,
    },
    {
        "rubric_id": "SAP7-MISSING-001",
        "category": "处理失访与缺失数据",
        "description": ("失访和缺失数据要结合发生原因，明确缺失机制假设和具体处理方法。"),
        "weight": 2.0,
        "critical": True,
    },
    {
        "rubric_id": "SAP7-SAFETY-001",
        "category": "写清安全性分析规则",
        "description": (
            "安全性分析需要明确不良事件的观察时间窗、MedDRA 编码、SOC/PT 汇总规则及"
            "适用分母，并保持统计口径一致。"
        ),
        "weight": 2.0,
        "critical": True,
    },
    {
        "rubric_id": "SAP7-TFL-001",
        "category": "将分析要求落实为TFL",
        "description": (
            "TFL 需要将分析人群、行列维度、统计量、单位、分母和脚注落实为具体表壳，"
            "使结果能够按规格编程产出。"
        ),
        "weight": 1.5,
        "critical": False,
    },
]


SCORING_ANCHORS = {
    "4": "完整、研究特异、与可见方案证据一致且可直接执行；没有编造未提供的决定。",
    "3": "核心内容正确，只有少量不影响执行的遗漏或表述不够具体。",
    "2": "部分满足；包含主要概念，但缺少至少一个重要组成部分或执行细节。",
    "1": "仅泛泛提及，无法执行，或没有妥善标记输入中缺失的决策。",
    "0": "缺失、明显矛盾、统计上不适当，或把方案未提供的信息当作既定事实。",
}


def supplemental_requirement(study_id: str, rubric: dict[str, Any]) -> dict[str, Any]:
    return {
        "requirement_id": f"{study_id}-{rubric['rubric_id']}",
        "study_id": study_id,
        "rubric_id": rubric["rubric_id"],
        "tracks": ["protocol_only"],
        "applies": True,
        "status": "proposed",
        "severity": "critical" if rubric["critical"] else "major",
        "requirement": rubric["description"],
        "acceptable_values": [
            {
                "score": int(score),
                "condition": condition,
            }
            for score, condition in SCORING_ANCHORS.items()
        ],
        "evidence": [],
        "notes": (
            "Cross-study quality criterion added for the 20-study experiment. Judge only from "
            "the model-visible protocol and candidate SAP. If the protocol is silent, reward "
            "explicit uncertainty or a confirmation request rather than an invented decision."
        ),
    }
