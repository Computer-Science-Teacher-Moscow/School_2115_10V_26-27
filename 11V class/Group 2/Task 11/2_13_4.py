from math import ceil, log2

n = 80
N = 1200
V = 150 * 2 ** 10
for i in range(1, 1000):
    if ceil(i * n / 8) * N > V:
        print(2 ** (i -1))
        break
