from functools import cache


@cache
def f(n):
    if n <= 1:
        return 1
    return f(n-1) - 3 * g(n-2) - 100

@cache
def g(n):
    if n <= 1:
        return 1
    return f(n-1) + g(n-2) - 200

print(round(f(123)/g(115)))