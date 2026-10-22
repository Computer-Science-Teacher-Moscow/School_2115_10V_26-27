from itertools import product

word = ''.join(sorted('АВЛОС'))

cnt = 0
for pr in product(word, repeat=4):
    w = ''.join(pr)
    cnt += 1
    if w[0] == 'Л':
        print(cnt)
        break