# # from sys import setrecursionlimit
#
# # setrecursionlimit(2000)
#
#
# def f(n):
#     print(f'f({n})')
#     if n == 1:
#         print('Базовый случай')
#         return 1
#     return f(n - 1) + n
#
# print(f(1100))

def factorial(n):
    print(f'f({n})')
    if n == 1:
        print('Базовый случай: выход из рекурсии')
        return 1
    return factorial(n-1) * n

print(factorial(5))