alph = sorted('1234567890abcdef')
def to_a(x, a):
    s = ''
    while x > 0:
        s = alph[x % a] + s
        x = x // a
    return s

for n in range(10000):
    if len(to_a(n, 7)) == 2 and len(to_a(n, 6)) == 3 and to_a(n, 13)[-1:] == '3':
        print(n)
# 42