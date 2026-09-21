#!/usr/bin/env python3
"""Score historical outputs on the deterministic pilot subset for error mining.

These runs are not controlled baselines. The script labels them as diagnostics and
must not be used for thesis model rankings.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BENCHMARK = ROOT / "research" / "benchmark"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    extractor = load_module("docx_extractor", BENCHMARK / "tools" / "extract_docx_blocks.py")
    scorer = load_module("deterministic_scorer", BENCHMARK / "evaluator" / "score_deterministic.py")

    runs = load_jsonl(BENCHMARK / "manifests" / "legacy_runs.jsonl")
    requirements = load_jsonl(BENCHMARK / "gold" / "PILOT-IOL-001" / "requirements.jsonl")
    output_dir = BENCHMARK / "results" / "legacy_sanity"
    output_dir.mkdir(parents=True, exist_ok=True)

    summary_rows = []
    for run in runs:
        path = ROOT / run["output_path"]
        candidate_text = "\n".join(
            block["text"] for block in extractor.iter_blocks(path, f"output-{run['run_id']}")
        )
        results = [scorer.evaluate(requirement, candidate_text, "protocol_only") for requirement in requirements]
        summary = scorer.build_summary(results)
        payload = {
            "diagnostic_only": True,
            "evaluation_track_assumption": "protocol_only",
            "warning": "Historical prompt, exact input, and decoding settings were not frozen; do not use for model ranking.",
            "run": run,
            "summary": summary,
            "results": results,
        }
        (output_dir / f"{run['run_id']}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        summary_rows.append(
            {
                "run_id": run["run_id"],
                "model": run["model"],
                "run_date": run["run_date"],
                "counts": summary["counts"],
                "deterministic_pass_rate": summary["deterministic_pass_rate"],
                "study_level_critical_pass": summary["study_level_critical_pass"],
            }
        )

    summary_payload = {
        "diagnostic_only": True,
        "benchmark_version": "0.1-pilot",
        "study_id": "PILOT-IOL-001",
        "evaluation_track_assumption": "protocol_only",
        "run_count": len(summary_rows),
        "runs": summary_rows,
    }
    (BENCHMARK / "results" / "legacy_sanity_summary.json").write_text(
        json.dumps(summary_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary_payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
