a = 9**8 + 3**5 - 2

def to_a(x, a):
    s = ''
    while x > 0:
        s = str(x % a) + s
        x = x // a
    return s

print(a, to_a(a, 3),  to_a(a, 3).count('2'))

# 4