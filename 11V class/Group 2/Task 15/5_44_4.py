def f(x):
    return (((x & 13 != 0) or (x & 39 == 0)) <= (x & 13 != 0)) or ((x & A == 0) and (x & 13 == 0))


for A in range(1000, 0, -1):
    if all(f(x) for x in range(1, 10000)):
        print(A)
        break

