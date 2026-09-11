size = 486 * 720
V = 80 * 2 ** 13

for i in range(1, 1000):
    if size * i * .85 > V:
        print(2 ** (i - 1))
        break
