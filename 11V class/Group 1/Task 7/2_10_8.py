k = 2
nu = 64_000
i = 16
t = 4 * 60
v = k * nu * i * t
v_compressed = v * 0.75
print(round(v_compressed / 2 ** 23, 0))