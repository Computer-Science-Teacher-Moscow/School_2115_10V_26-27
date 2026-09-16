def get_r(n):
    r = f'{n:b}'
    if n % 2 == 0:
        r = r.replace('0', '1')
    else:
        r = r[0] + r[1:].replace('1', '00')
    return int(r, 2)


# print(get_r(12))

res = []
for N in range(1000, 0, -1):
    R = get_r(N)
    if R <= 600:
        res.append((N,R))
# res.sort()
print(res)
print(max(res, key = lambda x: (x[1], x[0]))[0])

