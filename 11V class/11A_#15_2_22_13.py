# def f(x):
#     P = x in { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
#     Q = x in { 5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
#     A = x in a
#     return (A <= P) and (Q <= (not A))
#
# a = set(range(-10000, 10000))
# for x in range(-10000, 10000):
#     if f(x) == False:
#         a.remove(x)
# print(len(a), a)
#

