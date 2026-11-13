def f(n):
    if n == 257472: return 345454
    return (n + 4) * f(n - 5)


print((f(257487) // 683 + 67*f(257477)) // f(257472))
