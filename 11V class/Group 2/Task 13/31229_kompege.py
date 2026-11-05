# 31229

def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    s_c = str(curr)
    if '1' in s_c: return f(curr + 1, end) + f(int(s_c.replace('1', '3')), end)
    return f(curr + 1, end)

print(f(10, 84))
