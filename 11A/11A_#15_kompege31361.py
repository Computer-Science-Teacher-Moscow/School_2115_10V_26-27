def ТРЕУГ(a, b, c):
    a, b, c = sorted((a, b, c))
    return a + b > c


def f(x):
    return ТРЕУГ(A, 7, x) <= ((max(x+5, 14) <= 27) == (not ТРЕУГ(36, 21, x)))


for A in range(10000, 0, -1):
    if all(f(x) for x in range(1, 10000)):
        print(A)
        break
