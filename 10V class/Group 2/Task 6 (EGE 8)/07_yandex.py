# https://education.yandex.ru/ege/inf/task/dcc55612-3a7e-44d1-8205-9ca718f8786f

# from itertools import product
#
# cnt = 0
# for pr in product('0123456', repeat=5):
#     w = ''.join(pr)
#     if w[0] == '0':
#         continue
#     if w.count('6') == 1 and '00' not in w and '11' not in w and '22' not in w and '33' not in w and '44' not in w and '55' not in w and '66' not in w:
#         cnt +=1
#         print(w)
#
# print('------')
# print(cnt)

from itertools import product

cnt = 0
for pr in product('0123456', repeat=5):
    w = ''.join(pr)
    if w[0] == '0':
        continue
    print(w, [x * 2 not in w for x in w])
    if w.count('6') == 1 and all(x * 2 not in w for x in w):
        cnt += 1
        # print(w)

print('------')
print(cnt)
