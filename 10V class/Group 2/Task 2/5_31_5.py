def num_to_base5(n):
    res = []
    if n == 0:
        res.append('0')
    while n:
        r = n % 5
        res.append(str(r))
        n //= 5
    return ''.join(res[::-1])


def get_r(n):
    r = num_to_base5(n)
    if n % 2 == 0:
        r += num_to_base5(int(r[-1]) * 3)
    else:
        r = r[-1] + r[1:-1] + r[0] + '1'
    r = r.lstrip('0')
    return r




for N in range(1, 10000):
    R = get_r(N)
    # print(R)
    if R.count('0') == 4:
        print(N)
        break


