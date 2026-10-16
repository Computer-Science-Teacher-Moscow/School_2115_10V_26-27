from itertools import permutations


# def get_perestnovki(n):
#     t = set()
#     n1 = str(n)
#     for x in n1:
#         for y in n1:
#             num = x + y
#             if num[0] != 0 and x!=y and is_prime(int(num)):
#                  t.add(int(num))
#     print(t, n)
#     return t


def is_prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))

def get_r(n):
    ch = set(int(''.join(pr)) for pr in permutations(str(n), 2) if pr[0] != '0')
    ch = [x for x in ch if is_prime(x)]
    return ch


res = []
for N in range(100, 1000):
    res.append((len(get_r(N)), N))
print(max(res))
print('----' * 10)
print(get_r(121), 121)
# print((len(get_perestnovki(731)), 731))
# print((len(get_perestnovki(121)), 121))

# res = []
# for N in range(100, 1000):
#     res.append((len(get_perestnovki(N)), N))