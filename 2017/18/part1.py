#!/usr/bin/env python

import os

from collections import defaultdict, deque

with os.fdopen(0) as f:
    lines = [line for line in f.read().strip().splitlines()]

registers = defaultdict(int)
st = deque()
freq = -1
n = len(lines)
i = 0
while i < n:
    arr = lines[i].split()
    instruction = arr[0]
    x = arr[1]
    if len(arr) > 2:
        y = arr[2]
    else:
        y = ""

    if not y.lstrip("-").isdigit():
        y = registers[y]

    y = int(y)

    match instruction:
        case "snd":
            st.append(registers[x])
        case "set":
            registers[x] = y
        case "add":
            registers[x] += y
        case "mul":
            registers[x] *= y
        case "mod":
            registers[x] %= y
        case "rcv":
            v = registers[x]
            if v != 0:
                if st:
                    freq = st.pop()
                break
        case "jgz":
            if registers[x] > 0:
                i += y
                continue
    i += 1

print(freq)
