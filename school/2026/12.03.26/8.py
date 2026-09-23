alph = '0123456789abcdef'
lst1 = []
lst2 = []
for x in alph:
    for y in alph:
        n1 = f'27a{x}23'
        n2 = f'8{y}e5d2'
        a = int(n1, 16) + int(n2, 16)
        if a % 5 == 0:
            lst1.append(int(x, 16) + int(y, 16))
print(max(lst1))
# 29