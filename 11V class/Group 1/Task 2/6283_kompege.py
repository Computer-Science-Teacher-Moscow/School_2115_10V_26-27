from itertools import permutations, product


def f(x, y, w, z):
    return not (not (x <= (not w)) and z) and not (w <= z) and (x <= (not z))


res = []
for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    table = ((1, 0, a1, 0), (1, 0, a2, a3), (a4, 1, a5, 1))
    if len(set(table)) == 3:
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1, 0, 0]:
                res.append(''.join(per))
                print(*per, sep='')
print('----')
print(len(set(res)))
