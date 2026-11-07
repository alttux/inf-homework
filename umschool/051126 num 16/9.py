from functools import cache

@cache
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return f(n-1) + 10 * g(n-1) + 15 * n

@cache
def g(n):
    if n == 1:
        return 1
    elif n > 1:
        return f(n-1) - 2 * g(n-1)

print(str(f(555)).count('0'))