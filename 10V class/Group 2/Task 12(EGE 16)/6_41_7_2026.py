from functools import lru_cache


@lru_cache(5000)
def g(n):
    if n < 28: return 3 * n  - 4
    return g(n - 5 ) - 15


@lru_cache(5000)
def f(n):
    if n >=31054: return 3 * (g(n - 2) - 15)
    return f(n + 4) + 3020

for i in range(27, 31054): g(i)
for i in range(31054, 14, -1): f(i)

print(f(15))


