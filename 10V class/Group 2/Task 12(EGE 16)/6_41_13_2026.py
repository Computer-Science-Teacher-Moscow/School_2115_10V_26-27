from functools import lru_cache


@lru_cache(5000)
def g(n):
    if n >= 250000: return n // 20 + 45
    return g(n + 9) - 2


@lru_cache(5000)
def f(n):
    if n < 25: return 7 * (g(n - 9) - 40)
    return f(n - 6) + 4137
