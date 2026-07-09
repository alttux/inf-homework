alph = sorted('1234567890abcdef')
alph2 = sorted('9abcdef')
s = 16
c = 0
for x in alph:
    for y in alph2:
        if x < y:
            n1 = f'5{x}{y}c'
            n2 = f'8{x}{x}7'
            a = int(n1, s) + int(n2, alph.index(y))
            print(a)
            c+=1
print(c)
# 84