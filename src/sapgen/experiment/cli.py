from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from sapgen.experiment.runner import METHODS, ExperimentRunner


def _methods(values: list[str] | None) -> tuple[str, ...]:
    return tuple(values or METHODS)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sapgen-experiment")
    parser.add_argument("--root", default=".", help="sapgen_rebuild project root")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare")
    prepare.add_argument("--sample-size", type=int, default=20)
    prepare.add_argument("--seed", type=int, default=20261108)

    fetch = subparsers.add_parser("fetch")
    fetch.add_argument("--overwrite", action="store_true")

    subparsers.add_parser("prepare-inputs")

    run = subparsers.add_parser("run")
    run.add_argument("--method", action="append", choices=METHODS)
    run.add_argument("--study-id", action="append")
    run.add_argument("--force", action="store_true")

    judge = subparsers.add_parser("judge")
    judge.add_argument("--method", action="append", choices=METHODS)
    judge.add_argument("--study-id", action="append")
    judge.add_argument("--force", action="store_true")

    subparsers.add_parser("summarize")
    return parser


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = build_parser().parse_args()
    runner = ExperimentRunner(Path(args.root))
    if args.command == "prepare":
        value = runner.prepare(sample_size=args.sample_size, seed=args.seed)
    elif args.command == "fetch":
        value = runner.fetch_inputs(overwrite=args.overwrite)
    elif args.command == "prepare-inputs":
        value = runner.prepare_inputs()
    elif args.command == "run":
        value = runner.run_generation(
            methods=_methods(args.method),
            study_ids=set(args.study_id) if args.study_id else None,
            force=args.force,
        )
    elif args.command == "judge":
        value = runner.run_judging(
            methods=_methods(args.method),
            study_ids=set(args.study_id) if args.study_id else None,
            force=args.force,
        )
    else:
        value = runner.summarize()
    print(json.dumps(value, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
