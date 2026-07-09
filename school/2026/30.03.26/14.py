def to_a(x, a):
    s = ''
    while x > 0:
        s = str(x % a) + s
        x = x // a
    return s

lst = []
for x in range(1, 2031):
    a = 6**2030 + 6**100 - x
    a_to6 = to_a(a, 6)
    lst.append(a_to6.count('0'))

print(min(lst))