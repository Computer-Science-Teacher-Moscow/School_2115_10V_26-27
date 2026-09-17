# сумма цифр числа
# алгебраический подход
# n = 437
# sm  = 0
# while n:
#     sm += n % 10
#     n //= 10
# print(sm)

# программный подход
n = 567
sm = sum(int(x) for x in str(n))
print(sm)

# произведение всех цифр числа
# алгебраический подход
n = 437
pr  = 1
while n:
    pr *= n % 10
    n //= 10
print(pr)


# программный подход
from math import prod

n = 437
pr = prod(int(x) for x in str(n))
print(pr)

sm = pr
