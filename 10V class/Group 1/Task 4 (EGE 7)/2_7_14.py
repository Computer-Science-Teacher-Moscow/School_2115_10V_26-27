from math import ceil, log2
from time import process_time

size = 1280 * 1024
N = 39
tr_sp = 1_966_080
t = 280
for i in range(1, 1000):
    if size * i * N / tr_sp > t:
        print(2 ** (i - 1))
        break
