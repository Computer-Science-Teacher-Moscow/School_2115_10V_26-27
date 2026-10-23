# from sys import setrecursionlimit # Очень плохая практика
#
# setrecursionlimit(4000)

# from functools import lru_cache
#
# @lru_cache(4)
# def f(n):
#     if n == 1: return 1
#     return n * f(n - 1)
#
# for i in range(1, 3239): f(i)
#
#
# print((f(3238) // 2 + f(3237)) // f(3236))

def f(n):
    if n == 3236: return 654656
    return n * f(n - 1)

print((f(3238) // 2 + f(3237)) // f(3236))
