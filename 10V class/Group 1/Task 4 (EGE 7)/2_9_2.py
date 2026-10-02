from math import ceil

size = 1920 * 1080
i = 11
v_add = 5 * 2 ** 13
t = 24 * 60 ** 2
k = len(range(0, t, 20))
# print(t // 20)
# print(k)
v = ceil((size * i + v_add) * k / 2 ** 23)
print(v)
