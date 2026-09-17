n = 4899
# sm = 0
# while n:
#     sm += n % 10
#     n //= 10
# print(sm)
sm = sum(int(x) for x in str(n))
print(sm)
