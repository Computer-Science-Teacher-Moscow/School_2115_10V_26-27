# 31510
def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    s_curr = str(curr)
    if s_curr[-2] < s_curr[-1]: return f(curr + 1, end) + f(int(s_curr[:-2] + s_curr[-2:][::-1]), end)
    return f(curr + 1, end)


print(f(100, 141))

