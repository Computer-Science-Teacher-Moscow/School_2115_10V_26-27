from math import ceil, log2

size = 1920 * 1080
k = 65536
i = ceil(log2(k))
v = size * i
N = 512
for N_to_flash in range(1, 512):
    if 512 % N_to_flash == 52:
        N_to_flash = N_to_flash
        break
print(ceil(N_to_flash * v / 2 ** 23))
