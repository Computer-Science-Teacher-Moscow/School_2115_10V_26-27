size = 1280 * 1024
N = 39
tr_sp = 1966080
t = 280
for i in range(1, 100):
    if size * i * N / tr_sp > t:
        print(2 ** (i - 1))
        break