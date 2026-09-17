def get_r(n):
    r = f'{n:b}'
    if n % 2 == 0:
        r = r.replace('0', '1')
    else:
        r = '1' + r[1:].replace('1', '00')
    return int(r, 2)


# print(get_r(12))

res = []
for N in range(1, 1000):
    R = get_r(N)
    if R <= 600:
        res.append((R,N))

# res.sort(reverse=True)
print(max(res)[1])