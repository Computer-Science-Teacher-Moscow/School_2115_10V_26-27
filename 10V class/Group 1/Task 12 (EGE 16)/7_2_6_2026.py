from functools import lru_cache
from fractions import Fraction

@lru_cache(100)
def f(n):
    if n < 10: return 4
    return (n + 5 ) * f(n -6)

for i in   range(9, 264739): f(i)

print((Fraction(f(264738) , 319) +Fraction(f(264726) , 145)) / f(264714))

# 15397428749034026630
