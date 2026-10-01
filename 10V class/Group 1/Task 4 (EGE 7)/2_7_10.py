size = 1280 * 1024
i = 10
N = 220
tr_sp = 12_582_912
v_pack = size * i * N
t = v_pack // tr_sp
print(t)
