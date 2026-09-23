alph15 = '0123456789abcde'
alph17 = '0123456789abcdefgh'

lst = []
for x in range(15):
    n1 = '131' + alph15[x] + '1'
    n2 = '13' + alph17[x] + '3'
    a = int(n1, 15) + int(n2, 17)
    if a % 11 == 0:
        lst.append((a // 11))
print(max(lst))