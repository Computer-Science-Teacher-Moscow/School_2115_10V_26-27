from itertools import product, permutations


def f(a, b, c, d):
    return (a <= b) and (b <= (not c) and (c == (not d)))


for a1, a2, a3, a4 in product((0, 1), repeat=4):
    tabel = ((1, 1, 0, a1), (a2, 0, 1, 0), (1, 0, a3, 1), (0, a4, 0, 1))
    if len(set(tabel)) == 4:
        for per in permutations('abcd'):
            if [f(**dict(zip(per, row))) for row in tabel] == [1, 1, 1, 1]:
                print(*per, sep='')
