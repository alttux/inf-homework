n = 19
n1 = bin(n)[2:]

if n1.count('1') % 2 == 0:
    n1 += '0'
else:
    n1 += '1'

print(int(n1, 2))

