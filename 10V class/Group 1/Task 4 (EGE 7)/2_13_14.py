from math import ceil

i = 12
size = 800 * 640
v = size * (i + i // 3 + (1, 0)[i % 3 == 0])
print(ceil(v / 2 ** 13))
