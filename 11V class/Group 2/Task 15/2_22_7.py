def f(x):
    P = 10 <= x <= 80
    Q = 30 <= x <= 50
    A = a1 <= x <= a2
    return A <= (P and not Q)


ox = [dx for x in (10, 80, 30, 50) for dx in (x - 0.0001, x, x + 0.0001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append((a2 - a1))
print(round(max(res)))
# print(res)
