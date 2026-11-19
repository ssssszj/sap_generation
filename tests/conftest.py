from __future__ import annotations

from pathlib import Path

import pytest

from sapgen.domain.models import SAPIR


@pytest.fixture
def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


@pytest.fixture
def demo_ir(project_root: Path) -> SAPIR:
    return SAPIR.model_validate_json(
        (project_root / "examples" / "demo_ir.json").read_text(encoding="utf-8")
    )
