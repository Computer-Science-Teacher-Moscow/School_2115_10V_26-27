from math import log2, ceil

size = 486 * 720
v = 80 * 2 ** 13
for i in range(1, 1000):
    if size * i * .85 > v:
        print(2 ** (i - 1))
        break

# size = 486 * 720
# v = 80 * 2 ** 13
# for i in range(1000, 0, -1):
#     if size * i * .85 <= v:
#         print(2 ** i)
#         break