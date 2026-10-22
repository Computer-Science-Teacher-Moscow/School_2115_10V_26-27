from itertools import permutations, product


def f(x, y, w, z):
    return (w == z) or (not (y <= w)) or (not x)


for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    table = ((0, 0, 1, a1), (a2, 1, 1, a3), (0, a4, a5, 0))
    if len(set(table)) == 3:
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
                print(*per, sep='')
