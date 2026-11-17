def get_r(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    return int(r, 2)

# print(get_r(4))
# print(get_r(5))

res = []
for num in range(1, 13):
    res.append(get_r(num))

print(max(res))