k = 2
nu = 48_000
t = 60 * 2 + 15
v = 32 * 2 ** 23
i = v // (k * nu * t)
print(i)
for i in range(1, 100):
    if k * nu * i * t > v:
        print(i - 1)
        break
