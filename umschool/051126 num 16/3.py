from functools import cache


@cache
def f(n):
    if n < 10:
        return 5
    return (n+2) * f(n-5)

for i in range(2, 123_000, 5):
    f(i)

print((f(123_002)//7 + 2000 * f(122_997)) / f(122_992))