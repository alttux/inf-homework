from functools import cache
from sys import setrecursionlimit
setrecursionlimit(10**6)

@cache
def f(n):
    if n >= 27:
        return f(n-8) + 3531
    else:
        return 8 * (g(n-6) - 20)

@cache
def g(n):
    if n >= 179_403:
        return n / 16 + 59
    else:
        return g(n+12) -4

print(f(900))