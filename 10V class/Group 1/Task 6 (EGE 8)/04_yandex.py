# https://education.yandex.ru/ege/inf/task/155cc502-089b-4c59-bb9f-effe2bcbfaef

from itertools import product, repeat

word = ''.join(sorted('ЙТИОАВ'))
print(word)

cnt = 0
for pr in product(word, repeat=6):
    w = ''.join(pr)
    for char in 'ВЙТ':
        w = w.replace(char, '#')
    if '##' in w:
        cnt += 1
        print(w)
print('----' * 20)
print(cnt)
