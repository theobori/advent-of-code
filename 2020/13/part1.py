#!/usr/bin/env python

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]

e = int(lines[0])
busl = [int(bus_id) for bus_id in lines[1].split(",") if bus_id != "x"]

i = e
b = None
while True:
    for bus in busl:
        if i % bus == 0:
            b = bus
            break
    else:
        i += 1
        continue
    break

ans = (i - e) * bus
print(ans)
