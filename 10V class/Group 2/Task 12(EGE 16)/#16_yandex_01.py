from math import ceil, log2 

nA = 7
nB = 9
NA = 384
NB = 256
V = 7168
for N in range(1, 10000):
    if ceil(ceil(log2(N)) * nA / 8) * NA + ceil(ceil(log2(N)) * nB / 8) * NB == V:
        print(N)
        break

