from math import prod

def get_r(n, m):
    rn = [int(x) for x in str(n) if x in ('2', '4', '6', '8')]
    rm = [int(x) for x in str(m) if x in ('2', '4', '6', '8')]
    P1 = prod(rn + rm)
    # print(n, m)
    # print(rn, rm, P1)
    rn1 = [int(x) for x in str(n) if x in ('1', '3', '5', '7', '9')]
    rm1 = [int(x) for x in str(m) if x in ('1', '3', '5', '7', '9')]
    P2 = prod(rn1 + rm1)
    # print(n, m)
    # print(rn1, rm1, P2, P1)
    r = abs(P1 - P2)
    return r

for m in range(1, 100000):
    if get_r(120, m) == 29:
        print(m)
        break

# print(get_r(256, 108))