# 31562
from functools import cache


@cache
def f(curr, end):
    if curr == end: return 0
    if curr not in graph or curr == 3260: return float('inf')
    return min(f(to, end) + w for to, w in graph[curr])


with open('23_31562.txt') as file:
    graph = {}
    for s in file:
        start, end, w = s.split()
        graph.setdefault(int(start), []).append((int(end), float(w)))

print(int(f(514, 7836)))
