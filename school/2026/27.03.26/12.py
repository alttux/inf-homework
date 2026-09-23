a = 3 * 125**6 + 2 * 25**9 + 5**12 -625
def to_a(x, a):
    s = ''
    while x > 0:
        s = str(x % a) + s
        x = x // a
    return s
print(to_a(a, 5))
print(to_a(a, 5).count('0'))
