def f(n):
    if n == 1:
        return 1
    elif n%2==0:
        return f(n-1) + n
    elif n%2==1 and n > 1:
        return g(n-1) +2

def g(n):
    if n == 1:
        return 1
    elif n%2==0:
        return g(n-1)+3
    elif n%2==1 and n > 1:
        return f(n-1)+n

print(f(40))