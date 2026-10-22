#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    pairs = []
    starts = []
    for line in f.read().strip().splitlines():
        if line == "":
            continue

        pair = tuple(map(int, line.split("/")))
        if pair[0] == 0:
            starts.append(pair)
        pairs.append(pair)

seen = set()
ans = 0


def backtrack(prev, strength):
    global ans
    ans = max(ans, strength)

    for pair in pairs:
        if pair in seen:
            continue
        if prev[1] == pair[0]:
            seen.add(pair)
            backtrack(pair, strength + pair[0] + pair[1])
            seen.remove(pair)
        elif prev[1] == pair[1]:
            seen.add(pair)
            backtrack((pair[1], pair[0]), strength + pair[0] + pair[1])
            seen.remove(pair)


for start in starts:
    seen.add(start)
    backtrack(start, start[0] + start[1])

print(ans)
