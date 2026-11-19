from __future__ import annotations

import json
import sqlite3
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def _now() -> str:
    return datetime.now(UTC).isoformat()


class ProjectStore:
    def __init__(self, database: Path) -> None:
        self.database = database.resolve()
        self.database.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.database)
        connection.row_factory = sqlite3.Row
        try:
            yield connection
            connection.commit()
        finally:
            connection.close()

    def _initialize(self) -> None:
        with self.connect() as connection:
            connection.executescript(
                """
                PRAGMA journal_mode=WAL;
                CREATE TABLE IF NOT EXISTS projects (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    metadata_json TEXT NOT NULL DEFAULT '{}'
                );
                CREATE TABLE IF NOT EXISTS runs (
                    id TEXT PRIMARY KEY,
                    project_id TEXT NOT NULL REFERENCES projects(id),
                    status TEXT NOT NULL,
                    harness_session_id TEXT,
                    created_at TEXT NOT NULL,
                    finished_at TEXT,
                    result_json TEXT,
                    error TEXT
                );
                CREATE TABLE IF NOT EXISTS run_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    run_id TEXT NOT NULL REFERENCES runs(id),
                    sequence INTEGER NOT NULL,
                    event_type TEXT NOT NULL,
                    payload_json TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    UNIQUE(run_id, sequence)
                );
                """
            )

    def create_project(self, name: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        project_id = f"project-{uuid.uuid4().hex[:12]}"
        timestamp = _now()
        with self.connect() as connection:
            connection.execute(
                "INSERT INTO projects(id, name, created_at, updated_at, metadata_json) "
                "VALUES (?, ?, ?, ?, ?)",
                (project_id, name, timestamp, timestamp, json.dumps(metadata or {})),
            )
        return self.get_project(project_id)

    def get_project(self, project_id: str) -> dict[str, Any]:
        with self.connect() as connection:
            row = connection.execute(
                "SELECT * FROM projects WHERE id = ?", (project_id,)
            ).fetchone()
        if row is None:
            raise KeyError(project_id)
        result = dict(row)
        result["metadata"] = json.loads(result.pop("metadata_json"))
        return result

    def list_projects(self) -> list[dict[str, Any]]:
        with self.connect() as connection:
            rows = connection.execute("SELECT * FROM projects ORDER BY updated_at DESC").fetchall()
        result = []
        for row in rows:
            item = dict(row)
            item["metadata"] = json.loads(item.pop("metadata_json"))
            result.append(item)
        return result

    def start_run(self, project_id: str, harness_session_id: str | None = None) -> str:
        self.get_project(project_id)
        run_id = f"run-{uuid.uuid4().hex[:12]}"
        with self.connect() as connection:
            connection.execute(
                "INSERT INTO runs(id, project_id, status, harness_session_id, created_at) "
                "VALUES (?, ?, 'running', ?, ?)",
                (run_id, project_id, harness_session_id, _now()),
            )
            connection.execute(
                "UPDATE projects SET updated_at = ? WHERE id = ?", (_now(), project_id)
            )
        return run_id

    def append_event(self, run_id: str, event_type: str, payload: dict[str, Any]) -> None:
        with self.connect() as connection:
            row = connection.execute(
                "SELECT COALESCE(MAX(sequence), 0) + 1 AS next_sequence "
                "FROM run_events WHERE run_id = ?",
                (run_id,),
            ).fetchone()
            sequence = int(row["next_sequence"])
            connection.execute(
                "INSERT INTO run_events(run_id, sequence, event_type, payload_json, created_at) "
                "VALUES (?, ?, ?, ?, ?)",
                (run_id, sequence, event_type, json.dumps(payload, ensure_ascii=False), _now()),
            )

    def finish_run(self, run_id: str, result: dict[str, Any]) -> None:
        with self.connect() as connection:
            connection.execute(
                "UPDATE runs SET status = 'completed', result_json = ?, finished_at = ? WHERE id = ?",
                (json.dumps(result, ensure_ascii=False), _now(), run_id),
            )

    def fail_run(self, run_id: str, error: str) -> None:
        with self.connect() as connection:
            connection.execute(
                "UPDATE runs SET status = 'failed', error = ?, finished_at = ? WHERE id = ?",
                (error, _now(), run_id),
            )

    def get_run(self, run_id: str) -> dict[str, Any]:
        with self.connect() as connection:
            row = connection.execute("SELECT * FROM runs WHERE id = ?", (run_id,)).fetchone()
            events = connection.execute(
                "SELECT sequence, event_type, payload_json, created_at FROM run_events "
                "WHERE run_id = ? ORDER BY sequence",
                (run_id,),
            ).fetchall()
        if row is None:
            raise KeyError(run_id)
        result = dict(row)
        result_json = result.pop("result_json")
        result["result"] = json.loads(result_json) if result_json else None
        result["events"] = [
            {
                "sequence": event["sequence"],
                "event_type": event["event_type"],
                "payload": json.loads(event["payload_json"]),
                "created_at": event["created_at"],
            }
            for event in events
        ]
        return result
