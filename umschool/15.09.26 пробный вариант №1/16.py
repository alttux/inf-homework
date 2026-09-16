from sys import setrecursionlimit, set_int_max_str_digits
setrecursionlimit(10000)
set_int_max_str_digits(0)
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * f(n - 1)
n1 = f(2744) + 5 * f(2743)
n2 = f(2742)
print(n1/n2)
print((f(2744) + 5 * f(2743))/ f(2742))