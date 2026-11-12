from functools import lru_cache


@lru_cache(5000)
def g(n):
    if n <= 9: return 3 * n
    return g(n - 4) + 2


def f(n):
    return g(n - 1) + g(n - 3)


for i in range(9, 42999): g(i)


print(f(42999))
