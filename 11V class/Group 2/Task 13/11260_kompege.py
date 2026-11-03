def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr ** 2, end) + f(curr +4, end)+ f(curr + 3, end)


print(f(2, 33))
