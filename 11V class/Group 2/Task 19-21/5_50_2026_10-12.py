def f(s, m):
    if s >= 231: return m % 2 == 0
    if m == 0: return 0
    h = (f(s + 3, m - 1), f(s * 3, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', *(s for s in range(10, 121) if f(s,
                                              2)))  # Решаем return any(h) if (m - 1) % 2 == 0 else any(h) тольк 19, когда надо рассмотреть все возможные варианты
print('20)', *(s for s in range(10, 121) if not f(s, 1) and f(s, 3)))
print('21)', *(s for s in range(10, 121) if not f(s, 2) and f(s, 4)))
