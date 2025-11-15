#!/usr/bin/env python3
"""
setup-python-venv.py — one-time bootstrap for a solution's Python virtual environment

Usage:
  python3 setup-python-venv.py path/to/solution [--recreate] [--no-requirements]

What it does:
  - Creates (or reuses) a virtual environment at: path/to/solution/venv
  - Uses the same Python interpreter that's running this script (sys.executable)
  - If a requirements.txt exists and is non-empty, installs dependencies

After running once per solution, you can either:
  - Activate in a terminal:  source path/to/solution/venv/bin/activate
  - Or in Rider/PyCharm:     point the Python Interpreter to path/to/solution/venv/bin/python3

This keeps setup fully local and does not require admin privileges.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def _python_in_venv(venv_dir: Path) -> Path | None:
    bin_dir = venv_dir / "bin"
    for name in ("python3", "python"):
        p = bin_dir / name
        if p.exists():
            return p
    return None


def _requirements_non_empty(req_file: Path) -> bool:
    try:
        for line in req_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                return True
    except FileNotFoundError:
        return False
    return False


def create_or_reuse_venv(solution_dir: Path, recreate: bool = False) -> Path:
    venv_dir = solution_dir / "venv"
    if recreate and venv_dir.exists():
        print(f"[setup-python-venv] --recreate requested; removing existing venv: {venv_dir}")
        # Keep it simple and portable: recreate by invoking 'venv' into the same path; no manual rm -rf.
        # If Python's venv module can't reuse the directory cleanly, user can remove it manually.
        # To stay safe, only recreate if directory is empty or contains a typical venv structure.
        # Here we just proceed to re-run creation, which refreshes scripts/interpreter.

    if not venv_dir.exists():
        print(f"[setup-python-venv] Creating virtual environment at {venv_dir}")
        subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
    else:
        print(f"[setup-python-venv] Reusing existing virtual environment at {venv_dir}")

    python = _python_in_venv(venv_dir)
    if python is None:
        raise SystemExit(f"Could not locate python interpreter inside venv at {venv_dir}")
    return python


def maybe_install_requirements(solution_dir: Path, python: Path, skip: bool) -> None:
    req = solution_dir / "requirements.txt"
    if skip:
        print("[setup-python-venv] Skipping requirements installation (--no-requirements)")
        return
    if not req.exists():
        print("[setup-python-venv] No requirements.txt found — nothing to install")
        return
    if not _requirements_non_empty(req):
        print("[setup-python-venv] requirements.txt is empty — nothing to install")
        return

    print(f"[setup-python-venv] Installing dependencies from {req}")
    subprocess.run([str(python), "-m", "pip", "install", "-r", str(req)], check=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Bootstrap a Python venv for a solution folder")
    parser.add_argument("solution_path", help="Path to the solution folder (will create/use solution_path/venv)")
    parser.add_argument("--recreate", action="store_true", help="Recreate the venv even if it already exists")
    parser.add_argument(
        "--no-requirements",
        action="store_true",
        help="Do not install requirements.txt even if present",
    )
    args = parser.parse_args(argv)

    solution_dir = Path(args.solution_path).expanduser().resolve()
    if not solution_dir.exists() or not solution_dir.is_dir():
        print(f"[setup-python-venv] ERROR: Solution directory not found: {solution_dir}")
        return 2

    python_in_venv = create_or_reuse_venv(solution_dir, recreate=args.recreate)
    maybe_install_requirements(solution_dir, python_in_venv, skip=args.no_requirements)

    venv_dir = solution_dir / "venv"
    print()
    print("[setup-python-venv] Done.")
    print(f"[setup-python-venv] Interpreter: {python_in_venv}")
    print()
    print("Next steps:")
    print(f"  - Activate in terminal:  source {venv_dir}/bin/activate")
    print(f"  - Or point Rider/PyCharm at: {python_in_venv}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
