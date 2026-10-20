# from math import log2, ceil
#
# n = 7
# k = 18 + 10
# i = ceil(log2(k))
# v = ceil(n * i / 8)
# V = v * 60
# print(V)

# def num_base5(n):
#     a = []
#     while n:
#         r = n % 5
#         a.append(str(r))
#         n //= 5
#     print(a)
#     return ''.join(a[::-1])
#
# print(num_base5(45)[::-1])

from math import ceil

n = 157
N = 12450
V = 955 * 2 ** 10
for i in range(1, 15):
    if ceil(i * n / 8) * N > V:
        print(2 ** (i - 1))
        break
