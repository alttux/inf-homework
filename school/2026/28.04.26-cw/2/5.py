from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(1000000)

@lru_cache()
def f(n):
    sum_n = 0
    for i in str(n):
        sum_n+=int(i)
    if n>2 and sum_n%2==0:
        return f(n-1)-f(n-2)
    if n>2 and sum_n%2==1:
        return f(n-1)+f(n//2)
    if n<3:
        return 1

# print(f(10))
print(f(100))