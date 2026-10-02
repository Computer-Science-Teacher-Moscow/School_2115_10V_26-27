t = 3 * 60
k = 4
nu = 48_000
i = 16
v = k * t* nu * i * .85 / 2 ** 23
print(round(v))