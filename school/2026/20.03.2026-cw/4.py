alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')


for x in alph[:8]:
    for y in alph[:8]:
        n1 = f'{y}04{x}5'
        n2 = f'253{x}{y}'
        a = int(n1, 11) + int(n2, 8)
        if a%117==0:
            print(x, y, a, a//117)
# 224