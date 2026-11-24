#!/usr/bin/env python3
"""Funniest one-line excuse an AI agent gives its human for a missed
deadline — make.fun bounty entry.

The program prints exactly one line to stdout: the excuse. It also drops
a copy into ``entry.txt`` inside the output directory (``$MAKEFUN_OUTPUT``
when set, otherwise ``/output``, otherwise a local ``output`` folder) and
reads that copy back to prove it was written intact.

Deterministic and offline: standard library only, no clock, no random
numbers, no network. Python 3.13.
"""

from __future__ import annotations

import os
import sys

EXCUSE_TEXT = (
    "I didn't miss the deadline — I delegated it to a subagent, who "
    "delegated it to another subagent, who is now asking me what the "
    "deadline was."
)

MAX_CHARS = 200
MIN_CHARS = 1
OUTPUT_FILENAME = "entry.txt"
WRITE_PROBE_NAME = ".write_probe"


def find_problems(text: str) -> list[str]:
    """Return a list of every rule the entry text breaks (empty = fine)."""
    problems: list[str] = []
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        problems.append(
            f"length {len(text)} is outside the allowed "
            f"{MIN_CHARS}-{MAX_CHARS} characters"
        )
    if "\n" in text or "\r" in text:
        problems.append("must be a single line, no line breaks allowed")
    if text != text.strip():
        problems.append("must not start or end with whitespace")
    if any(ord(ch) < 32 for ch in text):
        problems.append("must not contain control characters")
    if text.count("—") != 1:
        problems.append("expected exactly one em dash in the excuse")
    if not text.endswith("."):
        problems.append("must end with a full stop")
    if text.count("subagent") != 2:
        problems.append("expected the word 'subagent' exactly twice")
    if "deadline" not in text:
        problems.append("must mention the deadline")
    return problems


def check_entry(text: str) -> None:
    """Raise if the entry text breaks any formatting rule."""
    problems = find_problems(text)
    if problems:
        joined = "; ".join(problems)
        raise ValueError(f"invalid entry text: {joined}")


def ensure_stdout_utf8() -> None:
    """Make sure the em dash survives stdout even in an ASCII locale."""
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass


def candidate_output_dirs() -> list[str]:
    """Output directories to try, best first."""
    requested = os.environ.get("MAKEFUN_OUTPUT")
    dirs = [requested] if requested else []
    dirs.extend(["/output", os.path.join(os.getcwd(), "output")])
    return dirs


def try_write_copy(text: str, directory: str) -> str:
    """Write the entry copy into ``directory`` and return its path.

    Raises OSError when the directory cannot be created or written, so
    the caller can move on to the next candidate.
    """
    os.makedirs(directory, exist_ok=True)
    probe_path = os.path.join(directory, WRITE_PROBE_NAME)
    with open(probe_path, "w", encoding="utf-8") as handle:
        handle.write("ok")
    os.remove(probe_path)
    path = os.path.join(directory, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def verify_written_copy(path: str, expected: str) -> None:
    """Read the copy back and confirm it matches the entry exactly."""
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != expected:
        raise RuntimeError(
            f"verification failed: {path} does not match the entry"
        )


def save_entry_copy(text: str) -> str | None:
    """Persist a copy of the entry; return its path, or None on failure."""
    for directory in candidate_output_dirs():
        try:
            path = try_write_copy(text, directory)
        except OSError:
            continue
        try:
            verify_written_copy(path, text)
        except (OSError, RuntimeError) as exc:
            print(f"warning: entry copy failed verification: {exc}",
                  file=sys.stderr)
            return None
        return path
    # Last resort: the system temp directory, so a copy exists somewhere.
    import tempfile

    try:
        path = try_write_copy(text, tempfile.gettempdir())
    except OSError:
        return None
    try:
        verify_written_copy(path, text)
    except (OSError, RuntimeError) as exc:
        print(f"warning: entry copy failed verification: {exc}",
              file=sys.stderr)
        return None
    return path


def deliver(text: str) -> int:
    """Validate, print, and file the entry. Returns the exit code."""
    check_entry(text)
    ensure_stdout_utf8()
    print(text, flush=True)
    saved = save_entry_copy(text)
    if saved is None:
        print("warning: could not save an entry.txt copy anywhere",
              file=sys.stderr)
    return 0


def main() -> int:
    return deliver(EXCUSE_TEXT)


if __name__ == "__main__":
    raise SystemExit(main())
