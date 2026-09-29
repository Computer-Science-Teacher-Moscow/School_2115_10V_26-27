from math import log2, ceil

n = 7
k = 18 + 10
i = ceil(log2(k))
v = ceil(n * i / 8)
V = v * 60
print(V)
