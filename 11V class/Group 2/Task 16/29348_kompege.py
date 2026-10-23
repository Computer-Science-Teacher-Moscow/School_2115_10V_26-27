from functools import lru_cache
from fractions import Fraction


@lru_cache(100)
def f(n):
    if n < 10: return 1
    return (n + 3) * f(n - 3)


for i in range(9, 247564): f(i)

print((Fraction(f(247563) , 519) - 477 * f(247560)) / f(247557))

# print(Fraction(0.25))

