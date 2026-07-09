from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(10000000)

@lru_cache()
def f(n):
    if n<3:
        return n
    if n > 2 and n%2==1:
        return f(n-1)+n
    if n > 2 and n%2==0:
        return f(n-3)+2*n

# @lru_cache()
# def g(n):
#     if n<10:
#         return n
#     else:
#         return g(n-3)+5

print(f(2048)-f(2041))