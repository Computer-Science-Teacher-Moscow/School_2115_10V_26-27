# def num_base8(n):
#     res = []
#     while n:
#         r = n % 8
#         res.append(str(r))
#         n = n // 8
#     return ''.join(res[::-1])

def get_r(n):
    r = oct(n)[2:]
    if r[0] == '5':
        r = r.replace('1', '#')
        r = r.replace('2', '1')
        r = r.replace('#', '2')
        r += '11'
    else:
        r += '10'
        r = '2' + r[1:]
    return int(r, 8)

for N in range(1000, 1, -1):
    R = get_r(N)
    if R < 1354:
        print(N)
        break

