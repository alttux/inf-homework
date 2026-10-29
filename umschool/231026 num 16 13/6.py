from functools import cache

@cache
def f(n):
    if n < 5:
        return n
    elif n >= 5 and n % 2 == 0:
        return f(n-2) + g(n-1)
    elif n >= 5 and n % 2 != 0:
        return g(n-1) + f(n-1) + n + 3

@cache
def g(n):
    if n < 5:
        return n
    elif n >= 5 and n % 2 == 0:
        return f(n-1)/2 + n
    elif n >= 5 and n % 2 != 0:
        return g(n-1) + 8

for i in range(200):
    f(i)
    g(i)
print((f(100)+g(90))/4991)

print(2+2+5+9+3+4+7)