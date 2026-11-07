from functools import cache
from sys import setrecursionlimit


setrecursionlimit(10000)

@cache
def f(n):
    if n < 6:
        return n
    return f(n-2)/3 + 6 * n

print((f(2234) + 3 * f(2232))/f(2230))