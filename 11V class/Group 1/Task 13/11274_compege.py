def f(curr, end):
    if curr < end: return 0
    if curr == end: return 1
    return f(curr - 3, end) + f(curr // 2, end)

print(f(28, 3))