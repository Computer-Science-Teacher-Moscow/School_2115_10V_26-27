from itertools import product # импортируем функцию перестановок с повторениями
word = ''.join(sorted('ВЕСНА'))
for i, pr in enumerate(product(word, repeat = 4), 1):
    w = ''.join(pr)
    if 'Е' not in w and 'АА' not in w:
        print(i, w)
        break

# cnt = 0
# word = ''.join(sorted('ВЕСНА'))
# print(word)
# for x1 in word:
#     for x2 in word:
#         for x3 in word:
#             for x4 in word:
#                 cnt += 1
#                 w = x1 + x2 + x3 + x4
#                 if 'Е' not in w and 'АА' not in w:
#                     print(cnt, w)
#                     exit()


