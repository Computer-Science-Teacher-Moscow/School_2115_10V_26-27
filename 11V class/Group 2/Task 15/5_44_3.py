def f(x):
    return (x & 87 == 0) <= ((x & 31 != 0) <= (x & A != 0))

for A in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(A)
        break
