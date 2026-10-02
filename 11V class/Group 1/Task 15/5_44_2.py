def ДЕЛ(a, b):
    return a % b == 0

def f(x):
    return (not ДЕЛ(x, A)) <= (not ДЕЛ(x, 21) and  (not ДЕЛ(x, 35)))

for A in range(1000, 0, -1):
    if all(f(x) for x in range(1, 10000)):
        print(A)
        break
