alph = sorted('1234567890a')
lst = []

def to_a(x, a):
    s = ''
    while x > 0:
        s = alph[x % a] + s
        x = x // a
    return s


for n in range(3001):
    b = 9 * 11**210 + 8 * 11**150 - n
    b_11 = to_a(b, 11)
    if b_11.count('0') == 60:
        lst.append(n)
print(max(lst))

# 2992