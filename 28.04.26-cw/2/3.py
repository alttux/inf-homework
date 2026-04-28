from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(1000000)

@lru_cache()
def f(n):
    if n==0:
        return 1
    if n==1:
        return 3
    if n >1:
        return f(n-1)-f(n-2)+3*n


print(f(40))