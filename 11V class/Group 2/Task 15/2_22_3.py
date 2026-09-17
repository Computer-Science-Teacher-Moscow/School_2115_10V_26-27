def f(x):
    P = 3 <= x <= 38
    Q = 21 <= x <= 57
    A = a1 <= x <= a2
    return (Q <= P) <= (not A)


ox = [dx for x in (3, 38, 21, 57) for dx in (x - 0.0001, x, x + 0.0001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append((a2 - a1))
print(round(max(res)))
# print(res)
