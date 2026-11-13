from fractions import Fraction

def f(n):
    if n == 341557: return 2
    return (n + 7) * f(n - 4)


print((Fraction(f(341569), 336) + f(341561) / 576) // f(341557))
# 118606232402129