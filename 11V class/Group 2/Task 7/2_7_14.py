size = 1280 * 1024
v_tr = 1_966_080
t_tr = 280
N = 39
for i in range(1, 1000):
    if size * i * N / v_tr > t_tr:
        print(2 ** (i - 1))
        break
