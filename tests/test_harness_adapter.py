from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

from sapgen.harness.base import HarnessResponseError
from sapgen.harness.deepseek import DeepSeekHarnessAdapter, DeepSeekHarnessConfig


def test_parse_plain_json() -> None:
    assert DeepSeekHarnessAdapter._parse_json('{"value": 1}') == {"value": 1}


def test_parse_fenced_json() -> None:
    value = '```json\n{"value": 2}\n```'
    assert DeepSeekHarnessAdapter._parse_json(value) == {"value": 2}


def test_parse_rejects_non_object() -> None:
    with pytest.raises(HarnessResponseError):
        DeepSeekHarnessAdapter._parse_json("[]")


def test_complete_json_retries_invalid_json_with_fresh_session(tmp_path: Path) -> None:
    class FlakyHarness:
        def __init__(self) -> None:
            self.calls: list[tuple[str, str]] = []

        def run(self, prompt: str, *, session_id: str):
            self.calls.append((prompt, session_id))
            response = '{"value": "broken"' if len(self.calls) == 1 else '{"value": "ok"}'
            return SimpleNamespace(finish_reason="completed", final_response=response)

    adapter = DeepSeekHarnessAdapter(DeepSeekHarnessConfig(dsh_home=tmp_path / "dsh", cwd=tmp_path))
    harness = FlakyHarness()
    adapter._harness = harness

    result = adapter.complete_json(
        system_prompt="Return data.",
        user_prompt="Input.",
        schema={"type": "object"},
        session_id="extract-design",
    )

    assert result == {"value": "ok"}
    assert adapter.call_count == 2
    assert [session for _, session in harness.calls] == [
        "extract-design",
        "extract-design-json-retry",
    ]
    assert "previous response was not valid complete JSON" in harness.calls[1][0]
