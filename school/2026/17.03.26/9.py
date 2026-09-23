alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')[:19]

for x in range(19):
    n1 = '55' + alph[x] + '36'
    n2 = alph[x] + '2724'
    a = int(n1, 19) + int(n2, 19)
    if a % 11 == 0:
        print(x, a // 11)
        break
