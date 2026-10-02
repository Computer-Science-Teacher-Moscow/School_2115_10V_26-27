k = 2
nu = 48_000
i = 34
N = 13
t = 42 * 60 + 20
v_add = 110 * 2 ** 13
tr_sp = 314_572_800
t = (k * i * nu * t + v_add * N) // tr_sp
print(t)
