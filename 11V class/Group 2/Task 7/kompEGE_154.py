from math import ceil, log2

i = 24
V = 12
i2 = ceil(log2(256))
v = V // (4 * i // i2)
print(v)
