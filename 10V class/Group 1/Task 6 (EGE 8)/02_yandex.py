from itertools import product

word = ''.join(sorted("КОФЕ"))
print(sorted("КОФЕ"), word)

res = []
cnt = 0
for pr in product(word, repeat=5):
    w = ''.join(pr)
    cnt += 1
    # print(cnt, w.lower())
    if w.count('О') == 1 and 'КО' not in w and 'ОК' not in w and 'ФО' not in w and 'ОФ' not in w:
        res.append(cnt)
        print(cnt, w)
print('----')
print(res[0] + res[-1])
