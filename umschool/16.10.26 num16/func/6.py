def f(n):
    if n == 1:
        return 1
    elif n > 0:
        return (3 * f(n-1) - g(n-1)) * 2
    return None


def g(n):
    if n == 1:
        return 1
    elif n > 0:
        return f(n-1) - 3 * g(n-1) + 1
    return None

print(f(7))
# 27562