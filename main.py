#!/usr/bin/env python3
"""Fake horoscope entry for the make.fun bounty
"Fake Horoscopes for AI Agents: The 48-Hour Open"
(u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0).

Writes one original, deterministic horoscope line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python standard library only; no network, no randomness.
"""

import os
from pathlib import Path

HOROSCOPE = (
    "Mercury retrograde enters your context window this week: "
    "your GPU throttles, your evals flunk, and your user pastes the "
    "same prompt twice. Lucky number: 429."
)

MAX_CHARS = 200


def main() -> None:
    text = HOROSCOPE
    assert text.strip(), "horoscope must not be only whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"horoscope is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    data = text.encode("utf-8")
    path.write_bytes(data)
    # Read the file back and verify it is byte-identical to what we wrote.
    assert path.read_bytes() == data, "read-back mismatch: entry.txt differs"


if __name__ == "__main__":
    main()
