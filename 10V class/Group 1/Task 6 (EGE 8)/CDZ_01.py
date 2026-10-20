# 8
# from itertools import product
#
# cnt = 0
# for pr in product('ВИШНЯ', repeat=6):
#     w = ''.join(pr)
#     if w[0] != 'Ш' and w[-1] not in ('И', 'Я')  and w.count('В') <= 1:
#         cnt += 1
#         print(w)
#
# print('----')
# print(cnt)

# # 5
# from itertools import product
#
# word = ''.join(sorted('АЛГОРИТМ'))
# print(word)
# i = 0
# cnt = 0
# for pr in product(word, repeat=5):
#     w = ''.join(pr)
#     i += 1
#     if i % 2 == 0 and w[0] != 'Л' and w.count('И') >= 2:
#         cnt += 1
#         # print(i, w)
# print('-----')
# print(cnt)

from math import ceil, log2

k = 510 + 10
i = ceil(log2(k))
print(i)