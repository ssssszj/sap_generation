from __future__ import annotations

from typing import Any, Protocol


class HarnessUnavailableError(RuntimeError):
    pass


class HarnessResponseError(RuntimeError):
    pass


class HarnessAdapter(Protocol):
    def complete_json(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        schema: dict[str, Any],
        session_id: str,
    ) -> dict[str, Any]: ...

    def close(self) -> None: ...
