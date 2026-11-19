from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _env_path(name: str, default: str, root: Path) -> Path:
    value = Path(os.getenv(name, default))
    return value if value.is_absolute() else (root / value).resolve()


@dataclass(frozen=True, slots=True)
class Settings:
    root: Path
    data_dir: Path
    database: Path
    dsh_home: Path
    dsh_profile: str
    dsh_provider: str
    dsh_model: str
    dsh_reasoning_effort: str | None
    dsh_node: Path | None
    dsh_js: Path | None
    host: str
    port: int

    @classmethod
    def load(cls, root: Path | None = None) -> Settings:
        project_root = (root or Path.cwd()).resolve()
        try:
            from dotenv import load_dotenv

            load_dotenv(project_root / ".env")
            load_dotenv(project_root / ".env.local")
        except ImportError:
            pass
        node_value = os.getenv("SAPGEN_DSH_NODE")
        js_value = os.getenv("SAPGEN_DSH_JS")
        return cls(
            root=project_root,
            data_dir=_env_path("SAPGEN_DATA_DIR", ".runtime/data", project_root),
            database=_env_path("SAPGEN_DATABASE", ".runtime/sapgen.sqlite3", project_root),
            dsh_home=_env_path("SAPGEN_DSH_HOME", ".runtime/dsh-home", project_root),
            dsh_profile=os.getenv("SAPGEN_DSH_PROFILE", "sdk"),
            dsh_provider=os.getenv("SAPGEN_DSH_PROVIDER", "deepseek-official"),
            dsh_model=os.getenv("SAPGEN_DSH_MODEL", "deepseek-v4-flash"),
            dsh_reasoning_effort=os.getenv("SAPGEN_DSH_REASONING_EFFORT") or None,
            dsh_node=(Path(node_value).expanduser().resolve() if node_value else None),
            dsh_js=(
                (project_root / js_value).resolve()
                if js_value and not Path(js_value).is_absolute()
                else Path(js_value).resolve()
                if js_value
                else None
            ),
            host=os.getenv("SAPGEN_HOST", "127.0.0.1"),
            port=int(os.getenv("SAPGEN_PORT", "3000")),
        )

    def ensure_directories(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.database.parent.mkdir(parents=True, exist_ok=True)
        self.dsh_home.mkdir(parents=True, exist_ok=True)
