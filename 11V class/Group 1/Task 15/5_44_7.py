def f(x):
    B = 160 <= x <= 180
    return B <= ((x % 35 == 0) <= (x % A == 0))


cnt = 0
for A in range(10000, 0, -1):
    if all(f(x) for x in range(1, 10000)):
        cnt += 1
print(cnt)
