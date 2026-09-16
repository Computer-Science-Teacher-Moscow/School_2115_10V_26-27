def get_r(n: int) -> int:
    # r = bin(n)[2:]
    r = f'{n:b}'
    r += r[-1]
    if f'{n:b}'.count('1') % 2 == 0:
        r += '0'
    else:
        r += '1'
    # r += '0' if r.count('1') % 2 == 0 else '1'
    # r += ('1', '0')[r.count('1') % 2 == 0]
    if r.count('1') % 2 == 0:
        r += '0'
    else:
        r += '1'
    return int(r, 2)

for N in range(1,100):
    R = get_r(N)
    if R > 136:
        print(N)
        break
