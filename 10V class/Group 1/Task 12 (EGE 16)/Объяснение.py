from sys import getsizeof
# setrecursionlimit(1050)
from functools import lru_cache

@lru_cache(1)
def f(n):
    # print(f'f({n})')
    if n == 1: return 1
    return f(n - 1) * n

for i in range(1, 1501): f(i)

a= f(1500)
print(f(1500))
print(getsizeof(a))