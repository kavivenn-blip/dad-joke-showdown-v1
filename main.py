#!/usr/bin/env python3
"""Dad Joke Showdown entry (u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Writes one dad joke, chosen and locked in this session, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Deterministic, no network, no dependencies beyond the standard library.
"""

import os
import stat

JOKE = '''I told the car tires they were tired. They said, "We've carried this family for years — we're running on empty now, and the spare has filed for retirement."'''


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = JOKE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
