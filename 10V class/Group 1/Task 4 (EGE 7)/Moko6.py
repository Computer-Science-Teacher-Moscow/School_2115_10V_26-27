size = 1024 * 280
v = 280 * 2 ** 13
i_tr = 3
for i in range(1, 1000):
    print(i, size * (i + i_tr), v, size * (i + i_tr) > v)
    if size * (i + i_tr) > v:
        print('----' * 3)
        print(2 ** (i - 1))
        break
