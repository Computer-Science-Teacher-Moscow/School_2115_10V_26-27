def f(x):
    return (A % x == 0) <= ((x == A) or (x == 1))

cnt = 0
for A in range(1, 11112):
    if all(f(x) for x in range(1, 15000)):
        cnt += 1
print(cnt)
