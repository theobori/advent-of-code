#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if line != ""]

ans = 0
for line in lines:
    words = line.split()
    seen = set(words)

    ans += len(words) == len(seen)

print(ans)
