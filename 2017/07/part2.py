#!/usr/bin/env python

import os


class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children


with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if line != ""]

graph = {}
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
    weight = int(first_splitted[1][1:-1])
    graph[name] = Node(name, weight, children)
    degrees_in[name] = degrees_in.get(name, 0)

root_name = ""
for name, degree_in in degrees_in.items():
    if degree_in == 0:
        root_name = name
        break

root = graph[root_name]


def solve(node):
    final = None

    def dfs(node):

        ans = node.weight

        subtower_weights = []
        child_node_weights = []
        for child_name in node.children:
            child_node = graph[child_name]
            subtower_weight = dfs(child_node)
            subtower_weights.append(subtower_weight)
            child_node_weights.append(child_node.weight)
            ans += subtower_weight

        nonlocal final
        if final is None and len(set(subtower_weights)) > 1:
            m = max(subtower_weights)
            mi = subtower_weights.index(m)

            final = child_node_weights[mi] - abs(
                subtower_weights[mi] - subtower_weights[mi - 1]
            )

        return ans

    dfs(node)

    return final


ans = solve(root)
print(ans)
