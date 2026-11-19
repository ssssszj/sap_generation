"""Wire compatible endpoints for clients of the pre-DSH SAP API."""

from __future__ import annotations

import io
import json
import re
import uuid
from pathlib import Path
from typing import Any
from urllib.parse import quote

from docx import Document
from fastapi import APIRouter, Request, UploadFile
from fastapi.responses import JSONResponse, Response, StreamingResponse

from sapgen.pipeline import SAPGenerationPipeline
from sapgen.storage import ProjectStore

CORE_ITEMS = (
    ("protocol-carryover", "Protocol 承接内容"),
    ("statistical-endpoints", "统计指标与终点口径"),
    ("result-presentation", "结果展示方向"),
    ("statistical-methods", "统计方法"),
    ("analysis-populations", "分析集"),
    ("key-statistical-rules", "关键统计规则"),
)
DOCX_TYPE = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"


def _reply(data: Any) -> JSONResponse:
    return JSONResponse({"code": 0, "data": data})


def _fail(message: str, status: int = 400, *, demo: bool = False) -> JSONResponse:
    return JSONResponse({"error": message} if demo else {"code": 1, "message": message}, status_code=status)


def _text(value: Any) -> str:
    return value.strip() if isinstance(value, str) else ""


def _outline(value: list[Any]) -> list[dict[str, str]]:
    roots: list[dict[str, Any]] = []
    for item in value:
        if not isinstance(item, dict):
            continue
        if item.get("level") == 2:
            if roots:
                roots[-1].setdefault("children", []).append(item)
            continue
        roots.append(dict(item))
    result = []
    for index, item in enumerate(roots, 1):
        title = _text(item.get("title"))
        if title:
            matched = re.match(r"^(\d+(?:\.\d+)*)\s+", title)
            result.append({
                "id": _text(item.get("id")) or (matched.group(1) if matched else str(index)),
                "title": title,
                "titleEn": _text(item.get("titleEn")),
            })
    return result


def _ndjson(event: dict[str, Any]) -> bytes:
    return (json.dumps(event, ensure_ascii=False) + "\n").encode("utf-8")


def _markdown_docx(markdown: str) -> bytes:
    document = Document()
    for line in markdown.splitlines():
        heading = re.match(r"^(#{1,6})\s+(.+)", line)
        if heading:
            document.add_heading(heading.group(2), level=min(len(heading.group(1)), 4))
        elif line.strip():
            document.add_paragraph(line.strip())
    stream = io.BytesIO()
    document.save(stream)
    return stream.getvalue()


def _markdown_pdf(markdown: str) -> bytes:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    from reportlab.pdfgen import canvas

    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    stream = io.BytesIO()
    page = canvas.Canvas(stream, pagesize=A4)
    page.setFont("STSong-Light", 10)
    y = A4[1] - 45
    for raw in markdown.splitlines():
        line = re.sub(r"^#{1,6}\s+", "", raw).strip()
        for start in range(0, max(1, len(line)), 85):
            if y < 45:
                page.showPage()
                page.setFont("STSong-Light", 10)
                y = A4[1] - 45
            page.drawString(45, y, line[start : start + 85])
            y -= 16
        if not line:
            y -= 8
    page.save()
    return stream.getvalue()


