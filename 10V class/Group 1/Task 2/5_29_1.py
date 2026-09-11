def get_r(n):
    r = bin(n)[2:]
    # print(r)
    if n % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    #     print(r)
    return int(r, 2)

res = []
for num in range(1, 100):
    R = get_r(num)
    if R > 52:
        res.append(R)
print(min(res))
