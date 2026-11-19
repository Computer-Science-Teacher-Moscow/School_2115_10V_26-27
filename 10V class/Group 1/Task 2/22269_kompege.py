def num_base5(n):
    res = []
    while n:
        r = n % 5
        res.append(str(r))
        n //= 5
    return ''.join(res[::-1])

def get_r(n):
    r = num_base5(n)
    if r[-1] == '0':
        r = '33' + r.replace('1','#').replace('4','1').replace('#', '4')
    else:
        r += '42'
        r = '3' + r[1:]
    return int(r, 5)

