L = -1
R = 1
N = 0
S = 2
command = {
    (' ', 0): (' ', L, 1),
    ('2', 1): ('1', L, 2),
    ('0', 2): ('1', S, 2),
    ('2', 2): ('0', L, 2),
}


def mt(s):
    print(s)
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

def num_base3(n):
    res = []
    while n:
        res.append(str(n%3))
        n //= 3
    return ''.join(res[::-1])



s_mt = mt(num_base3(101330))
print(int(s_mt, 3))
