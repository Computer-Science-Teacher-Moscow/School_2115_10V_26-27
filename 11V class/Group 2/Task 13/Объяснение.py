# 3 -> 11 (+1;+2)
def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 2, end)


print(f(3, 11))
