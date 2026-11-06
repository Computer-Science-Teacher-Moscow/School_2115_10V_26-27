# 31564
from functools import cache


@cache
def f(curr, end, cnt=0):
    # cnt += 1
    if curr == end: return 0
    if curr not in graph: return float('inf')
    return min(f(to, end, cnt) + w for to, w in graph[curr])


@cache
def f1(curr, end):
    # 196
    if curr == end: return 1
    if curr not in graph: return float('inf')
    return min(f(to, end) + 1 for to, w in graph[curr])


with open('23_31564.txt') as file:
    graph = {}
    for s in file:
        start, end, w = s.split()
        graph.setdefault(int(start), []).append((int(end), float(w)))

print(int(f(117, 7331)))
print(int(f1(117, 7331)))
