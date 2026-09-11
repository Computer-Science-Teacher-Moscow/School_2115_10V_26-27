from math import ceil, log2

size = 128 * 128
k = 128
i = ceil(log2(k))  # 7
v = i * size  # в битах
print(v // 2 ** 13)
