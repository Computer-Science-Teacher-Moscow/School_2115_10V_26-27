def get_r(n):
    # r = bin(n)[2:]
    r = f'{n:b}'
    if n % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    return int(r, 2)


# print(get_r(13))

res = []
for num in range(1, 1000):
    R = get_r(num)
    if R > 52:
        res.append(R)
print(res)
print(min(res))
