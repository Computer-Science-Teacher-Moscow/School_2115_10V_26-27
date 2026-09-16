from math import ceil, log2

k = 10 + 1234
i = ceil(log2(k))
N = 65_536
V = 2050 * 2 ** 10
# for n in range(1000, 0, -1):
#     if ceil(i * n / 8) * N <= V:
#         print(n)
#         break
for n in range(1, 1000):
    if ceil(i * n / 8) * N > V:
        print(n - 1)
        break
