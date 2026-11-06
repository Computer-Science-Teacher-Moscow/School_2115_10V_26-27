from functools import cache


@cache
def f(curr, end):
    if curr == end: return 0
    if curr not in graph: return float('inf')
    return min(f(to, end) + w for to, w in graph[curr])


with open('23_31561.txt') as file:
    graph = {}
    for s in file:
        start, end, w = s.split()
        graph.setdefault(int(start), []).append((int(end), float(w)))

print(int(f(726, 2767) + f(2767, 9517)))


from functools import cache

@cache
def f(curr, end, cnt=0):
    if curr == 2767: cnt += 1
    if curr == end: return 0 if cnt == 1 else float('inf')
    if curr not in graph: return float('inf')
    return min(f(to, end, cnt) + w for to, w in graph[curr])


with open('23_31561.txt') as file:
    graph = {}
    for s in file:
        start, end, w = s.split()
        graph.setdefault(int(start), []).append((int(end), float(w)))

print(int(f(726, 9517)))
