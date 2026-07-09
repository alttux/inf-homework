from sys import setrecursionlimit

setrecursionlimit(1000000)

def f(n):
    if n>=2222:
        return n
    else:
        return n**3+f(n+2)

print(f(4)-f(10))