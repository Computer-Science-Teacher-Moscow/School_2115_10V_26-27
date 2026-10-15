def f(x):
    return x & 47 == 0 or ((x & 13 == 0) <= (not (x & A == 0)))

for A in range(1, 1000):
    if all (f(x) for x in range(1, 10000)):
        print(A)
        break
