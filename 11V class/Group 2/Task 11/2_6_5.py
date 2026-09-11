from math import ceil, log2

n = 15
k = 26
# i = ceil(log2(k))
i = 5
v_id = ceil(n * i / 8)
n2 = 20
i2 = len(bin(2023)[2:])
v_descr = ceil(i2 * n2 / 8)
v_obj = v_id + v_descr  # в байтах
N = 65_536
V = 4 * 2 ** 20  # в байтах
for v_add in range(1, 1000000):
    if (v_obj + v_add) * N > V:
        print(v_add - 1)
        break
print(V/N - v_obj)
