from math import ceil, log2

n1 = 9
k = 26
i = ceil(log2(k))
v1 = n1 * i  # в битах
k = 4000
i2 = ceil(log2(k))
v2 = i2  # в битах
v_id = ceil((v1 + v2) / 8)
v_add = 11  # байт
V = 1000
for N in range(100, 0, -1):
    if (v_id + v_add) * N <= V:
        print(N)
        break
