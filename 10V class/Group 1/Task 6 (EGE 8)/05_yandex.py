# https://education.yandex.ru/ege/inf/task/cd99a6f6-d378-42ef-9673-9d6b0b761f3f

from itertools import product

word = ''.join(sorted('ФЕВРАЛЬ'))

i = 0
for pr in product(word, repeat=6):
    w = ''.join(pr)
    i += 1
    w = w.replace('Е', '#').replace('А', '#')
    if '#' not in w:
        print(i)
        break
