def f(n):
    if n == 1:
        return 3
    else:
        return f(n-1) + (n-1)*n

print(f(18))
# 1941