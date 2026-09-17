def f(x):
    P = x in {1, 12}
    Q = x in {12, 13, 14, 15, 16}
    A = x in a
    return (not A) <= (not P and not Q)



a = set()
for x in range(1, 1000):
    if f(x) == False:
        a.add(x)
print(len(a), a)

