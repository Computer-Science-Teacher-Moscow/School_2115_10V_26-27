# size = 480 * 768
# v = 405 * 2 ** 13
# for i in range(1, 100):
#     if size * (i + i // 2 + i % 2) > v:
#         print(2 ** (i - 1))
#         break
size = 315 * 3072
v = 735 * 2 ** 13
for i in range(1, 100):
    if size * i > v:
        print(2 ** (i - 1) + 1)
        break

