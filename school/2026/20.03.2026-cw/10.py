alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')


for x in alph[:11]:
    n1 = f'95{x}2'
    n2 = f'{x}458'
    a = int(n1, 11) + int(n2, 12)
    if a%136==0:
        print(x, a, a//136)
        # 139