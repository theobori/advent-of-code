#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    blocks = [block for block in f.read().split("\n\n") if len(block) > 0]

ans = 0
for block in blocks:
    lines = block.splitlines()
    fields = {}
    for line in lines:
        for pair in line.split():
            l, r = pair.split(":")
            fields[l] = r

    for name in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"):
        if name not in fields:
            break
    else:
        ans += 1

print(ans)
