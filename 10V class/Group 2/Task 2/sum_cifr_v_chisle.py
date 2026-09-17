# сумма цифр числа

# алгебраический подход
n = 4899
# sm = 0
# while n:
#     sm += n % 10
#     n //= 10
# print(sm)

# программный подход
n = 4899
sm = sum(int(x) for x in str(n))
print(sm)

# произведение всех цифр числа

# алгебраический подход
n = 4899
pr = 1
while n:
    pr *= n % 10
    n //= 10
print(pr)

# программный подход
from math import prod
n = 4899
# pr1 = prod(int(x) for x in str(n))
print(prod(int(x) for x in str(n)))

p = [123,3,45,6]
print(prod(p))