size = 1280 * 960
i = 11
v = size * i
v_tr = 96_468_992
t_tr = 132
for N in range(1, 1000):
    if v * N / v_tr > t_tr:
        print(N - 1)
        break
