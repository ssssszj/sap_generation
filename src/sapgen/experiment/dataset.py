from __future__ import annotations

import hashlib
import json
import random
from collections import Counter
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from sapgen.experiment.rubrics import SAP7_RUBRICS, supplemental_requirement

TARGET_COVERAGE = {
    "CORE-ESTIMAND-001": 6,
    "CORE-SENS-001": 8,
    "CORE-SAFE-001": 8,
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()
    ]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records)
    path.write_text(rendered, encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _question_rubrics(source_root: Path, question: dict[str, Any]) -> set[str]:
    requirements = load_jsonl(source_root / question["requirements_path"])
    return {item["rubric_id"] for item in requirements}


def select_questions(
    source_root: Path,
    *,
    sample_size: int = 20,
    seed: int = 20261108,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    question_set = load_json(source_root / "final_audit" / "initial_draft_question_set.json")
    questions = list(question_set["questions"])
    if sample_size > len(questions):
        raise ValueError(f"sample_size={sample_size} exceeds available questions={len(questions)}")

    rng = random.Random(seed)
    rng.shuffle(questions)
    rubrics_by_study = {
        item["study_id"]: _question_rubrics(source_root, item) for item in questions
    }
    selected: list[dict[str, Any]] = []
    coverage: Counter[str] = Counter()

    while len(selected) < sample_size:
        remaining = [item for item in questions if item not in selected]
        scored: list[tuple[int, int, dict[str, Any]]] = []
        for order, item in enumerate(remaining):
            item_rubrics = rubrics_by_study[item["study_id"]]
            gain = sum(
                coverage[rubric_id] < target and rubric_id in item_rubrics
                for rubric_id, target in TARGET_COVERAGE.items()
            )
            scored.append((gain, -order, item))
        _, _, chosen = max(scored, key=lambda row: (row[0], row[1]))
        selected.append(chosen)
        coverage.update(rubrics_by_study[chosen["study_id"]])

    selected.sort(key=lambda item: item["study_id"])
    return selected, dict(sorted(coverage.items()))


def build_experiment_package(
    benchmark_root: Path,
    *,
    sample_size: int = 20,
    seed: int = 20261108,
) -> Path:
    benchmark_root = benchmark_root.resolve()
    source_root = benchmark_root / "source"
    experiment_root = benchmark_root / "experiment"
    selected, coverage = select_questions(source_root, sample_size=sample_size, seed=seed)

    rubric_payload = {
        "rubric_set_id": "sap-seven-difficulties-v1",
        "version": "1.0.0",
        "judge_scale": {"minimum": 0, "maximum": 4},
        "rubrics": SAP7_RUBRICS,
    }
    write_json(experiment_root / "rubrics" / "sap7_v1.json", rubric_payload)

    sample_records = []
    for index, question in enumerate(selected, start=1):
        study_id = question["study_id"]
        supplements = [supplemental_requirement(study_id, rubric) for rubric in SAP7_RUBRICS]
        supplemental_path = experiment_root / "requirements" / f"{study_id}.sap7.jsonl"
        write_jsonl(supplemental_path, supplements)
        sample_records.append(
            {
                "sample_index": index,
                **question,
                "supplemental_requirements_path": str(
                    supplemental_path.relative_to(benchmark_root).as_posix()
                ),
            }
        )

    manifest = {
        "experiment_id": "sap-three-arm-20-v1",
        "benchmark_source_version": "0.3-initial-draft",
        "status": "pilot_not_frozen_test",
        "sampling": {
            "algorithm": "seeded greedy coverage, stable study-id output order",
            "seed": seed,
            "sample_size": sample_size,
            "minimum_targets": TARGET_COVERAGE,
            "observed_original_rubric_coverage": coverage,
        },
        "input_track": "protocol_only",
        "reference_sap_policy": "annotation_only_never_model_visible",
        "methods": ["direct_llm_native", "sap_ver1", "dsh_sap"],
        "questions": sample_records,
    }
    manifest_path = experiment_root / "sample.json"
    write_json(manifest_path, manifest)
    return manifest_path
