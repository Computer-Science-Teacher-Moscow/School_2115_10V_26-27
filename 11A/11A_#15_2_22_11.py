def f(x):
    P = 131 <= x <= 215
    Q = 36 <= x <= 384
    R = 243 <= x <= 355
    A = a1 <= x <= a2
    return (not (Q <= (P or R))) <= ((not A) <= (not Q))

ox = [dx for x in (131, 215, 36, 384, 243, 355) for dx in (x - 0.0001, x, x + 0.0001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1<=a2 and all(f(x) for x in ox):
            res.append(a2-a1)
print(round(min(res)))
