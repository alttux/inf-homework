from sys import setrecursionlimit
from functools import cache


setrecursionlimit(10**6)

@cache
def f(n):
    if n == 1:
        return 1
    elif n < 1: return False
    return (n+2) * f(n-1)

print((f(2626) - 4 * f(2625))/f(2624))
