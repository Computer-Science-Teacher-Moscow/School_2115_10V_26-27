# def f(n):
#     if n == 56: return 45345
#     return f(n + 2) + n + 3
#
#
# print(f(52) - f(56))

from functools import lru_cache


@lru_cache(5)
def f(n):
    if n >= 7000: return n
    return f(n + 2) + n + 3


for i in range(7000, 52, -1): f(i)

print(f(52) - f(56))
