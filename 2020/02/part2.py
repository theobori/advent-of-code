#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]

ans = 0
for line in lines:
    r, ch, password = line.split()
    lo, hi = list(map(int, r.split("-")))
    ch = ch[0:-1]

    count = int(password[lo - 1] == ch) + int(password[hi - 1] == ch)
    if count == 1:
        ans += 1

print(ans)
