from math import ceil, log2

size = 4000 * 6000
i = 24
v = i * size / 2 ** 23  # в битах
print(ceil(v))
