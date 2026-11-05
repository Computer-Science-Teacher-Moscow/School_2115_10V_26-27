# 31418
from functools import cache
@cache
def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) +f(curr + bin(curr)[2:].count('1'), end)


print(f(5, 40))
