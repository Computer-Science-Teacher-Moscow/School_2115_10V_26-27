size = 1024 * 120
v = 210 * 2 ** 13
i_tr = 7
for i in range(1, 1000):
    if size * (i + i_tr) > v:
        print(2 ** (i - 1))
        break