from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Self

from sapgen.harness.base import HarnessResponseError, HarnessUnavailableError


@dataclass(frozen=True, slots=True)
class DeepSeekHarnessConfig:
    dsh_home: Path
    cwd: Path
    provider: str = "deepseek-official"
    model: str = "deepseek-v4-flash"
    reasoning_effort: str | None = None
    max_tokens: int = 32768
    profile: str = "sdk"
    patches: tuple[str, ...] = ()
    base_url: str | None = None
    api_key: str | None = None
    node_executable: Path | None = None
    dsh_js: Path | None = None
    initialize_timeout_seconds: float = 120.0


class DeepSeekHarnessAdapter:
    """Thin compatibility boundary around the official Python SDK.

    The SDK owns the Agent Loop, tools, model adapter, durable session and event log.
    Domain decisions remain in SAP-IR and deterministic validators in this project.
    """

    def __init__(self, config: DeepSeekHarnessConfig) -> None:
        self.config = config
        self._harness: Any | None = None
        self.call_count = 0

    def _start(self) -> Any:
        if self._harness is not None:
            return self._harness
        try:
            from deepseek_harness import DeepSeekHarness
        except ImportError as exc:
            raise HarnessUnavailableError(
                "DeepSeek Harness SDK is not installed. "
                "Install the project with the 'harness' extra."
            ) from exc
        self.config.dsh_home.mkdir(parents=True, exist_ok=True)
        runtime_env = {"DSH_HOME": str(self.config.dsh_home.resolve())}
        launch_args = None
        if self.config.dsh_js is not None:
            if self.config.node_executable is None:
                raise HarnessUnavailableError(
                    "A Node executable is required when dsh_js is configured. "
                    "Set SAPGEN_DSH_NODE to Node.js 22.19 or newer."
                )
            if not self.config.node_executable.exists():
                raise HarnessUnavailableError(
                    f"Node executable not found: {self.config.node_executable}"
                )
            if not self.config.dsh_js.exists():
                raise HarnessUnavailableError(
                    f"DeepSeek Harness CLI not found: {self.config.dsh_js}"
                )
            launch_args = (
                str(self.config.node_executable.resolve()),
                str(self.config.dsh_js.resolve()),
                "--profile",
                self.config.profile,
                *(
                    argument
                    for patch in self.config.patches
                    for argument in ("--patch", str(Path(patch).resolve()))
                ),
            )
        self._harness = DeepSeekHarness(
            _launch_args=launch_args,
            dsh_home=str(self.config.dsh_home.resolve()),
            cwd=str(self.config.cwd.resolve()),
            provider=self.config.provider,
            model=self.config.model,
            reasoning_effort=self.config.reasoning_effort,
            max_tokens=self.config.max_tokens,
            profile=self.config.profile,
            patches=self.config.patches,
            env=runtime_env,
            base_url=self.config.base_url,
            api_key=self.config.api_key,
            initialize_timeout_seconds=self.config.initialize_timeout_seconds,
        )
        self._harness.start()
        return self._harness

    def complete_json(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        schema: dict[str, Any],
        session_id: str,
    ) -> dict[str, Any]:
        harness = self._start()
        schema_text = json.dumps(schema, ensure_ascii=False, separators=(",", ":"))
        last_error: HarnessResponseError | None = None
        for attempt in range(2):
            retry_instruction = (
                "A previous response was not valid complete JSON. Re-create it from the task input; "
                "use short field values, escape every quote and control character inside strings, "
                "and close every array and object. Do not copy or discuss the previous response. "
                if attempt
                else ""
            )
            prompt = (
                f"{system_prompt}\n\n"
                "This is a bounded structured-output call. Do not call tools, inspect files, create a "
                "plan, or narrate your work. Produce the final JSON immediately. Return exactly one "
                "valid JSON object. Do not use Markdown fences. "
                "Do not infer a protocol decision when the evidence is absent; use a missing status "
                "and add a clarification item instead. "
                f"{retry_instruction}\n\n"
                f"JSON Schema:\n{schema_text}\n\n"
                f"Task input:\n{user_prompt}"
            )
            attempt_session_id = session_id if attempt == 0 else f"{session_id}-json-retry"
            self.call_count += 1
            result = harness.run(prompt, session_id=attempt_session_id)
            if result.finish_reason not in {None, "completed"}:
                last_error = HarnessResponseError(
                    f"DeepSeek Harness ended with {result.finish_reason}: {result.final_response}"
                )
                continue
            try:
                return self._parse_json(result.final_response)
            except HarnessResponseError as exc:
                last_error = exc
        assert last_error is not None
        raise last_error

    @staticmethod
    def _parse_json(text: str) -> dict[str, Any]:
        value = text.strip()
        if value.startswith("```"):
            lines = value.splitlines()
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            value = "\n".join(lines).strip()
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            start = value.find("{")
            end = value.rfind("}")
            if start < 0 or end <= start:
                raise HarnessResponseError("Harness response did not contain a JSON object.")
            try:
                parsed = json.loads(value[start : end + 1])
            except json.JSONDecodeError as exc:
                raise HarnessResponseError(f"Invalid JSON from Harness: {exc}") from exc
        if not isinstance(parsed, dict):
            raise HarnessResponseError("Harness response must be a JSON object.")
        return parsed

    def close(self) -> None:
        if self._harness is not None:
            self._harness.close()
            self._harness = None

    def __enter__(self) -> Self:
        self._start()
        return self

    def __exit__(self, _exc_type: object, _exc: object, _tb: object) -> None:
        self.close()
