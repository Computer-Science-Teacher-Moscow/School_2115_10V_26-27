k = 4
nu = 32_000
i = 32
t = 2 * 60
V = i * k * nu * t

print(round(V / 2 ** 23, -1))
