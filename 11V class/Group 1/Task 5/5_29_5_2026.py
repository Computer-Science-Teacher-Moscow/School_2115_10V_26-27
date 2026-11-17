# def num_base3(n):
#     res = []
#     if n == 0: return 0
#     while n:
#         r = n % 3
#         res.append(str(r))
#         n //= 3
#     return ''.join(res[::-1])

# def num_base3(n):
#     res = []
#     if n == 0: return 0
#     while n:
#         n, r = divmod(n, 3)
#         res.append(str(r))
#     return ''.join(res[::-1])
#
# print(num_base3(12))

# def num_base(n, cs):
#     res = []
#     if n == 0: return 0
#     while n:
#         n, r = divmod(n, cs)
#         res.append(str(r))
#     return ''.join(res[::-1])
#
# print(num_base(12, 4))

from string import printable

# def num_base(n, cs):
#     res = []
#     if n == 0: return 0
#     while n:
#         n, r = divmod(n, cs)
#         res.append(printable[r])
#     return ''.join(res[::-1])
#
# # print(printable)
# print(num_base(154645, 21))

from string import printable as a

# def num_base(n, cs):
#     if n == 0: return 0
#     s = ''
#     while n:
#         n, r = divmod(n, cs)
#         s = a[r] + s
#     return s
# #
# print(num_base(5465, ))
# # # print(printable)
# print(num_base(154645, 21))

from string import printable as a

def num_base(n, cs):
    if n == 0: return 0
    s = ''
    while n:
        n, r = divmod(n, cs)
        s = a[r] + s
    return s

def get_r(n):
    r = num_base(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += num_base((n % 3) * 5, 3)
    return int(r, 3)

print(get_r(11))
print(get_r(12))

res = []
for num in range(1, 1000):
    R = get_r(num)
    if R > 133:
        res.append(R)
print(min(res))
print(res)