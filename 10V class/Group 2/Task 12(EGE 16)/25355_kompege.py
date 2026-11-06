# 25355
from functools import lru_cache


@lru_cache(1000)
def g(n):
    if n >= 248045: return n / 20 + 28
    return g(n + 9) - 4


# @lru_cache(1000)
def f(n):
    if n >= 19: return f(n - 4) + 3580
    return 6 * (g(n - 7) - 36)

for i in range(248045, 672, -1): g(i)
# for i in range(19, 674): f(i)

print(f(673))
