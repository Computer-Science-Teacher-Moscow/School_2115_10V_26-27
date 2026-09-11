size = 640 * 256
V = 170 * 2 ** 13

for i in range(1, 1000):
    if size * i / 1.35 > V:
        print(2 ** (i - 1))
        break
