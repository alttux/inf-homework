from functools import cache


def f(n):
    return 2 * (g(n-3) + 13)

@cache
def g(n):
    if n < 6:
        return 2*n
    return g(n-2)+3

for i in range(4, 15_000):
    f(i)

print(f(14_541))
# print(14538 - 2*7269)