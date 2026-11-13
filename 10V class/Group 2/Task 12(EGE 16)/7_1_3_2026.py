def f(n):
    if n == 2022: return 87687687
    return (n-1) * f(n - 1)



print((f(2024) / 7 - f(2023))/f(2022))
