# 31420
def f(curr, end, step = '0'):
    if curr > end: return 0
    if curr == end: return 1
    s_curr = str(curr)
    if step == 'r': return f(curr + 1, end, '+1') + f(curr + 3, end, '+3')
    if step == '+1': return f(curr + 3, end, '+3') + f(int(s_curr.replace('1', '3')), end, 'r') if '1' in s_curr else f(curr + 3, end, '+3')
    if step == '+3': return f(curr + 1, end, '+1') + f(int(s_curr.replace('1', '3')), end, 'r') if '1' in s_curr else f(curr + 1, end, '+1')
    return f(curr + 1, end, '+1') + f(curr + 3, end, '+3') + f(int(s_curr.replace('1', '3')), end, 'r')

print(f(11, 94))
