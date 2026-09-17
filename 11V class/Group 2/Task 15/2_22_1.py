def f(x):
    P = 2 <= x <= 10
    Q = 6 <= x <= 14
    A = a1 <= x <= a2
    return (A <= P) or Q


ox = [dx for x in (2, 10, 6, 14) for dx in (x - 0.0001, x, x + 0.0001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append((a2 - a1, a1, a2))
print(max(res))
# print(res)
