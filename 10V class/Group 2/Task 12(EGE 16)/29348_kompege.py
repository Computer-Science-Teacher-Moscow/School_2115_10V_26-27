# 29348
from functools import lru_cache
from fractions import Fraction # Fraction - переводит действиетльное число в конечную дробь (рациональное число)

@lru_cache(7)
def f(n):
    if n < 10: return 1
    return (n + 3) * f(n - 3)


for i in range(9, 247564):f(i)

print((Fraction(f(247563) , 519) - 477 * f(247560)) // f(247557))
