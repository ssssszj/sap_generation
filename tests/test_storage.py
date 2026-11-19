from __future__ import annotations

from sapgen.storage import ProjectStore


def test_run_events_are_append_only_and_ordered(tmp_path) -> None:
    store = ProjectStore(tmp_path / "store.sqlite3")
    project = store.create_project("test")
    run_id = store.start_run(project["id"], "session-1")
    store.append_event(run_id, "one", {"value": 1})
    store.append_event(run_id, "two", {"value": 2})
    store.finish_run(run_id, {"ok": True})

    run = store.get_run(run_id)
    assert [event["sequence"] for event in run["events"]] == [1, 2]
    assert run["result"] == {"ok": True}
