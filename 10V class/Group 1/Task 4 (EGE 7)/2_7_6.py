from math import log2, ceil

size = 1024 * 768
k= 4096
i = ceil(log2(k))
N = 256
v = size * i
v_pack = v * N / 2 ** 23
print(v_pack)

