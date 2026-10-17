#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = f.read().strip().splitlines()


class Pair:
    def __init__(self, row, delta, max_row):
        self.row = row
        self.delta = delta
        self.max_row = max_row

    def update(self):
        if self.delta > 0:
            if self.row >= self.max_row:
                self.delta = -1
        else:
            if self.row <= 1:
                self.delta = 1

        self.row += self.delta

    def __str__(self):
        return (
            "row "
            + str(self.row)
            + ", max_row "
            + str(self.max_row)
            + ", delta "
            + str(self.delta)
        )


start, end = float("inf"), float("-inf")
firewall = {}
for line in lines:
    depth, _range = line.split(":")

    depth = int(depth)
    _range = int(_range)
    firewall[depth] = Pair(row=1, delta=1, max_row=_range)
    start = min(start, depth)
    end = max(end, depth)


def solve(delay):

    # predict positions
    for col in firewall:
        period = 2 * (firewall[col].max_row - 1)
        if period == 0:
            return False

        if (col + delay) % period == 0:
            return False

    return True


ans = -1
i = 0
while True:
    if solve(i):
        ans = i
        break
    i += 1

print(ans)
