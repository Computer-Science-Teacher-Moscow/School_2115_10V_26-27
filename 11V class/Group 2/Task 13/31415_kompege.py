# 31415
from functools import cache

@cache
def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    s_curr = str(curr)
    if s_curr[0] < s_curr[-1]: return f(curr + 1, end) + f(int(s_curr[-1] + s_curr[1:-1] + s_curr[0]), end)
    # if s_curr[0] < s_curr[-1]: return f(curr + 1, end) + f(int(s_curr[::-1]), end) # как вариант для трёхзначных чисел
    return f(curr + 1, end)

print(f(102, 300))
