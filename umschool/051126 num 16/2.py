from functools import cache
from sys import setrecursionlimit, set_int_max_str_digits


setrecursionlimit(10**6)

@cache
def f(n):
    if n < 31:
        return n
    return (n-13) * f(n - 11)

print((f(36_924) - 2025 * f(36_913)) / f(36_902))
