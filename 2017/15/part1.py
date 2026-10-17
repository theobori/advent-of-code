#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = f.read().strip().splitlines()

assert len(lines) == 2

A = int(lines[0].split()[-1])
B = int(lines[1].split()[-1])

ans = 0
for _ in range(40 * 10**6):
    A = (A * 16807) % 2147483647
    B = (B * 48271) % 2147483647

    ans += A & 0xFFFF == B & 0xFFFF

print(ans)
