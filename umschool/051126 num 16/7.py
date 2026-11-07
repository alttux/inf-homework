from functools import cache
from sys import setrecursionlimit


setrecursionlimit(10**6)

def f(n):
    return g(n-2) + g(n-4)

@cache
def g(n):
    if n <= 11:
        return 2 * n
    return g(n-3) + 2


print(f(39_127))