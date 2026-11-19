#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    blocks = [block for block in f.read().split("\n\n") if len(block) > 0]

ans = 0
for block in blocks:
    lines = block.splitlines()
    fields = {}
    for line in lines:
        for pair in line.split():
            l, r = pair.split(":")
            fields[l] = r

    def f():
        for name in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"):
            if name not in fields:
                return False
        return True

    if not f():
        continue

    byr = int(fields["byr"])
    if byr < 1920 or byr > 2002:
        continue

    iyr = int(fields["iyr"])
    if iyr < 2010 or iyr > 2020:
        continue

    eyr = int(fields["eyr"])
    if eyr < 2020 or eyr > 2030:
        continue

    height_unity = fields["hgt"][-2:]
    height = int(fields["hgt"][0:-2])
    if height_unity == "cm":
        if height < 150 or height > 193:
            continue
    elif height_unity == "in":
        if height < 59 or height > 76:
            continue
    else:
        continue

    try:
        hcl = fields["hcl"]
        if hcl[0] != "#":
            continue
        hcl = hcl[1:]
        int(hcl, 16)
    except Exception as e:
        continue
    if fields["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        continue

    pid = fields["pid"]
    if len(pid) != 9 or not pid.isdigit():
        continue

    ans += 1

print(ans)
