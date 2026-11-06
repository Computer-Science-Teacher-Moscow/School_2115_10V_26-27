# 18931 Решить руками
from functools import lru_cache

@lru_cache(20)
def f(n):
    if n <= 3: return n - 1
    if n % 2 == 0: return f(n - 2) + n // 2 - f(n - 4)
    return f(n - 1) * n + f(n - 2)

for i in range(3, 4965): f(i)

print(f(4952) + 2 * f(4958) + f(4964))
