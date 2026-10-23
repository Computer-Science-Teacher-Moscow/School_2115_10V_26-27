# https://education.yandex.ru/ege/inf/task/dcc55612-3a7e-44d1-8205-9ca718f8786f

from itertools import product

cnt = 0
for pr in product('0123456', repeat=5):
    w = ''.join(pr)
    # w1 = w
    # print(w, [x + x not in w for x in w])
    if w[0] != '0' and w.count('6') == 1 and all(x + x not in w for x in w):
        cnt += 1
        print(w)
print('-----')
print(cnt)
