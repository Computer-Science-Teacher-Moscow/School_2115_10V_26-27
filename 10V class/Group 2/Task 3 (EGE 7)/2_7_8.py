size = 1366 * 1280
V = 2000 * 2 ** 13
for i in range(1, 100):
    if size * i * 0.75 > V:
        print(2 ** (i - 1))
        break
