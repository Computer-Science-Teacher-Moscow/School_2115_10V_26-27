from math import ceil, log2

k = 10 + 26 + 450
i = ceil(log2(k))
N = 708
V = 213 * 2 ** 10
for n in range(1, 1000):
    if ceil(i * n / 8) * N > V:
        print(n)
        break
