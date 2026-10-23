from sys import setrecursionlimit 
setrecursionlimit(2030)
def f(n):
    if n == 122:
        return 156
    elif n > 122:
        return 2 * f(n-1) + 4
# print('hi')
print(f(2017) - 4*f(2015))