from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(10**6)

@lru_cache(maxsize=None)
def t13(s: , e):
    if s > e:
        return 0
    elif s == e:
        return 1

    sn = int(str(s)[0] + str(s)[-1] + str(s)[-2])
    if int(str(s)[-2]) < int(str(s)[-1]):
        return t13(s+1, e) + t13(sn, e)
    else: t13(s+1, e)


print(t13(103, 162))