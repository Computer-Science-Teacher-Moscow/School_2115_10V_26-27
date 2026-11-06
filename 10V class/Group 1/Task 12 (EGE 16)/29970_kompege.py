# 29970_kompege
from functools import lru_cache


@lru_cache(20)
def g(n):
    if n <= 20: return n + 2
    return g(n - 3) + 1


def f(n):
    return 3 * g(n - 3) + 7


for i in range(20, 37811): g(i)

print(f(37811))
