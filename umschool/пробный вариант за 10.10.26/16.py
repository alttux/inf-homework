from sys import setrecursionlimit
from functools import lru_cache


setrecursionlimit(10000000)

@lru_cache(maxsize=None)
def f(n):
    if n < 10:
        return 1
    else:
        return (n+4) * f(n-4)

print(( f(31_313)//173 - 181*f(31_309) )//f(31_305) )