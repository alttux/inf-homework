def f(n):
    if n < 3:
        return n
    if n % 2 != 0:
        return f(n - 2) + f(n - 1)
    return f(n - 2) + n

print(f(29))