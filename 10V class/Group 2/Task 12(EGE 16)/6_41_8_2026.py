from functools import lru_cache


@lru_cache(5000)
def g(n):
    if n >= 265_182: return n / 4 + 12
    return 18 + g(n + 38)

@lru_cache(5000)
def f(n):
    if n < 30: return 4 * (g(n - 15) - 30)
    return f(n - 5) + 5123

for i in range(265_182, 2026, -1): g(i)
for i in range(29, 2027, 1): f(i)

print(f(2026))


