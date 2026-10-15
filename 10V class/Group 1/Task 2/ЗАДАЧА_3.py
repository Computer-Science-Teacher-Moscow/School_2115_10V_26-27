def get_z(n):
    n = str(n)
    S = sum(int(x) for x in n) # 12584
    M = int(max(n)) + int(min(n))
    L = int(n[0])
    R = int(n[-1])
    P1 = S - L
    P2 = M - R
    Z = str(P1) + str(P2)
    # Z = f'{P1}{P2}' #Как вариант
    # print(S, M, L, R, P1, P2, Z)
    return Z

# print(get_z(12502))
for num in range(99999, 9999, -1):
    if get_z(num) == '222':
        print(num)
        break