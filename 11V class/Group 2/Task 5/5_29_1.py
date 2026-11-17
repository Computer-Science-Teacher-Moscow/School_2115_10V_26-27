# def num_base3(n):
#     res = []
#     while n:
#         r = n % 3
#         res.append(str(r))
#         n //= 3
#     return ''.join(res[::-1])
#
#
# print(num_base3(345))

# def num_base(n, cs):
#     res = []
#     while n:
#         n, r = divmod(n, cs)
#         res.append(str(r))
#     return ''.join(res[::-1])
#
#
# print(num_base(345, 9 ))

# from string import printable as a
#
# def num_base(n, cs):
#     res = []
#     while n:
#         n, r = divmod(n, cs)
#         res.append(a[r])
#     return ''.join(res[::-1])
#
#
# print(num_base(34565445, 26 ))
# from string import printable as a
#
# def num_base(n, cs):
#     res = ''
#     while n:
#         n, r = divmod(n, cs)
#         res = a[r] + res
#     return res
#
#
# print(num_base(5646546, 26 ))

def num_base3(n):
    res = []
    if n == 0: return '0'
    while n:
        n, r = divmod(n, 3)
        res.append(str(r))
    return ''.join(res[::-1])

def get_r(n):
    r = num_base3(n)
    if r[-2] == r[-1]:
        r = num_base3(n -1) + '20'
    else:
        r = num_base3(n + 1) + '12'
    return int(r, 3)

print(get_r(8))
print(get_r(10))

res = []
for N in range(5, 10000):
    if 99 < (R:= get_r(N)) < 1000:
        res.append((R, N))
print(max(res))
