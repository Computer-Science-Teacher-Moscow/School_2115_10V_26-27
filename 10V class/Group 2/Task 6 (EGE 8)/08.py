from itertools import product

word = ''.join(sorted('ПРОБНИК'))

last_i= 0
for i,pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if w.count('О') == 3 and len(set(w)) == 4:
        # print(i, w)
        last_i = i
print(last_i)
