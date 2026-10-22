from itertools import permutations, product

def f(x, y, w, z):
    return ((x == (not y)) <= (not(w <= x))) or (not z)

for a1, a2, a3, a4, a5 in product((0,1), repeat=5):
    table = ((a1, 0,1,0),(0,a2,a3,0),(a4,1,1,a5))
    if len(set(table)) == 3:
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
                print(*per)