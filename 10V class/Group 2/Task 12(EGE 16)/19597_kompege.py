# 19597

def f(n):
    if n < 15: return 4
    if n % 3 == 0: return f(2 * n // 3) + n - 1
    return f(n - 1) + 3

for num in range(1000, 0, -1):
    F = f(num)
    if F == 251:
        print(num)
        break

