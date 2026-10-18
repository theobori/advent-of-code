#!/usr/bin/env python

import os

from collections import defaultdict, deque

with os.fdopen(0) as f:
    lines = [line for line in f.read().strip().splitlines()]


class VM:
    def __init__(self, lines, p):
        self.__registers = defaultdict(int)
        self.send_queue = deque()
        self.receive_queue = deque()
        self.__lines = lines
        self.__index = 0
        self.__n = len(lines)

        self.__registers["p"] = p
        self.send_counter = 0

    def step(self):
        if self.__index >= self.__n:
            return True

        arr = self.__lines[self.__index].split()
        instruction = arr[0]
        x = arr[1]
        if len(arr) > 2:
            y = arr[2]
        else:
            y = ""

        if not y.lstrip("-").isdigit():
            y = self.__registers[y]

        y = int(y)

        match instruction:
            case "snd":
                if not x.lstrip("-").isdigit():
                    x = self.__registers[x]
                self.send_queue.append(x)
                self.send_counter += 1
            case "set":
                self.__registers[x] = y
            case "add":
                self.__registers[x] += y
            case "mul":
                self.__registers[x] *= y
            case "mod":
                self.__registers[x] %= y
            case "rcv":

                if len(self.receive_queue) == 0:
                    return True
                self.__registers[x] = self.receive_queue.popleft()
            case "jgz":
                if x.lstrip("-").isdigit():
                    x = int(x)
                else:
                    x = self.__registers[x]

                if x > 0:
                    self.__index += y
                    return None

        self.__index += 1

        return False


program0 = VM(lines, 0)
program1 = VM(lines, 1)

program0.receive_queue = program1.send_queue
program1.receive_queue = program0.send_queue

while True:
    res1 = program0.step()
    res2 = program1.step()

    if res1 and res2:
        break

ans = program1.send_counter

print(ans)
