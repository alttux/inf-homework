from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(10000000)

@lru_cache()
def f(n):
    if n<=2:
        return n
    if n > 2:
        return g(n)+f(n-2)

@lru_cache()
def g(n):
    if n<=2:
        return n
    if n > 2:
        return f(n-1)-g(n-2)
# print(f(2048)-f(2041))
print(g(15))