def install_legacy_routes(app: Any, pipeline: SAPGenerationPipeline, store: ProjectStore) -> None:
    router = APIRouter()

    def generate(protocol: str, crf: str) -> tuple[str, Any]:
        if pipeline.harness is None:
            raise RuntimeError("DeepSeek Harness is not configured; start with serve --harness")
        project = store.create_project("legacy-api")
        folder = pipeline.data_dir / project["id"] / "submitted"
        folder.mkdir(parents=True, exist_ok=True)
        protocol_path, crf_path = folder / "protocol.txt", folder / "crf.txt"
        protocol_path.write_text(protocol, encoding="utf-8")
        crf_path.write_text(crf, encoding="utf-8")
        result = pipeline.run(
            project_id=project["id"],
            input_paths=[protocol_path, crf_path],
            allow_harness_fallback=False,
        )
        return Path(result.draft_markdown_path).read_text(encoding="utf-8"), pipeline.load_ir(Path(result.ir_path))

    def core_items(protocol: str, crf: str) -> list[dict[str, Any]]:
        _draft, ir = generate(protocol, crf)
        values = (
            f"{ir.study.title}\n{ir.study.design or ''}",
            "\n".join(f"{x.name}: {x.definition}" for x in ir.endpoints),
            "\n".join(x.body_markdown for x in ir.generated_sections if "tfl" in x.id),
            "\n".join(f"{x.model}; {x.effect_measure}" for x in ir.analysis_methods),
            "\n".join(f"{x.name}: {x.definition}" for x in ir.analysis_populations),
            "\n".join(x.question for x in ir.clarifications),
        )
        return [
            {"id": ident, "title": title, "content": value or "待确认", "confirmed": False}
            for (ident, title), value in zip(CORE_ITEMS, values, strict=True)
        ]

    def revise(protocol: str, crf: str, item: dict[str, Any], feedback: str, all_items: Any) -> dict[str, Any]:
        if pipeline.harness is None:
            raise RuntimeError("DeepSeek Harness is not configured")
        result = pipeline.harness.complete_json(
            system_prompt="Revise only the supplied SAP core content item using the protocol, CRF and feedback. Preserve factual accuracy. Return JSON with a content string.",
            user_prompt=json.dumps({"protocolText": protocol, "crfText": crf, "item": item, "feedback": feedback, "allCoreContents": all_items}, ensure_ascii=False),
            schema={"type": "object", "properties": {"content": {"type": "string"}}, "required": ["content"]},
            session_id=f"legacy-revise-{uuid.uuid4().hex}",
        )
        return {"id": item["id"], "title": item["title"], "content": str(result["content"]), "confirmed": False}

    def document(protocol: str, crf: str, outline: list[dict[str, str]], meta: Any, contents: Any) -> dict[str, Any]:
        draft, ir = generate(protocol, crf)
        if pipeline.harness is None:
            raise RuntimeError("DeepSeek Harness is not configured")
        sections = []
        for index, section in enumerate(outline):
            result = pipeline.harness.complete_json(
                system_prompt="Draft this SAP section as Markdown. Follow the confirmed core contents and supplied outline, preserve study facts from SAP-IR, and keep unresolved proposals visibly labelled.",
                user_prompt=json.dumps({"section": section, "priorSections": sections, "coreContents": contents, "sapIR": ir.model_dump(mode="json"), "draft": draft}, ensure_ascii=False),
                schema={"type": "object", "properties": {"content": {"type": "string"}}, "required": ["content"]},
                session_id=f"legacy-section-{uuid.uuid4().hex}-{index}",
            )
            sections.append({**section, "content": str(result["content"])})
        full_document = "\n\n".join(f"# {section['title']}\n\n{section['content']}" for section in sections)
        cover = {"studyTitle": ir.study.title}
        if isinstance(meta, dict):
            cover.update(meta)
        return {"documentContent": full_document, "contentType": "text/markdown", "coverMeta": cover, "sections": sections}

    async def json_body(request: Request) -> dict[str, Any]:
        try:
            value = await request.json()
            return value if isinstance(value, dict) else {}
        except Exception:  # noqa: BLE001 - match legacy JSON error envelope
            return {}

    @router.post("/ai/v1/sap/core-content/generate")
    @router.post("/api/ai/v1/sap/core-content/generate")
    async def core_generate(request: Request) -> Response:
        body = await json_body(request)
        protocol, crf = _text(body.get("protocolText")), _text(body.get("crfText"))
        if not protocol or not crf:
            return _fail("protocolText 和 crfText 不能为空")
        try:
            return _reply({"coreContents": core_items(protocol, crf)})
        except Exception as exc:  # noqa: BLE001 - match legacy 500 envelope
            return _fail(str(exc), 500)

    @router.post("/ai/v1/sap/core-content/regenerate")
    @router.post("/api/ai/v1/sap/core-content/regenerate")
    async def core_regenerate(request: Request) -> Response:
        body = await json_body(request)
        protocol, crf = _text(body.get("protocolText")), _text(body.get("crfText"))
        if not protocol or not crf:
            return _fail("protocolText 和 crfText 不能为空")
        item = body.get("item")
        if not isinstance(item, dict) or not all(_text(item.get(key)) for key in ("id", "title", "content")):
            return _fail("item 必须包含 id、title、content")
        feedback = _text(body.get("feedback"))
        if not feedback:
            return _fail("feedback 不能为空")
        try:
            return _reply({"coreContent": revise(protocol, crf, item, feedback, body.get("allCoreContents"))})
        except Exception as exc:  # noqa: BLE001 - match legacy 500 envelope
            return _fail(str(exc), 500)

    async def document_generate(request: Request) -> Response:
        body = await json_body(request)
        protocol, crf = _text(body.get("protocolText")), _text(body.get("crfText"))
        if not protocol or not crf:
            return _fail("protocolText 和 crfText 不能为空")
        contents = body.get("coreContents")
        if not isinstance(contents, list) or not contents:
            return _fail("coreContents 必须是已确认的核心内容列表")
        if any(isinstance(item, dict) and item.get("confirmed") is False for item in contents):
            return _fail("coreContents 中存在未确认项")
        raw_outline = body.get("outline")
        if not isinstance(raw_outline, list) or not raw_outline:
            return _fail("outline 必须是已确认的大纲列表")
        outline = _outline(raw_outline)
        if not outline:
            return _fail("outline 规范化后不能为空")
        try:
            return _reply(document(protocol, crf, outline, body.get("meta"), contents))
        except Exception as exc:  # noqa: BLE001 - match legacy 500 envelope
            return _fail(str(exc), 500)

    for suffix in ("generate", "generate-with-revision"):
        router.add_api_route(f"/ai/v1/sap/document/{suffix}", document_generate, methods=["POST"])
        router.add_api_route(f"/api/ai/v1/sap/document/{suffix}", document_generate, methods=["POST"])

    @router.post("/ai/v1/sap/document/export")
    @router.post("/api/ai/v1/sap/document/export")
    async def export(request: Request) -> Response:
        if "application/json" not in request.headers.get("content-type", "").lower():
            return _fail("Content-Type 必须是 application/json", 415)
        body = await json_body(request)
        markdown = _text(body.get("markdown")) or _text(body.get("documentContent"))
        if not markdown:
            return _fail("markdown 或 documentContent 不能为空")
        fmt = body.get("format")
        if fmt not in ("docx", "pdf"):
            return _fail("format 必须是 docx 或 pdf")
        name = re.sub(r'[\\/:*?"<>|]+', "-", _text(body.get("filename")) or "sap-document")
        name = re.sub(r"\.(docx|pdf)$", "", name, flags=re.IGNORECASE)[:120] or "sap-document"
        filename = f"{name}.{fmt}"
        try:
            payload = _markdown_docx(markdown) if fmt == "docx" else _markdown_pdf(markdown)
            encoded = quote(filename)
            return Response(payload, media_type=DOCX_TYPE if fmt == "docx" else "application/pdf", headers={
                "Content-Length": str(len(payload)),
                "Content-Disposition": f"attachment; filename=\"{encoded}\"; filename*=UTF-8''{encoded}",
            })
        except Exception as exc:  # noqa: BLE001 - match legacy 500 envelope
            return _fail(str(exc), 500)

    async def upload_text(upload: UploadFile | None, label: str) -> str:
        if upload is None:
            raise ValueError(f"{label} 文件解析失败: 文件内容为空")
        suffix = Path(upload.filename or "").suffix.lower()
        if suffix not in {".pdf", ".docx", ".txt", ".md"}:
            raise ValueError(f"{label} 文件解析失败: 不支持的文件类型")
        folder = pipeline.data_dir / "legacy-uploads" / uuid.uuid4().hex
        folder.mkdir(parents=True, exist_ok=True)
        source = folder / f"source{suffix}"
        source.write_bytes(await upload.read())
        corpus = pipeline.ingestor.ingest([source])
        value = "\n\n".join(chunk.text for chunk in corpus.chunks).strip()
        if not value:
            raise ValueError(f"{label} 文件解析失败: 文件内容为空")
        return value

    async def uploaded_pair(request: Request, *, tfl: bool = False) -> tuple[Any, str, str] | Response:
        form = await request.form()
        protocol_file, crf_file = form.get("protocol"), form.get("crf")
        if not isinstance(protocol_file, UploadFile) or not isinstance(crf_file, UploadFile):
            return _fail("请同时上传 Protocol 和 CRF 文件" if tfl else "请同时上传 Protocol 和 CRF/aCRF 文件", demo=True)
        try:
            return form, await upload_text(protocol_file, "Protocol"), await upload_text(crf_file, "CRF" if tfl else "CRF/aCRF")
        except ValueError as exc:
            return _fail(str(exc), demo=True)

    @router.post("/api/generate-core-content")
    async def demo_core(request: Request) -> Response:
        pair = await uploaded_pair(request)
        if isinstance(pair, Response):
            return pair
        _form, protocol, crf = pair
        try:
            return JSONResponse({"items": core_items(protocol, crf)})
        except Exception as exc:  # noqa: BLE001 - match legacy 500 envelope
            return _fail(str(exc), 500, demo=True)

    @router.post("/api/revise-core-content")
    async def demo_revise(request: Request) -> Response:
        pair = await uploaded_pair(request)
        if isinstance(pair, Response):
            return pair
        form, protocol, crf = pair
        if not _text(form.get("item")) or not _text(form.get("feedback")):
            return _fail("请提供需要修订的核心内容和反馈", demo=True)
        try:
            item = json.loads(str(form["item"]))
            all_items = json.loads(str(form["allItems"])) if form.get("allItems") else None
            return JSONResponse({"item": revise(protocol, crf, item, str(form["feedback"]), all_items)})
        except Exception as exc:  # noqa: BLE001 - match legacy 500 envelope
            return _fail(str(exc), 500, demo=True)

    @router.post("/api/generate-sap")
    async def demo_document(request: Request) -> Response:
        pair = await uploaded_pair(request)
        if isinstance(pair, Response):
            return pair
        form, protocol, crf = pair
        try:
            contents = json.loads(str(form["coreContent"])) if form.get("coreContent") else []
            if not isinstance(contents, list):
                return _fail("coreContent 必须是数组", demo=True)
        except ValueError:
            return _fail("coreContent 不是有效 JSON", demo=True)
        try:
            supplied = json.loads(str(form["outline"])) if form.get("outline") else []
            if not isinstance(supplied, list):
                return _fail("outline 必须是数组", demo=True)
        except ValueError:
            return _fail("outline 不是有效 JSON", demo=True)
        try:
            meta = json.loads(str(form["meta"])) if form.get("meta") else {}
        except ValueError:
            meta = {}

        def events():
            yield _ndjson({"type": "status", "message": "正在抽取 Fact Sheet（结构化事实表）..."})
            try:
                from sapgen.generation import CHAPTER_PLAN

                outline = _outline(supplied) if supplied else [
                    {"id": ident, "title": title, "titleEn": ""}
                    for ident, title, *_rest in CHAPTER_PLAN
                ]
                result = document(protocol, crf, outline, meta, contents)
                for index, section in enumerate(result["sections"], 1):
                    yield _ndjson({"type": "progress", "current": index, "total": len(outline), "section": {key: section[key] for key in ("id", "title", "titleEn")}})
                yield _ndjson({"type": "done", "result": {"success": True, "coverMeta": result["coverMeta"], "fullDocument": result["documentContent"], "sectionsCount": len(outline)}})
            except Exception as exc:  # noqa: BLE001 - preserve NDJSON error event
                yield _ndjson({"type": "error", "error": str(exc)})

        return StreamingResponse(events(), headers={"Content-Type": "application/x-ndjson"})

    @router.post("/api/generate-tfl-shells")
    async def demo_tfl(request: Request) -> Response:
        pair = await uploaded_pair(request, tfl=True)
        if isinstance(pair, Response):
            return pair
        form, protocol, crf = pair
        if not _text(form.get("sapText")):
            return _fail("请先生成 SAP 后再生成 TFL Shells，或传入 SAP 全文（sapText）", demo=True)

        def events():
            try:
                _draft, ir = generate(protocol, crf)
                shells = {}
                for step in ("table", "listing", "figure"):
                    yield _ndjson({"type": "progress", "step": step, "status": "generating"})
                    matching = [spec for spec in ir.tfl_specs if spec.kind.lower() == step]
                    shells[step] = "\n\n".join(
                        "\n".join((
                            f"## {spec.number} {spec.title}",
                            f"Population: {spec.population_id}; denominator: {spec.denominator}",
                            "Columns: " + ", ".join(spec.columns),
                            "Rows: " + ", ".join(spec.rows),
                            "Statistics: " + ", ".join(spec.statistics),
                        ))
                        for spec in matching
                    )
                    yield _ndjson({"type": "progress", "step": step, "status": "done"})
                yield _ndjson({"type": "done", "result": {"tableShells": shells["table"], "figureShells": shells["figure"], "listingShells": shells["listing"], "fullDocument": "\n\n".join(shells.values())}})
            except Exception as exc:  # noqa: BLE001 - preserve NDJSON error event
                yield _ndjson({"type": "error", "error": str(exc)})

        return StreamingResponse(events(), headers={"Content-Type": "application/x-ndjson"})

    app.include_router(router)
