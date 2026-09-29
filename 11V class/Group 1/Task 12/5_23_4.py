command = {
    (' ', 0): (' ', -1, 1),
    (' ', 2): (' ', 2, 2),
    ('0', 2): ('1', -1, 2),
    ('1', 1): ('2', 0, 2),
    ('1', 2): ('1', -1, 1),
    ('2', 1): ('0', -1, 1),
    ('2', 2): ('2', -1, 2),
}

def mt(s: str) -> str:
    s = list(f' {s} ')
    q = 0
    i = len(s) - 1
    while True:
        cmd_t = command[(s[i], q)]
        s[i] = cmd_t[0]
        if cmd_t[1] == 2:
            break
        i += cmd_t[1]
        q = cmd_t[2]
    return ''.join(s).strip()

st = '0' * 575 + '1' * 303 + '2' * 122
s1 = mt(st)
print(s1)
sm = sum(int(x) for x in s1)
print(sm)