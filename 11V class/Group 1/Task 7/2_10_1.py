k = 2
nu = 48_000
i = 24
V = 288 * 2 ** 23
t = V / (k * nu * i * 60)
print(round(t, 0))
