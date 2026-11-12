def f(n):
    if n == 2020: return 345454
    return n + 1 + f(n - 2)

print(f(2024) - f(2020))