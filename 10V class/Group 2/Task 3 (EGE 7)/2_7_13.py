from math import log2, ceil

size = 1280 * 960
k = 2048
i = ceil(log2(k))
v = size * i
tr_sp = 96_468_992
t = 132
for N in range(1, 1000):
    if v * N / tr_sp > t:
        print(N - 1)
        break
