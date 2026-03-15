# перевод в систему счисления
def to_a(x, a):
    s = ''
    while x > 0:
        s = str(x % a) + s
        x = x // a
    return s


print(to_a(52, 3))