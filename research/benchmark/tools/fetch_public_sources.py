#!/usr/bin/env python3
"""Fetch public benchmark documents and verify their frozen SHA-256 hashes."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import urllib.request


ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "research" / "benchmark" / "manifests" / "documents.jsonl"


def load_manifest() -> list[dict]:
    return [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--study-id", action="append", help="Fetch only this study; may be repeated")
    parser.add_argument("--document-id", action="append", help="Fetch only this document; may be repeated")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    studies = set(args.study_id or [])
    documents = set(args.document_id or [])
    selected = []
    for record in load_manifest():
        if record.get("availability") != "public" or not record.get("source_url"):
            continue
        if studies and record["study_id"] not in studies:
            continue
        if documents and record["document_id"] not in documents:
            continue
        selected.append(record)

    if not selected:
        print("No matching public documents.", file=sys.stderr)
        return 2

    failures = 0
    for record in selected:
        target = ROOT / record["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not args.overwrite:
            actual = sha256(target)
        else:
            temporary = target.with_suffix(target.suffix + ".part")
            with urllib.request.urlopen(record["source_url"], timeout=120) as response:
                temporary.write_bytes(response.read())
            actual = sha256(temporary)
            if actual == record["sha256"]:
                temporary.replace(target)
            else:
                temporary.unlink(missing_ok=True)
        ok = actual == record["sha256"]
        failures += int(not ok)
        print(json.dumps({"document_id": record["document_id"], "path": str(target), "sha256_ok": ok}))

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
