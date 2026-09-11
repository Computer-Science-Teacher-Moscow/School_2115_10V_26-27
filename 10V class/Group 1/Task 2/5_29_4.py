def get_r(n):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r += '0'
        r= '10' + r[2:]
    else:
        r += '1'
        r = '11' + r[2:]
    return int(r, 2)

# print(get_r(6))
# print(get_r(4))

for num in range(1,100):
    if get_r(num) >= 16:
        print(num)
        break





