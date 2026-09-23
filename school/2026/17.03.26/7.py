alph = '0123456789abc'

for x in range(13):
    n1 = '186' + alph[x] + '4'
    n2 = '5' + alph[x] + '716'
    a = int(n1, 13) + int(n2, 13)
    if a % 11 == 0:
        print(x, a // 11)
        break
