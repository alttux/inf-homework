# перевод в систему счисления
def to_a(x, a):
    x3 = ''
    while x > 0:
        x3 = str(x % a) + x3
        x = x // a
    return x3


print(to_a(52, 3))