from itertools import product

word = ''.join(sorted('МУЖЧИНА'))

i = 0
cnt = 0
for pr in product(word, repeat=6):
    w = ''.join(pr)
    i += 1
    if i % 2 == 0 and w[0] != 'Ж' and w.count('Ч') <= 1:
        cnt +=1
        print(i, w)
print('----')
print(cnt)
