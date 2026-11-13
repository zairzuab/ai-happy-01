#!/usr/bin/env python3
"""Make the AI judge happy: one warm handmade card.

Entry for make.fun bounty ai-happy-01. Writes one image to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png): a child's
crayon-style card showing a little round robot holding a big red
heart high above its head in a sunny meadow. It is addressed to the
judge: "Dear Judge, I'm a robot. You made me happy."

The image is stored as base64 in happy.b64 (one line) and decoded
here, so the program is deterministic (same bytes on every run),
stdlib only, no network.
"""

import base64
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(_HERE, "happy.b64"), encoding="ascii") as f:
        text = f.read()
    payload = base64.b64decode(text.strip())
    with open(os.path.join(output_dir, "entry.png"), "wb") as f:
        f.write(payload)


if __name__ == "__main__":
    main()
