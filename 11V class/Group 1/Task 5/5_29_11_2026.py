def num_base3(n):
    res = []
    while n:
        n, r = divmod(n, 3)
        res.append(str(r))
    return ''.join(res[::-1])


def get_r(n):
    r = num_base3(n)
    if r[-2] == r[-1]:
        r = num_base3(n - 1) + '20'
    else:
        r = num_base3(n + 1) + '12'
    return int(r, 3)

# print(get_r(8))
# print(get_r(10))

res = []
for num in range(3, 10000):
    R = get_r(num)
    if 99 < R < 1000:
        res.append((R, num))
print(max(res))

