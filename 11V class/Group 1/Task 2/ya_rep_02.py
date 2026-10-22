from itertools import permutations, product


def f(x, y, w, z):
    return (y == (not w)) <= (not (w and (x == (x or (w <= z)))))


for a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 in product((0, 1), repeat=10):
    table = ((a1, a2, 1, 1), (a3, a4, 1, a5), (a6, 1, a7, 1), (1, a8, a9, a10))
    if len(set(table)) == 4:
        for per in permutations('xywz'):
            if [f(**(dict(zip(per, row)))) for row in table] == [0, 0, 0, 1]:
                print(*per, sep='')
