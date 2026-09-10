from string import printable

def num_tu_base3(num, base=2):
    res = []
    while num:

        num, r = divmod(num, base)
        # print(divmod(num, base))
        res.append(printable[r])
        # print(printable[r], r)

    return ''.join(res[::-1])

print(printable)
# print(printable[10])
print(num_tu_base3(4088, 5))

# a = 16
# b = 6
# c = -4
# n = a + b + c
# _n1 = a + b - c
# print(a, b, c)
# f = a ** (1 / 3)
# print(f)
# # / деление
# # // целочисленное деление
# # ** возведение в степень
# s = a ** b
# # print(s)
# # ()
# # **
# #  * / (//)
# #  + -
# a = 3 * 2 ** 15 - 4 * 5 ** 2 + 4 ** (1/3)
