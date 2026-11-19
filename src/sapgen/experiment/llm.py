from __future__ import annotations

import http.client
import json
import ssl
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class LLMCallResult:
    text: str
    model: str
    elapsed_ms: int
    finish_reason: str | None
    usage: dict[str, int | None] = field(default_factory=dict)


class OpenAIChatClient:
    """Minimal OpenAI-compatible client with provider-default sampling."""

    def __init__(
        self,
        *,
        api_key: str,
        model: str,
        base_url: str,
        max_tokens: int,
        timeout_seconds: int = 1200,
        max_attempts: int = 3,
    ) -> None:
        self.api_key = api_key
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.max_tokens = max_tokens
        self.timeout_seconds = timeout_seconds
        self.max_attempts = max_attempts

    @property
    def endpoint(self) -> str:
        if self.base_url.endswith("/v1/chat/completions"):
            return self.base_url
        if self.base_url.endswith("/v1"):
            return f"{self.base_url}/chat/completions"
        return f"{self.base_url}/v1/chat/completions"

    def complete(self, messages: list[dict[str, str]]) -> LLMCallResult:
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": self.max_tokens,
        }
        encoded = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        last_error: Exception | None = None
        for attempt in range(1, self.max_attempts + 1):
            started = time.perf_counter()
            request = urllib.request.Request(
                self.endpoint,
                data=encoded,
                method="POST",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
            )
            try:
                with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                    body = response.read().decode("utf-8")
                value = json.loads(body)
                choice = value.get("choices", [{}])[0]
                text = choice.get("message", {}).get("content")
                if not isinstance(text, str) or not text.strip():
                    raise RuntimeError("LLM returned no textual content")
                usage = value.get("usage") or {}
                return LLMCallResult(
                    text=text.strip(),
                    model=value.get("model") or self.model,
                    elapsed_ms=round((time.perf_counter() - started) * 1000),
                    finish_reason=choice.get("finish_reason"),
                    usage={
                        "prompt_tokens": usage.get("prompt_tokens"),
                        "completion_tokens": usage.get("completion_tokens"),
                        "total_tokens": usage.get("total_tokens"),
                    },
                )
            except (
                urllib.error.URLError,
                urllib.error.HTTPError,
                http.client.IncompleteRead,
                http.client.RemoteDisconnected,
                ConnectionError,
                ssl.SSLError,
                TimeoutError,
                UnicodeDecodeError,
                json.JSONDecodeError,
                RuntimeError,
            ) as exc:
                last_error = exc
                if attempt >= self.max_attempts:
                    break
                time.sleep(1.5 * attempt)
        raise RuntimeError(f"LLM call failed after {self.max_attempts} attempts: {last_error}")


def parse_json_object(text: str) -> dict[str, Any]:
    value = text.strip()
    if value.startswith("```"):
        lines = value.splitlines()[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        value = "\n".join(lines).strip()
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        start = value.find("{")
        end = value.rfind("}")
        if start < 0 or end <= start:
            raise
        parsed = json.loads(value[start : end + 1])
    if not isinstance(parsed, dict):
        raise TypeError("Expected a JSON object")
    return parsed
