from functools import lru_cache


@lru_cache(30)
def g(n):
    if n < 8: return 3 * n
    return g(n - 3) + 2


def f(n):
    return 3 * (g(n - 2) + 5)


for i in range(7, 12346): g(i)

print(f(12345))
