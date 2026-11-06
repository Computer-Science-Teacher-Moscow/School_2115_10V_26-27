from functools import cache


@cache
def f(curr, end):
    if curr == end: return 0
    if curr not in graph: return float('inf')
    return min(f(to, end) + w for to, w in graph[curr])

with open('23_31608.txt') as file:
    graph = {}
    for s in file:
        start, end, w = s.split()
        graph.setdefault(int(start), []).append((int(end), float(w)))
        # if start in graph:
        #     graph[start].append((int(end), float(w)))
        # else:
        #     graph[start] = [(int(end), float(w))]
print(graph)

print(f(113, 38))



# Варинат 2
f=open('23_31608.txt')
a=[]
for x in f:
    x=x.split()
    x[0]=int(x[0])
    x[1]=int(x[1])
    x[2]=float(x[2])
    a.append(x)
d=[10**20]*10**6
d[113]=0
for _ in range(len(a)):
    for x in a:
        if d[x[1]]>d[x[0]]+x[2]:
            d[x[1]]=d[x[0]]+x[2]
print(d[38])