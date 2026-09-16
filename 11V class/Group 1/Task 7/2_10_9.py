k = 4
nu = 48_000
i = 16
t = 3 * 60
v = k * nu * i * t
v_compressed = v * 0.85
print(round(v_compressed / 2 ** 23, 0))