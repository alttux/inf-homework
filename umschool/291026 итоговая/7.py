# from functools import cache
# from sys import setrecursionlimit
# setrecursionlimit(10 ** 9)
# @cache
# def f(n):
#     if n < 11:
#         return 2
#     x = (3*n + 5)
#     n-=8
#     return x * f(n)
# for i in range(1, 100):
#     print(f(i))
# print((f(405716)/217 + 39*f(405700))/f(405692))

print((3*405716 + 5)*(3*405708+5)*(3*405700+5))
print(1803058554500371385/217)

print((3*405700+5))
print(1217105*39 + 8309025596775905)