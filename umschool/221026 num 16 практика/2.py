import sys
sys.setrecursionlimit(2600)
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return (2 * n - 2) * f(n - 1)

print(f(2555) / f(2553))
