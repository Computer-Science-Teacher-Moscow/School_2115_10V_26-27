size = 800 * 600
V = 600 * 2 ** 13
for i in range(1, 1000):
    if (i * size) > V:
        print(2 ** (i - 1))
        break
