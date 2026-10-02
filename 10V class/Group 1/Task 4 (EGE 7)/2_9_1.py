size = 128 * 256
i = 8
t = 24 * 60 ** 2
k = len(range(0, t, 6))
print(t // 6)
print(k)
v = size * i * k / 2 ** 23
print(v)
