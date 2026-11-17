from math import log2, ceil

n = 65
N = 131072
V = 9 * 2 ** 20
for k in range(1, 500):
    i = ceil(log2(k))
    v = ceil(i * n / 8)
    if v * N < V:
        print(k)
