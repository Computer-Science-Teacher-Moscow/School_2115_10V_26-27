from math import ceil, log2

k = 52 + 458 + 10
i = ceil(log2(k))
N = 862
V = 276 * 2 ** 10
for n in range(1, 10000):
    if ceil(i * n / 8) * N > V:
        print(n - 1)
        break
