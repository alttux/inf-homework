k = 0
for i in range(1000, 10000):
    s = sum(int(x) for x in str(i))
    b = bin(s)[2:]
    if b.count('1') % 2 != 0:
        b = '10' + b
    else:
        b = b + '01'
    if int(b, 2) == 13:
        k += 1
print(k)