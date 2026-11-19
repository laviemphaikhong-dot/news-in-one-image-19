#!/usr/bin/env python3
"""Deliver the finished front page for the 19 November news bounty.

The page itself ships in this repository as ``entry.png``. Running this
program publishes it: the PNG is copied, unchanged, into whichever
directory the grading harness points at through ``MAKEFUN_OUTPUT_DIR``
(falling back to ``/output``). The program reads no clock, opens no
network connection and rolls no dice, so repeated runs emit exactly
the same bytes.
"""

import os
import shutil
import pathlib

PAGE = pathlib.Path(__file__).resolve().with_name("entry.png")


def output_dir() -> pathlib.Path:
    named = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return pathlib.Path(named) if named else pathlib.Path("/output")


def main() -> None:
    if not PAGE.is_file():
        raise SystemExit(f"entry.png is missing beside {__file__}")
    folder = output_dir()
    folder.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(PAGE, folder / "entry.png")


if __name__ == "__main__":
    main()
