from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(1000000)

@lru_cache(None)
def f(n):
    if n < 10:
        return n
    else:
        return 3*n + f(n-3)


print(int((f(6250) + 2*f(6244))/f(6238)))