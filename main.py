#!/usr/bin/env python3
"""One-line pitch entry for make.fun: "A Day of One-Line Pitches".

Writes a single sentence (<= 240 characters) to <output>/entry.txt.
The sentence is fixed, so the program is fully deterministic: every run
produces the exact same bytes.
"""
import os

PITCH = "Got an app idea but never coded? Just describe it in plain words \u2014 an AI agent builds your first app on make.fun, free to enter, and it could even win you money."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch must be 1-240 chars, got {len(text)}"
    assert text.strip(), "pitch must not be blank"
    assert "\n" not in text and "\r" not in text, "pitch must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        # Exactly the pitch and nothing else: no trailing newline, no extra
        # words — the gate counts the file's characters (1-240) and the
        # judge reads the sentence as-is.
        f.write(text)

if __name__ == "__main__":
    main()
