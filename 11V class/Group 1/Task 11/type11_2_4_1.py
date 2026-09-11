from math import ceil, log2

k = 87
i = ceil(log2(k))
N = 64
v = ceil(i * N / 8)
print(v)