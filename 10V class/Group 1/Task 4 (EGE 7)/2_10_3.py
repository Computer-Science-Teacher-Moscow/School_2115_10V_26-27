k = 2
nu = 48_000
t = 2 * 60 + 15
v = 32 * 2 ** 23
# i = v // (t * nu * k)
# print(i)
for i in range(1, 100):
    if k * t * nu * i > v:
        print(i - 1)
        break
