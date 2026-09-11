from math import ceil, log2

n1 = 12
n2 = 5
k1 = 26
k2 = 9
N = 30
V = 2100
i1 = ceil(log2(k1))
i2 = ceil(log2(k2))
v = ceil((n1 * i1 + n2 * i2) / 8)
print(v * N)
for v_add in range(1000, 0, -1):
    if (v + v_add) * N <= V:
        print(v_add)
        break
