from math import log2, ceil

n = 440
N = 1_892_412
V = 305_726 * 1024
for k in range(1, 1000):
    i = ceil(log2(k))
    v = ceil(i * n / 8)
    if  v * N > V:
        print(k)
        break
