alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')

for x in alph[:15]:
    if int(f'12{x}35', 15) % 4 == 0:
        print(alph.index(x))
