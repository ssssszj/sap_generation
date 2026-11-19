from __future__ import annotations

import json
import mimetypes
import time
import urllib.error
import urllib.request
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from sapgen.experiment.llm import OpenAIChatClient
from sapgen.harness import DeepSeekHarnessAdapter, DeepSeekHarnessConfig
from sapgen.pipeline import SAPGenerationPipeline
from sapgen.storage import ProjectStore


@dataclass(slots=True)
class GenerationOutcome:
    method: str
    text: str
    elapsed_ms: int
    model: str
    calls: int
    usage: dict[str, int | None] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


class DirectLLMNativeAdapter:
    method = "direct_llm_native"

    def __init__(self, client: OpenAIChatClient) -> None:
        self.client = client

    def generate(
        self, protocol_text: str, _protocol_path: Path, _crf_path: Path
    ) -> GenerationOutcome:
        prompt = (
            "Using only the protocol below, write a complete, standalone Statistical Analysis Plan "
            "suitable for review and implementation. Do not discuss the task or the prompt. Do not "
            "claim that the protocol specifies information it does not contain; clearly mark "
            "unresolved information that requires confirmation.\n\n"
            "CRF status: no study-specific CRF was supplied for this protocol-only benchmark.\n\n"
            f"PROTOCOL\n{protocol_text}"
        )
        result = self.client.complete(
            [
                {
                    "role": "system",
                    "content": "You are a senior clinical-trial statistician.",
                },
                {"role": "user", "content": prompt},
            ]
        )
        return GenerationOutcome(
            method=self.method,
            text=result.text,
            elapsed_ms=result.elapsed_ms,
            model=result.model,
            calls=1,
            usage=result.usage,
            metadata={"finish_reason": result.finish_reason},
        )


class LegacyHTTPAdapter:
    method = "sap_ver1"

    def __init__(self, base_url: str, timeout_seconds: int = 7200) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds

    def healthcheck(self) -> None:
        try:
            with urllib.request.urlopen(self.base_url, timeout=30) as response:
                if response.status >= 400:
                    raise RuntimeError(f"legacy server returned HTTP {response.status}")
        except urllib.error.URLError as exc:
            raise RuntimeError(f"legacy server is unavailable at {self.base_url}: {exc}") from exc

    def generate(
        self, _protocol_text: str, protocol_path: Path, crf_path: Path
    ) -> GenerationOutcome:
        started = time.perf_counter()
        sap_payload = self._multipart_request(
            "/api/generate-sap",
            files={"protocol": protocol_path, "crf": crf_path},
            fields={},
        )
        sap_result = self._done_result(sap_payload)
        sap_text = sap_result["fullDocument"]
        tfl_payload = self._multipart_request(
            "/api/generate-tfl-shells",
            files={"protocol": protocol_path, "crf": crf_path},
            fields={"sapText": sap_text},
        )
        tfl_result = self._done_result(tfl_payload)
        combined = f"{sap_text}\n\n# TFL Shells\n\n{tfl_result['fullDocument']}\n"
        section_count = int(sap_result.get("sectionsCount") or 0)
        return GenerationOutcome(
            method=self.method,
            text=combined,
            elapsed_ms=round((time.perf_counter() - started) * 1000),
            model="configured-by-legacy-server",
            calls=1 + section_count + 3,
            metadata={
                "revision": False,
                "endpoint": "/api/generate-sap",
                "sections": section_count,
                "tfl_calls": 3,
            },
        )

    @staticmethod
    def _encode_multipart(files: dict[str, Path], fields: dict[str, str]) -> tuple[bytes, str]:
        boundary = f"----sapgen-{uuid.uuid4().hex}"
        body = bytearray()
        for name, value in fields.items():
            body.extend(f"--{boundary}\r\n".encode())
            body.extend(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode())
            body.extend(value.encode("utf-8"))
            body.extend(b"\r\n")
        for name, path in files.items():
            content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            body.extend(f"--{boundary}\r\n".encode())
            body.extend(
                (
                    f'Content-Disposition: form-data; name="{name}"; filename="{path.name}"\r\n'
                    f"Content-Type: {content_type}\r\n\r\n"
                ).encode()
            )
            body.extend(path.read_bytes())
            body.extend(b"\r\n")
        body.extend(f"--{boundary}--\r\n".encode())
        return bytes(body), f"multipart/form-data; boundary={boundary}"

    def _multipart_request(
        self, endpoint: str, *, files: dict[str, Path], fields: dict[str, str]
    ) -> list[dict[str, Any]]:
        data, content_type = self._encode_multipart(files, fields)
        request = urllib.request.Request(
            f"{self.base_url}{endpoint}",
            data=data,
            method="POST",
            headers={"Content-Type": content_type},
        )
        with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
            text = response.read().decode("utf-8")
        return [json.loads(line) for line in text.splitlines() if line.strip()]

    @staticmethod
    def _done_result(events: list[dict[str, Any]]) -> dict[str, Any]:
        errors = [event.get("error") for event in events if event.get("type") == "error"]
        if errors:
            raise RuntimeError(f"legacy generation failed: {errors[-1]}")
        for event in reversed(events):
            if event.get("type") == "done":
                return event["result"]
        raise RuntimeError("legacy generation returned no done event")


class DSHSAPAdapter:
    method = "dsh_sap"

    def __init__(
        self,
        *,
        experiment_root: Path,
        api_key: str,
        base_url: str,
        model: str,
        max_tokens: int,
        node_executable: Path | None,
        dsh_js: Path | None,
    ) -> None:
        runtime_root = experiment_root / "runtime" / "dsh_sap"
        self.store = ProjectStore(runtime_root / "runs.sqlite3")
        self.harness = DeepSeekHarnessAdapter(
            DeepSeekHarnessConfig(
                dsh_home=runtime_root / "dsh-home",
                cwd=experiment_root,
                provider="deepseek-official",
                model=model,
                max_tokens=max_tokens,
                profile="sdk",
                base_url=base_url,
                api_key=api_key,
                node_executable=node_executable,
                dsh_js=dsh_js,
            )
        )
        self.pipeline = SAPGenerationPipeline(
            data_dir=runtime_root / "data",
            store=self.store,
            harness=self.harness,
        )
        self.model = model

    def close(self) -> None:
        self.harness.close()

    def generate(
        self, _protocol_text: str, protocol_path: Path, crf_path: Path
    ) -> GenerationOutcome:
        started = time.perf_counter()
        calls_before = self.harness.call_count
        project = self.store.create_project(f"benchmark-{protocol_path.parent.name}")
        result = self.pipeline.run(
            project_id=project["id"],
            input_paths=[protocol_path, crf_path],
            allow_harness_fallback=False,
        )
        text = Path(result.draft_markdown_path).read_text(encoding="utf-8")
        return GenerationOutcome(
            method=self.method,
            text=text,
            elapsed_ms=round((time.perf_counter() - started) * 1000),
            model=self.model,
            calls=self.harness.call_count - calls_before,
            metadata={
                "harness_session_id": result.harness_session_id,
                "validation": result.report.counts(),
                "ir_path": result.ir_path,
                "tfl_docx_path": result.tfl_docx_path,
            },
        )
