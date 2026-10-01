def get_r(n):
    r = f'{n:b}'
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += f'{(n % 3) * 3:b}'
    return int(r, 2)

# print(get_r(6))
# print(get_r(4))
for N in range(1, 3000):
    R = get_r(N)
    if 120 <= R <= 140:
        print(R, N)

# Ответ 31