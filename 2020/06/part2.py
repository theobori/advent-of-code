#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    groups = [block.strip() for block in f.read().split("\n\n") if len(block) > 0]

ans = 0
for group in groups:
    freqs = {}
    lines = group.splitlines()
    n = len(lines)

    for line in lines:
        for question in line:
            freqs[question] = freqs.get(question, 0) + 1

    for freq in freqs:
        ans += freqs[freq] == n

print(ans)
