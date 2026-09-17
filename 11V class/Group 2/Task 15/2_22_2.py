def f(x):
    P = 3 <= x <= 13
    Q = 12 <= x <= 22
    A = a1 <= x <= a2
    return (A <= P) or Q


ox = [dx for x in (3, 13, 12, 22) for dx in (x - 0.0001, x, x + 0.0001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append((a2 - a1))
print(max(res))
# print(res)
