from functools import cache


@cache
def f(n):
    if n == 0: return 0
    if n % 2 == 0: return f(n // 2) - 1
    return 1 + f(n - 1)


cnt = 0
for num in range(0, 1000):
    if f(num) == 0:
        cnt += 1
print(cnt)
