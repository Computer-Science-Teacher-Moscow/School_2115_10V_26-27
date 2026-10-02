def f(x):
    P = x in {2, 4, 6, 8, 10, 12}
    Q = x in {4, 8, 12, 116}
    A = x in a
    return P <= ((Q and not A) <= (not P))


a = set()
for x in range(1, 1000):
    if f(x) == False:
        a.add(x)
print(sum(x for x in a), a)
