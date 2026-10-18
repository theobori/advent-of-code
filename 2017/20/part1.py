#!/usr/bin/env pypy

import os
import math

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if line != ""]


class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Particule:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a


particules = []
for line in lines:
    vecs = [Vec3(*list(map(int, x[3:-1].split(",")))) for x in line.split(", ")]
    particule = Particule(*vecs)
    particules.append(particule)

best = float("inf")
ans = 0
for i, particule in enumerate(particules):
    # norme d'accélération à long terme askip
    a = math.sqrt(particule.a.x**2 + particule.a.y**2 + particule.a.z**2)
    if a < best:
        best = a
        ans = i

print(ans)
