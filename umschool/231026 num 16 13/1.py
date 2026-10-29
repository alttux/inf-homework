from functools import cache


@cache
def f(n):
    if (n == 1) or (n == 2):
        return n
    elif n > 2:
        return f(n-2) - g(n-1) - 2*n

def g(n):
    if (n == 1) or (n == 2):
        return n
    elif n > 2:
        return f(n-1) + 2*g(n-1)

print(g(45))