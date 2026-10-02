k = 2
nu = 48_000
i = 34
t = 42 * 60 + 20
N = 13
v_add = 110 * 2 ** 13
tr_sp = 314_572_800
t = (k * nu * i * t + N * v_add) // tr_sp
print(t)
