# 27313


def f(curr, end, cnt=0):
    if curr in (15, 26): cnt += 1
    if curr > end or curr in (20, 33): return 0
    if curr == end: return cnt > 0
    return f(curr + 3, end, cnt) + f(curr + 4, end, cnt) + f(curr * 2, end, cnt)


print(f(3, 63))
