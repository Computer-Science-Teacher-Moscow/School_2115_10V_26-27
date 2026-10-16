# from itertools import product  # импортируем перестановки с повторениями
#
# word = ''.join(sorted('ВЕСНА'))
# # print(word)
# cnt = 0
# for pr in product(word, repeat=4):
#     cnt += 1
#     w = ''.join(pr)
#     if 'Е' not in w and 'АА' not in w:
#         print(cnt, w)
#         break

# from itertools import product  # импортируем перестановки с повторениями
#
# word = ''.join(sorted('ВЕСНА'))
#
# for i, pr in enumerate(product(word, repeat=4), 1):
#     w = ''.join(pr)
#     if 'Е' not in w and 'АА' not in w:
#         print(i, w)
#         break

cnt = 0
word = ''.join(sorted('ВЕСНА'))
for x1 in word:
    for x2 in word:
        for x3 in word:
            for x4 in word:
                w = x1 + x2 + x3 + x4
                cnt += 1
                if 'Е' not in w and 'АА' not in w:
                    print(cnt, w)
                    exit()
