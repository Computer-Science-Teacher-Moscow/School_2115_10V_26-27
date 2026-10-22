from itertools import product

cnt = 0
for pr in product('0123456789', repeat=4):
    w = ''.join(pr)
    print(w, pr)
    # if w[0]!=0 :

print('----')

# https://education.yandex.ru/ege/inf/training/8/task/4?examTaskId=7e0b4dbb-b87d-4f1a-80e3-fdf2a1a50a3e&examTaskNumber=8&categoryId=ed62f12f-ceed-4bde-a9f4-a7418677f2fa&categoryId=cb6e105f-1d6a-43fb-8a80-51dd775a3188&from=main