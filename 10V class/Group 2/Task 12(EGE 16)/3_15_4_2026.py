def f(n):
    if n <= 1: return n
    if n % 3 == 0: return n + f(n // 3)
    return n + f(n + 3)

for num in range(1, 1000):
    try:
        if (F:=f(num)) > 100:
            print(num, F)
            break
    except RecursionError:
        print('Поймали реальнго глюка с n = ', num)
        continue