from itertools import product

word = ''.join(sorted('МУЖЧИНА'))

cnt = 0
for i,pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if i % 2 == 0 and w[0] != 'Ж' and w.count('Ч') <= 1:
        cnt += 1
        #print(w)
print(cnt)
