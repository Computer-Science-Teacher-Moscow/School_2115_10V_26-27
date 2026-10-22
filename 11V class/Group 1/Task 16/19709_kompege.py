# from functools import lru_cache
#
# @lru_cache(5)
# def f(n):
#     if n == 1: return 1
#     return n ** 3 + f(n - 1)
#
# for i in range(1, 2026): f(i)
#
# print(f(2025)- f(2022))


def f(n):
    if n == 2022: return 345345
    return n ** 3 + f(n - 1)

print(f(2025)- f(2022))