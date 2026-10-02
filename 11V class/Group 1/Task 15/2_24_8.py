def f(x):
    P = x in {1, 2, 3, 4, 5, 6}
    Q = x in {3, 5, 15}
    A = x in a
    return (not A) <= ((not P and Q) or not Q)

a = set()
for x in range(1, 1000):
    if f(x) == False:
        a.add(x)
print(len(a), a)

