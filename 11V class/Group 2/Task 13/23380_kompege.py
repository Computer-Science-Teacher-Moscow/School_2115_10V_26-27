# def f(curr, end):
#     if curr > end or curr == 10: return 0
#     if curr == end: return 1
#     return f(curr + 1, end) + f(curr + 2, end) + f(curr * 2, end)
#
#
# print(f(3, 7) * f(7, 20))

def f(curr, end, cnt=0):
    if curr == 7: cnt += 1
    if curr > end or curr == 10: return 0
    if curr == end: return cnt == 1
    return f(curr + 1, end, cnt) + f(curr + 2, end, cnt) + f(curr * 2, end, cnt)


print(f(3, 20))
