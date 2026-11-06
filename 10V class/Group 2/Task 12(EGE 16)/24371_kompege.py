from functools import lru_cache

@lru_cache(20)
def g(n):
    if n < 100: return n
    return f(n-3) + 1

def f(n):
    return g(n-2)

for i in range(99, 5000): g(i)

print(f(5000))