from functools import cache


# def f(n):
    # print(5*g(n-1)-9)

@cache
def g(n):
    if n < 13:
        return n + 6
    return g(n-4) + 3

for i in range(21_000):
    g(i)

print(5*g(20_001-1)-9)