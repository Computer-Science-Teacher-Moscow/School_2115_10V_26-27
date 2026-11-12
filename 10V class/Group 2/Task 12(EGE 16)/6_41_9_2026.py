from functools import lru_cache


# @lru_cache(5000)
def g(n):
    if n >= 40000: return (n - 7) ** 2
    return 8 + n + g(n + 8)


@lru_cache(5000)
def f(n):
    if n < 40000: return 4 * n + g(n - 5)
    return 2 * n + f(n - 7)


# for i in range(40000, 2026, -1): g(i)
for i in range(39999, 54322): f(i)

print(f(54321))
