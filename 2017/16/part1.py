#!/usr/bin/env pypy

import os

from collections import deque

with os.fdopen(0) as f:
    moves = f.read().strip().split(",")

indexes = {}
programs = deque(list("abcdefghijklmnop"))

for move in moves:
    if move[0] == "s":
        for _ in range(int(move[1:])):
            programs.appendleft(programs.pop())
    elif move[0] == "x":
        i, j = list(map(int, move[1:].split("/")))
        programs[i], programs[j] = programs[j], programs[i]
    elif move[0] == "p":
        a, b = move[1:].split("/")

        for i, program in enumerate(programs):
            indexes[program] = i

        i, j = indexes[a], indexes[b]
        programs[i], programs[j] = programs[j], programs[i]

print("".join(programs))
