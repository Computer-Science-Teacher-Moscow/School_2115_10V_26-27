from math import ceil


def f(s1, s2, m):
    if s1 + s2 <= 36: return m % 2 == 0
    if m == 0: return 0
    h = (f(s1 - 3, s2, m - 1), f(s1, s2 - 3, m - 1), f(ceil(s1 / 2), s2, m - 1), f(s1, ceil(s2 / 2), m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', *(s for s in range(17, 500) if f(20, s, 2)))
print('20)', *(s for s in range(17, 500) if not f(20, s, 1) and f(20, s, 3)))
print('21)', *(s for s in range(17, 500) if not f(20, s, 2) and f(20, s, 4)))
