alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')


for x in alph[:21]:
    n1 = f'2496{x}2'
    n2 = f'8{x}223'
    n3 = f'2331768{x}3'

    a = int(n1, 21) + int(n2, 21) + int(n3, 21)

    if a%20==0:
        print(x, a, a//20)
        # 4066120204