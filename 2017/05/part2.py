#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    code = [int(line) for line in f.read().splitlines() if line != ""]

ip = 0
n = len(code)
ans = 0

while True:
    ans += 1
    offset = code[ip]
    if offset >= 3:
        code[ip] -= 1
    else:
        code[ip] += 1

    ip += offset
    if ip < 0 or ip >= n:
        break

print(ans)
