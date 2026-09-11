k = 2
nu = 48_000
t = 2 * 60 + 15
V = 32 * 2 ** 23
# print(V // (k * nu* t))
for i in range(1,100):
    if k * nu * t * i > V:
        print(i - 1)
        break