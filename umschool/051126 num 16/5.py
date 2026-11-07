from functools import cache
from sys import setrecursionlimit


setrecursionlimit(10**6)

@cache
def f(n):
    if n < 15:
        return n
    return 5 * n + f(n-4)

print(f(8032)-f(8024))