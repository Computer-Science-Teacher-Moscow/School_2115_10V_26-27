def f(x):
    P = 22 <= x <= 72
    Q = 42 <= x <= 102
    A = a1 <= x <= a2
    return not (not A and P) or Q


ox = [dx for x in (22, 72, 42, 102) for dx in (x - 0.0001, x, x + 0.0001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append((a2 - a1))
print(round(min(res)))
# print(res)
