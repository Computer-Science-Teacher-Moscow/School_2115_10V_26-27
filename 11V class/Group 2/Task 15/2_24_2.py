def f(x):
    P = 13 <= x <= 21
    Q = 23 <=x <= 35
    R = 28 <= x <= 38
    A = a1 <= x <= a2
    return (not(Q <= (P or R))) <= ((not A)<= (not Q))

ox = [dx for x in (13, 21, 23, 35, 28, 38) for dx in (x - 0.00001, x, x + 0.00001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1<=a2 and all(f(x) for x in ox):
            res.append(a2-a1)
print(round(min(res)))

