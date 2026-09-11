size = 1024 * 768
v_add = 640 * 2 ** 13
N = 2048
V = 2 * 2 ** 33
for i in range(1, 1000):
    if (size * i + v_add) * N > V:
        print(2 ** (i - 1))
        break
