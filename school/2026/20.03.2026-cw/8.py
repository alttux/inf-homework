alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')


for x in alph[:9]:
    for y in alph[:9]:
        n1 = f'2{y}66{x}'
        n2 = f'{x}0{y}1'
        a = int(n1, 9) + int(n2, 12)
        if a%170==0:
            print(x, y, a, a//170)
            # 169