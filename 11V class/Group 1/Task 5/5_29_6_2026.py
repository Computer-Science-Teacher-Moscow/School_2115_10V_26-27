def num_base3(n):
    res = []
    while n:
        n, r = divmod(n, 3)
        res.append(str(r))
    return ''.join(res[::-1])

def get_r(n):
    r = num_base3(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r += num_base3((n % 3) * 4)
    return int(r, 3)

# print(get_r(11))
# print(get_r(12))


# for num in range(1000, 0, -1):
#     R = get_r(num)
#     if R < 199:
#         print(num)
#         break

for num in range(1, 1000):
    R = get_r(num)
    if R < 199:
        print(num)
