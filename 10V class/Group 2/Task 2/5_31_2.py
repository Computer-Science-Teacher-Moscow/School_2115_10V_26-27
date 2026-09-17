def num_to_base3(n):
    res = []
    while n:
        r = n % 3
        res.append(str(r))
        n //= 3
    return ''.join(res[::-1])

def get_r(n):
    r = num_to_base3(n)
    # print(r)
    r += str(sum(int(x) for x in r) % 3)
    r += str(sum(int(x) for x in r) % 3)
    # print(r)
    return int(r, 3)

# print(get_r(8))

for N in range(1000, 0, -1):
    R = get_r(N)
    if R <= 905:
        print(N)
        break

