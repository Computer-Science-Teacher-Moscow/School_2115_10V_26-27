from functools import lru_cache

def f(n):
    if n >= 21: return f(n - 8) + 1095
    return 10 * (g(n - 7) - 36)


@lru_cache(1000)
def g(n):
    if n >= 22560: return n / 23 + 33
    return g(n + 11) - 4

for i in range(22560, 547, -1): g(i)

print(f(548))