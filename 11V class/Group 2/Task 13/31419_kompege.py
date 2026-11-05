# 31419

def f(curr, end, step='0', cnt_B=0):
    if step == 'r': cnt_B += 1
    if curr > end or cnt_B > 3: return 0
    if curr == end: return cnt_B == 3
    s_curr = str(curr)
    if '1' in s_curr: return f(curr + 1, end, '+1', cnt_B) + f(int(s_curr.replace('1', '3')), end, 'r', cnt_B)
    return f(curr + 1, end, '+1', cnt_B)


print(f(11, 94))
