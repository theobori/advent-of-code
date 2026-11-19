#!/usr/bin/env python

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]

code = []
for line in lines:
    op, rest = line.split()
    sign = rest[0]
    arg = int(rest[1:]) * -1 if sign == "-" else int(rest[1:])
    code.append((op, arg))

ip = 0
acc = 0
seen = set()
n = len(code)
while ip < n:
    op, arg = code[ip]
    if ip in seen:
        break

    match op:
        case "acc":
            acc += arg
        case "jmp":
            ip += arg
            continue
        case "nop":
            pass
        case _:
            raise ValueError()

    seen.add(ip)
    ip += 1


ans = acc
print(ans)
