def num_base3(n):
    s = ''
    while n:
        r = n % 3
        s = str(r) + s
        n //= 3
    return s

def get_r(n):
    r = num_base3(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += num_base3(sum(int(x) for x in r) * 2)
    return int(r, 3)

#print(get_r(8))
#print(get_r(9))

res = []
for num in range(3, 1000):
    R = get_r(num)
    if R % 2 != 0 and R > 520:
        res.append(R)
print(res)
print(min(res))

