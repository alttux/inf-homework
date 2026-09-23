alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
lst = []

for x in alph[:25]:
    n1 = f'11353{x}12'
    n2 = f'135{x}21'
    a = int(n1, 25) + int(n2, 25)
    if a%24==0:
        print(x, a/24)

# 266249847