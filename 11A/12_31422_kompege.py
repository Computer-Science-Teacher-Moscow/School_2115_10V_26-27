L = -1
R = 1
N = 0
S = 2
command = {
    (' ', 0): (' ', R, 1),
    (' ', 3): (' ', S, 3),
    ('0', 1): ('0', R, 2),
    ('0', 2): ('1', R, 3),
    ('0', 3): ('1', R, 4),
    ('0', 4): ('0', R, 1),
    ('1', 1): ('1', R, 2),
    ('1', 2): ('1', R, 3),
    ('1', 3): ('0', R, 4),
    ('1', 4): ('0', R, 1),
}


def mt(s):
    print(s)
    s = list(f' {s} ')
    q = 0
    i = 0
    while True:
        cmd_t = command[(s[i], q)]
        s[i] = cmd_t[0]
        if cmd_t[1] == 2:
            break
        i += cmd_t[1]
        q = cmd_t[2]
    return ''.join(s).strip()


s_mt = mt(bin(13613)[2:])
print(int(s_mt, 2))
