alph = sorted('1234567890abc')
print(alph)
s = 13
for x in alph:
    n1 = f'537{x}623'
    n2 = f'6{x}35{x}2'
    a = int(n1, s) - int(n2, s)
    if a % 3 == 0:
        print(a)
# 22949928