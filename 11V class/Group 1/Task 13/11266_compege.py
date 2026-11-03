def f(curr, end):
    if curr < end or curr == 11: return 0
    if curr == end: return 1
    return f(curr // 3, end) + f(curr - 1, end) + f(curr - 2, end)

print(f(30, 8))