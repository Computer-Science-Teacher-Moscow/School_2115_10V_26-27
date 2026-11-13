from functools import lru_cache


@lru_cache(5000)
def g(n):
    if n < 40: return 30 * n + 24
    return g(n - 3) - 20


@lru_cache(5000)
def f(n):
    if n > 250194: return 3 * (g(n - 5) + 27)
    return f(n+8) + 1050

for i in range(39, 250195): g(i)
for i in range(250195, 9, -1): f(i)

print(f(10))

