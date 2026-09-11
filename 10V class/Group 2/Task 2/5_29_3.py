def get_r(n):
    r  = bin(n)[2:]
    for _ in range(2):
        r += str(r.count('1') % 2)
    return int(r, 2)

res = []
for num in range(1, 500):
    # R = get_r(num)
    if (R:=get_r(num)) > 75:
        res.append(R)
print(res)
# print(min(res))