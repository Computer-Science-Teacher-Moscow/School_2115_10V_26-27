# from functools import lru_cache
#
# @lru_cache(50)
def f(n):
    # print(f'f({n})')
    if n < 3: return 2
    if n > 2 and n % 2 == 0: return 2 * f(n - 2) - f(n - 1) + 2
    return 2 * f(n - 1) - f(n - 2) - 2

# for i in range(2,40): f(i)

print(f(40))
