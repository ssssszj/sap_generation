from __future__ import annotations

from copy import deepcopy
from typing import Any


class FakeHarnessAdapter:
    def __init__(self, response: dict[str, Any] | list[dict[str, Any]]) -> None:
        self.response = response
        self.calls: list[dict[str, Any]] = []

    def complete_json(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        schema: dict[str, Any],
        session_id: str,
    ) -> dict[str, Any]:
        self.calls.append(
            {
                "system_prompt": system_prompt,
                "user_prompt": user_prompt,
                "schema": schema,
                "session_id": session_id,
            }
        )
        if isinstance(self.response, list):
            if not self.response:
                raise RuntimeError("Fake harness has no response left.")
            return deepcopy(self.response.pop(0))
        return deepcopy(self.response)

    def close(self) -> None:
        return None
