from math import ceil, log2

n = 261
N = 252_500
V = 31 * 2 ** 20
for i in range(1, 12):
    print(i, ceil(i * n / 8) * N, V, 2 ** i, 2 ** (i - 1) + 1)
    if ceil(i * n / 8) * N > V:
        print(2 ** (i - 1) + 1)
        break
