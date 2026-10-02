def ДЕЛ(a, b):
    return a % b == 0

def f(x):
    return (not ДЕЛ(x, A)) <= (ДЕЛ(x, 6) <= (not ДЕЛ(x, 4)))


# def f(x):
#     return  (not (x % A == 0)) <= ((x % 6 == 0) <= (not (x % 4 == 0)))

for A in range(1000, 0, -1):
    if all(f(x) for x in range(10000)):
        print(A)
        break
