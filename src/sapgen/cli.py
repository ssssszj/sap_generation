from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from sapgen.api import create_app
from sapgen.config import Settings
from sapgen.domain.models import SAPIR
from sapgen.domain.rules import RuleEngine
from sapgen.harness import DeepSeekHarnessAdapter, DeepSeekHarnessConfig
from sapgen.pipeline import SAPGenerationPipeline
from sapgen.storage import ProjectStore


def _settings(args: argparse.Namespace) -> Settings:
    return Settings.load(Path(args.root).resolve() if getattr(args, "root", None) else None)


def _harness(settings: Settings) -> DeepSeekHarnessAdapter:
    return DeepSeekHarnessAdapter(
        DeepSeekHarnessConfig(
            dsh_home=settings.dsh_home,
            cwd=settings.root,
            provider=settings.dsh_provider,
            model=settings.dsh_model,
            reasoning_effort=settings.dsh_reasoning_effort,
            profile=settings.dsh_profile,
            api_key=os.getenv("DEEPSEEK_API_KEY") or None,
            base_url=os.getenv("DEEPSEEK_BASE_URL") or None,
            node_executable=settings.dsh_node,
            dsh_js=settings.dsh_js,
        )
    )


def cmd_init(args: argparse.Namespace) -> int:
    settings = _settings(args)
    settings.ensure_directories()
    project = ProjectStore(settings.database).create_project(args.name)
    print(json.dumps(project, ensure_ascii=False, indent=2))
    return 0


def cmd_generate(args: argparse.Namespace) -> int:
    settings = _settings(args)
    settings.ensure_directories()
    store = ProjectStore(settings.database)
    project_id = args.project_id
    if project_id is None:
        project_id = store.create_project(args.name)["id"]
    harness = _harness(settings) if args.harness else None
    pipeline = SAPGenerationPipeline(data_dir=settings.data_dir, store=store, harness=harness)
    seed_ir = (
        SAPIR.model_validate_json(Path(args.ir).read_text(encoding="utf-8")) if args.ir else None
    )
    try:
        result = pipeline.run(
            project_id=project_id,
            input_paths=[Path(value) for value in args.input],
            seed_ir=seed_ir,
            allow_harness_fallback=not args.strict_harness,
        )
    finally:
        if harness is not None:
            harness.close()
    print(result.model_dump_json(indent=2))
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    ir = SAPIR.model_validate_json(Path(args.ir).read_text(encoding="utf-8"))
    report = RuleEngine().validate(ir)
    print(report.model_dump_json(indent=2))
    return 1 if report.has_errors else 0


def cmd_serve(args: argparse.Namespace) -> int:
    import uvicorn

    settings = _settings(args)
    settings.ensure_directories()
    harness = _harness(settings) if args.harness else None
    app = create_app(settings, harness=harness)
    uvicorn.run(app, host=settings.host, port=settings.port)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sapgen")
    parser.add_argument("--root", help="Project root used for relative runtime paths")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create a project")
    init_parser.add_argument("--name", required=True)
    init_parser.set_defaults(func=cmd_init)

    generate_parser = subparsers.add_parser("generate", help="Run the SAP pipeline")
    generate_parser.add_argument("--project-id")
    generate_parser.add_argument("--name", default="SAP generation project")
    generate_parser.add_argument("--input", action="append", required=True)
    generate_parser.add_argument("--ir", help="Optional reviewed SAP-IR seed JSON")
    generate_parser.add_argument("--harness", action="store_true")
    generate_parser.add_argument("--strict-harness", action="store_true")
    generate_parser.set_defaults(func=cmd_generate)

    validate_parser = subparsers.add_parser("validate", help="Validate SAP-IR")
    validate_parser.add_argument("--ir", required=True)
    validate_parser.set_defaults(func=cmd_validate)

    serve_parser = subparsers.add_parser("serve", help="Start API and review UI")
    serve_parser.add_argument("--harness", action="store_true")
    serve_parser.set_defaults(func=cmd_serve)
    return parser


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
