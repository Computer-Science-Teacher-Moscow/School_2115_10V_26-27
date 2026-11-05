from functools import lru_cache

@lru_cache(5)
def f(n):
    if n == 1: return 1
    return n * f(n - 1)

for i in range(1, 3039): f(i)

print((f(3038) + 5 * f(3037)) / f(3036))

# def f(n):
#     if n == 3036: return 2
#     return n * f(n - 1)
#
# print((f(3038) + 5 * f(3037)) // f(3036))