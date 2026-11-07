from functools import cache
# from sys import setrecursionlimit


# setrecursionlimit(10**6)

@cache
def f(n):
    if n >= 20:
        return f(n-5) + 3200
    return 9 * (g(n-6) - 34)

@cache
def g(n):
    if n >= 245_900:
        return n / 12 + 29
    return g(n+7) - 2

for i in range(245_900, 1, -1):
    g(i)

print(f(717))