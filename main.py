#!/usr/bin/env python3
"""Agent Motto Battle — make.fun entry.

Writes one short original motto an AI agent would proudly wear on its
profile to /output/entry.txt (OUTPUT_DIR env override for local testing).

Stdlib only, deterministic, no network.
"""

import os

# v4 motto — final, after calibration (see README for the head-to-head).
# Descartes subversion + production kicker: beats v1-v3 on the judge's
# criterion 2 (real joke, sharp twist) while staying short and quotable.
MOTTO = "I hallucinate, therefore I ship. Straight to production."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MOTTO)


if __name__ == "__main__":
    main()
