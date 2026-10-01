# def f(x):
#     return (not (x % A == 0)) <= ((x % 6 == 0) <= (not (x % 4 == 0)))
def ДЕЛ(a, b):
    return not a % b

def f(x):
    return (not ДЕЛ(x, A)) <= (not ДЕЛ(x, 21) and not ДЕЛ(x, 35))

for A in range(1000, 0, -1):
    if all(f(x) for x in range(1, 10000)):
        print(A)
        break
