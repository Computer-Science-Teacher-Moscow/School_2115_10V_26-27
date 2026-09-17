def f(x):
    P = 15 <= x <= 60
    Q = 15 <= x <= 30
    A = a1 <= x <= a2
    return (not Q or P) and A


ox = [dx for x in (15, 60, 30) for dx in (x - 0.0001, x, x + 0.0001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and not all(f(x) for x in ox):
            res.append((a2 - a1))
print(round(min(res)))
# print(res)
