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
        self.alive = True


particules = []
for line in lines:
    vecs = [Vec3(*list(map(int, x[3:-1].split(",")))) for x in line.split(", ")]
    particule = Particule(*vecs)
    particules.append(particule)

for _ in range(10**4):
    seen = set()
    pos_to_particule_obj = {}
    for particule in particules:
        if particule.alive is False:
            continue

        triplet = (particule.p.x, particule.p.y, particule.p.z)
        if triplet in seen:
            particule.alive = False
            pos_to_particule_obj[triplet].alive = False
            continue

        seen.add(triplet)
        pos_to_particule_obj[triplet] = particule

        particule.v.x += particule.a.x
        particule.v.y += particule.a.y
        particule.v.z += particule.a.z

        particule.p.x += particule.v.x
        particule.p.y += particule.v.y
        particule.p.z += particule.v.z

ans = 0
for particule in particules:
    ans += particule.alive is True

print(ans)
