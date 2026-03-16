alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')

for x in alph[:15]:
    if int(f'123{x}5', 15) % 14 == 0:
        print(x)
