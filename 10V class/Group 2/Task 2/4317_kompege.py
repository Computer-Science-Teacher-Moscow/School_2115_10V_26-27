def num_base5(n):
    res = []
    while n:
        r = n % 5
        res.append(str(r))
        n //= 5
    return ''.join(res[::-1])


def get_r(n):
    r = num_base5(n)
    if int(r[-1]) % 2 == 0:
        r += '2'
    else:
        r = '2' + r + '3'
    return int(r, 5)


# print(get_r(13))

for N in range(1_000_000, 0, -1):
    if get_r(N) < 1000:
        print(N)
        break
