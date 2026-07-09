alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')

for x in alph[:22]:
    if int(f'{x}23{x}5', 22) % 37 == 0:
        print(alph.index(x))
