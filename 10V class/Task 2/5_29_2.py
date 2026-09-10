def get_r(n):
    r = bin(n)[2:]
    # print(r)
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    # print(r)
    return int(r,2)


# R = get_r(5)
# print(R)
res = []
for num in range(1, 13):
    res.append(get_r(num))
# res.sort()
print(max(res))
print(res)
