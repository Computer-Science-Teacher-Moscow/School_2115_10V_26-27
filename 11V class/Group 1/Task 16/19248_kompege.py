# from functools import lru_cache
#
#
# @lru_cache(10)
# def f(n):
#     if n < 5: return n
#     return 2 * n * f(n - 4)
#
#
# for i in range(4, 13767): f(i)
#
# print((f(13766) - 9 * f(13762)) // f(13758))

def f(n):
    if n == 13758: return 87657
    return 2 * n * f(n - 4)

print((f(13766) - 9 * f(13762)) // f(13758))