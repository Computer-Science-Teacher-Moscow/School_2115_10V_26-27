# 27312


def f(curr, end, cnt=0):
    if curr in (48, 61): cnt += 1
    if curr < end: return 0
    if curr == end: return cnt == 1
    return f(curr -1, end, cnt) + f(curr // 2, end, cnt) + f(curr // 3, end, cnt)


print(f(106, 6))
