from functools import lru_cache

@lru_cache(50)
def f(n):
    print(f'f({n})')
    if n <= 2: return 1
    return f(n - 1) + f(n-2)

# for i in range(1,1007): f(i)
print(f(50))
