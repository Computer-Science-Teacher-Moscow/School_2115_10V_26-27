# from sys import setrecursionlimit
# setrecursionlimit(1005)
from functools import lru_cache

@lru_cache(None)
def f(n):
    # print(f'f({n})')
    if n == 1: return 1
    return f(n - 1) * n

for i in range(1,1007): f(i)
print(f(1006))
