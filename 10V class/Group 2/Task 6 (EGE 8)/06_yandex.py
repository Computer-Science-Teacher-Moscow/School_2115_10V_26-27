# https://education.yandex.ru/ege/inf/task/c66a1998-8288-47b1-8172-eb5509452f3b

from itertools import product

cnt = 0
for pr in product('0123456789AB', repeat=7):
    w = ''.join(pr)
    if w[0] == '0':
        continue
    for c in '0369':
        w = w.replace(c, '#')
    for c in '124578AB':
        w = w.replace(c, '*')
    if w in ('#*#*#*#', '*#*#*#*'):
        cnt += 1

print(cnt)
