from itertools import product

cnt = 0
for pr in product('0123456789AB', repeat=5):
    w = ''.join(pr)
    if w[0] != '0' and w.count('7') == 1 and sum(int(x, 12) > 8 for x in w) <=3:
        cnt += 1
        print(w)

print(cnt)

