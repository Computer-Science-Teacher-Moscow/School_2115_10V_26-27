size = 480 * 768
v = 405 * 2 ** 13

for i in range(1, 1000):
    if size * (i + i // 2 + i % 2) > v:
        print(2 ** (i - 1))
        break
