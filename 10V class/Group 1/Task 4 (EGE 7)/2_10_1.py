k = 2
nu = 48000
i = 24
v = 288 * 2 ** 23
t = v / (k * nu * i) / 60
print(round(t))