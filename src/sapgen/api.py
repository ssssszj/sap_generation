from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated, Any

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from sapgen.config import Settings
from sapgen.domain.models import SAPIR
from sapgen.harness.base import HarnessAdapter
from sapgen.legacy_api import install_legacy_routes
from sapgen.pipeline import SAPGenerationPipeline
from sapgen.storage import ProjectStore


class ProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    metadata: dict[str, Any] = Field(default_factory=dict)


def create_app(
    settings: Settings | None = None,
    harness: HarnessAdapter | None = None,
) -> FastAPI:
    config = settings or Settings.load()
    config.ensure_directories()
    store = ProjectStore(config.database)
    pipeline = SAPGenerationPipeline(data_dir=config.data_dir, store=store, harness=harness)
    app = FastAPI(
        title="SAP Generation System",
        version="0.1.0",
        description="Evidence-traceable clinical trial SAP generation and review API",
    )
    app.state.settings = config
    app.state.store = store
    app.state.pipeline = pipeline

    @app.get("/api/health")
    def health() -> dict[str, Any]:
        return {
            "status": "ok",
            "harness_configured": pipeline.harness is not None,
            "data_dir": str(config.data_dir),
        }

    @app.get("/api/projects")
    def list_projects() -> list[dict[str, Any]]:
        return store.list_projects()

    @app.post("/api/projects", status_code=201)
    def create_project(payload: ProjectCreate) -> dict[str, Any]:
        project = store.create_project(payload.name, payload.metadata)
        (config.data_dir / project["id"] / "inputs").mkdir(parents=True, exist_ok=True)
        return project

    @app.get("/api/projects/{project_id}")
    def get_project(project_id: str) -> dict[str, Any]:
        try:
            project = store.get_project(project_id)
        except KeyError as exc:
            raise HTTPException(status_code=404, detail="Project not found") from exc
        project_dir = config.data_dir / project_id
        project["inputs"] = [
            path.name for path in sorted((project_dir / "inputs").glob("*")) if path.is_file()
        ]
        working_ir = project_dir / "working-ir.json"
        project["has_working_ir"] = working_ir.exists()
        return project

    @app.post("/api/projects/{project_id}/inputs", status_code=201)
    async def upload_inputs(
        project_id: str,
        files: Annotated[list[UploadFile], File(...)],
    ) -> dict[str, Any]:
        try:
            store.get_project(project_id)
        except KeyError as exc:
            raise HTTPException(status_code=404, detail="Project not found") from exc
        input_dir = config.data_dir / project_id / "inputs"
        input_dir.mkdir(parents=True, exist_ok=True)
        accepted = []
        for upload in files:
            filename = Path(upload.filename or "input").name
            suffix = Path(filename).suffix.lower()
            if suffix not in pipeline.ingestor.supported_suffixes:
                raise HTTPException(status_code=400, detail=f"Unsupported file: {filename}")
            destination = input_dir / filename
            destination.write_bytes(await upload.read())
            accepted.append(filename)
        return {"files": accepted}

    @app.get("/api/projects/{project_id}/ir")
    def get_working_ir(project_id: str) -> dict[str, Any]:
        path = config.data_dir / project_id / "working-ir.json"
        if not path.exists():
            raise HTTPException(status_code=404, detail="Working SAP-IR not found")
        return json.loads(path.read_text(encoding="utf-8"))

    @app.put("/api/projects/{project_id}/ir")
    def put_working_ir(project_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        try:
            store.get_project(project_id)
        except KeyError as exc:
            raise HTTPException(status_code=404, detail="Project not found") from exc
        ir = SAPIR.model_validate(payload)
        path = config.data_dir / project_id / "working-ir.json"
        pipeline.save_ir(ir, path)
        return {"path": str(path), "schema_version": ir.schema_version}

    @app.post("/api/projects/{project_id}/runs", status_code=201)
    def run_generation(
        project_id: str,
        use_working_ir: Annotated[bool, Form()] = False,
        allow_harness_fallback: Annotated[bool, Form()] = True,
    ) -> dict[str, Any]:
        try:
            store.get_project(project_id)
        except KeyError as exc:
            raise HTTPException(status_code=404, detail="Project not found") from exc
        project_dir = config.data_dir / project_id
        inputs = [path for path in sorted((project_dir / "inputs").glob("*")) if path.is_file()]
        if not inputs:
            raise HTTPException(status_code=400, detail="Upload at least one input document")
        seed_ir = None
        if use_working_ir:
            ir_path = project_dir / "working-ir.json"
            if not ir_path.exists():
                raise HTTPException(status_code=400, detail="Working SAP-IR not found")
            seed_ir = pipeline.load_ir(ir_path)
        try:
            result = pipeline.run(
                project_id=project_id,
                input_paths=inputs,
                seed_ir=seed_ir,
                allow_harness_fallback=allow_harness_fallback,
            )
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Generation failed: {exc}") from exc
        return result.model_dump(mode="json")

    @app.get("/api/runs/{run_id}")
    def get_run(run_id: str) -> dict[str, Any]:
        try:
            return store.get_run(run_id)
        except KeyError as exc:
            raise HTTPException(status_code=404, detail="Run not found") from exc

    @app.get("/api/runs/{run_id}/artifacts/{artifact_name}")
    def get_artifact(run_id: str, artifact_name: str) -> FileResponse:
        allowed = {
            "sap-ir.json": "ir_path",
            "validation-report.json": "validation_path",
            "sap-draft.md": "draft_markdown_path",
            "sap-draft.docx": "docx_path",
            "tfl-shells.docx": "tfl_docx_path",
        }
        field = allowed.get(artifact_name)
        if field is None:
            raise HTTPException(status_code=404, detail="Artifact not found")
        try:
            run = store.get_run(run_id)
        except KeyError as exc:
            raise HTTPException(status_code=404, detail="Run not found") from exc
        if not run["result"]:
            raise HTTPException(status_code=409, detail="Run has no completed artifacts")
        path = Path(run["result"][field]).resolve()
        expected_root = (config.data_dir / run["project_id"] / "runs" / run_id).resolve()
        if expected_root not in path.parents or not path.exists():
            raise HTTPException(status_code=404, detail="Artifact not found")
        return FileResponse(path, filename=artifact_name)

    install_legacy_routes(app, pipeline, store)
    web_dir = Path(__file__).parent / "web"
    app.mount("/", StaticFiles(directory=web_dir, html=True), name="web")
    return app
