from __future__ import annotations

import json

from sapgen.pipeline import SAPGenerationPipeline
from sapgen.storage import ProjectStore


def test_end_to_end_pipeline_writes_traceable_artifacts(tmp_path, project_root, demo_ir) -> None:
    database = tmp_path / "sapgen.sqlite3"
    data_dir = tmp_path / "data"
    store = ProjectStore(database)
    project = store.create_project("demo")
    pipeline = SAPGenerationPipeline(data_dir=data_dir, store=store)

    result = pipeline.run(
        project_id=project["id"],
        input_paths=[project_root / "examples" / "demo_protocol.txt"],
        seed_ir=demo_ir,
    )

    for path in (
        result.ir_path,
        result.validation_path,
        result.draft_markdown_path,
        result.docx_path,
        result.tfl_docx_path,
    ):
        assert __import__("pathlib").Path(path).exists()
    run = store.get_run(result.run_id)
    assert run["status"] == "completed"
    assert [event["event_type"] for event in run["events"]][-1] == "artifacts.exported"
    ir_payload = json.loads(__import__("pathlib").Path(result.ir_path).read_text(encoding="utf-8"))
    assert len(ir_payload["tfl_specs"]) >= 1
    assert ir_payload["decision_support"]
    assert any(
        item["id"] == "confirm-analysis-EST-PRIMARY" for item in ir_payload["clarifications"]
    )
