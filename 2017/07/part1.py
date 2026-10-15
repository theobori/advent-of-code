#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if line != ""]

degrees_in = {}

for line in lines:
    line_splitted = line.split("->")

    first = line_splitted[0]
    if len(line_splitted) > 1:
        children = line_splitted[1].strip().split(", ")
    else:
        children = []

    for child in children:
        degrees_in[child] = degrees_in.get(child, 0) + 1

    first_splitted = first.split()
    name = first_splitted[0]
    degrees_in[name] = degrees_in.get(name, 0)

ans = ""
for name, degree_in in degrees_in.items():
    if degree_in == 0:
        ans = name
        break

print(ans)
