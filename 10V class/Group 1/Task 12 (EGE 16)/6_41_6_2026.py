from functools import lru_cache


@lru_cache(5000)
def g(n):
    if n >= 301208: return 10 * n + 50
    return g(n + 7) - 21


def f(n):
    if n <= 40: return 3 * (g(n - 2) - 15)
    return f(n - 4) + 3020

for i in range(301209, 39, -1): g(i)

print(f(2026))
