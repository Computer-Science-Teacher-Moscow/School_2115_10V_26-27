def get_r(n):
    r = f'{n:b}'
    r += r[-1]
    if f'{n:b}'.count('1') % 2 == 0:
        r += '0'
    else:
        r += '1'
    # if r.count('1') % 2 == 0:
    #     r += '0'
    # else:
    #     r += '1'
    r += str(r.count('1') % 2) # как вариант
    return int(r, 2)

for N in range(1, 100):
    R = get_r(N)
    if R > 136:
        print(N)
        break
