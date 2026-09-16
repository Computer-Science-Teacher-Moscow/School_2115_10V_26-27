from math import ceil, log2

n = 1231
N = 523_872
V = 432 * 2 ** 20
for i in range(1, 1000):
    if ceil(i * n / 8) * N > V:
        print(2 ** (i - 1) + 1)
        break
