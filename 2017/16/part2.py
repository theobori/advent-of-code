#!/usr/bin/env pypy

import os

from collections import deque

with os.fdopen(0) as f:
    moves = f.read().strip().split(",")

indexes = {}
programs = deque(list("abcdefghijklmnop"))


def dance():
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


seen = set()
cycle_size = 0
for i in range(10**9):
    if "".join(programs) in seen:
        cycle_size = i
        break
    seen.add("".join(programs))

    dance()


remaining_dances = 10**9 % cycle_size

for _ in range(remaining_dances):
    dance()

print("".join(programs))
