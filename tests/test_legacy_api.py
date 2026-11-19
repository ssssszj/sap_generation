from __future__ import annotations

import json
from types import SimpleNamespace

from sapgen.api import create_app
from sapgen.config import Settings
from sapgen.domain.models import SAPIR


class RequestStub:
    def __init__(self, body=None, content_type="application/json"):
        self.body = body or {}
        self.headers = {"content-type": content_type}

    async def json(self):
        return self.body

    async def form(self):
        return self.body


def _endpoint(app, path):
    routes = [
        child
        for route in app.routes
        for child in getattr(getattr(route, "original_router", route), "routes", [route])
    ]
    return next(route.endpoint for route in routes if getattr(route, "path", None) == path)


def _run(coroutine):
    # The validation branches do not perform I/O; drive them without an event loop.
    try:
        coroutine.send(None)
    except StopIteration as result:
        return result.value
    raise AssertionError("The route unexpectedly awaited external I/O")


def test_versioned_routes_keep_legacy_envelopes(tmp_path) -> None:
    app = create_app(Settings.load(tmp_path))
    for prefix in ("/ai/v1/sap", "/api/ai/v1/sap"):
        response = _run(_endpoint(app, f"{prefix}/core-content/generate")(RequestStub()))
        assert response.status_code == 400
        assert json.loads(response.body) == {"code": 1, "message": "protocolText 和 crfText 不能为空"}

        response = _run(_endpoint(app, f"{prefix}/document/generate")(RequestStub({"protocolText": "p", "crfText": "c"})))
        assert response.status_code == 400
        assert json.loads(response.body) == {"code": 1, "message": "coreContents 必须是已确认的核心内容列表"}

        response = _run(_endpoint(app, f"{prefix}/document/export")(RequestStub(content_type="text/plain")))
        assert response.status_code == 415
        assert json.loads(response.body) == {"code": 1, "message": "Content-Type 必须是 application/json"}


def test_document_export_keeps_binary_contract(tmp_path) -> None:
    app = create_app(Settings.load(tmp_path))
    endpoint = _endpoint(app, "/ai/v1/sap/document/export")
    for fmt, signature in (("docx", b"PK"), ("pdf", b"%PDF")):
        response = _run(endpoint(RequestStub({
            "format": fmt, "filename": "SAP-测试", "documentContent": "# 统计分析计划\n正文",
        })))
        assert response.status_code == 200
        assert response.body.startswith(signature)
        assert int(response.headers["content-length"]) == len(response.body)
        assert "filename*=UTF-8''" in response.headers["content-disposition"]


def test_demo_upload_error_shape(tmp_path) -> None:
    app = create_app(Settings.load(tmp_path))
    for path in ("/api/generate-core-content", "/api/revise-core-content", "/api/generate-sap", "/api/generate-tfl-shells"):
        response = _run(_endpoint(app, path)(RequestStub()))
        assert response.status_code == 400
        assert set(json.loads(response.body)) == {"error"}


def test_success_payloads_keep_frontend_field_names(tmp_path, monkeypatch) -> None:
    app = create_app(Settings.load(tmp_path))
    markdown = tmp_path / "draft.md"
    ir_path = tmp_path / "ir.json"
    markdown.write_text("# SAP\n\nDraft", encoding="utf-8")
    ir_path.write_text(SAPIR().model_dump_json(), encoding="utf-8")
    monkeypatch.setattr(app.state.pipeline, "run", lambda **_kwargs: SimpleNamespace(
        draft_markdown_path=markdown, ir_path=ir_path,
    ))
    monkeypatch.setattr(app.state.pipeline, "harness", SimpleNamespace(
        complete_json=lambda **_kwargs: {"content": "Generated content"},
    ))
    core = _run(_endpoint(app, "/ai/v1/sap/core-content/generate")(RequestStub({
        "protocolText": "Protocol", "crfText": "CRF",
    })))
    items = json.loads(core.body)["data"]["coreContents"]
    assert len(items) == 6
    assert set(items[0]) == {"id", "title", "content", "confirmed"}

    revised = _run(_endpoint(app, "/ai/v1/sap/core-content/regenerate")(RequestStub({
        "protocolText": "Protocol", "crfText": "CRF", "item": items[0], "feedback": "Improve",
    })))
    assert set(json.loads(revised.body)["data"]["coreContent"]) == set(items[0])

    confirmed = [{**item, "confirmed": True} for item in items]

    document = _run(_endpoint(app, "/ai/v1/sap/document/generate")(RequestStub({
        "protocolText": "Protocol", "crfText": "CRF", "coreContents": confirmed,
        "outline": [{"id": "2", "title": "2 Methods", "titleEn": "Methods"}],
    })))
    data = json.loads(document.body)["data"]
    assert set(data) == {"documentContent", "contentType", "coverMeta", "sections"}
    assert set(data["sections"][0]) == {"id", "title", "titleEn", "content"}
