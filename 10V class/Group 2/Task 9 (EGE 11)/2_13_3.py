from math import ceil, log2

k = 26 + 450 + 10
i = ceil(log2(k))

N = 708
V = 213 * 2 ** 10
for n in range(1, 10000):
    if ceil(i * n / 8) * N > V:
        print(n)
        break
