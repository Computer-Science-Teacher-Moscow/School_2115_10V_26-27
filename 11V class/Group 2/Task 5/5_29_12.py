from string import printable as a


def num_base(n, cs):
    res = ''
    while n:
        n, r = divmod(n, cs)
        res = a[r] + res
    return res


def get_r(n):
    r = num_base(n, 8)
    if r[0] == '5':
        r = r.replace('2', '#').replace('1', '2').replace('#', '1') + '11'
    else:
        r += '10'
        r = '2' + r[1:]
    return int(r, 8)


res = []
for N in range(5, 10000):
    if (R := get_r(N)) < 1354:
        res.append((R, N))
print(sorted(res, reverse=1))
print(max(res))
