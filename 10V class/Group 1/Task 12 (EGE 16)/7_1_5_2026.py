def f(n):
    if n == 257472: return 345454
    return (n + 4) * f(n - 5)


print(str((f(257487) // 683 + f(257477) // 67) // f(257472))[-8:])
