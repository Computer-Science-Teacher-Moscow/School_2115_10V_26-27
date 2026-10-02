k = 4
i = 16
nu = 48_000
t = 180
tr_sp = 4800
v = k * i * nu * t * .5
t =  v / tr_sp
print(t // 60)