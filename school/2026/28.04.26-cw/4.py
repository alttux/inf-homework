def f(n):
    if n <= 1:
        return 0.5
    else:
        return (n+1)*f(n-1)

print(f(100))
print(f(200)/f(198))