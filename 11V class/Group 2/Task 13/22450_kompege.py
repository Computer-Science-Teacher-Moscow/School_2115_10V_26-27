def f(curr, end):
    if curr < end: return 0
    if curr == end: return 1
    return f(curr - int(str(curr)[0]), end) + f(curr - int((2, str(curr)[-1])[curr % 10 != 0]), end) + f(curr // 2, end)


print(f(47, 40) * f(40, 18) * f(18, 14))

def f(curr, end, cnt=0):
    if curr in  (40,18): cnt += 1
    if curr < end: return 0
    if curr == end: return cnt == 2
    return f(curr - int(str(curr)[0]), end, cnt) + f(curr - int(2 if curr % 10 != 0 else curr % 10), end, cnt) + f(curr // 2, end, cnt)


print(f(47, 14))
