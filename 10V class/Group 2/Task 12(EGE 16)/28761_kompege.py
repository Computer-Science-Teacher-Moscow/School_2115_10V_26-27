# 28761
# from functools import lru_cache
#
# @lru_cache(100)
# def f(n):
#     if n < 10: return 3
#     return (n + 4) * f(n - 5)
#
# for i in range(9, 257488): f(i)
#
#
# print((f(257487) // 683 + 67 * f(257477)) // f(257472))

def f(n):
    print(f'f({n})')
    if n == 257472: return 2
    return (n + 4) * f(n - 5)


print((f(257487) // 683 + 67 * f(257477)) // f(257472))