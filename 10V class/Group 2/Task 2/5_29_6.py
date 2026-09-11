def num_base3(n):
    res = []
    while n:
        # r = n % 3
        n, r = divmod(n, 3)
        res.append(str(r))
        # n //= 3
    return ''.join(res[::-1])

def get_r(n):
    r = num_base3(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r += num_base3(n % 3 * 4)
    return int(r, 3)

for n in range(100, 1, -1):
    R = get_r(n)
    if R < 199:
        print(n, R)
        break

