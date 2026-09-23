alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
lst = []

for x in alph[:29]:
    n1 = f'923{x}874'
    n2 = f'524{x}6152'
    a = int(n1, 29) + int(n2, 29)
    if a%28==0:
        print(x, a/28)

# 3318831885