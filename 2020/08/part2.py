#!/usr/bin/env python

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]

code = []
for line in lines:
    op, rest = line.split()
    sign = rest[0]
    arg = int(rest[1:]) * -1 if sign == "-" else int(rest[1:])
    code.append([op, arg])


n = len(code)


def is_repair(code):
    ip = 0
    acc = 0
    seen = set()
    while ip < n:
        op, arg = code[ip]
        if ip in seen:
            return False, None

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

    return True, acc


ans = 0
for i in range(n):
    op = code[i][0]
    match op:
        case "jmp":
            code[i][0] = "nop"
        case "nop":
            code[i][0] = "jmp"

    ok, acc = is_repair(code)
    if ok:
        ans = acc
        break

    code[i][0] = op

print(ans)
