k = 2
nu = 48_000
i = 34
N = 13
t_a = 42 * 60  + 20
v_zag = 110 * 2 ** 13
v_tr = 314_572_800
v_audio = k * nu * i * t_a
v_album = v_audio + N * v_zag
print(v_album // v_tr)