def f(x):
    P = 25 <= x <= 42
    Q = 1 <= x <= 98
    A = a1 <= x <= a2
    return Q <= ((not P and Q) <= A)


ox = [dx for x in (25, 42, 1, 98) for dx in (x - 0.0001, x, x + 0.0001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append((a2 - a1))
print(round(min(res)))
# print(res)
