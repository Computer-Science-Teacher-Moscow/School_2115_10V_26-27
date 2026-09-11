def num_base3(n):
    res = []
    while n:
        # r %= 3
        n, r = divmod(n, 3)
        res.append(str(r))
        # n //= 3
    return ''.join(res[::-1])


def get_r(n):
    r = num_base3(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += num_base3(n % 3 * 5)
    return int(r, 3)


# print(get_r(11))
# print(get_r(12))

res = []
for n in range(1, 300):
    if (R:=get_r(n)) > 133:
        res.append(R)
print(min(res))
